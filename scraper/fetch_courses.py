"""Fetch course-detail pages for every ``unit_id`` in a catalogue snapshot.

Stage 2 of the scraper pipeline:

    scrape.py        → tmp/{period}.json          (catalogue tree, with unit_ids)
    fetch_courses.py → tmp/{period}-courses.json  (this file)
    render_markdown  → data/{period-slug}/        (final corpus)

Unique ``unit_id``s are deduplicated — a single course can be referenced
from multiple catalogue leaves (a Vorlesung used by several POs); we
fetch each detail page exactly once.

Parallelism: ``--parallel N`` spawns N worker threads, each with its own
CampoClient (own JSESSIONID, own per-session rate limit). At ``--interval
0.5`` and ``--parallel 4`` the effective request rate is ≈ 8 req/s split
across four sessions — comfortably within HISinOne's tolerance.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import logging
import sys
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT_DIR))

from campo_client import CampoClient  # noqa: E402
from parse_detail import parse_course_detail  # noqa: E402
from schema import Course  # noqa: E402

log = logging.getLogger("campo.fetch_courses")

DETAIL_URL_TPL = (
    "https://www.campo.fau.de/qisserver/pages/startFlow.xhtml"
    "?_flowId=detailView-flow&unitId={unit_id}&periodId={period_id}"
)


def collect_unit_ids(snapshot: dict, *, path_contains: str | None) -> list[tuple[int, str]]:
    """Return ``[(unit_id, fallback_title), …]`` from the snapshot.

    If ``path_contains`` is given, only nodes whose path contains that
    segment string are kept (handy for testing on a subtree).
    """
    seen: set[int] = set()
    out: list[tuple[int, str]] = []
    for n in snapshot["nodes"]:
        uid = n.get("unitId")
        if not uid:
            continue
        if uid in seen:
            continue
        if path_contains and path_contains not in n["path"]:
            continue
        seen.add(uid)
        out.append((uid, n.get("name", "")))
    return out


def _read_existing_progress(out_path: Path) -> tuple[list[dict], list[dict]]:
    """Load courses + failures already on disk so a re-run can skip them."""
    if not out_path.exists():
        return [], []
    try:
        existing = json.loads(out_path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        log.warning("existing %s unreadable (%s) — starting fresh", out_path, e)
        return [], []
    return list(existing.get("courses") or []), list(existing.get("failures") or [])


def _write_progress(
    out_path: Path,
    period_id: int,
    period_name: str,
    courses: list,
    failures: list[dict],
) -> None:
    """Atomic write of the current courses + failures.

    Called periodically inside :func:`fetch_courses` so an interrupted run
    leaves ``--resume``-able state on disk.
    """
    payload = {
        "periodId": period_id,
        "periodName": period_name,
        "fetchedAt": _dt.datetime.now(_dt.timezone.utc).isoformat(timespec="seconds"),
        "courses": [c.to_dict() if hasattr(c, "to_dict") else c for c in courses],
        "failures": failures,
    }
    out_path.parent.mkdir(parents=True, exist_ok=True)
    tmp = out_path.with_suffix(out_path.suffix + ".tmp")
    tmp.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(out_path)


def _fetch_one(
    client: CampoClient, uid: int, fallback_title: str, period_id: int
):
    """Fetch + parse one course detail. Returns (course, None) or (None, err)."""
    url = DETAIL_URL_TPL.format(unit_id=uid, period_id=period_id)
    try:
        r = client.get(url)
        r.raise_for_status()
        course = parse_course_detail(
            r.text, unit_id=uid, period_id=period_id, fallback_title=fallback_title,
        )
        return course, None
    except Exception as e:  # noqa: BLE001
        return None, e


def fetch_courses(
    snapshot: dict,
    *,
    interval: float,
    path_contains: str | None,
    max_courses: int | None,
    out_path: Path | None = None,
    resume: bool = False,
    save_every: int = 25,
    parallel: int = 1,
) -> dict:
    period_id = int(snapshot["periodId"])
    period_name = snapshot.get("periodName", f"(period {period_id})")

    all_units = collect_unit_ids(snapshot, path_contains=path_contains)
    if max_courses and len(all_units) > max_courses:
        log.info("limiting to first %d of %d unit_ids", max_courses, len(all_units))
        all_units = all_units[:max_courses]

    courses_existing: list[dict] = []
    failures: list[dict] = []
    skip: set[int] = set()
    if resume and out_path:
        courses_existing, failures = _read_existing_progress(out_path)
        skip = {int(c["unit_id"]) for c in courses_existing}
        skip |= {int(f["unitId"]) for f in failures if "unitId" in f}
        if skip:
            log.info("resume: %d courses + %d failures already on disk", len(courses_existing), len(failures))

    todo = [(uid, t) for (uid, t) in all_units if uid not in skip]
    log.info(
        "fetching %d new course details (%d skipped via resume) — parallel=%d, interval=%.2fs",
        len(todo), len(skip), parallel, interval,
    )

    courses: list = list(courses_existing)
    if parallel <= 1:
        # Sequential path (unchanged) — single client, single rate limit.
        client = CampoClient(min_interval=interval)
        last_save_count = 0
        for i, (uid, fallback_title) in enumerate(todo, 1):
            course, err = _fetch_one(client, uid, fallback_title, period_id)
            if err is not None:
                log.warning("unit_id=%d failed: %s", uid, err)
                failures.append({"unitId": uid, "error": str(err)})
            else:
                courses.append(course)
            if i % 25 == 0 or i == len(todo):
                log.info(
                    "progress %d/%d (total: %d ok, %d failed)",
                    i, len(todo), len(courses), len(failures),
                )
            if out_path and save_every > 0 and (i - last_save_count) >= save_every:
                _write_progress(out_path, period_id, period_name, courses, failures)
                last_save_count = i
    else:
        # Parallel path: N worker threads, each with its own CampoClient.
        # Locks guard the shared courses/failures lists and the periodic
        # save. Effective request rate is N * (1 / interval).
        clients = [CampoClient(min_interval=interval) for _ in range(parallel)]
        client_pool = list(clients)
        pool_lock = threading.Lock()
        results_lock = threading.Lock()
        done = [0]
        last_save_count = [0]

        def take_client() -> CampoClient:
            with pool_lock:
                return client_pool.pop()

        def return_client(c: CampoClient) -> None:
            with pool_lock:
                client_pool.append(c)

        def worker(uid_title: tuple[int, str]):
            uid, title = uid_title
            client = take_client()
            try:
                course, err = _fetch_one(client, uid, title, period_id)
            finally:
                return_client(client)
            return uid, course, err

        with ThreadPoolExecutor(max_workers=parallel) as ex:
            futures = [ex.submit(worker, ut) for ut in todo]
            for fut in as_completed(futures):
                uid, course, err = fut.result()
                with results_lock:
                    if err is not None:
                        log.warning("unit_id=%d failed: %s", uid, err)
                        failures.append({"unitId": uid, "error": str(err)})
                    else:
                        courses.append(course)
                    done[0] += 1
                    if done[0] % 50 == 0 or done[0] == len(todo):
                        log.info(
                            "progress %d/%d (total: %d ok, %d failed)",
                            done[0], len(todo), len(courses), len(failures),
                        )
                    if (
                        out_path
                        and save_every > 0
                        and (done[0] - last_save_count[0]) >= save_every
                    ):
                        _write_progress(
                            out_path, period_id, period_name, courses, failures
                        )
                        last_save_count[0] = done[0]

    return {
        "periodId": period_id,
        "periodName": period_name,
        "fetchedAt": _dt.datetime.now(_dt.timezone.utc).isoformat(timespec="seconds"),
        "courses": [c.to_dict() if hasattr(c, "to_dict") else c for c in courses],
        "failures": failures,
    }


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--in", dest="inp", type=Path, required=True, help="catalogue snapshot JSON")
    p.add_argument("--out", type=Path, required=True, help="course-detail JSON output")
    p.add_argument(
        "--interval",
        type=float,
        default=1.0,
        help="min seconds between requests (default 1.0; ≥ 0.5 only)",
    )
    p.add_argument(
        "--path-contains",
        default=None,
        help="only fetch courses whose catalogue path contains this segment "
        "(e.g. 'title:17991' for the Musizieren section)",
    )
    p.add_argument("--max-courses", type=int, default=None, help="stop after N (testing)")
    p.add_argument(
        "--resume",
        action="store_true",
        help="if --out already exists, skip course unit_ids already in it and append the rest",
    )
    p.add_argument(
        "--save-every",
        type=int,
        default=25,
        help="atomically write --out after every N successful fetches (default 25; 0 disables)",
    )
    p.add_argument(
        "--parallel",
        type=int,
        default=1,
        help="number of concurrent worker sessions (each w/ own JSESSIONID + rate limit). "
        "Try 4–6 for speed; default 1 (sequential, fully polite).",
    )
    p.add_argument("-v", "--verbose", action="count", default=0)
    args = p.parse_args(argv)

    level = logging.WARNING - 10 * args.verbose
    logging.basicConfig(level=max(level, logging.DEBUG), format="%(levelname)s %(name)s: %(message)s")

    snapshot = json.loads(args.inp.read_text(encoding="utf-8"))
    out = fetch_courses(
        snapshot,
        interval=args.interval,
        path_contains=args.path_contains,
        max_courses=args.max_courses,
        out_path=args.out,
        resume=args.resume,
        save_every=args.save_every,
        parallel=args.parallel,
    )
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(
        f"wrote {args.out}: courses={len(out['courses'])} failures={len(out['failures'])}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
