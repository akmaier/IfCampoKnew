"""Pull Professor:innen-Einträge aus FAUdir und schreibe sie als Markdown.

FAUdir (`https://faudir.fau.de`) ist eine Vue-SPA, deren Backend-Daten
über eine *publicDir*-REST-Schnittstelle bereitstehen. Discovery via
Playwright (siehe Entry 0014); ab dann reicht plain HTTP. Endpunkt::

    GET /publicDir/persons?search=Professur&page=N&limit=100

Pagination: ``limit`` cap effektiv 100; ``total=1001`` für die
``Professur``-Suche → 11 Seiten reichen, um alle Professor:innen zu
holen.

Pro Person extrahieren wir:

  * ``identifier`` (stabile FAUdir-ID)
  * ``personalTitle`` (Prof. Dr., Prof. Dr.-Ing., …)
  * ``givenName`` / ``familyName``
  * Für jeden ``contacts[]`` -Eintrag: Organisations-Name + ``function``
    + ``functionLabel`` (de/en).
  * **W-Rang** wird aus dem Organisationsnamen geparst, falls explizit
    *"W1-Professur"* / *"W2-Professur"* / *"W3-Professur"* (manche
    Lehrstühle führen keinen W-Rang im Namen — das wird als ``W?``
    markiert; meist sind das reguläre Lehrstuhlprofessuren = W3).

Output: eine einzelne Markdown-Datei
``data/personen/faudir-professoren.md`` mit YAML-Frontmatter,
Statistik-Header und alphabetischer Personen-Liste.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import logging
import re
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path
from typing import Iterable

import requests

ROOT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT_DIR))

log = logging.getLogger("fau.faudir")

ENDPOINT = "https://faudir.fau.de/publicDir/persons"
DEFAULT_UA = (
    "Mozilla/5.0 (compatible; IfCampoKnew/0.1; "
    "+https://github.com/akmaier/IfCampoKnew)"
)


def fetch_persons_page(
    session: requests.Session, search: str, page: int, *, limit: int = 100, timeout: float = 30.0
) -> dict:
    """One page of ``/publicDir/persons``."""
    r = session.get(
        ENDPOINT,
        params={"search": search, "page": page, "limit": limit, "fetchAll": "false"},
        headers={"Accept": "application/json"},
        timeout=timeout,
    )
    r.raise_for_status()
    return r.json()


def fetch_all_persons(
    queries: list[str], *, interval: float = 1.0, max_pages_per_query: int = 100
) -> list[dict]:
    """Run each query, paginate, union by identifier.

    A single search query never returns *all* FAUdir persons — the search
    matches the substring against names + affiliation labels. We therefore
    union several prof-related queries to cover both *Professur* (W-Profs)
    and *Lehrstuhl* (Lehrstuhlinhaber, who do not always have *Professur*
    in their org name).
    """
    s = requests.Session()
    s.headers.update({"User-Agent": DEFAULT_UA})
    out: dict[str, dict] = {}
    total_pages = 0
    for q in queries:
        page = 1
        while page <= max_pages_per_query:
            log.info(
                "search=%r page %d — union has %d persons so far",
                q, page, len(out),
            )
            try:
                payload = fetch_persons_page(s, q, page)
            except requests.HTTPError as e:
                log.error("HTTP %s on page %d for q=%r — abort this query",
                          e.response.status_code if e.response else "?", page, q)
                break
            contacts = payload.get("contacts") or []
            if not contacts:
                log.info("query %r exhausted at page %d", q, page)
                break
            for p in contacts:
                ident = p.get("identifier")
                if ident and ident not in out:
                    out[ident] = p
            page += 1
            total_pages += 1
            time.sleep(interval)
    log.info("done: %d pages fetched, %d unique persons", total_pages, len(out))
    return list(out.values())


def filter_to_professors(persons: list[dict]) -> list[dict]:
    """Keep only persons with at least one prof-like ``function`` in their
    affiliations. ``function`` values seen in FAUdir include
    ``"professor"`` / ``"juniorProfessor"`` / ``"honoraryProfessor"`` etc.
    """
    out: list[dict] = []
    for p in persons:
        prof_like = False
        for c in p.get("contacts") or []:
            fn = (c.get("function") or "").lower()
            if "prof" in fn:
                prof_like = True
                break
            # also catch by organisation name: "Lehrstuhl" / "Professur"
            org = (c.get("organization") or {}).get("name") or ""
            if re.search(r"Professur|Lehrstuhl|Honorarprofessur", org, re.IGNORECASE):
                prof_like = True
                break
        if prof_like:
            out.append(p)
    return out


# ── parsing helpers ────────────────────────────────────────────────────────


_W_RANK_RE = re.compile(r"\bW([1-3])-Professur\b", re.IGNORECASE)
_HONORARY_PROF_RE = re.compile(r"\bHonorarprofessur\b", re.IGNORECASE)
_AUSSER_PROF_RE = re.compile(r"\bAußerplanmäßige|außerplanmä|apl\.?-?Prof", re.IGNORECASE)
_JUNIOR_PROF_RE = re.compile(r"\b(Juniorprofessur|Junior-Professur)\b", re.IGNORECASE)


def parse_w_rank(org_name: str) -> str:
    """Best-effort W-rank from organisation name. ``"W1"`` / ``"W2"`` / ``"W3"``,
    ``"W?"`` for explicit Lehrstuhl/Professur without a W-number,
    ``"Hon."``/``"apl."``/``"Junior"`` for honorary/außerplanmäßige/Junior,
    or empty for non-prof affiliations."""
    if _W_RANK_RE.search(org_name):
        return "W" + _W_RANK_RE.search(org_name).group(1)
    if _HONORARY_PROF_RE.search(org_name):
        return "Hon."
    if _AUSSER_PROF_RE.search(org_name):
        return "apl."
    if _JUNIOR_PROF_RE.search(org_name):
        return "Junior"
    if re.search(r"\b(Lehrstuhl|Professur)\b", org_name, re.IGNORECASE):
        return "W?"
    return ""


def slugify_person(p: dict) -> str:
    last = (p.get("familyName") or "").lower()
    first = (p.get("givenName") or "").lower()
    raw = f"{last}-{first}"
    raw = (
        raw.replace("ä", "ae").replace("ö", "oe").replace("ü", "ue").replace("ß", "ss")
    )
    raw = re.sub(r"[^a-z0-9]+", "-", raw).strip("-")
    return raw[:80]


# ── markdown render ────────────────────────────────────────────────────────


_TOKEN_BUDGET_PER_FILE = 80_000  # ~26 k tokens — sweet spot for the F-TOKEN policy


def _person_md(p: dict) -> str:
    title = p.get("personalTitle") or ""
    last = p.get("familyName") or ""
    first = p.get("givenName") or ""
    head = f"{last}, {first}".strip(", ")
    if title:
        head = f"{head} ({title})"
    out = [f"### {head}"]

    ranks_seen: list[str] = []
    for c in p.get("contacts") or []:
        org = (c.get("organization") or {}).get("name") or ""
        r = parse_w_rank(org)
        if r and r not in ranks_seen:
            ranks_seen.append(r)
    if ranks_seen:
        out.append(f"- **Rang:** {', '.join(ranks_seen)}")
    ident = p.get("identifier")
    if ident:
        out.append(
            f"- **FAUdir-ID:** `{ident}` "
            f"([Profil](https://faudir.fau.de/public/person/{ident}))"
        )
    if p.get("email"):
        out.append(f"- **E-Mail:** {p['email']}")
    if p.get("contacts"):
        out.append("- **Affiliationen:**")
        for c in p["contacts"]:
            org = (c.get("organization") or {}).get("name") or "?"
            fn = c.get("function") or "?"
            fnlabel = (c.get("functionLabel") or {}).get("de") or fn
            phones = ", ".join(c.get("phones") or [])
            phones_s = f" · ☎ {phones}" if phones else ""
            out.append(
                f"  - {org} — *{fnlabel}* (`function={fn}`){phones_s}"
            )
    out.append("")
    return "\n".join(out)


def _shared_header(rank_counts: Counter[str], source: str, total: int, range_label: str) -> str:
    fm: list[str] = ["---", 'kind: "fau-faudir-professoren-chunk"', f"total_persons: {total}"]
    fm.append(f"chunk: {json.dumps(range_label, ensure_ascii=False)}")
    fm.append(f"source: {json.dumps(source, ensure_ascii=False)}")
    fm.append(
        f"scraped_at: {_dt.datetime.now(_dt.timezone.utc).isoformat(timespec='seconds')}"
    )
    if rank_counts:
        fm.append("rank_distribution:")
        for k in ["W1", "W2", "W3", "W?", "apl.", "Hon.", "Junior", "other"]:
            if rank_counts.get(k):
                fm.append(f"  {k}: {rank_counts[k]}")
    fm.append("---")
    fm.append("")
    body = [
        f"# FAUdir — Professor:innen ({range_label})",
        "",
        "Teil-Datei eines alphabetisch chunked Korpus aus FAUdir. Vorbehalte "
        "stehen in der Schwester-Datei `faudir-INDEX.md`.",
        "",
    ]
    return "\n".join(fm + body)


def chunk_persons_by_size(
    persons: list[dict], char_budget: int
) -> list[tuple[str, list[dict]]]:
    """Partition the alphabetically sorted person list into chunks whose
    rendered markdown is below ``char_budget`` chars each. Returns
    ``[(range_label, [persons]), …]`` where ``range_label`` is e.g.
    ``"A-Be"``.
    """
    persons_sorted = sorted(
        persons,
        key=lambda x: (
            (x.get("familyName") or "").lower(),
            (x.get("givenName") or "").lower(),
        ),
    )
    chunks: list[tuple[str, list[dict]]] = []
    cur: list[dict] = []
    cur_size = 0
    for p in persons_sorted:
        md = _person_md(p)
        size = len(md)
        if cur and cur_size + size > char_budget:
            first = cur[0]
            last = cur[-1]
            label = (
                (first.get("familyName") or "")[:3].title()
                + "_"
                + (last.get("familyName") or "")[:3].title()
            )
            chunks.append((label, cur))
            cur = []
            cur_size = 0
        cur.append(p)
        cur_size += size
    if cur:
        first = cur[0]
        last = cur[-1]
        label = (
            (first.get("familyName") or "")[:3].title()
            + "_"
            + (last.get("familyName") or "")[:3].title()
        )
        chunks.append((label, cur))
    return chunks


def render_index_md(
    persons: list[dict], source: str, chunks: list[tuple[str, list[dict]]]
) -> str:
    rank_counts: Counter[str] = Counter()
    for p in persons:
        ranks = set()
        for c in p.get("contacts") or []:
            org = (c.get("organization") or {}).get("name") or ""
            r = parse_w_rank(org)
            if r:
                ranks.add(r)
        if not ranks:
            rank_counts["other"] += 1
        else:
            for r in ranks:
                rank_counts[r] += 1
    fm: list[str] = [
        "---",
        'kind: "fau-faudir-professoren-index"',
        f"total_persons: {len(persons)}",
        f"chunks: {len(chunks)}",
        f"source: {json.dumps(source, ensure_ascii=False)}",
        f"scraped_at: {_dt.datetime.now(_dt.timezone.utc).isoformat(timespec='seconds')}",
        "rank_distribution:",
    ]
    for k in ["W1", "W2", "W3", "W?", "apl.", "Hon.", "Junior", "other"]:
        if rank_counts.get(k):
            fm.append(f"  {k}: {rank_counts[k]}")
    fm.append("---")
    fm.append("")
    body = [
        "# FAUdir — Professor:innen (Übersicht)",
        "",
        "Diese Datei ist die Einstiegsseite für den FAUdir-Personen-Korpus. "
        f"Insgesamt **{len(persons)}** Personen mit professorartiger Funktion "
        "wurden aus FAUdir gepullt; sie liegen in alphabetisch geordneten "
        f"Teil-Dateien (à ~26 k Tokens) im selben Verzeichnis. "
        f"({len(chunks)} Chunks)",
        "",
        "## Vorbehalte",
        "",
        "* FAUdir wird als Self-Service betrieben (Banner auf der Seite: "
        "*„currently still in the test phase, the quality and completeness "
        "of data may vary“*) — Vollständigkeit nicht garantiert.",
        "* **W-Rang-Heuristik:** wir parsen explizite Strings "
        "*„W1-Professur“*, *„W2-Professur“*, *„W3-Professur“* aus dem "
        "Organisationsnamen. Wenn der Name *„Lehrstuhl für …“* lautet "
        "(ohne W-Nummer), markieren wir mit `W?` — solche "
        "Lehrstuhlprofessuren sind in Deutschland *meistens* W3, aber "
        "der RAG-Agent prüft das bei Bedarf bitte selbst.",
        "* `apl.` = außerplanmäßige Professur, `Hon.` = Honorarprofessur, "
        "`Junior` = Juniorprofessur (W1).",
        "",
        "## Rang-Verteilung",
        "",
    ]
    for k in ["W1", "W2", "W3", "W?", "Junior", "apl.", "Hon.", "other"]:
        if rank_counts.get(k):
            body.append(f"- **{k}**: {rank_counts[k]}")
    body.append("")
    body.append("## Chunks")
    body.append("")
    for label, ps in chunks:
        first = ps[0]
        last = ps[-1]
        first_name = f"{first.get('familyName','')}, {first.get('givenName','')}".strip(", ")
        last_name = f"{last.get('familyName','')}, {last.get('givenName','')}".strip(", ")
        body.append(
            f"- [`faudir-{label}.md`](faudir-{label}.md): "
            f"{len(ps)} Personen — *{first_name}* … *{last_name}*"
        )
    body.append("")
    return "\n".join(fm + body)


def render_chunk_md(
    range_label: str, persons: list[dict], source: str, total: int
) -> str:
    rank_counts: Counter[str] = Counter()
    for p in persons:
        ranks = set()
        for c in p.get("contacts") or []:
            org = (c.get("organization") or {}).get("name") or ""
            r = parse_w_rank(org)
            if r:
                ranks.add(r)
        if not ranks:
            rank_counts["other"] += 1
        else:
            for r in ranks:
                rank_counts[r] += 1
    head = _shared_header(rank_counts, source, total, range_label)
    body_parts: list[str] = [head]
    for p in persons:
        body_parts.append(_person_md(p))
    return "\n".join(body_parts).rstrip() + "\n"


# ── main ───────────────────────────────────────────────────────────────────


def main(argv: Iterable[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument(
        "--out",
        type=Path,
        default=Path("data/personen/faudir-professoren.md"),
        help="output markdown path",
    )
    p.add_argument(
        "--queries",
        nargs="+",
        default=["Professur", "Lehrstuhl", "Honorarprofessur", "Juniorprofessur", "Außerplanmäßig"],
        help="search queries to union (each paginated separately). Default "
        "covers W-Professuren + Lehrstühle + Honorar/Junior/apl.",
    )
    p.add_argument("--interval", type=float, default=1.0, help="seconds between requests")
    p.add_argument(
        "--max-pages",
        type=int,
        default=100,
        help="hard pagination cap per query (default 100)",
    )
    p.add_argument(
        "--no-filter",
        action="store_true",
        help="emit every person from the union, not just those with a prof-like "
        "function. Useful for debugging.",
    )
    p.add_argument("-v", "--verbose", action="count", default=0)
    args = p.parse_args(list(argv) if argv else None)

    level = logging.WARNING - 10 * args.verbose
    logging.basicConfig(level=max(level, logging.DEBUG), format="%(levelname)s %(name)s: %(message)s")

    persons = fetch_all_persons(args.queries, interval=args.interval, max_pages_per_query=args.max_pages)
    log.info("union after %d queries: %d persons", len(args.queries), len(persons))
    if not args.no_filter:
        persons = filter_to_professors(persons)
        log.info("after prof-filter: %d persons", len(persons))

    out_dir = args.out.parent
    out_dir.mkdir(parents=True, exist_ok=True)

    # Wipe any previous chunk files so renames don't leave orphans behind.
    for old in out_dir.glob("faudir-*.md"):
        old.unlink()

    chunks = chunk_persons_by_size(persons, _TOKEN_BUDGET_PER_FILE)
    total = sum(len(ps) for _, ps in chunks)

    # Per-chunk files
    for label, ps in chunks:
        chunk_path = out_dir / f"faudir-{label}.md"
        chunk_path.write_text(
            render_chunk_md(label, ps, ENDPOINT, total),
            encoding="utf-8",
        )
        log.info("wrote %s — %d persons", chunk_path, len(ps))

    # INDEX
    index_path = out_dir / "faudir-INDEX.md"
    index_path.write_text(
        render_index_md(persons, ENDPOINT, chunks),
        encoding="utf-8",
    )
    print(
        f"wrote {index_path} + {len(chunks)} chunk file(s) "
        f"({total} persons total)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
