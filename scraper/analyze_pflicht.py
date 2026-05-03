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
    """True if the text describes Pflicht (mandatory) modules.

    Two paths:
    1. ``Pflicht*`` not preceded by ``Wahl`` — the standard Pflicht marker.
    2. ``Obligatorisch nachzuweisend*`` — FAU BA/MA Medizintechnik phrasing.
       Covers both ``Obligatorisch nachzuweisende Module`` (strict Pflicht)
       and ``Obligatorisch nachzuweisende Wahlpflichtmodule`` (mandatory
       selection from a fixed catalogue, treated as Pflicht per project
       policy — students MUST pass the required count).
    """
    if re.search(r"(?<!Wahl)Pflicht\w*", text, flags=re.IGNORECASE):
        return True
    if re.search(r"\bObligatorisch\s+nachzuweisend", text, flags=re.IGNORECASE):
        return True
    return False


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


_COURSE_FAC_HINTS: dict[str, set[str]] = {
    "tech": {
        "engineering", "technology", "informatik", "informatics", "programming",
        "robotik", "robotics", "elektrotechnik", "mechanik", "mechanical",
        "computational", "kommunikation", "communications", "signal",
        "energietechnik", "werkstoff", "materials", "fertigung",
        "mechatronik", "mechatronics", "automation", "computer",
        "software", "data", "ai", "artificial",
    },
    "nat": {
        "physik", "physics", "chemie", "chemistry", "mathematik", "mathematics",
        "mathematical", "biologie", "biology", "biological", "molecular",
        "geologie", "geology", "meteor", "klima", "climate",
        "geographie", "geography", "biophysics", "biochemistry",
    },
    "med": {
        "medizin", "medical", "klinisch", "clinical", "anatomie", "physiologie",
        "chirurgie", "surgery", "pharmazie", "pharmaceutical", "krebs", "cancer",
        "immunology", "epidemiologie", "neurolog", "kardiolog", "onkolog",
        "psychiatrie", "psychiatry", "diagnostik",
    },
    "phil": {
        "philosophie", "philosophy", "theologie", "theology", "geschichte",
        "history", "kultur", "culture", "ethno", "judaistik", "religion",
        "sprachwissenschaft", "linguistik", "linguistics", "literatur",
        "literature", "soziolog", "sociology", "ethik",
        "anglistik", "germanistik", "romanistik", "slavistik",
        "klassische archäolog", "alte geschichte", "mittelalter",
    },
    "rw": {
        "wirtschaft", "economics", "recht", "law", "rechtswissenschaft",
        "management", "betriebswirtschaft", "volkswirtschaft", "finance",
        "finanzen", "marketing", "controlling", "accounting",
    },
}


def _course_faculty_hints(title: str) -> set[str]:
    """Best-effort faculty tagging from a course title's keywords."""
    t = title.lower()
    out: set[str] = set()
    for fac, kws in _COURSE_FAC_HINTS.items():
        for kw in kws:
            if kw in t:
                out.add(fac)
                break
    return out


def _po_faculty(po_rel: str) -> str | None:
    """Faculty implied by the PO file's path; ``None`` for cross-faculty bins
    (Lehramt, Sprachpruefungen) where any course faculty is plausible."""
    parts = po_rel.split("/")
    if "technische-fakultaet" in parts:
        return "tech"
    if "naturwissenschaftliche-fakultaet" in parts:
        return "nat"
    if "medizinische-fakultaet" in parts:
        return "med"
    if "philosophische-fakultaet" in parts:
        return "phil"
    if "rw" in parts:
        return "rw"
    return None


def _faculty_compatible(course_title: str, po_rel: str) -> bool:
    """Return True if the course's title-implied faculty/-ies overlap with
    the PO's path-implied faculty (or either side is ambiguous)."""
    po_fac = _po_faculty(po_rel)
    if po_fac is None:
        return True  # cross-faculty PO bin → don't filter
    course_facs = _course_faculty_hints(course_title)
    if not course_facs:
        return True  # course title has no faculty signal → don't filter
    return po_fac in course_facs


