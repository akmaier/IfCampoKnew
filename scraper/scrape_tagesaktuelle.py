"""Iterate the *Tagesaktuelle Veranstaltungen* flow over a date range.

Each call to::

    GET .../currentLectures.xhtml?_flowId=showEventsAndExaminationsOnDate-flow
        &date=YYYY-MM-DD

renders the events of that day; the response carries one
``href=".../detailView-flow&unitId=NNN&periodId=…"`` per event row. We sweep
the whole lecture period, dedupe by ``unitId``, and emit a JSON file
suitable for ``fetch_courses.py --resume``::

    {
      "periodId": 589,
      "periodName": "Sommersemester 2026",
      "swept": "YYYY-MM-DD..YYYY-MM-DD",
      "scrapedAt": "...",
      "nodes": [
        {"unitId": 86267, "first_seen": "2026-04-23", "name": ""},
        ...
      ]
    }

The ``nodes`` list is shaped so it slots into ``fetch_courses.collect_unit_ids``
without code changes (snapshot-style ``unitId`` field on each node).

Why this exists: depth-4 Campo walks miss ~95 % of regular faculty courses
because their leaves live deeper than depth 4. A full-depth walk takes
days; this date-sweep covers an entire semester at one request per day
(≤ 2 minutes wall-clock).
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import logging
import re
import sys
from pathlib import Path
from typing import Iterable

ROOT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT_DIR))

from campo_client import CampoClient  # noqa: E402

log = logging.getLogger("campo.tagesaktuelle")

DAY_URL_TPL = (
    "https://www.campo.fau.de/qisserver/pages/cm/exa/timetable/currentLectures.xhtml"
    "?_flowId=showEventsAndExaminationsOnDate-flow&date={date}"
)
DETAIL_LINK_RE = re.compile(
    r'_flowId=detailView-flow(?:&amp;|&)unitId=(?P<uid>\d+)'
    r'(?:&amp;|&)periodId=(?P<pid>\d+)',
    re.IGNORECASE,
)
ROW_TITLE_RE = re.compile(
    r'title="Details für Veranstaltung\s+(?P<title>[^"]+?)\s+anzeigen"',
    re.IGNORECASE,
)
RESULT_HEADING_RE = re.compile(
    r"Suchergebnisse für\s+([^<]+?)\s*</h2>",
    re.IGNORECASE,
)


def _daterange(start: _dt.date, end_inclusive: _dt.date) -> Iterable[_dt.date]:
    cur = start
    one = _dt.timedelta(days=1)
    while cur <= end_inclusive:
        yield cur
        cur += one


def fetch_one_day(
    client: CampoClient, day: _dt.date, *, expected_period: int | None = None
) -> dict[int, str]:
    """Fetch one day, return ``{unit_id: first-seen-title}``."""
    url = DAY_URL_TPL.format(date=day.isoformat())
    r = client.get(url)
    r.raise_for_status()
    text = r.text
    out: dict[int, str] = {}
    # Walk the HTML once, pairing each detail link with the closest preceding
    # title= attribute.
    last_title = ""
    pos = 0
    while True:
        m_title = ROW_TITLE_RE.search(text, pos)
        m_link = DETAIL_LINK_RE.search(text, pos)
        if not m_link:
            break
        if m_title and m_title.start() < m_link.start():
            last_title = m_title.group("title")
            pos = m_title.end()
            continue
        uid = int(m_link.group("uid"))
        pid = int(m_link.group("pid"))
        if expected_period and pid != expected_period:
            pos = m_link.end()
            continue
        if uid not in out:
            out[uid] = last_title
        pos = m_link.end()
    log.debug(
        "%s: %d unique unit_ids (heading=%s)",
        day, len(out),
        (RESULT_HEADING_RE.search(text) or [None]).__getitem__(0)
        if RESULT_HEADING_RE.search(text) else "?",
    )
    return out


def sweep(
    *, period_id: int, period_name: str, start: _dt.date, end: _dt.date,
    interval: float = 1.0, skip_sundays: bool = True,
) -> dict:
    client = CampoClient(min_interval=interval)
    units: dict[int, dict] = {}
    days_done = 0
    for d in _daterange(start, end):
        if skip_sundays and d.weekday() == 6:
            continue
        try:
            day_units = fetch_one_day(client, d, expected_period=period_id)
        except Exception as e:  # noqa: BLE001
            log.warning("skip %s (%s)", d.isoformat(), e)
            continue
        new = 0
        for uid, title in day_units.items():
            if uid not in units:
                units[uid] = {"unitId": uid, "first_seen": d.isoformat(), "name": title}
                new += 1
        days_done += 1
        if days_done % 7 == 0 or new > 0:
            log.info(
                "%s — %d events that day, +%d new (total %d unique)",
                d.isoformat(), len(day_units), new, len(units),
            )
    nodes = sorted(units.values(), key=lambda x: x["unitId"])
    return {
        "periodId": period_id,
        "periodName": period_name,
        "swept": f"{start.isoformat()}..{end.isoformat()}",
        "scrapedAt": _dt.datetime.now(_dt.timezone.utc).isoformat(timespec="seconds"),
        "nodes": nodes,
    }


def parse_iso(s: str) -> _dt.date:
    return _dt.date.fromisoformat(s)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--period", type=int, required=True, help="periodId, e.g. 589")
    p.add_argument(
        "--period-name", default="Sommersemester 2026", help="for the JSON header"
    )
    p.add_argument(
        "--start", type=parse_iso, default=_dt.date(2026, 4, 13),
        help="first day to sweep (default 2026-04-13, SoSe-Vorlesungsbeginn)",
    )
    p.add_argument(
        "--end", type=parse_iso, default=_dt.date(2026, 7, 19),
        help="last day to sweep (inclusive; default 2026-07-19, SoSe lecture end)",
    )
    p.add_argument(
        "--out", type=Path, default=Path("tmp/589-tagesaktuelle.json"),
        help="JSON output path",
    )
    p.add_argument("--interval", type=float, default=1.0)
    p.add_argument("-v", "--verbose", action="count", default=0)
    args = p.parse_args(argv)

    level = logging.WARNING - 10 * args.verbose
    logging.basicConfig(level=max(level, logging.DEBUG), format="%(levelname)s %(name)s: %(message)s")

    payload = sweep(
        period_id=args.period,
        period_name=args.period_name,
        start=args.start,
        end=args.end,
        interval=args.interval,
    )
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(
        f"wrote {args.out}: unique unit_ids={len(payload['nodes'])} "
        f"({args.start.isoformat()} .. {args.end.isoformat()})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
