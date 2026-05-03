"""Strukturierte Pflichtmodul-Extraktion aus PO-Anlagen.

The previous heuristic (`analyze_pflicht.py`) only scans PO text for the
word *Pflicht*; that catches paragraphs but misses the *Studienverlaufs-
plan* / *Curricular-Übersicht* tables in Anlage 1/1b/2/2b which are the
authoritative source of which modules a study program demands.

This module parses those markdown tables (preserved by `pymupdf4llm` for
~2 360 of 3 196 PO files) and emits the *list of Pflicht-modules per
PO* — module name + module number + ECTS — to
``data/analyse/pflichtmodule.md``.

Scope and caveats:

* Only PO files whose Anlage-tables actually have a recognisable
  Pflicht-section column (``Grundlagen``, ``Pflichtbereich``,
  ``Basismodule``, ``Kernbereich``, ``Kernmodule``, ``Pflichtmodule``,
  ``Bachelorarbeit``, ``Masterarbeit``) are mined. Other PO formats
  (image-rendered tables, free-text appendices) are not yet supported
  and contribute zero modules — that's a known gap.
* *Wahlpflicht*, *Wahl*, *Aufbau*, *Vertiefung*, *Schwerpunkt*,
  *Schlüsselqualifikationen* are deliberately **excluded**; modules
  in those sections are not strict Pflicht.
* Module *names* are extracted; the cross-reference to actual Campo
  course events is left to the existing ``analyze_pflicht.py`` (which
  matches by token overlap — imperfect because module names diverge
  from course titles).
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

from render_markdown import _parse_frontmatter  # noqa: E402

log = logging.getLogger("campo.extract_pflicht_module")


# Section markers that mean "this is Pflicht / mandatory" in a PO Anlage.
_PFLICHT_SECTION_RE = re.compile(
    r"^(?:"
    r"Pflichtbereich|Pflichtmodule?|Pflichtfa(?:ch|ecker)|"
    r"Grundlagen(?:\s+der)?|"
    r"Basismodule?|Kernbereich|Kernmodule?|"
    r"Bachelorarbeit|Masterarbeit|"
    # FAU BA/MA Medizintechnik (BMT/MMT) POs use two related phrasings,
    # both of which are interpreted as Pflicht per project policy:
    #   * "Obligatorisch nachzuweisende Module" — strict Pflicht.
    #   * "Obligatorisch nachzuweisende Wahlpflichtmodule" — mandatory
    #     selection from a fixed catalogue. The student MUST pass the
    #     required count of these courses; the choice is which subset.
    # Both are surfaced as Pflicht here so e.g. "Pattern Recognition"
    # (declared in Anlage 3a-e of every BMT/MMT version) is no longer
    # invisible to the analyse.
    r"Obligatorisch\s+nachzuweisend\w*\s+(?:Wahlpflicht)?Module?|"
    r"Obligatory(?:\s+core)?\s+modules?|"
    r"Pflicht(?:bereich|module?|fach)\b"
    r")\b",
    re.IGNORECASE,
)
# Section markers that **mean Wahl** — even when they look superficially close.
_WAHL_SECTION_RE = re.compile(
    r"^(?:"
    r"Wahlpflicht\w*|Wahlbereich|Wahlmodule?|Wahlfach|"
    r"Aufbaumodule?|Vertiefungs(?:bereich|modul\w*)|"
    r"Schwerpunkt\w*|Schl[uü]sselqualifikation\w*|"
    r"Nebenfach|Erg[aä]nzungsbereich"
    r")\b",
    re.IGNORECASE,
)
# Lines that are *table data*: start with a pipe, end with a pipe.
_TABLE_ROW_RE = re.compile(r"^\|.*\|\s*$")
_TABLE_SEP_RE = re.compile(r"^\|\s*[:\-\s|]+\|\s*$")


def _strip_emph(s: str) -> str:
    s = re.sub(r"\*+([^*]+)\*+", r"\1", s)
    # PyMuPDF4LLM occasionally inserts <br> in cell content — collapse to a space.
    s = re.sub(r"<br\s*/?>", " ", s, flags=re.IGNORECASE)
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def _split_row(line: str) -> list[str]:
    """Split a markdown table row into cells (no leading/trailing pipes)."""
    parts = line.strip().split("|")
    # First and last are empty if the line starts/ends with |
    if parts and parts[0] == "":
        parts = parts[1:]
    if parts and parts[-1] == "":
        parts = parts[:-1]
    return [p.strip() for p in parts]


def _is_section_marker(cell: str) -> str | None:
    """Return ``"pflicht"``, ``"wahl"`` or None for a stripped cell text."""
    text = _strip_emph(cell)
    if not text:
        return None
    if _PFLICHT_SECTION_RE.match(text):
        return "pflicht"
    if _WAHL_SECTION_RE.match(text):
        return "wahl"
    return None


def _likely_module_name(s: str) -> bool:
    """Cheap filter: a cell text looks like a module name."""
    s = _strip_emph(s)
    if not s or len(s) < 4:
        return False
    if re.fullmatch(r"[\d.,\s\-]+", s):
        return False
    if re.fullmatch(r"[A-Z]{1,3}", s):  # column letters etc.
        return False
    if re.search(r"^\(?\s*\d", s):
        return False
    # Modulgruppe/Bereich row labels — these appear as section dividers in
    # BA/MA Medizintechnik and similar POs (e.g. "M2 BDV/IDP Engineering
    # core modules gemäß § 44a Abs. 2"). They reference a regulation
    # ("gemäß § …") or a multi-Studienrichtung group. Strip them so the
    # actual module name (in the next column) is what we capture instead.
    if re.search(r"\bgem(?:ä|ae)ß\s+§", s, re.IGNORECASE):
        return False
    if re.match(r"^M\s*\d+\b", s) and ("/" in s or len(s.split()) > 4):
        # "M2 BDV/IDP Engineering core modules" pattern
        return False
    if s.lower() in {
        "modul", "modulbezeichnung", "lehrveranstaltung", "summe",
        "ects", "sws", "vorlesung", "übung", "seminar", "praktikum",
        "tafelübung", "klausur", "modulnote", "modulnr", "nr.",
        "kennung", "module", "fach", "bezeichnung", "jeweils", "j",
        "fs", "sem", "sem.", "fachsem.", "art und umfang",
        "studienleistung", "prüfung", "fakulät", "fakultät",
        "prüfungsleistung", "bonusleistung",
    }:
        return False
    # Aggregate row labels — "Summe(n) Grundlagen", "Summe SWS und ECTS-Punkte" etc.
    if re.match(r"^(?:Summen?|Total|Insgesamt|Gesamt|Zwischensumme)\b", s, re.IGNORECASE):
        return False
    # Bare section labels accidentally captured as module names
    # ("Pflichtmodule", "Pflichtbereich", "Wahlpflichtbereich" …). We use a
    # *full-match* test against a short closed set so module names that
    # happen to *begin* with "Grundlagen" (e.g. "Grundlagen der
    # Programmierung") still survive.
    if re.fullmatch(
        r"(?:Pflichtbereich(?:\s*\(\d+\s*ECTS\))?|Pflichtmodule?|Pflichtfa(?:ch|ecker)|"
        r"Grundlagen|Grundlagen\s+der|"
        r"Basismodule?|Kernbereich|Kernmodule?|"
        r"Wahlpflicht\w*|Wahlbereich|Wahlmodule?|"
        r"Aufbaumodule?|Vertiefungsmodule?|Schwerpunkt\w*|"
        r"Schl[uü]sselqualifikation\w*|Nebenfach|Erg[aä]nzungsbereich)",
        s, re.IGNORECASE,
    ):
        return False
    # Garbled OCR-like fragments (PyMuPDF column-bleed: "S SWS d ECTSPk").
    tokens = s.split()
    short_tokens = sum(1 for t in tokens if len(t) <= 2)
    if tokens and short_tokens > len(tokens) // 2:
        return False
    # Must contain at least one letter
    if not re.search(r"[A-Za-zÄÖÜäöüß]", s):
        return False
    return True


def _detect_module_name_column(header: list[str]) -> int | None:
    """If the header row mentions Modulbezeichnung or similar, return its
    column index. Else return None (caller will fall back to a default).

    Also handles tables whose header has a *plain* "Name" column — common
    in FAU BA/MA Medizintechnik POs where the structure is
    ``[Nr. | Name (Gruppe) | ECTS | Name (Modul) | …]``. We prefer the
    LAST "Name" cell because it's the more specific one (module level)."""
    last_name_col: int | None = None
    for i, cell in enumerate(header):
        text = _strip_emph(cell).lower()
        if "modulbezeichnung" in text:
            return i
        if text in {"modul", "module"}:
            return i
        if "fach" == text or "bezeichnung" == text:
            return i
        if text == "name":
            last_name_col = i
    return last_name_col


