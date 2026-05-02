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
from people_index import split_concatenated_names  # noqa: E402

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

    If ``program_slug_hint`` is given, courses whose program *is* known and
    doesn't match the hint are dropped; courses **without** known program
    info (sweep-only) stay in the candidate pool — token-overlap is the
    only gate for them.
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
            if prog_name:
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


def load_structured_pflicht_modules(po_root: Path) -> dict[Path, list[dict]]:
    """Reuse :mod:`extract_pflicht_module` to get structured Pflicht-module
    names per PO. This is a strictly better match source than free-text
    Pflicht-paragraphs because it lists module names parsed from Anlage
    tables (e.g. ``Analysis I``, ``Lineare Algebra II``)."""
    try:
        from extract_pflicht_module import collect_per_po
    except Exception as e:  # noqa: BLE001
        log.warning("extract_pflicht_module unavailable (%s)", e)
        return {}
    per_po = collect_per_po(po_root)
    return {p: d["modules"] for p, d in per_po.items()}


def match_courses_to_module_names(
    courses: list[dict],
    module_names: list[str],
    *,
    program_slug_hint: str | None = None,
    min_overlap: int = 2,
) -> list[dict]:
    """Match Campo courses to *structured* Pflichtmodul-Bezeichnungen.

    Stricter than the free-text Pflicht-paragraph match: we require ≥
    ``min_overlap`` ≥5-char non-noise tokens of the **module name** to
    appear in the course title. Because module names are short
    (``Analysis I`` = 2 tokens), even ``min_overlap=2`` keeps the
    precision tight.
    """
    matched: list[tuple[int, dict]] = []
    if program_slug_hint:
        h = program_slug_hint.lower()
        course_pool = [
            c for c in courses
            if not c.get("program_name")
            or h in re.sub(r"[^a-z0-9]+", "-", c["program_name"].lower())
        ]
    else:
        course_pool = courses
    for module_name in module_names:
        mod_tokens = _course_tokens(module_name)
        if len(mod_tokens) < 2:
            continue
        for c in course_pool:
            ctitle = c.get("title", "").lower()
            overlap = sum(1 for t in mod_tokens if t in ctitle)
            if overlap < min_overlap:
                continue
            if overlap < max(2, len(mod_tokens) // 2):
                continue
            matched.append((overlap, c))
    # Dedupe by unit_id
    seen: set[int] = set()
    out: list[dict] = []
    for _, c in sorted(matched, key=lambda p: -p[0]):
        uid = int(c["unit_id"])
        if uid in seen:
            continue
        seen.add(uid)
        out.append(c)
    return out


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


def _norm_name(s: str) -> str:
    """Normalize a name for fuzzy comparison: lowercase, strip titles."""
    s = s.lower()
    # Strip common title tokens
    s = re.sub(
        r"\b(prof\.?|dr\.?(-ing\.?| ?med\.?| ?phil\.?| ?rer\.?\s*nat\.?| ?habil\.?| ?hc\.?)?|"
        r"univ\.?-prof\.?|hon\.?-?prof\.?|pd|apl\.?|em\.?|dipl\.?(-ing\.?)?|m\.?sc\.?|b\.?sc\.?|mba)"
        r"\b",
        "",
        s,
    )
    s = re.sub(r"[^\w\säöüß]", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def load_faudir_lookup(faudir_json_path: Path) -> dict[str, dict]:
    """Read ``tmp/faudir-persons.json`` → ``{normalised_name: faudir_entry}``.

    The same FAUdir entry is keyed under multiple normalised names so the
    Campo instructor string can match either ``Vorname Nachname``,
    ``Nachname, Vorname`` or just ``Nachname``.
    """
    if not faudir_json_path.exists():
        return {}
    try:
        data = json.loads(faudir_json_path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}
    out: dict[str, dict] = {}
    for p in data.get("persons", []):
        last = (p.get("familyName") or "").strip()
        first = (p.get("givenName") or "").strip()
        if not last:
            continue
        # Build candidate keys
        keys = {
            _norm_name(f"{first} {last}"),
            _norm_name(f"{last} {first}"),
            _norm_name(f"{last}, {first}"),
            _norm_name(last),
        }
        # Determine W-rank set across affiliations
        ranks: list[str] = []
        for c in p.get("contacts") or []:
            from faudir_scrape import parse_w_rank  # noqa: WPS433
            org = (c.get("organization") or {}).get("name") or ""
            r = parse_w_rank(org)
            if r and r not in ranks:
                ranks.append(r)
        entry = {
            "identifier": p.get("identifier"),
            "personalTitle": p.get("personalTitle") or "",
            "givenName": first,
            "familyName": last,
            "ranks": ranks,
            "affiliations": [
                (c.get("organization") or {}).get("name") or ""
                for c in (p.get("contacts") or [])
            ],
        }
        for k in keys:
            if k:
                out[k] = entry  # last write wins; ambiguous names get any one
    return out


def fuzzy_lookup_faudir(campo_name: str, faudir_lookup: dict[str, dict]) -> dict | None:
    """Try several normalisations of the Campo string against the FAUdir lookup."""
    candidates = [campo_name]
    # also try the part after the last comma / dot
    candidates.append(re.sub(r"^.*?,\s*", "", campo_name))
    candidates.append(re.sub(r"^[^,]+,\s*", "", campo_name))  # if "Last, First"
    for cand in candidates:
        norm = _norm_name(cand)
        if norm in faudir_lookup:
            return faudir_lookup[norm]
        # also try just the surname (last token)
        toks = norm.split()
        if toks:
            last_only = toks[-1]
            if last_only in faudir_lookup:
                return faudir_lookup[last_only]
    return None


def render_profs_ohne_pflichtlehre_md(
    courses_with_meta: list[dict],
    pflicht_unit_ids: set[int],
    period_label: str,
    faudir_lookup: dict[str, dict],
) -> str:
    """The "real" answer to the user's question — W1/W2/W3-Profs aus FAUdir,
    die in der Periode keine Pflichtveranstaltung halten."""
    # name-string → {pflicht: [course], other: [course], faudir: entry|None}
    by_person: dict[str, dict] = defaultdict(
        lambda: {"pflicht": [], "other": [], "faudir": None}
    )
    for c in courses_with_meta:
        uid = int(c["unit_id"])
        is_pflicht = uid in pflicht_unit_ids
        names: set[str] = set()
        for raw in (c.get("instructors_resp") or []) + (c.get("instructors_exec") or []):
            for n in split_concatenated_names(raw):
                names.add(n.strip())
        for a in c.get("appointments") or []:
            for raw in a.get("instructors") or []:
                for n in split_concatenated_names(raw):
                    names.add(n.strip())
        for full in names:
            if not full:
                continue
            entry = by_person[full]
            (entry["pflicht"] if is_pflicht else entry["other"]).append(c)
            if entry["faudir"] is None:
                entry["faudir"] = fuzzy_lookup_faudir(full, faudir_lookup)

    # Filter to FAUdir-confirmed Profs with no Pflicht teaching
    candidates: list[tuple[str, dict]] = []
    for full, info in by_person.items():
        if info["pflicht"]:
            continue
        if not info["other"]:
            continue
        fau = info["faudir"]
        if not fau:
            continue
        # FAUdir-confirmed prof, no Pflicht-flagged courses
        candidates.append((full, info))

    # Group by primary rank
    by_rank: dict[str, list[tuple[str, dict]]] = defaultdict(list)
    for full, info in candidates:
        ranks = info["faudir"]["ranks"] or ["W?"]
        primary = ranks[0]
        by_rank[primary].append((full, info))

    rank_order = ["W3", "W2", "W1", "W?", "Junior", "apl.", "Hon."]
    lines: list[str] = [
        "---",
        'kind: "profs-ohne-pflichtlehre"',
        f'period: {json.dumps(period_label, ensure_ascii=False)}',
        f"candidates_total: {len(candidates)}",
        "rank_distribution:",
    ]
    for r in rank_order:
        if by_rank.get(r):
            lines.append(f"  {r}: {len(by_rank[r])}")
    lines.append(
        f"scraped_at: {_dt.datetime.now(_dt.timezone.utc).isoformat(timespec='seconds')}"
    )
    lines.append("---")
    lines.append("")
    lines.append("# Profs ohne Pflichtlehre (FAUdir × Campo)")
    lines.append("")
    lines.append(
        "Liste der **FAUdir-bestätigten Professor:innen**, die in der "
        "angegebenen Periode mindestens eine Veranstaltung in Campo halten, "
        "aber **keine** der heuristisch als Pflichtveranstaltung markierten "
        "Kurse (siehe `pflichtveranstaltungen.md`)."
    )
    lines.append("")
    lines.append("## Vorbehalte")
    lines.append("")
    lines.append(
        "* **W-Rang-Heuristik:** ergibt sich aus dem Organisationsnamen in "
        "FAUdir. `W3`/`W2`/`W1` sind explizit aus *„W3-Professur“* etc. "
        "abgeleitet; `W?` bezeichnet Lehrstühle/Professuren ohne expliziten "
        "W-Code im Namen (de facto meistens W3)."
    )
    lines.append(
        "* **Pflicht-Klassifikation** ist heuristisch (siehe "
        "`pflichtveranstaltungen.md`). Falsch-Negative (verpasste Pflicht-"
        "Module) → der/die Prof landet hier irrtümlich."
    )
    lines.append(
        "* **Namens-Matching** Campo ↔ FAUdir geht über fuzzy-normalisierte "
        "Strings (Titel-Präfix entfernt, Sonderzeichen normalisiert). "
        "Mehrdeutige Namen (z. B. zwei Profs mit demselben Nachnamen) "
        "werden hier zur ersten Treffer-Variante zugeordnet."
    )
    lines.append(
        "* Diese Datei dient als **Vergleichsgrundlage (B)** für die "
        "RAG-Antwort (A) auf dieselbe Frage. Bei Inkonsistenz ist die "
        "RAG-Antwort meist belastbarer."
    )
    lines.append("")
    lines.append(f"**Periode:** {period_label}  ")
    lines.append(f"**Kandidaten:** {len(candidates)} FAUdir-bestätigte Profs ohne Pflichtlehre")
    lines.append("")
    lines.append("## Verteilung nach W-Rang")
    lines.append("")
    for r in rank_order:
        if by_rank.get(r):
            lines.append(f"- **{r}**: {len(by_rank[r])}")
    lines.append("")
    for r in rank_order:
        if not by_rank.get(r):
            continue
        lines.append(f"## Rang {r}")
        lines.append("")
        for full, info in sorted(by_rank[r], key=lambda t: (t[1]["faudir"]["familyName"].lower(), t[0].lower())):
            fau = info["faudir"]
            name = f"{fau['familyName']}, {fau['givenName']}".strip(", ")
            title = fau.get("personalTitle") or ""
            ident = fau.get("identifier") or ""
            lines.append(f"### {name} ({title})")
            if ident:
                lines.append(f"- **FAUdir:** [`{ident}`](https://faudir.fau.de/public/person/{ident})")
            if fau["affiliations"]:
                primary = fau["affiliations"][0]
                lines.append(f"- **Affiliation:** {primary}")
                if len(fau["affiliations"]) > 1:
                    lines.append(
                        f"- **Weitere Affiliationen:** "
                        f"{'; '.join(fau['affiliations'][1:])}"
                    )
            lines.append(
                f"- **Veranstaltungen ohne Pflicht-Markierung:** {len(info['other'])}"
            )
            for c in info["other"][:10]:
                title_str = c.get("title", "?")
                ctype = c.get("course_type") or ""
                rel = c.get("program_rel_path", "")
                pname = c.get("program_name", "?")
                if rel:
                    lines.append(f"  - in [{pname}]({rel}): \"{title_str}\" — {ctype}")
                else:
                    lines.append(f"  - in {pname}: \"{title_str}\" — {ctype}")
            if len(info["other"]) > 10:
                lines.append(f"  - … und {len(info['other'])-10} weitere")
            lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def render_profs_mit_pflichtlehre_md(
    courses_with_meta: list[dict],
    pflicht_unit_ids: set[int],
    period_label: str,
    faudir_lookup: dict[str, dict],
) -> str:
    """The companion of ``profs-ohne-pflichtlehre.md`` — FAUdir-confirmed
    Professor:innen, die in der Periode mindestens eine Pflichtveranstaltung
    halten. Same FAUdir matching + W-Rang grouping; opposite Pflicht filter.
    """
    by_person: dict[str, dict] = defaultdict(
        lambda: {"pflicht": [], "other": [], "faudir": None}
    )
    for c in courses_with_meta:
        uid = int(c["unit_id"])
        is_pflicht = uid in pflicht_unit_ids
        names: set[str] = set()
        for raw in (c.get("instructors_resp") or []) + (c.get("instructors_exec") or []):
            for n in split_concatenated_names(raw):
                names.add(n.strip())
        for a in c.get("appointments") or []:
            for raw in a.get("instructors") or []:
                for n in split_concatenated_names(raw):
                    names.add(n.strip())
        for full in names:
            if not full:
                continue
            entry = by_person[full]
            (entry["pflicht"] if is_pflicht else entry["other"]).append(c)
            if entry["faudir"] is None:
                entry["faudir"] = fuzzy_lookup_faudir(full, faudir_lookup)

    candidates: list[tuple[str, dict]] = []
    for full, info in by_person.items():
        if not info["pflicht"]:
            continue
        if info["faudir"] is None:
            continue
        candidates.append((full, info))

    by_rank: dict[str, list[tuple[str, dict]]] = defaultdict(list)
    for full, info in candidates:
        ranks = info["faudir"]["ranks"] or ["W?"]
        primary = ranks[0]
        by_rank[primary].append((full, info))

    rank_order = ["W3", "W2", "W1", "W?", "Junior", "apl.", "Hon."]
    lines: list[str] = [
        "---",
        'kind: "profs-mit-pflichtlehre"',
        f'period: {json.dumps(period_label, ensure_ascii=False)}',
        f"candidates_total: {len(candidates)}",
        "rank_distribution:",
    ]
    for r in rank_order:
        if by_rank.get(r):
            lines.append(f"  {r}: {len(by_rank[r])}")
    lines.append(
        f"scraped_at: {_dt.datetime.now(_dt.timezone.utc).isoformat(timespec='seconds')}"
    )
    lines.append("---")
    lines.append("")
    lines.append("# Profs mit Pflichtlehre (FAUdir × Campo)")
    lines.append("")
    lines.append(
        "Liste der **FAUdir-bestätigten Professor:innen**, die in der "
        "angegebenen Periode mindestens **eine** der heuristisch als "
        "Pflichtveranstaltung markierten Veranstaltungen halten. Komplement "
        "zu [`profs-ohne-pflichtlehre.md`](profs-ohne-pflichtlehre.md) — "
        "zusammen partitionieren beide Dateien die FAUdir-bestätigten "
        "Lehrenden in *mit* und *ohne* Pflichtlehre."
    )
    lines.append("")
    lines.append("## Vorbehalte")
    lines.append("")
    lines.append(
        "* **Pflicht-Heuristik:** siehe `pflichtveranstaltungen.md`. "
        "Falsch-Positive (eine Veranstaltung wird irrtümlich als Pflicht "
        "markiert) → der/die Prof landet hier irrtümlich als pflichtlehrend."
    )
    lines.append(
        "* **W-Rang** stammt aus dem FAUdir-Organisationsnamen (W3/W2/W1 "
        "explizit aus *„Wn-Professur“*; `W?` für Lehrstühle ohne explizites "
        "W in der Bezeichnung — meist W3)."
    )
    lines.append(
        "* Pro Person werden bis zu 10 Pflichtveranstaltungen aufgelistet; "
        "weitere werden gezählt aber nicht aufgeführt. Nicht-Pflicht-"
        "Veranstaltungen erscheinen hier *nicht* — die finden sich in der "
        "Programmdatei der jeweiligen Veranstaltung."
    )
    lines.append(
        "* Vergleichsgrundlage (B) für die RAG-Antwort (A); bei "
        "Inkonsistenz ist die RAG-Antwort meist belastbarer."
    )
    lines.append("")
    lines.append(f"**Periode:** {period_label}  ")
    lines.append(
        f"**Kandidaten:** {len(candidates)} FAUdir-bestätigte Profs mit Pflichtlehre"
    )
    lines.append("")
    lines.append("## Verteilung nach W-Rang")
    lines.append("")
    for r in rank_order:
        if by_rank.get(r):
            lines.append(f"- **{r}**: {len(by_rank[r])}")
    lines.append("")
    for r in rank_order:
        if not by_rank.get(r):
            continue
        lines.append(f"## Rang {r}")
        lines.append("")
        for full, info in sorted(
            by_rank[r],
            key=lambda t: (t[1]["faudir"]["familyName"].lower(), t[0].lower()),
        ):
            fau = info["faudir"]
            name = f"{fau['familyName']}, {fau['givenName']}".strip(", ")
            title = fau.get("personalTitle") or ""
            ident = fau.get("identifier") or ""
            lines.append(f"### {name} ({title})")
            if ident:
                lines.append(
                    f"- **FAUdir:** [`{ident}`](https://faudir.fau.de/public/person/{ident})"
                )
            if fau["affiliations"]:
                primary = fau["affiliations"][0]
                lines.append(f"- **Affiliation:** {primary}")
                if len(fau["affiliations"]) > 1:
                    lines.append(
                        f"- **Weitere Affiliationen:** "
                        f"{'; '.join(fau['affiliations'][1:])}"
                    )
            lines.append(
                f"- **Pflichtveranstaltungen (heuristisch):** {len(info['pflicht'])}"
            )
            for c in info["pflicht"][:10]:
                title_str = c.get("title", "?")
                ctype = c.get("course_type") or ""
                rel = c.get("program_rel_path", "")
                pname = c.get("program_name", "?")
                if rel:
                    lines.append(f"  - in [{pname}]({rel}): \"{title_str}\" — {ctype}")
                else:
                    lines.append(f"  - in {pname}: \"{title_str}\" — {ctype}")
            if len(info["pflicht"]) > 10:
                lines.append(f"  - … und {len(info['pflicht'])-10} weitere")
            if info["other"]:
                lines.append(
                    f"- *(zusätzlich {len(info['other'])} Nicht-Pflicht-Veranstaltungen "
                    "— hier nicht aufgeführt)*"
                )
            lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def render_lehrende_ohne_pflicht_md(
    courses_with_meta: list[dict],
    pflicht_unit_ids: set[int],
    period_label: str,
    *,
    faudir_lookup: dict[str, dict] | None = None,
) -> str:
    """Produce a list of Lehrende whose courses (in the matched period) are
    *not* among the courses heuristically flagged as Pflicht — **excluding**
    every person already cross-referenced into FAUdir (those live in
    ``profs-ohne-pflichtlehre.md``).

    Intended as Verifikations-Vergleichsmaterial against the RAG-driven
    answer to the same question — focused on the *remaining* Lehrende
    that are *not* W-Profs in FAUdir (Lehrbeauftragte, externe Dozent:innen,
    Professor:innen ohne FAUdir-Match …). Together with
    ``profs-ohne-pflichtlehre.md`` the union is exhaustive without
    duplicates.
    """
    # name → {pflicht_courses, other_courses}
    by_person: dict[str, dict] = defaultdict(
        lambda: {"pflicht": [], "other": [], "title": ""}
    )
    for c in courses_with_meta:
        uid = int(c["unit_id"])
        is_pflicht = uid in pflicht_unit_ids
        names: set[str] = set()
        for raw in (c.get("instructors_resp") or []) + (c.get("instructors_exec") or []):
            for n in split_concatenated_names(raw):
                names.add(n.strip())
        for a in c.get("appointments") or []:
            for raw in a.get("instructors") or []:
                for n in split_concatenated_names(raw):
                    names.add(n.strip())
        for full in names:
            if not full:
                continue
            entry = by_person[full]
            target = entry["pflicht"] if is_pflicht else entry["other"]
            target.append(c)

    faudir_lookup = faudir_lookup or {}

    # Filter: only Lehrende with **at least one** matching course but **none**
    # marked Pflicht **and** no FAUdir match (so they don't double-appear in
    # profs-ohne-pflichtlehre.md).
    candidates: list[tuple[str, list[dict], bool]] = []
    skipped_due_to_faudir = 0
    for full, info in by_person.items():
        if info["pflicht"]:
            continue
        if not info["other"]:
            continue
        if faudir_lookup and fuzzy_lookup_faudir(full, faudir_lookup) is not None:
            skipped_due_to_faudir += 1
            continue
        is_prof = "prof" in full.lower()
        candidates.append((full, info["other"], is_prof))

    candidates.sort(key=lambda t: (not t[2], t[0].lower()))

    lines: list[str] = [
        "---",
        'kind: "campo-lehrende-ohne-pflicht"',
        f'period: {json.dumps(period_label, ensure_ascii=False)}',
        f"candidates: {len(candidates)}",
        f"excluded_because_in_faudir: {skipped_due_to_faudir}",
        f"scraped_at: {_dt.datetime.now(_dt.timezone.utc).isoformat(timespec='seconds')}",
        "---",
        "",
        "# Lehrende ohne Pflichtlehre — *ohne FAUdir-Match*",
        "",
        "Liste der Personen, die in der angegebenen Periode mindestens **eine** "
        "Veranstaltung in Campo halten, aber **keine** der heuristisch als "
        "Pflichtveranstaltung markierten Kurse (siehe `pflichtveranstaltungen.md` "
        "im selben Verzeichnis) — und die **nicht** in FAUdir gefunden wurden.",
        "",
        "Die FAUdir-bestätigten Personen sind in der Schwester-Datei "
        "[`profs-ohne-pflichtlehre.md`](profs-ohne-pflichtlehre.md) "
        "aufgeführt; jede Person erscheint **genau in einer** der beiden "
        "Dateien (Partition statt Duplikation).",
        "",
        "## Vorbehalte",
        "",
        "* Diese Liste enthält typischerweise: Lehrbeauftragte, externe "
        "  Dozent:innen, wissenschaftliche Mitarbeiter:innen ohne eigenen "
        "  FAUdir-Eintrag, sowie Personen, deren Campo-Namens-String so "
        "  stark von ihrem FAUdir-Namen abweicht, dass das Fuzzy-Matching "
        "  scheitert.",
        "* **Falsch-Positive sind sehr wahrscheinlich.** Die Pflicht-"
        "  Klassifikation in `pflichtveranstaltungen.md` ist heuristisch und "
        "  unvollständig (PO-Texte sind unstandardisiert; viele Pflichtmodule "
        "  stehen nur in Anlagen). Eine Person ohne markierte Pflichtlehre "
        "  kann in Wirklichkeit eine Pflichtveranstaltung halten, deren "
        "  PO-Match die Heuristik nicht hergegeben hat.",
        "* Die `is_prof`-Markierung (\"Prof.\" in der Namens-Zeichenkette) "
        "  ist nur ein grober Indikator — der genaue Rang fehlt für diese "
        "  Personen, weil sie in FAUdir nicht aufgefunden wurden.",
        "* Diese Datei dient als **Vergleichsgrundlage** zur RAG-Antwort auf "
        "  dieselbe Frage. Bei Inkonsistenz ist die RAG-Antwort meist "
        "  belastbarer.",
        "",
        f"**Periode:** {period_label}",
        "",
        f"**Kandidaten:** {len(candidates)} "
        f"(davon {sum(1 for _, _, p in candidates if p)} mit \"Prof\" im Namen)  ",
        f"**Ausgeschlossen, weil bereits in FAUdir-Liste:** {skipped_due_to_faudir}",
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

    # Build per-course metadata (title + program info if available).
    # Courses NOT in the catalogue tree (e.g. those collected only by the
    # Tagesaktuelle-sweep) keep empty program info; the matchers below
    # have a special case to include them when no program scope filter
    # would otherwise let them in.
    by_segment = {n["segment"]: n for n in snapshot["nodes"]}
    uid_to_program: dict[int, dict] = {}
    for n in snapshot["nodes"]:
        uid = n.get("unitId")
        if uid and len(n["path"]) >= 3:
            program = by_segment.get(n["path"][2])
            if program:
                uid_to_program[int(uid)] = program

    courses_with_meta: list[dict] = []
    courses_without_program = 0
    for c in courses_data.get("courses", []):
        uid = int(c["unit_id"])
        program = uid_to_program.get(uid)
        if program is not None:
            program_node_id = int(program["segment"].split(":", 1)[1])
            rel = (
                f"../{period_slug}/{slugify(program['name'])[:88]}-{program_node_id}.md"
            )
            courses_with_meta.append(
                {**c,
                 "program_name": program["name"],
                 "program_segment": program["segment"],
                 "program_rel_path": rel}
            )
        else:
            courses_without_program += 1
            courses_with_meta.append(
                {**c, "program_name": "", "program_segment": "", "program_rel_path": ""}
            )

    log.info(
        "ingested %d courses (%d with catalogue program, %d sweep-only)",
        len(courses_with_meta),
        len(courses_with_meta) - courses_without_program,
        courses_without_program,
    )

    po_root = args.data / "pruefungsordnungen"
    if not po_root.is_dir():
        log.warning("no PO directory at %s — nothing to do", po_root)
        return 0

    # Pre-load structured Pflichtmodul-Bezeichnungen for every PO whose
    # Anlage tables we could parse. This gives us tight match strings
    # (e.g. "Analysis I") instead of legal prose.
    structured_modules = load_structured_pflicht_modules(po_root)
    log.info(
        "structured Pflichtmodule loaded for %d POs",
        len(structured_modules),
    )

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
        slug_hint = _path_program_slug(po_md_path)

        # Primary path: match Campo courses against structured Pflichtmodul-
        # Bezeichnungen from this PO's Anlage tables.
        primary_matches: list[dict] = []
        primary_module_names: list[str] = []
        if po_md_path in structured_modules:
            mods = structured_modules[po_md_path]
            primary_module_names = [m["module_name"] for m in mods]
            primary_matches = match_courses_to_module_names(
                courses_with_meta,
                primary_module_names,
                program_slug_hint=slug_hint,
            )

        # Fallback path: free-text Pflicht-paragraph token overlap (the
        # original heuristic). Catches POs without parseable Anlagen.
        fallback_matches: list[dict] = []
        if not primary_matches:
            pflicht_text = "\n\n".join(b["body"] for b in blocks)
            fallback_matches = match_courses_to_pflicht_text(
                courses_with_meta, pflicht_text, program_slug_hint=slug_hint
            )

        # Union — dedupe by unit_id, keep primary first
        all_matched: list[dict] = []
        seen_uids: set[int] = set()
        for c in primary_matches + fallback_matches:
            uid = int(c["unit_id"])
            if uid in seen_uids:
                continue
            seen_uids.add(uid)
            all_matched.append(c)

        if not all_matched:
            continue
        rel = str(po_md_path.relative_to(args.data))
        by_po[rel] = {
            "title": title,
            "blocks": blocks,
            "matched_courses": all_matched,
            "structured_modules": primary_module_names,
            "match_source": "structured" if primary_matches else "fallback",
        }

    log.info(
        "scanned %d PO files; %d had Pflicht mentions; %d also matched ≥1 course "
        "(structured: %d / fallback: %d)",
        pos_seen, pos_with_pflicht, len(by_po),
        sum(1 for d in by_po.values() if d["match_source"] == "structured"),
        sum(1 for d in by_po.values() if d["match_source"] == "fallback"),
    )

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(
        render_analyse_md(by_po, period_name, args.data, args.out),
        encoding="utf-8",
    )

    # ── Companion file 1: every Lehrende, no FAUdir filter ──────────
    pflicht_unit_ids: set[int] = set()
    for d in by_po.values():
        for c in d["matched_courses"]:
            pflicht_unit_ids.add(int(c["unit_id"]))
    # ── Load FAUdir lookup first so the partition between the two files
    # is computed consistently. ────────────────────────────────────────
    faudir_json = Path("tmp/faudir-persons.json")
    faudir_lookup = load_faudir_lookup(faudir_json)

    # Companion files 2a + 2b: FAUdir-confirmed Profs *ohne* / *mit*
    # Pflichtlehre — together a partition of the FAUdir-matched cohort.
    if faudir_lookup:
        out_ohne = args.out.parent / "profs-ohne-pflichtlehre.md"
        out_ohne.write_text(
            render_profs_ohne_pflichtlehre_md(
                courses_with_meta, pflicht_unit_ids, period_name, faudir_lookup
            ),
            encoding="utf-8",
        )
        out_mit = args.out.parent / "profs-mit-pflichtlehre.md"
        out_mit.write_text(
            render_profs_mit_pflichtlehre_md(
                courses_with_meta, pflicht_unit_ids, period_name, faudir_lookup
            ),
            encoding="utf-8",
        )
        print(
            f"wrote {out_ohne} + {out_mit} "
            f"({len(faudir_lookup)} FAUdir name-keys loaded)"
        )
    else:
        log.info(
            "tmp/faudir-persons.json not present — profs-{ohne,mit}-pflichtlehre.md skipped"
        )

    # Companion file 1: every Lehrende ohne FAUdir-Match — excludes the
    # persons that are already in the FAUdir-confirmed file so each person
    # appears in exactly one of the two analyse/-files.
    out_lehrende = args.out.parent / "lehrende-ohne-pflicht.md"
    out_lehrende.write_text(
        render_lehrende_ohne_pflicht_md(
            courses_with_meta, pflicht_unit_ids, period_name,
            faudir_lookup=faudir_lookup,
        ),
        encoding="utf-8",
    )

    print(
        f"wrote {args.out}: po_files={len(by_po)} "
        f"matched_courses={sum(len(d['matched_courses']) for d in by_po.values())} "
        f"unique_pflicht_unit_ids={len(pflicht_unit_ids)}"
    )
    print(f"wrote {out_lehrende}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
