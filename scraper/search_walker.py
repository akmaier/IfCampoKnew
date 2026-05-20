"""Backfill courses missed by the catalogue tree walk.

Stage 1b (between ``scrape.py`` and ``fetch_courses.py``):

    scrape.py        → tmp/{period}.json          (catalogue tree)
    search_walker.py → tmp/{period}-search.json   (this module)
    fetch_courses.py → tmp/{period}-courses.json  (final corpus)

The catalogue tree walk (`scrape.py`) reaches courses listed under the
``showCourseCatalog-flow`` tree at the configured ``--max-depth``. Some
courses live deeper than that (depth 7+) or aren't reachable via the
tree at all (cross-listed Veranstaltungen, niche Lehrstuhl seminars,
co-taught modules under non-Prof affiliates). They surface only via
Campo's public **course search** at
``_flowId=searchCourseNonStaff-flow``.

This module drives that search flow with JSF POSTs:

1. Bootstrap the flow (GET → ``e1s1`` flowExecutionKey + ViewState).
2. Discover the form-field IDs at runtime (Campo embeds hashes in
   names like ``inputField_0_{hash}:id{hash}``; the hashes are stable
   per Campo deployment but extracting them from the rendered HTML
   keeps the walker robust against re-deploys).
3. POST one search per query term, harvest the ``unitId=`` references
   from the result page.
4. Paginate via the JSF "next page" link until exhausted or the
   ``--max-pages`` cap is reached.
5. Aggregate unique ``unitId``s and emit a snapshot JSON with the same
   shape as ``scrape.py`` so ``fetch_courses.py --resume`` can pick it
   up without changes.

Usage::

    python scraper/search_walker.py --period 589 \\
        --queries Mustererkennung Medizintechnik "Artificial Intelligence" \\
        --out tmp/589-search.json -v
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import logging
import re
import sys
from pathlib import Path
from typing import Optional

ROOT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT_DIR))

from campo_client import CampoClient  # noqa: E402

log = logging.getLogger("campo.search_walker")

SEARCH_FLOW_URL = (
    "https://www.campo.fau.de/qisserver/pages/startFlow.xhtml"
    "?_flowId=searchCourseNonStaff-flow"
)
POST_URL_TPL = (
    "https://www.campo.fau.de/qisserver/pages/startFlow.xhtml"
    "?_flowId=searchCourseNonStaff-flow&_flowExecutionKey={key}"
)


def _bootstrap_search(client: CampoClient) -> dict[str, str]:
    """Land on the search form and return the form context needed to POST.

    Returns ``{view_state, flow_key, suchbegriffe_id, post_url,
    hidden_fields}`` — everything the POST handler needs.
    """
    r = client.get(SEARCH_FLOW_URL)
    if r.status_code != 200 or "Suchbegriffe" not in r.text:
        raise RuntimeError(
            f"search-flow bootstrap returned {r.status_code} or missing 'Suchbegriffe'"
        )
    text = r.text
    vs_m = re.search(r'name="javax\.faces\.ViewState"[^>]*value="([^"]+)"', text)
    if not vs_m:
        raise RuntimeError("no javax.faces.ViewState on the search form")
    view_state = vs_m.group(1)

    suchbegriffe_m = re.search(
        r'<label[^>]*for="([^"]+)"[^>]*>\s*Suchbegriffe\s*</label>',
        text,
    )
    if not suchbegriffe_m:
        raise RuntimeError("no 'Suchbegriffe' label on the search form")
    suchbegriffe_id = suchbegriffe_m.group(1)

    hidden: dict[str, str] = {}
    for n, v in re.findall(
        r'<input[^>]*type="hidden"[^>]*name="([^"]+)"[^>]*value="([^"]*)"',
        text,
    ):
        hidden[n] = v

    return {
        "view_state": view_state,
        "flow_key": view_state,  # e1s1 form == flow_key for this flow
        "suchbegriffe_id": suchbegriffe_id,
        "post_url": POST_URL_TPL.format(key=view_state),
        "hidden": hidden,
        "referer": r.url,
    }


def _extract_unit_ids(html: str) -> dict[int, str]:
    """Return ``{unit_id: best-guess-title}`` from a search-result page.

    The result page's course rows carry a permalink button whose
    ``data-page-permalink-title`` (rare) or surrounding link text
    carries the course title. We also capture ``unitId=N`` references
    that appear in the row.
    """
    out: dict[int, str] = {}
    # Find every detailView-flow URL on the page; each carries one unit_id.
    for m in re.finditer(
        r'(?:href|data-[a-z\-]+)="([^"]*?_flowId=detailView-flow[^"]*?unitId=(\d+)[^"]*)"',
        html,
    ):
        uid = int(m.group(2))
        if uid not in out:
            out[uid] = ""
    # Pair unit_ids with the permalink-title (where present)
    for m in re.finditer(
        r'unitId=(\d+)[^"]*?"[^>]*?(?:data-page-permalink-title|aria-label)="([^"]+)"',
        html,
    ):
        uid = int(m.group(1))
        title = m.group(2).strip()
        if uid in out and not out[uid]:
            out[uid] = title
    return out


def _find_next_page_command(html: str) -> Optional[tuple[str, str]]:
    """Find the JSF command name + value for the "next page" link.

    Returns ``(source, value)`` for the ``javax.faces.source`` POST
    parameter that advances the result page, or ``None`` if there's no
    next page on the current view.
    """
    # The JSF behaviour links use commandLink with onclick="...jsf.ajax.request('source', ...)"
    # Look for any link whose visible text contains "Nächste Seite" / "Next page" /
    # the right-arrow glyph, OR aria-label says "next page".
    pat = (
        r'<(?:a|button)[^>]*\b(?:id|name)="([^"]+)"[^>]*'
        r'(?:aria-label="[^"]*(?:nächste|next)[^"]*"|>\s*(?:Nächste Seite|Weiter|»))'
    )
    m = re.search(pat, html, re.IGNORECASE)
    if not m:
        return None
    return m.group(1), ""


def search_query(
    client: CampoClient,
    query: str,
    max_pages: int = 5,
) -> dict[int, str]:
    """Run one search; return ``{unit_id: title}``.

    Bootstraps the form fresh on every call. We tried session-reuse
    across queries but Campo's flow advances on every POST (e1sN →
    e1sN+1) and subsequent POSTs returned stale results from the
    previous query's state. The extra ~1 s per query for the GET is
    worth the correctness.
    """
    ctx = _bootstrap_search(client)

    form: dict[str, str] = dict(ctx["hidden"])
    form[ctx["suchbegriffe_id"]] = query
    form["genericSearchMask:buttonsBottom:search"] = "Suchen"
    form["genericSearchMask_SUBMIT"] = "1"
    form["javax.faces.ViewState"] = ctx["view_state"]

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Referer": ctx["referer"],
    }

    try:
        r = client.session.post(
            ctx["post_url"],
            data=form,
            headers=headers,
            timeout=client.timeout,
            allow_redirects=True,
        )
    except Exception as e:  # noqa: BLE001
        log.warning("search %r: POST raised %s", query, e)
        return {}

    if r.status_code != 200:
        log.warning("search %r: POST returned %d", query, r.status_code)
        return {}

    found = _extract_unit_ids(r.text)
    log.info("query %r: page 1 → %d hits", query, len(found))

    # Best-effort pagination — Campo's result table uses JSF behaviour
    # links for paging; reproducing those requires the exact ajax-request
    # form. v1 takes only page 1 (typically up to 10 results) and relies
    # on narrow, specific queries to keep results bounded.
    # TODO: pagination support if/when broad queries become common.
    return found


def collect(
    queries: list[str],
    period_id: int,
    period_name: str,
    *,
    interval: float = 0.5,
    parallel: int = 1,
    max_pages: int = 5,
) -> dict:
    """Run all queries and aggregate into a scrape.py-shaped snapshot.

    ``parallel >= 2`` spawns N worker threads, each with its own
    :class:`CampoClient` (own JSESSIONID, own per-session rate limit).
    Each worker independently bootstraps a fresh flow per query (the
    flow advances per POST and produces stale results on re-use within
    a single session — see comment in :func:`search_query`). Workers
    pull queries from a thread-safe deque; results are merged under a
    lock.

    At ``parallel=4`` we observed ~40 queries/min on Campo's runner
    (vs ~9 queries/min single-session), so the full FAUdir + instructor
    backfill list (~5 000 queries) fits comfortably in a single cron
    step.
    """
    aggregate: dict[int, str] = {}

    if parallel <= 1:
        client = CampoClient(min_interval=interval)
        for i, q in enumerate(queries):
            if not q.strip():
                continue
            try:
                hits = search_query(client, q.strip(), max_pages=max_pages)
            except Exception as e:  # noqa: BLE001
                log.warning("query %r failed: %s", q, e)
                continue
            if (i + 1) % 50 == 0:
                log.info(
                    "progress: %d/%d queries, %d unique unit_ids so far",
                    i + 1, len(queries), len(aggregate),
                )
            for uid, title in hits.items():
                if uid not in aggregate or (not aggregate[uid] and title):
                    aggregate[uid] = title
    else:
        # ── Parallel path: N worker threads + shared deque ────────────
        import threading
        from collections import deque
        from concurrent.futures import ThreadPoolExecutor

        clients = [CampoClient(min_interval=interval) for _ in range(parallel)]
        for c in clients:
            c.start_session()

        deq: "deque[str]" = deque(q for q in queries if q.strip())
        total = len(deq)
        deq_lock = threading.Lock()
        agg_lock = threading.Lock()
        done = [0]
        last_log_at = [0]

        def take_query() -> Optional[str]:
            with deq_lock:
                if not deq:
                    return None
                return deq.popleft()

        def worker(client_idx: int) -> None:
            client = clients[client_idx]
            while True:
                q = take_query()
                if q is None:
                    return
                q = q.strip()
                try:
                    hits = search_query(client, q, max_pages=max_pages)
                except Exception as e:  # noqa: BLE001
                    log.warning("[w%d] query %r failed: %s", client_idx, q, e)
                    hits = {}
                with agg_lock:
                    for uid, title in hits.items():
                        if uid not in aggregate or (not aggregate[uid] and title):
                            aggregate[uid] = title
                    done[0] += 1
                    if done[0] - last_log_at[0] >= 50:
                        log.info(
                            "progress: %d/%d queries, %d unique unit_ids",
                            done[0], total, len(aggregate),
                        )
                        last_log_at[0] = done[0]

        log.info(
            "running %d queries against periodId=%d with %d parallel workers",
            total, period_id, parallel,
        )
        with ThreadPoolExecutor(max_workers=parallel) as ex:
            futures = [ex.submit(worker, i) for i in range(parallel)]
            for f in futures:
                f.result()
        log.info(
            "search-walker done: %d queries processed, %d unique unit_ids",
            done[0], len(aggregate),
        )

    nodes = [
        {
            "segment": f"search:{uid}",
            "name": title or f"(via search, unit_id {uid})",
            "path": [],
            "parentSegment": None,
            "kind": "search-result",
            "unitId": uid,
            "children": [],
        }
        for uid, title in sorted(aggregate.items())
    ]
    return {
        "periodId": period_id,
        "periodName": period_name,
        "scrapedAt": _dt.datetime.now(_dt.timezone.utc).isoformat(timespec="seconds"),
        "rootSegment": None,
        "maxDepth": 0,
        "nodes": nodes,
    }


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument(
        "--period", type=int, required=True,
        help="Campo periodId (e.g. 589 for SoSe 2026)",
    )
    p.add_argument(
        "--period-name", default=None,
        help="Optional period display name (else: 'period {N}')",
    )
    p.add_argument(
        "--queries", nargs="+", default=None,
        help="Search terms (multiple allowed). Each is POSTed to "
        "searchCourseNonStaff-flow's Suchbegriffe field.",
    )
    p.add_argument(
        "--queries-file", type=Path, default=None,
        help="Path to a text file with one search term per line.",
    )
    p.add_argument("--out", type=Path, required=True, help="output JSON")
    p.add_argument(
        "--interval", type=float, default=0.5,
        help="min seconds between requests (default 0.5)",
    )
    p.add_argument(
        "--max-pages", type=int, default=5,
        help="max result pages to walk per query (default 5; v1 honours page 1 only)",
    )
    p.add_argument(
        "--parallel", type=int, default=1,
        help="number of concurrent worker sessions (each with own JSESSIONID + rate limit). "
        "Default 1; 4 cuts wall-clock by ~4× on a multi-thousand-query list. "
        "Total HTTP rate ≈ parallel/interval r/s; stay ≤ 4 r/s aggregate per the rate probe.",
    )
    p.add_argument("-v", "--verbose", action="count", default=0)
    args = p.parse_args(argv)

    level = logging.WARNING - 10 * args.verbose
    logging.basicConfig(
        level=max(level, logging.DEBUG),
        format="%(levelname)s %(name)s: %(message)s",
    )

    queries: list[str] = []
    if args.queries:
        queries.extend(args.queries)
    if args.queries_file:
        queries.extend(
            [ln.strip() for ln in args.queries_file.read_text(encoding="utf-8").splitlines() if ln.strip()]
        )
    if not queries:
        p.error("supply --queries or --queries-file")

    log.info(
        "running %d queries against periodId=%d (parallel=%d, interval=%.2fs)",
        len(queries), args.period, args.parallel, args.interval,
    )
    snap = collect(
        queries,
        period_id=args.period,
        period_name=args.period_name or f"period {args.period}",
        interval=args.interval,
        parallel=args.parallel,
        max_pages=args.max_pages,
    )
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(snap, ensure_ascii=False, indent=2), encoding="utf-8")
    print(
        f"wrote {args.out}: periodId={args.period} unit_ids={len(snap['nodes'])}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
