"""Alive-check Campo bulk-data candidates that we don't yet exploit.

Sends a *small, fixed* number of polite requests (<=15 total, paced at
0.5s) and reports for each candidate:

* HTTP status
* Content-Type
* response size
* a one-line shape hint (heuristic: looks like JSON / iCal / sitemap /
  paginated HTML / nothing)

The point is to tell us **whether** the endpoint is mounted and **what
shape** of bulk data it returns. We do *not* spider, paginate, or
hammer — that's left for the dedicated scraper modules once we've
chosen the winners.

Usage::

    python scraper/probe_bulk_apis.py --period 589 --unit-id 88134 -v
"""
from __future__ import annotations

import argparse
import logging
import re
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urlencode

import requests

ROOT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT_DIR))

from campo_client import CampoClient  # noqa: E402

log = logging.getLogger("campo.probe_bulk")

BASE = "https://www.campo.fau.de"


@dataclass
class ProbeResult:
    name: str
    url: str
    status: int | None
    content_type: str
    size_bytes: int
    elapsed_ms: float
    shape_hint: str
    error: str | None = None
    snippet: str = ""

    def fmt(self) -> str:
        if self.error:
            return f"  [{self.name}] ERROR: {self.error}  ({self.url})"
        return (
            f"  [{self.name}] {self.status} {self.content_type or '?'} "
            f"{self.size_bytes:>7} B  {self.elapsed_ms:>4.0f}ms  → {self.shape_hint}\n"
            f"      {self.url}"
        )


def _shape_hint(text: str, content_type: str) -> str:
    """Cheap classifier — what is this thing?"""
    t = text.lstrip()
    ct = (content_type or "").lower()
    if t.startswith("BEGIN:VCALENDAR") or "BEGIN:VEVENT" in t[:500]:
        return "iCal feed"
    if t.startswith("{") or t.startswith("["):
        return "JSON"
    if t.startswith("<?xml") and "sitemap" in t[:200].lower():
        return "XML sitemap"
    if t.startswith("<?xml") and "rss" in t[:200].lower():
        return "RSS feed"
    if t.startswith("<?xml"):
        return f"XML ({len(t)} chars)"
    if "application/json" in ct:
        return "JSON (by Content-Type)"
    if "text/calendar" in ct:
        return "iCal (by Content-Type)"
    if "<html" in t[:200].lower() or "<!doctype html" in t[:200].lower():
        # detect paginated HTML hints
        hint_terms = []
        if re.search(r"rowsPerPage|pagingNavigation|naviTab", t, re.IGNORECASE):
            hint_terms.append("JSF-paginated")
        if re.search(r"detailView-flow|unitId=", t):
            hint_terms.append("links to detail flow")
        if re.search(r"showCourseCatalog|showStudyPathway", t):
            hint_terms.append("catalogue links")
        if "errorPage" in t or "Fehler" in t[:1000]:
            hint_terms.append("looks like error page")
        return "HTML" + (f" ({', '.join(hint_terms)})" if hint_terms else "")
    if not t:
        return "empty"
    return "unknown"


def probe(client: CampoClient, name: str, url: str, *, snippet_len: int = 200) -> ProbeResult:
    log.info("probing %s: %s", name, url)
    t0 = time.monotonic()
    try:
        r = client.session.get(url, timeout=30, allow_redirects=True)
        elapsed = 1000 * (time.monotonic() - t0)
        ct = r.headers.get("Content-Type", "")
        text = r.text or ""
        return ProbeResult(
            name=name,
            url=r.url,  # post-redirect
            status=r.status_code,
            content_type=ct.split(";")[0].strip(),
            size_bytes=len(r.content),
            elapsed_ms=elapsed,
            shape_hint=_shape_hint(text, ct),
            snippet=text[:snippet_len].replace("\n", " "),
        )
    except requests.RequestException as e:
        return ProbeResult(
            name=name,
            url=url,
            status=None,
            content_type="",
            size_bytes=0,
            elapsed_ms=1000 * (time.monotonic() - t0),
            shape_hint="connection failure",
            error=type(e).__name__ + ": " + str(e)[:200],
        )


