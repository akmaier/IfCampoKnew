"""Merge N per-shard ``courses.json`` files into one unified file.

The companion to :mod:`shard_fetch`. Each fetch shard runs
``fetch_courses.py`` on its slice of unit-id nodes and writes its own
``courses.json``; this script unions those files into a single
``courses.json`` in the exact shape ``fetch_courses.py`` emits (which
is what :mod:`render_markdown` expects as its ``--courses`` argument).

Usage::

    python scraper/merge_courses.py \\
        --in tmp/courses-0.json tmp/courses-1.json ... tmp/courses-7.json \\
        --out tmp/589-courses.json

Merge rules:

* All inputs must share the same ``periodId`` (defensive check — a
  mismatch means somebody wired the wrong shard set together).
* ``periodName`` is taken from the first input.
* ``courses`` are unioned deduplicated by ``unit_id``. On duplicate uid
  across shards the first-seen record wins. In practice each uid
  belongs to exactly one shard so duplicates only appear if the shard
  boundaries were miscomputed; first-wins is a defensive fallback.
  Final list is sorted by ``unit_id`` ascending for determinism.
* ``failures`` are unioned deduplicated by ``unitId``. Order is
  preserved input-by-input (first input's failures first, then the
  second's, ...).
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

log = logging.getLogger("campo.merge_courses")

def merge_courses(shard_payloads: list[dict]) -> dict:
    """Union N ``fetch_courses.py``-shaped payloads into one.

    Raises ``ValueError`` on ``periodId`` mismatch; the caller (``main``)
    converts that to a ``SystemExit`` with a helpful message.
    """
    if not shard_payloads:
        raise ValueError("no shard payloads to merge")

    first = shard_payloads[0]
    period_id = first.get("periodId")
    if period_id is None:
        raise ValueError("first shard has no periodId")
    period_name = first.get("periodName", "")

    for i, s in enumerate(shard_payloads[1:], start=1):
        if s.get("periodId") != period_id:
            raise ValueError(
                f"shard #{i} periodId={s.get('periodId')!r} "
                f"≠ first shard's periodId={period_id!r}"
            )

    # Dedup courses by unit_id, first-wins.
    courses_by_uid: dict[int, dict] = {}
    for i, s in enumerate(shard_payloads):
        raw = s.get("courses") or []
        if not isinstance(raw, list):
            raise ValueError(
                f"shard #{i} 'courses' must be a list, got {type(raw).__name__}"
            )
        for c in raw:
            uid = c.get("unit_id")
            if uid is None:
                log.warning(
                    "shard #%d: skipping course without unit_id: %r", i, c
                )
                continue
            uid_int = int(uid)
            if uid_int not in courses_by_uid:
                courses_by_uid[uid_int] = c
            else:
                log.debug(
                    "shard #%d: duplicate unit_id=%d (first-wins)",
                    i,
                    uid_int,
                )

    # Dedup failures by unitId, first-wins, preserving input order.
    failures_by_uid: dict[int, dict] = {}
    for i, s in enumerate(shard_payloads):
        raw_f = s.get("failures") or []
        if not isinstance(raw_f, list):
            raise ValueError(
                f"shard #{i} 'failures' must be a list, got {type(raw_f).__name__}"
            )
        for f in raw_f:
            uid = f.get("unitId")
            if uid is None:
                log.warning(
                    "shard #%d: skipping failure without unitId: %r", i, f
                )
                continue
            uid_int = int(uid)
            if uid_int not in failures_by_uid:
                failures_by_uid[uid_int] = f

    ordered_courses = sorted(
        courses_by_uid.values(), key=lambda c: int(c["unit_id"])
    )
    # Preserve first-seen order for failures (dict insertion order in 3.7+).
    ordered_failures = list(failures_by_uid.values())

    return {
        "periodId": period_id,
        "periodName": period_name,
        "fetchedAt": _dt.datetime.now(_dt.timezone.utc).isoformat(timespec="seconds"),
        "courses": ordered_courses,
        "failures": ordered_failures,
    }

def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description=(
            "Union N per-shard courses.json files into one merged "
            "courses.json in the shape fetch_courses.py normally emits."
        )
    )
    p.add_argument(
        "--in",
        dest="in_paths",
        type=Path,
        nargs="+",
        required=True,
        help="per-shard courses.json files (as produced by fetch_courses.py)",
    )
    p.add_argument(
        "--out",
        type=Path,
        required=True,
        help="output courses.json path (parent created if missing)",
    )
    p.add_argument("-v", "--verbose", action="count", default=0)
    args = p.parse_args(argv)

    level = logging.WARNING - 10 * args.verbose
    logging.basicConfig(
        level=max(level, logging.DEBUG),
        format="%(levelname)s %(name)s: %(message)s",
    )

    shard_payloads: list[dict] = []
    for path in args.in_paths:
        log.info("reading %s", path)
        shard_payloads.append(json.loads(path.read_text(encoding="utf-8")))

    try:
        merged = merge_courses(shard_payloads)
    except ValueError as e:
        raise SystemExit(f"merge_courses: {e}") from e

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(
        json.dumps(merged, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(
        f"wrote {args.out}: periodId={merged['periodId']} "
        f"courses={len(merged['courses'])} failures={len(merged['failures'])}"
    )
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
