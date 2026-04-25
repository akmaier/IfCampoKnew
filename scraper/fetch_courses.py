"""Fetch course-detail pages for every ``unit_id`` in a catalogue snapshot.

Stage 2 of the scraper pipeline:

    scrape.py        → tmp/{period}.json          (catalogue tree, with unit_ids)
    fetch_courses.py → tmp/{period}-courses.json  (this file)
    render_markdown  → data/{period-slug}/        (final corpus)

Unique ``unit_id``s are deduplicated — a single course can be referenced
from multiple catalogue leaves (a Vorlesung used by several POs); we
fetch each detail page exactly once.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import logging
import sys
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


def fetch_courses(
    snapshot: dict,
    *,
    interval: float,
    path_contains: str | None,
    max_courses: int | None,
) -> dict:
    period_id = int(snapshot["periodId"])
    period_name = snapshot.get("periodName", f"(period {period_id})")

    units = collect_unit_ids(snapshot, path_contains=path_contains)
    if max_courses and len(units) > max_courses:
        log.info("limiting to first %d of %d unit_ids", max_courses, len(units))
        units = units[:max_courses]
    log.info("fetching %d course details", len(units))

    client = CampoClient(min_interval=interval)
    courses: list[Course] = []
    failures: list[dict] = []
    for i, (uid, fallback_title) in enumerate(units, 1):
        url = DETAIL_URL_TPL.format(unit_id=uid, period_id=period_id)
        try:
            r = client.get(url)
            r.raise_for_status()
            course = parse_course_detail(
                r.text,
                unit_id=uid,
                period_id=period_id,
                fallback_title=fallback_title,
            )
            courses.append(course)
        except Exception as e:  # noqa: BLE001
            log.warning("unit_id=%d failed: %s", uid, e)
            failures.append({"unitId": uid, "error": str(e)})
        if i % 25 == 0 or i == len(units):
            log.info("progress %d/%d (%d ok, %d failed)", i, len(units), len(courses), len(failures))

    return {
        "periodId": period_id,
        "periodName": period_name,
        "fetchedAt": _dt.datetime.now(_dt.timezone.utc).isoformat(timespec="seconds"),
        "courses": [c.to_dict() for c in courses],
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
    )
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(
        f"wrote {args.out}: courses={len(out['courses'])} failures={len(out['failures'])}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