def _is_container_bucket(program_name: str) -> bool:
    """A *container bucket* is a Campo catalogue program that groups
    courses across multiple study programs rather than belonging to one.

    Conventions encountered in Campo:
      * ``- Frühstudium -`` / ``- Mathematik (FAU Scientia)  -`` —
        leading-dash bucket names.
      * ``Veranstaltungen aus der Technischen Fakultät`` (and the
        Naturwissenschaftliche, Medizinische, Philosophische, RW
        siblings) — faculty-level catalogue groupings used for cross-
        listed courses (e.g. *Pattern Recognition* for MSc Medizintechnik
        students appears here, not under MSc Medizintechnik directly).
      * Frühstudium / Studium Generale / Schlüsselqualifikationen /
        Sonstige Veranstaltungen — interdisciplinary buckets.

    A course catalogued in any of these is NOT bound to a single
    Studiengang and must stay matchable against POs whose slug hint
    (e.g. ``informatik``) doesn't appear in the bucket name.
    """
    if not program_name:
        return False
    pn = program_name.strip().lower()
    if pn.startswith("- ") or pn.startswith("-"):
        return True
    return any(
        kw in pn for kw in (
            "frühstudium",
            "fau scientia",
            "studium generale",
            "schlüsselqualifikation",
            "sonstige veranstaltungen",
            # Faculty-level catalogue groupings (cross-listed courses).
            "veranstaltungen aus der technischen fakultät",
            "veranstaltungen aus der naturwissenschaftlichen fakultät",
            "veranstaltungen aus der medizinischen fakultät",
            "veranstaltungen aus der philosophischen fakultät",
            "veranstaltungen aus der rechts- und wirtschaftswissenschaftlichen",
            "veranstaltungen aus zentralen wissenschaftlichen einrichtungen",
        )
    )


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
    po_rel: str | None = None,
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
            prog_name = c.get("program_name", "")
            # Container buckets (Frühstudium, FAU Scientia, …) hold
            # courses that belong to multiple study programs — don't
            # exclude them on slug mismatch.
            if prog_name and not _is_container_bucket(prog_name):
                prog_slug = re.sub(r"[^a-z0-9]+", "-", prog_name.lower())
                if program_slug_hint not in prog_slug:
                    continue
        overlap = sum(1 for t in tokens if t in pf_lower)
        if overlap < min_overlap:
            continue
        if overlap < max(2, len(tokens) // 2):
            continue
        # Same faculty cross-check as in match_courses_to_module_names.
        if po_rel and not _faculty_compatible(c.get("title", ""), po_rel):
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
    po_rel: str | None = None,
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
            # Container buckets (Frühstudium, FAU Scientia, Studium Generale,
            # Sonstige Veranstaltungen, …) are catch-all catalogue sections.
            # A WiSe Pflicht-Modul like "Grundlagen der Programmierung" is
            # frequently catalogued under "- Frühstudium -" even though the
            # PO declares it as Informatik-Pflicht — exclude these from the
            # slug filter so they stay matchable.
            or _is_container_bucket(c.get("program_name", ""))
            or h in re.sub(r"[^a-z0-9]+", "-", c["program_name"].lower())
        ]
    else:
        course_pool = courses
    for module_name in module_names:
        mod_tokens = _course_tokens(module_name)
        if len(mod_tokens) >= 2:
            # Standard path: ≥ 2 strong (≥ 5-char) tokens overlap.
            for c in course_pool:
                ctitle = c.get("title", "").lower()
                overlap = sum(1 for t in mod_tokens if t in ctitle)
                if overlap < min_overlap:
                    continue
                if overlap < max(2, len(mod_tokens) // 2):
                    continue
                # Faculty cross-check: drop matches where the course's title
                # implies a different faculty than the PO's path
                # (e.g. Phil Fak PO ↔ Med-Tech course is almost surely a
                # false positive from generic-keyword overlap).
                if po_rel and not _faculty_compatible(c.get("title", ""), po_rel):
                    continue
                matched.append((overlap, c))
            continue

        # Fallback path: short multi-word module names like "Deep Learning",
        # "Analysis I", "Algebra II" reduce to ≤ 1 strong token (because the
        # 5-char tokenizer drops "Deep", "I", "II"). Use whole-phrase substring
        # matching so they don't get silently skipped. ~441 of 5 243 PO-
        # extracted Pflichtmodul-Bezeichnungen fall into this bucket — most
        # of them are short multi-word labels we want to honour.
        mod_norm = re.sub(r"\s+", " ", module_name.strip().lower())
        words = mod_norm.split()
        if len(words) < 2:
            # Ultra-short single-word labels ("Algebra", "Bachelorarbeit",
            # "Internship") are too ambiguous for a substring match — skip.
            continue
        pattern = re.compile(rf"\b{re.escape(mod_norm)}\b")
        for c in course_pool:
            ctitle_norm = re.sub(r"\s+", " ", c.get("title", "").strip().lower())
            if not pattern.search(ctitle_norm):
                continue
            if po_rel and not _faculty_compatible(c.get("title", ""), po_rel):
                continue
            # Score by word count so dedupe prefers longer phrase matches.
            matched.append((len(words) + 1, c))
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


def _faudir_is_prof(faudir_entry: dict | None) -> bool:
    """True iff this FAUdir entry exists AND has a Prof-level title.

    Centralised so all three Lehrende-cohort files share the same
    definition of who counts as a Professor.
    """
    if not faudir_entry:
        return False
    return _is_professor_title(faudir_entry.get("personalTitle") or "")


def _is_professor_title(personal_title: str) -> bool:
    """Return True if the FAUdir ``personalTitle`` indicates a Professor.

    Includes ``Prof.``, ``Prof. Dr.``, ``Prof. Dr.-Ing.``, ``Prof. Dr.
    med.``, ``apl. Prof.``, ``Hon. Prof.``, ``Juniorprofessor`` and
    siblings (the ``\\bProf\\b`` match catches every variant in the
    FAUdir corpus). Explicitly excludes:

    * ``PD`` / ``PD Dr.`` / ``PD Dr. habil.`` — Privatdozent. Has
      Habilitation and may teach but is *not* a Professor.
    * Empty title — typically ``scientific_employee`` (Wissenschaftliche
      Mitarbeitende), ``M.Sc.``, ``Dr.`` alone, etc. — research staff
      affiliated WITH a Professur but not Profs themselves.
    """
    if not personal_title:
        return False
    t = personal_title.strip()
    # Privatdozent — explicitly excluded per project policy.
    if re.match(r"^PD\b", t, re.IGNORECASE):
        return False
    if re.search(r"\bProf\b", t, re.IGNORECASE):
        return True
    # Juniorprofessor / Jun.-Prof. (the latter still matches \bProf\b
    # above; this branch covers spellings without the Prof segment).
    if re.search(r"\bJuniorprof", t, re.IGNORECASE):
        return True
    return False


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


def _aggregate_by_faudir(by_person: dict) -> dict:
    """Merge ``by_person`` entries that share a FAUdir identifier into one
    aggregated record per unique person.

    Without this, raw instructor strings that differ in trivial ways
    (e.g. *"Beck, Silvan"* vs. *"Christopher Beck"* both fuzzy-resolving
    to the same FAUdir id, or two `Held, Pascal` records with adjacent
    name variants) become independent buckets — and a person whose
    Pflicht courses live under one variant and non-Pflicht courses under
    another lands in BOTH the *mit* and *ohne* files. Aggregating by
    FAUdir id collapses them into a single record before partitioning.

    Entries WITHOUT a FAUdir match are passed through unchanged (keyed
    by their raw name) — those are handled by the lehrende-ohne-pflicht
    file, not by the FAUdir-confirmed partition.
    """
    aggregated: dict[tuple[str, str], dict] = {}
    for full, info in by_person.items():
        fau = info.get("faudir")
        ident = (fau or {}).get("identifier") or ""
        # FAUdir-matched persons collapse on `id`; unmatched stay
        # separate under `noid` (one bucket per raw name).
        key = ("id", ident) if ident else ("noid", full)
        if key not in aggregated:
            aggregated[key] = {
                "pflicht": [],
                "other": [],
                "faudir": fau,
                "_full": full,  # a representative raw name (for fallback sort)
            }
        aggregated[key]["pflicht"].extend(info.get("pflicht") or [])
        aggregated[key]["other"].extend(info.get("other") or [])
        # Belt-and-braces: if the first bucket had no FAUdir match but a
        # later same-id bucket does, retain the FAUdir record.
        if aggregated[key]["faudir"] is None and fau:
            aggregated[key]["faudir"] = fau

    # De-dupe courses by (unit_id, period_id) within each aggregated
    # entry — the same course taught under several name-string variants
    # of the same person would otherwise appear multiple times. We keep
    # the period in the key so a course that genuinely runs in both
    # terms (same unit_id across periods, like "Deep Learning") still
    # surfaces once per term.
    for entry in aggregated.values():
        for k in ("pflicht", "other"):
            seen: set[tuple[int, int]] = set()
            unique = []
            for c in entry[k]:
                try:
                    uid = int(c["unit_id"])
                except Exception:  # noqa: BLE001
                    continue
                pid = int(c.get("_period_id") or 0)
                key = (uid, pid)
                if key in seen:
                    continue
                seen.add(key)
                unique.append(c)
            entry[k] = unique
    return aggregated


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

    # Aggregate by FAUdir identifier so name-variants of the same person
    # don't produce duplicate entries (and don't end up in both
    # profs-mit and profs-ohne).
    aggregated = _aggregate_by_faudir(by_person)

    # Filter to FAUdir-confirmed Profs with no Pflicht teaching.
    # Per project policy: only persons whose `personalTitle` indicates
    # a Professor (Prof., apl. Prof., Hon. Prof., Juniorprofessor) count
    # — affiliations alone don't make someone a Prof. PD (Privatdozent),
    # Dr., M.Sc., or empty titles are excluded; those land in
    # lehrende-ohne-pflicht.md instead.
    candidates: list[tuple[str, dict]] = []
    for key, info in aggregated.items():
        if info["pflicht"]:
            continue
        if not info["other"]:
            continue
        if not _faudir_is_prof(info["faudir"]):
            continue
        candidates.append((info["_full"], info))

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
    *,
    pflicht_sources: dict[int, list[dict]] | None = None,
) -> str:
    """The companion of ``profs-ohne-pflichtlehre.md`` — FAUdir-confirmed
    Professor:innen, die in der Periode mindestens eine Pflichtveranstaltung
    halten. Same FAUdir matching + W-Rang grouping; opposite Pflicht filter.

    If ``pflicht_sources`` is given (a ``unit_id → [{po_rel, po_title,
    program_slug}]`` map), each Pflichtveranstaltung is annotated with the
    PO(s) it appears in and the implied study-program.
    """
    pflicht_sources = pflicht_sources or {}
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

    # Aggregate by FAUdir identifier so different name-string variants
    # of the same person collapse into one record (avoids adjacent
    # duplicate entries and partition violations against profs-ohne).
    aggregated = _aggregate_by_faudir(by_person)

    # Same Prof-title filter as profs-ohne so the partition stays
    # restricted to actual Professors (Prof./apl. Prof./Hon. Prof./
    # Juniorprofessor); PD / Dr. / M.Sc. / empty land in lehrende-ohne-
    # pflicht.md instead.
    candidates: list[tuple[str, dict]] = []
    for key, info in aggregated.items():
        if not info["pflicht"]:
            continue
        if not _faudir_is_prof(info["faudir"]):
            continue
        candidates.append((info["_full"], info))

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
            # Group Pflichtveranstaltungen by source period so the reader
            # sees at a glance which terms a Prof teaches Pflicht in.
            pflicht_by_period: dict[str, list[dict]] = defaultdict(list)
            for c in info["pflicht"]:
                pflicht_by_period[c.get("_period_name", "")].append(c)
            ordered_periods = sorted(pflicht_by_period.keys(), key=lambda s: (
                0 if "Winter" in s else 1 if "Sommer" in s else 2, s,
            ))
            shown = 0
            for per in ordered_periods:
                courses_in_per = pflicht_by_period[per]
                if len(ordered_periods) > 1:
                    lines.append(f"  - **{per or '(Periode unbekannt)'}** ({len(courses_in_per)})")
                    indent = "    "
                else:
                    indent = "  "
                for c in courses_in_per:
                    if shown >= 10:
                        break
                    shown += 1
                    title_str = c.get("title", "?")
                    ctype = c.get("course_type") or ""
                    rel = c.get("program_rel_path", "")
                    pname = c.get("program_name", "?") or "(nicht im Katalog)"
                    if rel:
                        lines.append(f"{indent}- **\"{title_str}\"** — {ctype} (Campo-Studiengang: [{pname}]({rel}))")
                    else:
                        lines.append(f"{indent}- **\"{title_str}\"** — {ctype} (Campo-Studiengang: {pname})")
                    # Show PO sources for this course (where it's flagged Pflicht).
                    src_indent = indent + "  "
                    sources = pflicht_sources.get(int(c["unit_id"]), [])
                    if sources:
                        # group identical (program_slug, po_title) entries
                        seen = set()
                        deduped = []
                        for s in sources:
                            key = (s.get("po_rel"), s.get("po_title"))
                            if key in seen:
                                continue
                            seen.add(key)
                            deduped.append(s)
                        if len(deduped) <= 5:
                            for s in deduped:
                                prog = s.get("program_slug") or "?"
                                po_link = f"../{s['po_rel']}" if s.get("po_rel") else ""
                                po_title = s.get("po_title") or s.get("po_rel", "?")
                                if po_link:
                                    lines.append(
                                        f"{src_indent}- Pflicht laut: [{po_title}]({po_link}) "
                                        f"(Studiengang: `{prog}`)"
                                    )
                                else:
                                    lines.append(
                                        f"{src_indent}- Pflicht laut: {po_title} (Studiengang: `{prog}`)"
                                    )
                        else:
                            # many POs — collapse to a count + the first 3
                            progs = sorted({s.get("program_slug") or "?" for s in deduped})
                            lines.append(
                                f"{src_indent}- Pflicht in **{len(deduped)} POs** "
                                f"(Studiengänge: {', '.join(f'`{p}`' for p in progs[:8])}"
                                f"{'…' if len(progs) > 8 else ''})"
                            )
                            for s in deduped[:3]:
                                po_link = f"../{s['po_rel']}" if s.get("po_rel") else ""
                                po_title = s.get("po_title") or s.get("po_rel", "?")
                                if po_link:
                                    lines.append(f"{src_indent}  - [{po_title}]({po_link})")
            if len(info["pflicht"]) > 10:
                lines.append(f"  - … und {len(info['pflicht'])-10} weitere")
            # Also list non-Pflicht courses so the reader sees the full
            # Lehre at a glance — distinguished from the Pflicht block by
            # a visual separator and a header. Up to 10 shown per period.
            if info["other"]:
                lines.append(f"- **Weitere Lehre (nicht Pflicht):** {len(info['other'])}")
                other_by_period: dict[str, list[dict]] = defaultdict(list)
                for c in info["other"]:
                    other_by_period[c.get("_period_name", "")].append(c)
                ordered_periods = sorted(other_by_period.keys(), key=lambda s: (
                    0 if "Winter" in s else 1 if "Sommer" in s else 2, s,
                ))
                shown = 0
                for per in ordered_periods:
                    courses_in_per = other_by_period[per]
                    if len(ordered_periods) > 1:
                        lines.append(f"  - **{per or '(Periode unbekannt)'}** ({len(courses_in_per)})")
                        indent = "    "
                    else:
                        indent = "  "
                    for c in courses_in_per:
                        if shown >= 10:
                            break
                        shown += 1
                        title_str = c.get("title", "?")
                        ctype = c.get("course_type") or ""
                        rel = c.get("program_rel_path", "")
                        pname = c.get("program_name", "?") or "(nicht im Katalog)"
                        if rel:
                            lines.append(f"{indent}- \"{title_str}\" — {ctype} (Campo-Studiengang: [{pname}]({rel}))")
                        else:
                            lines.append(f"{indent}- \"{title_str}\" — {ctype} (Campo-Studiengang: {pname})")
                if len(info["other"]) > 10:
                    lines.append(f"  - … und {len(info['other'])-10} weitere")
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
    # marked Pflicht **and** no FAUdir-Prof match (so they don't double-appear
    # in profs-ohne-pflichtlehre.md).
    #
    # The FAUdir match check is now Prof-aware: a person whose FAUdir record
    # has a non-Prof personalTitle (e.g. ``Dr.``, ``M.Sc.``, empty,
    # ``PD Dr.``) is NOT excluded — they belong here, not in profs-{ohne,
    # mit}-pflichtlehre.md, since those files are restricted to Professors.
    candidates: list[tuple[str, list[dict], bool]] = []
    skipped_due_to_faudir = 0
    for full, info in by_person.items():
        if info["pflicht"]:
            continue
        if not info["other"]:
            continue
        if faudir_lookup:
            fau = fuzzy_lookup_faudir(full, faudir_lookup)
            if _faudir_is_prof(fau):
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
        default=None,
        help=(
            "Optional. Single periodId for backwards compatibility. When "
            "passing multiple --tree/--courses pairs, this is ignored — the "
            "periodId is read from each tree JSON."
        ),
    )
    p.add_argument(
        "--tree",
        type=Path,
        nargs="+",
        required=True,
        help=(
            "Path(s) to the period tree JSON. Pass multiple to combine "
            "periods (e.g. WiSe + SoSe of one academic year). Each --tree "
            "is paired with the --courses at the same index."
        ),
    )
    p.add_argument(
        "--courses",
        type=Path,
        nargs="+",
        required=True,
        help=(
            "Path(s) to the period courses JSON. Must have same count as "
            "--tree (pairs are matched by index)."
        ),
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

    if len(args.tree) != len(args.courses):
        p.error(
            f"--tree ({len(args.tree)} paths) must have the same count as "
            f"--courses ({len(args.courses)} paths)"
        )

    courses_with_meta: list[dict] = []
    period_names: list[str] = []
    courses_without_program = 0
    for tree_path, courses_path in zip(args.tree, args.courses):
        snapshot = json.loads(tree_path.read_text(encoding="utf-8"))
        courses_data = json.loads(courses_path.read_text(encoding="utf-8"))
        per_period_id = int(snapshot.get("periodId") or args.period or 0)
        per_period_name = snapshot.get("periodName", f"period-{per_period_id}")
        per_period_slug = f"{per_period_id}-{slugify(per_period_name)}"
        period_names.append(per_period_name)
        log.info(
            "loading period %d (%s) — tree=%s courses=%s",
            per_period_id, per_period_name, tree_path, courses_path,
        )

        # Build per-course metadata (title + program info if available).
        # Courses NOT in the catalogue tree (e.g. those collected only by
        # the Tagesaktuelle-sweep) keep empty program info; matchers
        # downstream include them via the no-scope special case.
        by_segment = {n["segment"]: n for n in snapshot["nodes"]}
        uid_to_program: dict[int, dict] = {}
        for n in snapshot["nodes"]:
            uid = n.get("unitId")
            if uid and len(n["path"]) >= 3:
                program = by_segment.get(n["path"][2])
                if program:
                    uid_to_program[int(uid)] = program

        for c in courses_data.get("courses", []):
            uid = int(c["unit_id"])
            program = uid_to_program.get(uid)
            if program is not None:
                program_node_id = int(program["segment"].split(":", 1)[1])
                rel = (
                    f"../{per_period_slug}/"
                    f"{slugify(program['name'])[:88]}-{program_node_id}.md"
                )
                courses_with_meta.append(
                    {**c,
                     "program_name": program["name"],
                     "program_segment": program["segment"],
                     "program_rel_path": rel,
                     "_period_id": per_period_id,
                     "_period_name": per_period_name}
                )
            else:
                courses_without_program += 1
                courses_with_meta.append(
                    {**c,
                     "program_name": "",
                     "program_segment": "",
                     "program_rel_path": "",
                     "_period_id": per_period_id,
                     "_period_name": per_period_name}
                )

    period_name = " + ".join(period_names) if len(period_names) > 1 else period_names[0]
    log.info(
        "ingested %d courses across %d period(s) (%d with catalogue program, %d sweep-only)",
        len(courses_with_meta), len(period_names),
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

        rel = str(po_md_path.relative_to(args.data))

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
                po_rel=rel,
            )

        # Fallback path: free-text Pflicht-paragraph token overlap (the
        # original heuristic). Catches POs without parseable Anlagen.
        fallback_matches: list[dict] = []
        if not primary_matches:
            pflicht_text = "\n\n".join(b["body"] for b in blocks)
            fallback_matches = match_courses_to_pflicht_text(
                courses_with_meta, pflicht_text,
                program_slug_hint=slug_hint, po_rel=rel,
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

    # Build inverse map: unit_id → list of POs that flag it as Pflicht
    # (with the PO title + path-derived program slug). Used by
    # render_profs_mit_pflichtlehre_md so each course shows where it's
    # mandatory.
    pflicht_sources: dict[int, list[dict]] = defaultdict(list)
    for po_rel, d in by_po.items():
        slug = _path_program_slug(Path(po_rel))
        for c in d["matched_courses"]:
            pflicht_sources[int(c["unit_id"])].append(
                {"po_rel": po_rel, "po_title": d["title"], "program_slug": slug}
            )

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
                courses_with_meta, pflicht_unit_ids, period_name, faudir_lookup,
                pflicht_sources=dict(pflicht_sources),
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