def _detect_table_section_from_header(header: list[str]) -> str | None:
    """If any header cell is a Pflicht/Wahl section marker (e.g. the BA/MA
    Medizintechnik POs put ``Obligatorisch nachzuweisende Module`` in the
    column header), return that classification — applied to the whole
    table unless overridden by a marker in a later data row."""
    for cell in header:
        m = _is_section_marker(cell)
        if m:
            return m
    return None


# Heading-text section detection. Unlike `_is_section_marker` (anchored
# match for table cells), heading text often carries prefixes like
# "Anlage 3a:" before the meaningful marker — so we use re.search.
# Order matters: "Obligatorisch nachzuweisende ..." takes precedence so
# "Anlage 3a: Obligatorisch nachzuweisende Wahlpflichtmodule für alle
# Studienrichtungen" is classified as Pflicht (per project policy).
_HEADING_PFLICHT_RE = re.compile(
    r"\bObligatorisch\s+nachzuweisend"
    r"|\b(?:Pflichtbereich|Pflichtmodule?|Pflichtfa(?:ch|ecker)|"
    r"Bachelorarbeit|Masterarbeit|Kernmodule?|Kernbereich|Basismodule?)\b",
    re.IGNORECASE,
)
_HEADING_WAHL_RE = re.compile(
    r"\b(?:Wahlpflicht\w*|Wahlbereich|Wahlmodule?|Wahlfach|"
    r"Aufbaumodule?|Vertiefungs(?:bereich|modul\w*)|"
    r"Schwerpunkt\w*|Schl[uü]sselqualifikation\w*|"
    r"Nebenfach|Erg[aä]nzungsbereich)\b",
    re.IGNORECASE,
)