def build_candidates(period_id: int, unit_id: int) -> list[tuple[str, str]]:
    """Return [(label, url), …] of bulk-API candidates to probe."""
    detail_qs = urlencode({"_flowId": "detailView-flow", "unitId": unit_id, "periodId": period_id})
    candidates = [
        # 1. Sitemap — does qisserver expose one?
        ("sitemap.xml", f"{BASE}/sitemap.xml"),
        ("qisserver/sitemap.xml", f"{BASE}/qisserver/sitemap.xml"),
        # 2. Robots.txt — also useful to know what's "allowed"
        ("robots.txt", f"{BASE}/robots.txt"),
        # 3. The legacy HISinOne 'rds' query interface (state-based bulk export)
        # If mounted, this can return CSV/XML for arbitrary states.
        (
            "rds-state-wtree",
            f"{BASE}/qisserver/rds?state=wtree&search=1&trex=step&root120251=0%7C0",
        ),
        (
            "rds-state-verpublish",
            f"{BASE}/qisserver/rds?state=verpublish&status=init&vmfile=no",
        ),
        # 4. iCal export attempts on a course detail page (HISinOne sometimes
        # has a "Termine als iCal" link). We try common URL patterns.
        (
            "iCal-flowParam",
            f"{BASE}/qisserver/pages/startFlow.xhtml?{detail_qs}&export=ics",
        ),
        (
            "iCal-flow-direct",
            f"{BASE}/qisserver/pages/cm/exa/timetable/icsExport.xhtml"
            f"?_flowId=icsExport-flow&unitId={unit_id}&periodId={period_id}",
        ),
        # 5. Veranstaltungssuche — distinct from showCourseCatalog. Some
        # builds expose this with a higher rowsPerPage parameter.
        (
            "Veranstaltungssuche-flow",
            f"{BASE}/qisserver/pages/cm/exa/coursecatalog/showSearchByName.xhtml"
            f"?_flowId=showSearchByName-flow",
        ),
        # 6. Old-style JSP search (some FAU paths still respond)
        (
            "search-by-name",
            f"{BASE}/qisserver/rds?state=change&type=6&moduleParameter=Search",
        ),
        # 7. Person directory in HISinOne
        (
            "person-search-flow",
            f"{BASE}/qisserver/pages/cm/per/personSearch/showStartPersonSearch.xhtml"
            f"?_flowId=showStartPersonSearch-flow",
        ),
        # 8. Curricular catalogue ICS — sometimes exposes whole-period iCal
        (
            "studyPlanICS",
            f"{BASE}/qisserver/pages/cm/exa/timetable/myExamSchedule.xhtml"
            f"?_flowId=showStudyPlanIcs-flow&periodId={period_id}",
        ),
        # 9. Standard FAU.de-side data hooks (RSS / News)
        ("fau-feed-rss", f"{BASE}/feeds/all/rss.xml"),
    ]
    return candidates


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--period", type=int, default=589)
    p.add_argument("--unit-id", type=int, default=88134, help="sample unit_id for course-level probes")
    p.add_argument("--interval", type=float, default=0.5, help="min seconds between probes")
    p.add_argument("-v", "--verbose", action="count", default=0)
    args = p.parse_args(argv)

    level = logging.WARNING - 10 * args.verbose
    logging.basicConfig(
        level=max(level, logging.DEBUG),
        format="%(levelname)s %(name)s: %(message)s",
    )

    client = CampoClient(min_interval=args.interval)
    client.start_session()  # bootstrap once, share JSESSIONID across probes

    candidates = build_candidates(args.period, args.unit_id)
    log.info("probing %d candidates with %.1fs spacing", len(candidates), args.interval)

    results: list[ProbeResult] = []
    for name, url in candidates:
        client._rate_limit()  # respect the spacing between probes
        results.append(probe(client, name, url))

    print("\n=== BULK-API PROBE RESULTS ===")
    for r in results:
        print(r.fmt())

    print("\n=== ALIVE / INTERESTING ===")
    interesting = [r for r in results if r.status == 200 and r.size_bytes > 100]
    for r in interesting:
        marker = ""
        h = r.shape_hint.lower()
        if "ical" in h or "json" in h or "sitemap" in h:
            marker = "  ⭐ STRUCTURED — worth following up"
        elif "html" in h and "error" not in h:
            marker = "  • HTML (still useful)"
        print(f"  [{r.name}] → {r.shape_hint}{marker}")
        if r.snippet:
            print(f"      first 200 chars: {r.snippet[:200]}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
