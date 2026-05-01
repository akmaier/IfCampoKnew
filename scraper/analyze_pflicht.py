"""Heuristic Pflicht-Extraktion aus FAU-Prüfungsordnungen.

For each PO-PDF markdown under ``data/pruefungsordnungen/**``:

  1. Find every Markdown section (heading) whose title mentions ``Pflicht``
     (Pflichtmodul, Pflichtbereich, …) and capture the section body.
  2. Additionally grab every paragraph that mentions ``Pflicht*`` *outside*
     of a Pflicht heading — POs often reference Pflicht-modules by number
     (e.g. *"Pflichtmodulen Nrn. 11 und 12"*) inside § paragraphs.
  3. Cross-reference: collect all Campo course titles + program-file
     locations (from the per-period courses-JSON), then list every course
     whose title-tokens appear inside the captured Pflicht text. This is
     a *suggestion* — POs often abbreviate or use module names that
     differ from the Campo course title.

Output: one big ``data/analyse/pflichtveranstaltungen.md`` (kept under the
10-30 k-token bucket via PO-grouping; if it gets too big in future, split).

The user explicitly asked for both this pre-computed analysis (B) **and**
a parallel RAG-driven path (A). This file is intended to serve as
ground-truth for verification once the RAG side is up: a tester compares
the agent's "Profs ohne Pflichtlehre" list against this file's matched
courses + the Campo people index.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import logging
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Iterable

ROOT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT_DIR))

from render_markdown import slugify, node_basename, _parse_frontmatter  # noqa: E402

log = logging.getLogger("campo.analyze_pflicht")


# ──────────────────────────────────────────────────────────────────────────
# heuristics
# ──────────────────────────────────────────────────────────────────────────


# A heading line mentioning Pflicht (any level): "## **§ 42 Mathematische Wahlpflichtmodule**"
# We accept Pflicht as a substring (Pflichtmodul, Wahlpflicht…, Pflichtbereich, …).
# But filter out *Wahlpflicht* — the user asked for hard Pflicht specifically.
_HEADING_RE = re.compile(r"^(#+)\s+(.*?)\s*$", re.MULTILINE)
_PFLICHT_RE = re.compile(r"\bPflicht\w*", re.IGNORECASE)
_WAHLPFLICHT_RE = re.compile(r"\bWahlpflicht\w*", re.IGNORECASE)


def _strip_md_emphasis(s: str) -> str:
    return re.sub(r"\*+([^*]+)\*+", r"\1", s).strip()


def _has_real_pflicht(text: str) -> bool:
    """True if the text mentions ``Pflicht*`` *not* as part of ``Wahlpflicht*``."""
    return bool(re.search(r"(?<!Wahl)Pflicht\w*", text, flags=re.IGNORECASE))


def extract_pflicht_blocks(po_md: str) -> list[dict]:
    """Return ``[{heading_level, heading_text, body, kind}, …]``.

    ``kind`` is ``"section"`` if the entire heading + body refers to Pflicht,
    or ``"paragraph"`` if the heading itself doesn't mention Pflicht but a
    paragraph below it does — we capture only the matching paragraph.
    """
    out: list[dict] = []
    if not po_md:
        return out

    # Find heading positions first.
    headings: list[tuple[int, int, str]] = []  # (start, level, title)
    for m in _HEADING_RE.finditer(po_md):
        headings.append((m.start(), len(m.group(1)), _strip_md_emphasis(m.group(2))))

    if not headings:
        # No headings at all — just dump every Pflicht-paragraph.
        for para in po_md.split("\n\n"):
            if _has_real_pflicht(para):
                out.append({"heading_level": 0, "heading_text": "(no heading)",
                             "body": para.strip(), "kind": "paragraph"})
        return out

    for i, (start, level, title) in enumerate(headings):
        end = headings[i + 1][0] if i + 1 < len(headings) else len(po_md)
        section_body = po_md[start:end]
        # body without its heading
        body_only = section_body.split("\n", 1)[1] if "\n" in section_body else ""

        if _has_real_pflicht(title):
            out.append(
                {
                    "heading_level": level,
                    "heading_text": title,
                    "body": body_only.strip(),
                    "kind": "section",
                }
            )
        else:
            # collect paragraphs that mention Pflicht
            for para in re.split(r"\n{2,}", body_only):
                if _has_real_pflicht(para):
                    out.append(
                        {
                            "heading_level": level,
                            "heading_text": title,
                            "body": para.strip(),
                            "kind": "paragraph",
                        }
                    )
    return out


_TOKEN_RE = re.compile(r"[A-Za-zäöüßÄÖÜ]{5,}")  # ≥5 chars to dodge "Modul"/"Recht"

# Words that appear so often in PO + course titles that they'd cause
# false positives. Drop them from token sets before matching.
_NOISE_TOKENS = {
    "modul", "module", "vorlesung", "uebung", "übung", "seminar", "praktikum",
    "kurs", "veranstaltung", "studienangebot", "pflichtmodul", "wahlpflichtmodul",
    "studierende", "studierenden", "studium", "fach", "faecher", "fächer", "kompetenz",
    "kompetenzen", "ggf", "fpo", "abpo", "absatz", "satz", "anlage", "ects",
    "leistungspunkt", "leistungspunkte", "punkte", "studienarbeit", "bestanden",
    "anfertigung", "anrechnen", "anrechenbar", "abschluss", "fakultaet", "fakultät",
    "studiengang", "studiengangs", "studiengangs", "studienabschnitt", "studienjahr",
    "qualifikationsziel", "qualifikationsziele", "literatur", "termine", "nachweis",
}


def _course_tokens(title: str) -> set[str]:
    """Significant tokens of a course title (≥ 5 chars, lowercased) minus
    common Hochschul-Vokabular."""
    return {t.lower() for t in _TOKEN_RE.findall(title)} - _NOISE_TOKENS


def _path_program_slug(po_md_path: Path) -> str | None:
    """Best-guess Campo program slug from the PO file's path.

    For ``pruefungsordnungen/{faculty}/{program}/file.md`` the program-folder
    name is a strong hint (e.g. ``informatik``, ``mathematik``). For Lehramt
    files we extract the subject token from the filename stem (e.g.
    ``la-informatik-fpo-la-inf-20240904`` → ``informatik``).
    """
    parts = po_md_path.parts
    if "lehramtsfaecher" in parts:
        stem = po_md_path.stem.lower()
        # take the first non-prefix token: "la", "lapo", "1aes", "20la", numeric prefixes
        tokens = [t for t in stem.split("-") if not re.fullmatch(r"\d+(la|lapo|aes)?|la|lapo|aes|[0-9]+", t)]
        if tokens:
            return tokens[0]
    if "pruefungsordnungen" in parts:
        idx = parts.index("pruefungsordnungen")
        # parent folder = program folder
        if len(parts) >= idx + 3 and parts[-1].endswith(".md"):
            program_folder = parts[-2]
            # strip leading number prefixes like "1aes-" if any
            return program_folder.split("/")[-1]
    return None


def match_courses_to_pflicht_text(
    courses: list[dict],
    pflicht_text: str,
    *,
    min_overlap: int = 3,
    program_slug_hint: str | None = None,
) -> list[dict]:
    """Courses whose title shares ≥ ``min_overlap`` ≥5-char non-noise tokens
    with the captured Pflicht text **and** at least covers half the title.

    If ``program_slug_hint`` is given, only courses whose Campo program
    matches that hint (substring on the slugified program name) are
    considered — this stops a Lehramt-Mathe PO from matching every random
    course at FAU.
    """
    pf_lower = pflicht_text.lower()
    matched: list[tuple[int, dict]] = []
    for c in courses:
        title = c.get("title", "")
        tokens = _course_tokens(title)
        if len(tokens) < 2:
            continue
        if program_slug_hint:
            prog_name = c.get("program_name", "").lower()
            prog_slug = re.sub(r"[^a-z0-9]+", "-", prog_name)
            if program_slug_hint not in prog_slug:
                continue
        overlap = sum(1 for t in tokens if t in pf_lower)
        if overlap < min_overlap:
            continue
        if overlap < max(2, len(tokens) // 2):
            continue
        matched.append((overlap, c))
    matched.sort(key=lambda p: (-p[0], p[1].get("title", "")))
    return [c for _, c in matched]


# ──────────────────────────────────────────────────────────────────────────
# rendering
# ──────────────────────────────────────────────────────────────────────────


def render_analyse_md(
    by_po: dict[str, dict],
    period_label: str,
    out_root: Path,
    target_md: Path,
) -> str:
    lines: list[str] = []
    lines.append("---")
    lines.append('kind: "campo-pflicht-analyse"')
    lines.append(f'period: {json.dumps(period_label, ensure_ascii=False)}')
    lines.append(f"po_files_scanned: {len(by_po)}")
    total_courses = sum(len(d['matched_courses']) for d in by_po.values())
    lines.append(f"matched_courses_total: {total_courses}")
    lines.append(
        f"scraped_at: {_dt.datetime.now(_dt.timezone.utc).isoformat(timespec='seconds')}"
    )
    lines.append("---")
    lines.append("")
    lines.append("# Pflichtveranstaltungen — Heuristische Analyse")
    lines.append("")
    lines.append(
        "Diese Datei wird **automatisch** aus den Markdown-Versionen der "
        "FAU-Prüfungsordnungen erzeugt. Pro PO werden alle "
        "Markdown-Abschnitte und Absätze aufgelistet, die das Wort "
        "*Pflicht* (ohne *Wahlpflicht*) enthalten. Anschließend werden "
        "Campo-Veranstaltungen vorgeschlagen, deren Titel mit der Pflicht-"
        "Textstelle terminologisch überlappt — als **Vorschlag**, nicht "
        "autoritativ. PO-Texte sind nicht standardisiert; viele Module "
        "stehen in einer separaten Anlage und werden nur in den §-Texten "
        "über Nummern referenziert."
    )
    lines.append("")
    lines.append("## Vorbehalte")
    lines.append("")
    lines.append(
        "* Module-Namen vs Veranstaltungs-Titel: ein Pflichtmodul "
        "*\"Algorithmen und Datenstrukturen\"* taucht in Campo häufig als "
        "*\"Algorithmen und Datenstrukturen 1 - Vorlesung\"* + "
        "*\"...übung\"* auf. Beide Veranstaltungs-Einträge zählen hier als "
        "Treffer."
    )
    lines.append(
        "* Die Heuristik filtert *Wahlpflicht\\** explizit raus, aber andere "
        "Sonderbereiche (\"Schwerpunktbereich\", \"Vertiefungsfach\") "
        "werden **nicht** als Pflicht gewertet — auch wenn sie für "
        "individuelle Studierende verbindlich sein können."
    )
    lines.append(
        "* Diese Datei dient als **Vergleichsgrundlage** für die "
        "RAG-Antwort auf dieselbe Frage, nicht als alleinige Quelle."
    )
    lines.append("")
    lines.append(f"**Quellperiode für Veranstaltungs-Matches:** {period_label}")
    lines.append("")
    lines.append("## PO-Dateien mit Pflicht-Mentions")
    lines.append("")

    # One section per PO
    for po_rel in sorted(by_po.keys()):
        d = by_po[po_rel]
        title = d["title"] or po_rel
        # relative link to the PO from the analyse/ folder
        po_link = f"../{po_rel}"
        lines.append(f"### {title}")
        lines.append("")
        lines.append(f"PO-Quelle: [`{po_rel}`]({po_link})  ")
        lines.append(f"Pflicht-Stellen gefunden: **{len(d['blocks'])}**  ")
        lines.append(f"Vorgeschlagene Pflichtveranstaltungen: **{len(d['matched_courses'])}**")
        lines.append("")
        if d["matched_courses"]:
            lines.append("#### Pflichtveranstaltungen (Vorschlag)")
            lines.append("")
            # Group courses by program for nicer presentation
            by_prog: dict[tuple[str, str], list[dict]] = defaultdict(list)
            for c in d["matched_courses"]:
                key = (c.get("program_name", ""), c.get("program_segment", ""))
                by_prog[key].append(c)
            for (pname, _pseg), evts in sorted(by_prog.items()):
                if pname:
                    lines.append(f"**Studiengang:** {pname}")
                    lines.append("")
                for c in evts:
                    title_str = c.get("title", "?")
                    ctype = c.get("course_type") or ""
                    # extract instructor names if any
                    insts = ", ".join(c.get("instructors_resp") or []) or ""
                    insts_x = ", ".join(c.get("instructors_exec") or [])
                    inst_str = insts or insts_x or ""
                    suffix = f" — {inst_str}" if inst_str else ""
                    rel = c.get("program_rel_path", "")
                    if rel:
                        lines.append(
                            f"- [{title_str} — {ctype}]({rel}){suffix}"
                        )
                    else:
                        lines.append(f"- {title_str} — {ctype}{suffix}")
                lines.append("")

        # Show the Pflicht-text excerpts (cap to 4, max 800 chars each).
        if d["blocks"]:
            lines.append("#### Auszüge aus dem PO-Text")
            lines.append("")
            for blk in d["blocks"][:4]:
                lines.append(f"**{blk['heading_text']}** _({blk['kind']})_")
                lines.append("")
                excerpt = blk["body"].strip()
                if len(excerpt) > 800:
                    excerpt = excerpt[:800] + " …"
                lines.append(excerpt)
                lines.append("")
            if len(d["blocks"]) > 4:
                lines.append(f"_(+ {len(d['blocks']) - 4} weitere Treffer in dieser PO — "
                             f"siehe das vollständige PO-Dokument)_")
                lines.append("")
        lines.append("---")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


# ──────────────────────────────────────────────────────────────────────────
# main
# ──────────────────────────────────────────────────────────────────────────


def render_lehrende_ohne_pflicht_md(
    courses_with_meta: list[dict],
    pflicht_unit_ids: set[int],
    period_label: str,
) -> str:
    """Produce a list of Lehrende whose courses (in the matched period) are
    *not* among the courses heuristically flagged as Pflicht.

    This is the user's "Profs ohne Pflichtlehre"-style cross-check — minus
    the W-status filter (which depends on FAUdir, not yet integrated).
    Intended as Verifikations-Vergleichsmaterial against the RAG-driven
    answer to the same question.
    """
    # name → {pflicht_courses, other_courses}
    by_person: dict[str, dict] = defaultdict(
        lambda: {"pflicht": [], "other": [], "title": ""}
    )
    for c in courses_with_meta:
        uid = int(c["unit_id"])
        is_pflicht = uid in pflicht_unit_ids
        names: set[str] = set()
        for n in (c.get("instructors_resp") or []) + (c.get("instructors_exec") or []):
            names.add(n.strip())
        for a in c.get("appointments") or []:
            for n in a.get("instructors") or []:
                names.add(n.strip())
        for full in names:
            if not full:
                continue
            entry = by_person[full]
            target = entry["pflicht"] if is_pflicht else entry["other"]
            target.append(c)

    # Filter: only Lehrende with **at least one** matching course but **none**
    # marked Pflicht.
    candidates: list[tuple[str, list[dict]]] = []
    for full, info in by_person.items():
        if info["pflicht"]:
            continue
        if not info["other"]:
            continue
        # Heuristic priority: focus on plausible "Profs". The user wants W1/W2/W3
        # eventually — we approximate by looking for "Prof" in the name string.
        is_prof = "prof" in full.lower()
        candidates.append((full, info["other"], is_prof))

    candidates.sort(key=lambda t: (not t[2], t[0].lower()))

    lines: list[str] = [
        "---",
        'kind: "campo-lehrende-ohne-pflicht"',
        f'period: {json.dumps(period_label, ensure_ascii=False)}',
        f"candidates: {len(candidates)}",
        f"scraped_at: {_dt.datetime.now(_dt.timezone.utc).isoformat(timespec='seconds')}",
        "---",
        "",
        "# Lehrende ohne Pflichtlehre (Vorschlag)",
        "",
        "Liste der Personen, die in der angegebenen Periode mindestens **eine** "
        "Veranstaltung in Campo halten, aber **keine** der heuristisch als "
        "Pflichtveranstaltung markierten Kurse (siehe `pflichtveranstaltungen.md` "
        "im selben Verzeichnis).",
        "",
        "## Vorbehalte",
        "",
        "* Akademischer Rang (W1/W2/W3) ist hier **nicht** ausgewiesen — Campo "
        "  liefert nur den Namens-String. Die *is_prof*-Markierung erkennt "
        "  lediglich die Zeichenkette \"Prof\" im Namen und ist deshalb "
        "  bestenfalls eine Heuristik. Für die genaue W1/W2/W3-Zuordnung wird "
        "  eine FAUdir-Integration benötigt (siehe `personen/INDEX.md`).",
        "* **Falsch-Positive sind sehr wahrscheinlich.** Die Pflicht-"
        "  Klassifikation in `pflichtveranstaltungen.md` ist heuristisch und "
        "  unvollständig (PO-Texte sind unstandardisiert; viele Pflichtmodule "
        "  stehen nur in Anlagen). Eine Person ohne markierte Pflichtlehre "
        "  kann in Wirklichkeit eine Pflichtveranstaltung halten, deren "
        "  PO-Match die Heuristik nicht hergegeben hat.",
        "* Diese Datei dient als **Vergleichsgrundlage** zur RAG-Antwort auf "
        "  dieselbe Frage. Bei Inkonsistenz ist die RAG-Antwort meist "
        "  belastbarer, weil ein Sprachmodell die Modul-zu-Veranstaltungs-"
        "  Zuordnung mit mehr Kontext lösen kann.",
        "",
        f"**Periode:** {period_label}",
        "",
        f"**Kandidaten gefunden:** {len(candidates)} "
        f"(davon {sum(1 for _, _, p in candidates if p)} mit \"Prof\" im Namen)",
        "",
        "## Liste",
        "",
    ]
    for full, others, is_prof in candidates:
        title, plain = "", ""
        from people_index import split_title  # noqa: WPS433
        title, plain = split_title(full)
        head = plain or full
        prof_tag = " — **(Prof.)**" if is_prof else ""
        lines.append(f"### {head}{prof_tag}")
        if title:
            lines.append(f"  *Titel:* `{title}`")
        lines.append(f"- Veranstaltungen ohne Pflicht-Markierung: **{len(others)}**")
        # group by program
        by_prog: dict[str, list[dict]] = defaultdict(list)
        for c in others:
            by_prog[c.get("program_name", "?")].append(c)
        for pname, evts in by_prog.items():
            for c in evts:
                title_str = c.get("title", "?")
                ctype = c.get("course_type") or ""
                rel = c.get("program_rel_path", "")
                if rel:
                    lines.append(f"  - in [{pname}]({rel}): \"{title_str}\" — {ctype}")
                else:
                    lines.append(f"  - in {pname}: \"{title_str}\" — {ctype}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main(argv: Iterable[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument(
        "--data",
        type=Path,
        default=Path("data"),
        help="corpus root containing pruefungsordnungen/ and {period}/",
    )
    p.add_argument(
        "--period",
        type=int,
        required=True,
        help="periodId for the courses-JSON to use for cross-reference (e.g. 589)",
    )
    p.add_argument(
        "--tree",
        type=Path,
        required=True,
        help="path to the period's tree JSON, e.g. tmp/589.json",
    )
    p.add_argument(
        "--courses",
        type=Path,
        required=True,
        help="path to the period's courses JSON, e.g. tmp/589-courses.json",
    )
    p.add_argument(
        "--out",
        type=Path,
        default=Path("data/analyse/pflichtveranstaltungen.md"),
        help="output markdown path",
    )
    p.add_argument("-v", "--verbose", action="count", default=0)
    args = p.parse_args(list(argv) if argv else None)

    level = logging.WARNING - 10 * args.verbose
    logging.basicConfig(level=max(level, logging.DEBUG), format="%(levelname)s %(name)s: %(message)s")

    snapshot = json.loads(args.tree.read_text(encoding="utf-8"))
    courses_data = json.loads(args.courses.read_text(encoding="utf-8"))
    period_name = snapshot.get("periodName", f"period-{args.period}")
    period_slug = f"{args.period}-{slugify(period_name)}"

    # Build per-course metadata (title + program info)
    by_segment = {n["segment"]: n for n in snapshot["nodes"]}
    courses_with_meta: list[dict] = []
    for c in courses_data.get("courses", []):
        uid = int(c["unit_id"])
        # find the catalog node matching this unit_id (look it up via path)
        program: dict | None = None
        for n in snapshot["nodes"]:
            if n.get("unitId") == uid and len(n["path"]) >= 3:
                program = by_segment.get(n["path"][2])
                break
        if program is None:
            continue
        program_node_id = int(program["segment"].split(":", 1)[1])
        rel = (
            f"../{period_slug}/{slugify(program['name'])[:88]}-{program_node_id}.md"
        )
        courses_with_meta.append({**c,
                                  "program_name": program["name"],
                                  "program_segment": program["segment"],
                                  "program_rel_path": rel})

    log.info("ingested %d courses with program info", len(courses_with_meta))

    po_root = args.data / "pruefungsordnungen"
    if not po_root.is_dir():
        log.warning("no PO directory at %s — nothing to do", po_root)
        return 0

    by_po: dict[str, dict] = {}
    pos_seen = 0
    pos_with_pflicht = 0
    for po_md_path in sorted(po_root.rglob("*.md")):
        if po_md_path.name == "INDEX.md":
            continue
        pos_seen += 1
        text = po_md_path.read_text(encoding="utf-8", errors="replace")
        fm = _parse_frontmatter(po_md_path)
        title = fm.get("title", po_md_path.stem)
        blocks = extract_pflicht_blocks(text)
        if not blocks:
            continue
        pos_with_pflicht += 1
        # combine all Pflicht text and find courses
        pflicht_text = "\n\n".join(b["body"] for b in blocks)
        slug_hint = _path_program_slug(po_md_path)
        matched = match_courses_to_pflicht_text(
            courses_with_meta, pflicht_text, program_slug_hint=slug_hint
        )
        # The user-facing analysis is most useful for POs that *do* match
        # courses we know about. POs that mention Pflicht but don't match
        # our depth-4 course set are recorded as a count only — including
        # their full text would balloon the file to MB-scale legal prose
        # for little value.
        if not matched:
            continue
        rel = str(po_md_path.relative_to(args.data))
        by_po[rel] = {"title": title, "blocks": blocks, "matched_courses": matched}

    log.info(
        "scanned %d PO files; %d had Pflicht mentions; %d also matched ≥1 course",
        pos_seen, pos_with_pflicht, len(by_po),
    )

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(
        render_analyse_md(by_po, period_name, args.data, args.out),
        encoding="utf-8",
    )

    # ── Companion file: Lehrende ohne Pflichtlehre ───────────────────
    pflicht_unit_ids: set[int] = set()
    for d in by_po.values():
        for c in d["matched_courses"]:
            pflicht_unit_ids.add(int(c["unit_id"]))
    out_persons = args.out.parent / "lehrende-ohne-pflicht.md"
    out_persons.write_text(
        render_lehrende_ohne_pflicht_md(courses_with_meta, pflicht_unit_ids, period_name),
        encoding="utf-8",
    )

    print(
        f"wrote {args.out}: po_files={len(by_po)} "
        f"matched_courses={sum(len(d['matched_courses']) for d in by_po.values())} "
        f"unique_pflicht_unit_ids={len(pflicht_unit_ids)}"
    )
    print(f"wrote {out_persons}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