def _heading_section_marker(text: str) -> str | None:
    """Classify a markdown heading's text as ``"pflicht"`` / ``"wahl"`` /
    ``None``. Pflicht is checked first so headings that combine both
    signals (e.g. the BA/MA Medizintechnik *"Obligatorisch nachzuweisende
    Wahlpflichtmodule"*) come out as Pflicht."""
    if not text:
        return None
    if _HEADING_PFLICHT_RE.search(text):
        return "pflicht"
    if _HEADING_WAHL_RE.search(text):
        return "wahl"
    return None


_MD_HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*$")


def extract_pflicht_modules_from_md(po_md: str) -> list[dict]:
    """Walk the markdown and yield Pflicht-module entries.

    Returns ``[{section, module_no, module_name, raw_row}, …]``.
    """
    lines = po_md.split("\n")
    # State: are we inside a markdown table? what's the current section?
    in_table = False
    header: list[str] | None = None
    module_col: int | None = None
    current_section: str | None = None
    out: list[dict] = []
    seen: set[str] = set()

    # Section context applied to the whole next table by its header row
    # (BA/MA Medizintechnik tables put "Obligatorisch nachzuweisende
    # Module" in column headers, not in data-row first cells).
    table_default_section: str | None = None
    # Section context derived from the most recent markdown heading
    # (some POs put "Anlage 3a: Obligatorisch nachzuweisende Wahlpflicht-
    # module …" in a heading and follow with a plain table).
    heading_section: str | None = None

    def _row_is_subheader(cells: list[str]) -> bool:
        """A row that looks like a column-label row (sub-header), not real
        data. Heuristic: most non-empty cells are short and look like
        labels (Nr., Name, ECTS, V, Ü, P, S, …)."""
        nonempty = [_strip_emph(c) for c in cells if _strip_emph(c)]
        if not nonempty:
            return False
        labelish = sum(
            1 for c in nonempty
            if len(c) <= 20
            and (
                c.lower() in {
                    "nr.", "nr", "name", "ects", "sws", "v", "ü", "ue",
                    "p", "s", "tut", "ü/tut", "modul", "modulbezeichnung",
                    "fach", "bezeichnung", "punkten", "1", "2", "3", "4",
                    "5", "6", "7", "8", "lp", "credits",
                }
                or re.fullmatch(r"\*+[^*]{1,15}\*+", c.strip())
            )
        )
        return labelish >= max(2, len(nonempty) // 2)

    i = 0
    while i < len(lines):
        line = lines[i]
        # Markdown heading: update the rolling section context BEFORE we
        # decide what to do with the line.
        h = _MD_HEADING_RE.match(line)
        if h:
            heading_text = _strip_emph(h.group(2))
            heading_section = _heading_section_marker(heading_text)
            # A new heading clears any pending table-default section so
            # an Obligatorisch-Pflicht table can't bleed into the table
            # under the next "Wahlpflichtmodule" heading.
            table_default_section = None
            i += 1
            continue
        if _TABLE_ROW_RE.match(line):
            row = _split_row(line)
            # Sep line marks end of header
            if _TABLE_SEP_RE.match(line):
                in_table = True
                # Carry the header-derived section into the row walker —
                # falling back to the heading-derived context if the
                # table itself didn't carry a marker.
                effective = table_default_section or heading_section
                if effective:
                    current_section = effective
                i += 1
                continue
            if not in_table:
                # Likely header
                header = row
                module_col = _detect_module_name_column(header)
                table_default_section = _detect_table_section_from_header(header)
                i += 1
                continue
            # Real data row inside a table.
            # Some PO tables (BA/MA Medizintechnik) have additional sub-
            # header rows AFTER the separator that hold the actual column
            # labels (Nr. | Name | ECTS | Name | V | Ü | P | S | …). When
            # the top header didn't yield a module-name column AND this
            # row looks like a sub-header, re-detect from THIS row.
            if module_col is None and _row_is_subheader(row):
                module_col = _detect_module_name_column(row)
                i += 1
                continue
            # Section detection: first cell, bold or otherwise, may set section.
            if row:
                first = row[0]
                marker = _is_section_marker(first)
                if marker:
                    current_section = marker
                # If the row's first cell is empty but second cell is bold
                # ("**1**" → Grundlagen still active) — section sticks.
            # If we're in a Pflicht section, capture module name.
            if current_section == "pflicht":
                # Determine which column to read. Try the detected column
                # first; if that cell is empty (often the case in 2-tier
                # PO tables where a Modulgruppe row holds col 0 and the
                # actual module rows have col 0 empty + col 1 set), fall
                # through to the next column as a recovery.
                primary = module_col if module_col is not None else 2
                candidates_to_try = [primary]
                if primary + 1 < len(row):
                    candidates_to_try.append(primary + 1)
                captured = False
                for col in candidates_to_try:
                    if col >= len(row):
                        continue
                    candidate = _strip_emph(row[col])
                    if _likely_module_name(candidate):
                        module_no = _strip_emph(row[1]) if len(row) > 1 else ""
                        key = (candidate.lower(),)
                        if key not in seen:
                            seen.add(key)
                            out.append(
                                {
                                    "section": current_section,
                                    "module_no": module_no,
                                    "module_name": candidate,
                                    "raw_row": " | ".join(row),
                                }
                            )
                        captured = True
                        break
                # Some POs split a module across multiple rows (e.g.
                # one row per Lehrveranstaltung within a module). The
                # module-no column is empty on continuation rows; we only
                # keep the first row of each module via the seen-set.
            i += 1
            continue
        else:
            # Not a table row — table ends; reset state
            if in_table:
                in_table = False
                header = None
                module_col = None
                current_section = None
                table_default_section = None
            i += 1
    return out


def collect_per_po(po_root: Path) -> dict[Path, dict]:
    """Walk every PO markdown; return ``{path: {title, modules}}`` for those
    that actually yielded ≥ 1 Pflicht-module."""
    out: dict[Path, dict] = {}
    for po_md in sorted(po_root.rglob("*.md")):
        if po_md.name == "INDEX.md":
            continue
        text = po_md.read_text(encoding="utf-8", errors="replace")
        modules = extract_pflicht_modules_from_md(text)
        if not modules:
            continue
        fm = _parse_frontmatter(po_md)
        out[po_md] = {
            "title": fm.get("title", po_md.stem),
            "modules": modules,
        }
    return out


def render_md(per_po: dict[Path, dict], data_root: Path) -> str:
    total_modules = sum(len(d["modules"]) for d in per_po.values())
    lines: list[str] = [
        "---",
        'kind: "campo-pflichtmodule-aus-po"',
        f"po_files_with_pflicht_modules: {len(per_po)}",
        f"total_pflicht_modules: {total_modules}",
        f"scraped_at: {_dt.datetime.now(_dt.timezone.utc).isoformat(timespec='seconds')}",
        "---",
        "",
        "# Pflichtmodule — direkt aus PO-Anlagen extrahiert",
        "",
        "Diese Datei sammelt strukturierte Pflichtmodul-Listen, die wir aus "
        "den *Studienverlaufsplan*- und *Curricular-Übersicht*-Tabellen der "
        "FAU-Prüfungsordnungen gelesen haben (Markdown-Tables, vom "
        "PyMuPDF4LLM-Konverter aus den PDF-Anlagen erzeugt). Pro PO wird "
        "die Sektion verfolgt — Module aus Sektionen *Grundlagen*, "
        "*Pflichtbereich*, *Basismodule*, *Kernbereich*, *Bachelorarbeit*, "
        "*Masterarbeit* gelten als Pflicht. *Wahlpflicht*, *Wahlbereich*, "
        "*Aufbaumodule*, *Vertiefungsmodule*, *Schwerpunkte* und "
        "*Schlüsselqualifikationen* werden ausgenommen.",
        "",
        "## Vorbehalte",
        "",
        "* **Vollständigkeit:** ~74 % der PO-Markdown-Dateien enthalten "
        "  überhaupt erkennbare Tabellen; davon haben wieder nur ~30 % "
        "  klare Pflicht-Section-Marker. Etwa die Hälfte aller POs liefert "
        "  hier deshalb noch kein Ergebnis — bei vielen ist die Anlage als "
        "  **Bild** im PDF eingebettet (typisches Beispiel: *Curricular-"
        "  Übersicht* als Diagramm) und entzieht sich der Text-Extraktion.",
        "* **Modul-Name vs. Veranstaltungs-Titel:** ein Pflichtmodul "
        "  *Analysis I* erscheint in Campo als *Vorlesung Analysis I* + "
        "  *Übung Analysis I* + *Tafelübung Analysis I*. Hier wird nur das "
        "  Modul gelistet; das Cross-Mapping zu Campo-Veranstaltungen "
        "  übernimmt die Heuristik in `pflichtveranstaltungen.md` bzw. "
        "  ein RAG-Agent zur Anfragezeit.",
        "* **Modul-Reihenfolge:** Module erscheinen in der Reihenfolge des "
        "  Studienverlaufsplans (typisch nach Fachsemester sortiert).",
        "",
        f"**Statistik:** {len(per_po)} POs lieferten zusammen "
        f"{total_modules} eindeutige Pflichtmodul-Einträge.",
        "",
        "## Pro PO",
        "",
    ]
    for po_path in sorted(per_po.keys(), key=lambda p: str(p)):
        d = per_po[po_path]
        rel = str(po_path.relative_to(data_root))
        lines.append(f"### {d['title']}")
        lines.append("")
        lines.append(f"PO-Quelle: [`{rel}`](../{rel})")
        lines.append("")
        lines.append(f"**Pflichtmodule ({len(d['modules'])}):**")
        for m in d["modules"]:
            no = m["module_no"]
            name = m["module_name"]
            prefix = f"({no}) " if no and re.fullmatch(r"\d+\w?", no) else ""
            lines.append(f"- {prefix}{name}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main(argv: Iterable[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument(
        "--data", type=Path, default=Path("data"), help="corpus root"
    )
    p.add_argument(
        "--out", type=Path, default=Path("data/analyse/pflichtmodule.md"),
        help="output markdown path",
    )
    p.add_argument("-v", "--verbose", action="count", default=0)
    args = p.parse_args(list(argv) if argv else None)

    level = logging.WARNING - 10 * args.verbose
    logging.basicConfig(level=max(level, logging.DEBUG), format="%(levelname)s %(name)s: %(message)s")

    po_root = args.data / "pruefungsordnungen"
    if not po_root.is_dir():
        log.warning("no PO directory at %s — nothing to do", po_root)
        return 0

    per_po = collect_per_po(po_root)
    log.info("found Pflicht-modules in %d PO files", len(per_po))
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(render_md(per_po, args.data), encoding="utf-8")
    total = sum(len(d["modules"]) for d in per_po.values())
    print(f"wrote {args.out}: po_files={len(per_po)} pflicht_modules={total}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
