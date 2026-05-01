"""Render a Campo catalogue snapshot as an AI-readable markdown corpus.

**Layout (Entry 0013 redesign — flat, RAG-friendly):**

    out/{period-slug}/
        INDEX.md                       # programs grouped by section
        {program-slug-id}.md           # ONE merged file per Campo program
                                       # (depth-3 catalogue node), with:
                                       #   • FAU.de Studiengang content inlined
                                       #     (Steckbrief, sections, links) when matched,
                                       #   • every PO-version listed with permalinks
                                       #     and matched dated PDF references,
                                       #   • every course attached to any leaf in
                                       #     the program's subtree inlined as
                                       #     ``### Title — Type`` with full
                                       #     Eckdaten + Termine + instructors,
                                       #   • Lehramts-Prüfungsordnungen list when
                                       #     the program is a Lehramt-subject node.

Each program file therefore stands alone — a RAG agent can answer most
questions about a program by reading exactly one file, with all back-links
to original Campo URLs and FAU.de pages preserved in the markdown body
and the YAML front-matter.

Slugs are Campo-faithful German with explicit umlaut expansion
(ä→ae, ö→oe, ü→ue, ß→ss). Every basename ends in ``-<segmentId>`` so file
paths stay stable across weekly scrapes even when Campo renames a node.

The big PO-PDF markdowns stay separate under
``out/pruefungsordnungen/{faculty}/{program}/{po-slug}.md`` — they're already
10–30 k tokens each and naturally too large to inline.
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import unicodedata
from pathlib import Path
from typing import Iterable


CAMPO_BASE = "https://www.campo.fau.de"
CATALOG_URL = (
    f"{CAMPO_BASE}/qisserver/pages/cm/exa/coursecatalog/showCourseCatalog.xhtml"
    "?_flowId=showCourseCatalog-flow"
)

# Slug suffixes the FAU.de Studiengang URLs use to encode the degree.
# A Campo program "Informatik" (one node) maps to several FAU slugs like
# "informatik-b-sc", "informatik-m-sc", "informatik-it-sicherheit-b-sc".
_DEGREE_SUFFIXES = (
    "-b-a", "-b-sc", "-b-ed",
    "-m-a", "-m-sc", "-m-ed", "-m-eng",
    "-staatsexamen", "-zertifikat", "-magister", "-promotion",
    "-diplom", "-erweiterungsstudium",
)


# ── slug helpers ────────────────────────────────────────────────────────────


_UMLAUT_FOLD = str.maketrans(
    {
        "ä": "ae",
        "ö": "oe",
        "ü": "ue",
        "Ä": "Ae",
        "Ö": "Oe",
        "Ü": "Ue",
        "ß": "ss",
    }
)


def slugify(name: str, max_len: int = 80) -> str:
    """Campo-faithful, deterministic slug.

    Rules:
      * Strip HTML tags Campo embeds in some catalogue names (rare but real).
      * Fold German umlauts to two-letter form.
      * NFKD-normalise + drop non-ASCII.
      * Lowercase.
      * Replace runs of non-alphanumeric with a single ``-``; trim ``-``.
      * Cap at ``max_len`` characters (still trim trailing ``-`` after cut).
      * Empty result falls back to ``"unnamed"``.
    """
    s = re.sub(r"<[^>]+>", "", name)
    s = s.translate(_UMLAUT_FOLD)
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if c.isascii())
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    if len(s) > max_len:
        s = s[:max_len].rstrip("-")
    return s or "unnamed"


def node_basename(node: dict, max_len: int = 100) -> str:
    """File / folder basename for one node: ``<slug>-<id>``.

    Always appending the numeric ID guarantees uniqueness within a parent
    folder *and* keeps paths stable when Campo renames a node.
    """
    nid = node["nodeId"]
    suffix = f"-{nid}"
    s = slugify(node["name"], max_len=max(8, max_len - len(suffix)))
    return f"{s}{suffix}"


# ── permalinks ──────────────────────────────────────────────────────────────


def catalog_permalink(node: dict, period_id: int) -> str:
    """The exact permalink Campo would render for this node."""
    path_str = "|".join(node["path"])
    return f"{CATALOG_URL}&periodId={period_id}&path={path_str}"


# ── markdown builders ───────────────────────────────────────────────────────


def _strip_inline_html(name: str) -> str:
    """Drop tags so display headings stay clean — but **keep** them in
    INDEX bullet lines so author-supplied links remain clickable."""
    return re.sub(r"<[^>]+>", "", name).strip()


def _front_matter(period_id: int, period_name: str, **extra) -> str:
    lines = [
        "---",
        f"period_id: {period_id}",
        f"period_name: {json.dumps(period_name, ensure_ascii=False)}",
    ]
    for k, v in extra.items():
        if v is None:
            continue
        lines.append(f"{k}: {json.dumps(v, ensure_ascii=False)}")
    lines.append("---\n\n")
    return "\n".join(lines)


def _md_escape_cell(s: str | None) -> str:
    """Escape pipe characters in a markdown table cell."""
    if not s:
        return "—"
    return s.replace("|", "\\|").replace("\n", " ")


def render_course_md(node: dict, course: dict, period_id: int, period_name: str) -> str:
    """Full course-detail leaf — Eckdaten + Termine + Organisation."""
    lines: list[str] = []
    lines.append(
        _front_matter(
            period_id,
            period_name,
            unit_id=course.get("unit_id"),
            segment=node["segment"],
        )
    )
    title_clean = _strip_inline_html(node["name"]).lstrip("- ").strip()
    course_type = course.get("course_type") or ""
    heading = title_clean
    if course_type and course_type.lower() not in title_clean.lower():
        heading = f"{title_clean} — {course_type}"
    lines.append(f"# {heading}\n")

    lines.append(
        f"**Period:** {period_name} · **Segment:** `{node['segment']}` · "
        f"**unitId:** `{course.get('unit_id')}`\n"
    )
    lines.append(f"**Katalog-Permalink:** <{catalog_permalink(node, period_id)}>\n")
    if course.get("permalink"):
        lines.append(f"**Veranstaltungs-Permalink:** <{course['permalink']}>\n")

    # Eckdaten
    eckdaten = [
        ("Veranstaltungsart", course.get("course_type")),
        ("Kurztext", course.get("short_text")),
        ("ECTS-Punkte", course.get("ects")),
        ("Unterrichtssprache", course.get("language")),
        ("Turnus", course.get("turnus")),
    ]
    eckdaten = [(k, v) for k, v in eckdaten if v not in (None, "", [])]
    if eckdaten:
        lines.append("## Eckdaten\n")
        lines.append("| Feld | Wert |")
        lines.append("|---|---|")
        for k, v in eckdaten:
            lines.append(f"| {k} | {_md_escape_cell(str(v))} |")
        lines.append("")

    # Verantwortliche / Durchführende
    inst_resp = course.get("instructors_resp") or []
    inst_exec = course.get("instructors_exec") or []
    if inst_resp or inst_exec:
        lines.append("## Lehrende\n")
        if inst_resp:
            lines.append(f"- **Verantwortlich:** {', '.join(inst_resp)}")
        if inst_exec:
            lines.append(f"- **Durchführend:** {', '.join(inst_exec)}")
        lines.append("")

    # Termine
    appts = course.get("appointments") or []
    lines.append("## Termine\n")
    if appts:
        lines.append("| Rhythmus | Tag | Zeit | Datum von–bis | Raum | Dozent/-in |")
        lines.append("|---|---|---|---|---|---|")
        for a in appts:
            time_cell = (
                f"{a['time_from']}–{a['time_to']}"
                if a.get("time_from") and a.get("time_to")
                else "—"
            )
            date_cell = (
                f"{a['date_from']}–{a['date_to']}"
                if a.get("date_from") and a.get("date_to")
                else (a.get("date_from") or "—")
            )
            lines.append(
                "| "
                + " | ".join(
                    _md_escape_cell(s)
                    for s in [
                        a.get("rhythm"),
                        a.get("weekday"),
                        time_cell,
                        date_cell,
                        a.get("room"),
                        ", ".join(a.get("instructors") or []) or None,
                    ]
                )
                + " |"
            )
        lines.append("")
        if any(a.get("cancelled_dates") for a in appts):
            lines.append("**Ausfalltermine:**")
            for a in appts:
                if a.get("cancelled_dates"):
                    lines.append(f"- {', '.join(a['cancelled_dates'])}")
            lines.append("")
    else:
        lines.append(
            "_Keine festen Termine in der Termine-Tabelle gelistet (z. B. Block-Praktikum)._\n"
        )

    # Organisation
    if course.get("org_unit"):
        lines.append("## Organisation / Studiengänge\n")
        # Campo joins multiple org-unit assignments with whitespace; pretty-print as bullets.
        org = course["org_unit"]
        # Try to split on " (Verantwortlicher)" or "Mehr..." markers
        chunks = re.split(r"\s+(?=(?:TechFak|PhilFak|RWFak|NatFak|MedFak|FB ))", org)
        if len(chunks) > 1:
            for ch in chunks:
                ch = ch.strip().rstrip(".").rstrip("…").strip()
                if ch:
                    lines.append(f"- {ch}")
        else:
            lines.append(org.strip())
        lines.append("")

    return "\n".join(lines).lstrip("\n")


def render_index_md(
    node: dict,
    period_id: int,
    period_name: str,
    children: list[dict],
    child_targets: dict[str, str],
) -> str:
    """Folder index: name, breadcrumbs, permalink, child list."""
    lines: list[str] = []
    lines.append(_front_matter(period_id, period_name))
    lines.append(f"# {_strip_inline_html(node['name'])}\n")
    lines.append(
        f"**Period:** {period_name} · **Segment:** `{node['segment']}` · "
        f"**Depth:** {len(node['path'])}\n"
    )
    lines.append(f"**Permalink:** <{catalog_permalink(node, period_id)}>\n")
    lines.append(f"## Children ({len(children)})\n")
    for ch in sorted(children, key=lambda x: x["name"].lower()):
        target = child_targets[ch["segment"]]
        lines.append(f"- [{ch['name']}]({target}) — `{ch['segment']}`")
    lines.append("")
    return "\n".join(lines).lstrip("\n")


def render_leaf_md(node: dict, period_id: int, period_name: str) -> str:
    """Leaf content file (no children at the scraped depth)."""
    lines: list[str] = []
    lines.append(_front_matter(period_id, period_name))
    lines.append(f"# {_strip_inline_html(node['name'])}\n")
    lines.append(
        f"**Period:** {period_name} · **Segment:** `{node['segment']}` · "
        f"**Depth:** {len(node['path'])}\n"
    )
    lines.append(f"**Permalink:** <{catalog_permalink(node, period_id)}>\n")
    lines.append("## Status\n")
    lines.append(
        "This is a leaf at the catalogue depth scraped. The Campo permalink above "
        "navigates to this node. Course-level details (instructors, schedules, "
        "Inhalte) are not yet attached and will be filled in by a later scraper "
        "pass that joins to the search-flow."
    )
    lines.append("")
    return "\n".join(lines).lstrip("\n")


# ── render the whole snapshot ───────────────────────────────────────────────


_FRONT_MATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
_FM_LINE_RE = re.compile(r'^([\w_\-]+):\s*"?([^"\n]*?)"?\s*$', re.MULTILINE)


def _parse_frontmatter(path: Path) -> dict:
    """Lightweight YAML front-matter reader (no PyYAML dependency)."""
    try:
        head = path.read_text(encoding="utf-8")[:2000]
    except OSError:
        return {}
    m = _FRONT_MATTER_RE.match(head)
    if not m:
        return {}
    return {k: v.strip() for k, v in _FM_LINE_RE.findall(m.group(1))}


def _strip_degree_suffix(slug: str) -> str:
    for sfx in _DEGREE_SUFFIXES:
        if slug.endswith(sfx):
            return slug[: -len(sfx)]
    return slug


def load_fau_index(out_root: Path) -> dict:
    """Build a small lookup of the FAU.de markdowns alongside the Campo corpus.

    Returns a dict with three indexes:
      * ``studiengang``  (keyed by slug-base): list of {slug, title, fakultaet, rel_path}
      * ``po_folders``   (keyed by leaf folder name): list of {rel_dir, leaf, rel_index}
      * ``lehramt_pdfs`` (a flat list of lehramt PDF entries with their stem
        tokens) — for matching Campo Lehramt-subject nodes that have no
        FAU.de Studiengang page but do have a regulation in
        ``pruefungsordnungen/lehramt/lehramtsfaecher/``.
    """
    studiengang_by_base: dict[str, list[dict]] = {}
    sg_dir = out_root / "studiengang"
    if sg_dir.is_dir():
        for f in sorted(sg_dir.glob("*.md")):
            if f.name == "INDEX.md":
                continue
            base = _strip_degree_suffix(f.stem)
            fm = _parse_frontmatter(f)
            studiengang_by_base.setdefault(base, []).append(
                {
                    "slug": f.stem,
                    "title": fm.get("title", f.stem),
                    "fakultaet": fm.get("fakultät", ""),
                    "abschluss": fm.get("abschluss", ""),
                    "rel_path": f.relative_to(out_root).as_posix(),
                }
            )

    po_folders_by_leaf: dict[str, list[dict]] = {}
    po_dir = out_root / "pruefungsordnungen"
    if po_dir.is_dir():
        for index_md in sorted(po_dir.rglob("INDEX.md")):
            folder = index_md.parent
            if folder == po_dir:
                continue  # skip the root /pruefungsordnungen/INDEX.md itself
            leaf = folder.name
            po_folders_by_leaf.setdefault(leaf, []).append(
                {
                    "leaf": leaf,
                    "rel_dir": folder.relative_to(out_root).as_posix(),
                    "rel_index": index_md.relative_to(out_root).as_posix(),
                }
            )

    lehramt_pdfs: list[dict] = []
    lehramt_dir = po_dir / "lehramt" / "lehramtsfaecher" if po_dir.is_dir() else None
    if lehramt_dir and lehramt_dir.is_dir():
        for pdf_md in sorted(lehramt_dir.glob("*.md")):
            if pdf_md.name == "INDEX.md":
                continue
            tokens = set(pdf_md.stem.split("-"))
            fm = _parse_frontmatter(pdf_md)
            lehramt_pdfs.append(
                {
                    "stem": pdf_md.stem,
                    "tokens": tokens,
                    "title": fm.get("title", pdf_md.stem),
                    "rel_path": pdf_md.relative_to(out_root).as_posix(),
                }
            )

    return {
        "studiengang": studiengang_by_base,
        "po_folders": po_folders_by_leaf,
        "lehramt_pdfs": lehramt_pdfs,
    }


_LEHRAMT_SUBJECT_ABBREVIATIONS = {
    # Campo full token → token actually used in lehramtsfaecher PDF stems
    "mathematik": "mathe",
    "wirtschaftswissenschaften": "wirtschaftswiss",
    "evangelische": "ev",
    "katholische": "kath",
    "informationstechnologie": "it",
}


def _lehramt_pdf_matches(node: dict, fau_index: dict) -> list[dict]:
    """For a Campo node whose slug appears as a token in a Lehramt PDF
    filename, return the matching PDFs. Avoids false positives by requiring
    the campo slug (or a known abbreviation) to be a *complete* hyphen
    token in the PDF stem.
    """
    pdfs = fau_index.get("lehramt_pdfs") or []
    if not pdfs:
        return []
    name_slug = slugify(node["name"])
    candidates: set[str] = set()
    # full slug, plus its first non-stopword token, plus any known abbrev
    stopwords = {"fuer", "der", "die", "das", "des", "dem", "in", "im", "mit", "an",
                 "von", "als", "und", "oder", "ein", "eine", "lehramt"}
    for tok in name_slug.split("-"):
        if tok and tok not in stopwords and len(tok) >= 3:
            candidates.add(tok)
            if tok in _LEHRAMT_SUBJECT_ABBREVIATIONS:
                candidates.add(_LEHRAMT_SUBJECT_ABBREVIATIONS[tok])
    if not candidates:
        return []
    matches: list[dict] = []
    for pdf in pdfs:
        if pdf["tokens"] & candidates:
            matches.append(pdf)
    return matches


def _candidate_slugs(name: str) -> list[str]:
    """Several normalised slug variants to try when matching Campo → FAU.

    Campo and FAU.de don't always agree on connectors and qualifiers — e.g.
    *"Elektrotechnik - Elektronik und Informationstechnik"* on Campo vs the
    FAU slug *"elektrotechnik-elektronik-informationstechnik-b-sc"* (no
    *und*). We try the literal slug, then progressively-cleaned variants.
    """
    base = re.sub(r"\([^)]*\)", "", name).strip()  # drop "(Elite)" etc.
    candidates = [slugify(name), slugify(base)]
    # Drop common connector tokens that vary between sources.
    for cand in list(candidates):
        cleaned = re.sub(r"-(?:und|and|or|oder|with|mit|in|im|of|der|die|das|the|the)-", "-", cand)
        if cleaned != cand:
            candidates.append(cleaned)
    # de-dupe, preserve order
    seen: set[str] = set()
    out: list[str] = []
    for c in candidates:
        if c and c not in seen:
            seen.add(c)
            out.append(c)
    return out


def _find_related_fau(node: dict, fau_index: dict) -> dict:
    """For a Campo program-level node, find matching FAU.de entries."""
    studiengang: list[dict] = []
    po_folders: list[dict] = []
    seen_sg: set[str] = set()
    seen_po: set[str] = set()
    for cand in _candidate_slugs(node["name"]):
        for sg in fau_index["studiengang"].get(cand, []):
            if sg["slug"] in seen_sg:
                continue
            seen_sg.add(sg["slug"])
            studiengang.append(sg)
        for po in fau_index["po_folders"].get(cand, []):
            if po["rel_dir"] in seen_po:
                continue
            seen_po.add(po["rel_dir"])
            po_folders.append(po)
    return {"studiengang": studiengang, "po_folders": po_folders}


def _relative_link_from(md_file: Path, target_rel_in_root: str, out_root: Path) -> str:
    """Posix relative path from *md_file*'s folder to ``out_root/target``."""
    target = out_root / target_rel_in_root
    rel = Path(target).resolve().relative_to(Path(out_root).resolve())
    # Compute relative from md_file's parent to target
    src_parent = md_file.parent.resolve()
    target_abs = target.resolve()
    try:
        return str(target_abs.relative_to(src_parent)).replace("\\", "/")
    except ValueError:
        # Need to walk up
        from os.path import relpath
        return relpath(target_abs, src_parent).replace("\\", "/")


def _related_fau_section(node: dict, fau_index: dict, md_file: Path, out_root: Path) -> str:
    """Render the 'Verwandte FAU-Inhalte' block for a program node, or ''."""
    rel = _find_related_fau(node, fau_index)
    lehramt = _lehramt_pdf_matches(node, fau_index) if not rel["studiengang"] else []
    if not rel["studiengang"] and not rel["po_folders"] and not lehramt:
        return ""
    lines: list[str] = ["## Verwandte FAU-Inhalte"]
    if rel["studiengang"]:
        lines.append("")
        lines.append("**Studiengangsseite(n):**")
        for sg in rel["studiengang"]:
            link = _relative_link_from(md_file, sg["rel_path"], out_root)
            note = sg.get("abschluss") or sg.get("fakultaet") or ""
            tail = f" — {note}" if note else ""
            lines.append(f"- [{sg['title']}]({link}){tail}")
    if rel["po_folders"]:
        lines.append("")
        lines.append("**Prüfungsordnungen:**")
        for po in rel["po_folders"]:
            link = _relative_link_from(md_file, po["rel_index"], out_root)
            lines.append(f"- [{po['leaf']}]({link}) — `{po['rel_dir']}`")
    if lehramt:
        # Cap to a reasonable number to avoid overwhelming the index.
        lines.append("")
        lines.append("**Lehramts-Prüfungsordnungen:**")
        for pdf in lehramt[:30]:
            link = _relative_link_from(md_file, pdf["rel_path"], out_root)
            lines.append(f"- [{pdf['title']}]({link})")
        if len(lehramt) > 30:
            lines.append(f"- … und {len(lehramt)-30} weitere unter `pruefungsordnungen/lehramt/lehramtsfaecher/`")
    lines.append("")
    return "\n".join(lines)


_PO_VERSION_YEAR_RE = re.compile(r"PO-Version\s+(\d{4})\d?", re.IGNORECASE)


def _po_version_years(name: str) -> list[str]:
    """Years implied by a Campo PO-version name.

    Campo writes them as ``PO-Version 2007`` (single year) or
    ``PO-Version 20222`` (year + variant digit). We return the leading
    4-digit year — that's the one that turns up in FAU PDF filenames.
    """
    m = _PO_VERSION_YEAR_RE.search(name)
    return [m.group(1)] if m else []


def _po_pdfs_for_version(
    po_node: dict,
    program_node: dict,
    fau_index: dict,
    out_root: Path,
    md_file: Path,
) -> list[tuple[str, str]]:
    """For a Campo PO-version leaf, list FAU PO PDFs whose filename
    mentions the same 4-digit year. Returns ``[(label, rel_link), …]``.
    """
    related = _find_related_fau(program_node, fau_index)
    if not related["po_folders"]:
        return []
    years = _po_version_years(po_node["name"])
    if not years:
        return []
    matches: list[tuple[str, str]] = []
    seen: set[Path] = set()
    for po_folder in related["po_folders"]:
        folder = out_root / po_folder["rel_dir"]
        for pdf_md in sorted(folder.glob("*.md")):
            if pdf_md.name == "INDEX.md" or pdf_md in seen:
                continue
            stem = pdf_md.stem
            if not any(y in stem for y in years):
                continue
            seen.add(pdf_md)
            fm = _parse_frontmatter(pdf_md)
            label = fm.get("title") or stem
            link = _relative_link_from(
                md_file, pdf_md.relative_to(out_root).as_posix(), out_root
            )
            matches.append((label, link))
    return matches


def _related_pdf_section(
    po_node: dict,
    program_node: dict,
    fau_index: dict,
    out_root: Path,
    md_file: Path,
) -> str:
    pdfs = _po_pdfs_for_version(po_node, program_node, fau_index, out_root, md_file)
    if not pdfs:
        return ""
    lines = ["## Verwandte Prüfungsordnungs-PDFs (FAU.de)", ""]
    for label, link in pdfs:
        lines.append(f"- [{label}]({link})")
    lines.append("")
    return "\n".join(lines)


_STUB_FOLD_THRESHOLD = 24_000   # ≈ 8 k tokens — enough for a list of stubs.
_COURSE_FOLD_THRESHOLD = 90_000  # ≈ 30 k tokens — fits the F-TOKEN sweet spot.
_AVG_COURSE_CHARS = 2_500


def _empty_leaf_chars() -> int:
    """Rough size of a placeholder leaf (no course attached)."""
    return 700


def _estimate_folder_chars(
    kids: list[dict], courses_by_uid: dict[int, dict]
) -> tuple[int, bool]:
    """Estimated total chars + whether any kid is course-bearing."""
    total = 1500  # folder INDEX overhead
    has_courses = False
    for k in kids:
        uid = int(k.get("unitId") or 0)
        if uid and courses_by_uid.get(uid):
            total += _AVG_COURSE_CHARS
            has_courses = True
        else:
            total += _empty_leaf_chars()
    return total, has_courses


def _compute_fold_set(
    by_segment: dict[str, dict],
    children_of: dict[str, list[dict]],
    courses_by_uid: dict[int, dict],
) -> set[str]:
    """Decide which subtrees should collapse into one merged file.

    A segment folds iff:
      * it has children, all of which are themselves leaves (no grand-children), AND
      * the estimated total content fits below the appropriate threshold —
        small for stub-only folders (so they don't bloat) and 30 k-tokens
        for course-bearing folders (so an agent can read all events in one
        shot, e.g. "Musizieren an der Universität" with 17 Übungen).

    Re-evaluated on every render: when a deeper walk later adds
    grand-children, the fold is automatically dropped on the next render.
    """
    fold: set[str] = set()
    for seg, kids in children_of.items():
        if not kids:
            continue
        if any(children_of.get(k["segment"]) for k in kids):
            continue
        total, has_courses = _estimate_folder_chars(kids, courses_by_uid)
        threshold = _COURSE_FOLD_THRESHOLD if has_courses else _STUB_FOLD_THRESHOLD
        if total < threshold:
            fold.add(seg)
    return fold


def _course_h3_section(node: dict, course: dict, period_id: int) -> str:
    """A single course rendered as an ``###``-headed inline section
    inside a folded program file. Mirrors `render_course_md` but uses
    H3 for the title and H4 for sub-sections so the parent's H1/H2
    hierarchy survives."""
    title_clean = _strip_inline_html(node["name"]).lstrip("- ").strip()
    course_type = course.get("course_type") or ""
    heading = title_clean
    if course_type and course_type.lower() not in title_clean.lower():
        heading = f"{title_clean} — {course_type}"

    lines: list[str] = [f"### {heading}\n"]
    lines.append(
        f"- **Segment:** `{node['segment']}` · **unitId:** `{course.get('unit_id')}`"
    )
    lines.append(f"- **Katalog-Permalink:** <{catalog_permalink(node, period_id)}>")
    if course.get("permalink"):
        lines.append(f"- **Veranstaltungs-Permalink:** <{course['permalink']}>")

    eckdaten = [
        ("Veranstaltungsart", course.get("course_type")),
        ("ECTS-Punkte", course.get("ects")),
        ("Unterrichtssprache", course.get("language")),
        ("Turnus", course.get("turnus")),
    ]
    eckdaten = [(k, v) for k, v in eckdaten if v not in (None, "", [])]
    if eckdaten:
        lines.append("")
        for k, v in eckdaten:
            lines.append(f"- **{k}:** {v}")

    inst_resp = course.get("instructors_resp") or []
    inst_exec = course.get("instructors_exec") or []
    if inst_resp or inst_exec:
        lines.append("")
        if inst_resp:
            lines.append(f"- **Verantwortlich:** {', '.join(inst_resp)}")
        if inst_exec:
            lines.append(f"- **Durchführend:** {', '.join(inst_exec)}")

    appts = course.get("appointments") or []
    if appts:
        lines.append("")
        lines.append("#### Termine")
        lines.append("")
        lines.append("| Rhythmus | Tag | Zeit | Datum von–bis | Raum | Dozent/-in |")
        lines.append("|---|---|---|---|---|---|")
        for a in appts:
            time_cell = (
                f"{a['time_from']}–{a['time_to']}"
                if a.get("time_from") and a.get("time_to")
                else "—"
            )
            date_cell = (
                f"{a['date_from']}–{a['date_to']}"
                if a.get("date_from") and a.get("date_to")
                else (a.get("date_from") or "—")
            )
            lines.append(
                "| "
                + " | ".join(
                    _md_escape_cell(s)
                    for s in [
                        a.get("rhythm"),
                        a.get("weekday"),
                        time_cell,
                        date_cell,
                        a.get("room"),
                        ", ".join(a.get("instructors") or []) or None,
                    ]
                )
                + " |"
            )
    lines.append("")
    return "\n".join(lines)


def render_folded_md(
    program_node: dict,
    kids: list[dict],
    period_id: int,
    period_name: str,
    *,
    courses_by_uid: dict[int, dict] | None = None,
    fau_index: dict | None = None,
    md_file: Path | None = None,
    out_root: Path | None = None,
) -> str:
    """One merged file per folded program: program metadata + each leaf
    rendered as an H3 section. Replaces the program's INDEX.md folder
    when ``_compute_fold_set`` flagged it. If ``courses_by_uid`` is
    given, course content is inlined; otherwise the H3 section just
    holds metadata. If ``fau_index`` is given, "Verwandte FAU-Inhalte"
    is appended.
    """
    courses_by_uid = courses_by_uid or {}
    has_courses = any(courses_by_uid.get(int(k.get("unitId") or 0)) for k in kids)
    lines: list[str] = []
    lines.append(_front_matter(period_id, period_name, folded="true"))
    lines.append(f"# {_strip_inline_html(program_node['name'])}\n")
    lines.append(
        f"**Period:** {period_name} · **Segment:** `{program_node['segment']}` · "
        f"**Depth:** {len(program_node['path'])}\n"
    )
    lines.append(f"**Permalink:** <{catalog_permalink(program_node, period_id)}>\n")
    if has_courses:
        lines.append(
            "_All catalogue entries beneath this program are course events, "
            "merged here as one file so an agent can read every Termin in a "
            "single pass._\n"
        )
    else:
        lines.append(
            "_This program's PO-versions had no course content attached at the "
            "scraped catalogue depth, so they have been folded into this single "
            "file (instead of a subfolder + many tiny placeholders) — easier for "
            "agents to read in one pass._\n"
        )
    label = "Veranstaltungen" if has_courses else "PO-Versionen"
    lines.append(f"## {label} ({len(kids)})\n")
    for ch in sorted(kids, key=lambda k: k["name"].lower()):
        course = courses_by_uid.get(int(ch.get("unitId") or 0))
        if course:
            lines.append(_course_h3_section(ch, course, period_id))
        else:
            lines.append(f"### {_strip_inline_html(ch['name'])}\n")
            lines.append(f"- **Segment:** `{ch['segment']}`")
            lines.append(f"- **Permalink:** <{catalog_permalink(ch, period_id)}>")
            lines.append("")

    body = "\n".join(lines).lstrip("\n")

    # Append FAU cross-links if requested AND the program is at the
    # depth-3 layer where the linker has rules.
    if (
        fau_index is not None
        and md_file is not None
        and out_root is not None
        and len(program_node["path"]) == 3
        and program_node["segment"].startswith("title:")
    ):
        section = _related_fau_section(program_node, fau_index, md_file, out_root)
        if section:
            body = body.rstrip() + "\n\n" + section
    return body


_FRONT_MATTER_BLOCK_RE = re.compile(r"\A---\n.*?\n---\n+", re.DOTALL)
_H1_LINE_RE = re.compile(r"^# [^\n]*\n+", re.MULTILINE)


def _read_studiengang_body(rel_path_inside_root: str, out_root: Path) -> tuple[str, str]:
    """Return ``(source_url, body_md_without_frontmatter_or_h1)`` for one
    FAU.de Studiengang markdown that we want to inline. Empty strings if
    the file is missing or unreadable."""
    target = out_root / rel_path_inside_root
    try:
        text = target.read_text(encoding="utf-8")
    except OSError:
        return "", ""
    fm = _parse_frontmatter(target)
    src = fm.get("source_url", "")
    body = _FRONT_MATTER_BLOCK_RE.sub("", text, count=1)
    body = _H1_LINE_RE.sub("", body, count=1)
    body = body.strip()
    return src, body


def _walk_subtree(
    root_seg: str, children_of: dict[str, list[dict]]
) -> Iterable[dict]:
    """Yield every descendant node (excluding the root itself), depth-first."""
    stack = list(children_of.get(root_seg, []))
    while stack:
        n = stack.pop(0)
        yield n
        kids = children_of.get(n["segment"], [])
        if kids:
            # depth-first → push to front
            stack[:0] = kids


def render_program_md(
    program: dict,
    by_segment: dict[str, dict],
    children_of: dict[str, list[dict]],
    courses_by_uid: dict[int, dict],
    fau_index: dict,
    out_root: Path,
    md_path: Path,
    period_id: int,
    period_name: str,
) -> tuple[str, dict]:
    """Render *one* merged Campo-program markdown.

    Returns ``(content, stats_for_this_file)``. The file inlines:

      * matched FAU.de Studiengang content (Steckbrief + sections),
      * every PO-version under the program with permalinks +
        year-matched dated PDF references,
      * every course attached to any leaf in the subtree (full Eckdaten +
        Termine + instructors),
      * a Lehramts-Prüfungsordnungen list when the program has no
        Studiengang match but matches Lehramt PDFs.

    Source links are preserved verbatim (Campo permalinks, FAU.de URLs,
    PDF source URLs all appear inline so a RAG can cite them).
    """
    file_stats = {"po_versions": 0, "courses": 0, "studiengang_inlines": 0, "lehramt_pdfs": 0}

    # Collect descendants → split into PO-versions vs courses
    po_versions: list[dict] = []
    course_pairs: list[tuple[dict, dict]] = []
    for n in _walk_subtree(program["segment"], children_of):
        kids = children_of.get(n["segment"], [])
        if kids:
            continue  # internal node: not a course, not a leaf PO-version
        # leaf
        uid = int(n.get("unitId") or 0)
        if uid and courses_by_uid.get(uid):
            course_pairs.append((n, courses_by_uid[uid]))
        else:
            po_versions.append(n)

    # FAU matches
    related = _find_related_fau(program, fau_index)
    has_studiengang = bool(related["studiengang"])

    # ── Front-matter ──────────────────────────────────────────────────
    fm: list[str] = ["---"]
    fm.append(f"period_id: {period_id}")
    fm.append(f"period_name: {json.dumps(period_name, ensure_ascii=False)}")
    fm.append(f'campo_segment: "{program["segment"]}"')
    fm.append(f'campo_path: "{"|".join(program["path"])}"')
    fm.append(f'campo_permalink: "{catalog_permalink(program, period_id)}"')
    fm.append(f"po_version_count: {len(po_versions)}")
    fm.append(f"course_count: {len(course_pairs)}")
    if has_studiengang:
        fm.append("fau_studiengang:")
        for sg in related["studiengang"]:
            fm.append(f'  - title: {json.dumps(sg["title"], ensure_ascii=False)}')
            fm.append(f'    rel_path: {json.dumps(sg["rel_path"], ensure_ascii=False)}')
    fm.append("---")
    fm.append("")

    body: list[str] = []
    body.append(f"# {_strip_inline_html(program['name'])}")
    body.append("")
    body.append(f"**Campo-Permalink:** <{catalog_permalink(program, period_id)}>")
    body.append("")
    body.append(
        f"_Section: {by_segment[program['path'][1]]['name']}_  "
        if len(program["path"]) >= 2
        else ""
    )
    body.append("")

    # ── FAU.de Studiengang content ────────────────────────────────────
    if has_studiengang:
        body.append("## FAU.de Studiengang-Seiten")
        body.append("")
        for sg in related["studiengang"]:
            src_url, sg_body = _read_studiengang_body(sg["rel_path"], out_root)
            note = sg.get("abschluss") or sg.get("fakultaet") or ""
            tail = f" — {note}" if note else ""
            body.append(f"### {sg['title']}{tail}")
            body.append("")
            if src_url:
                body.append(f"**Quelle (FAU.de):** <{src_url}>")
                body.append("")
            if sg_body:
                # Demote H2 → H4 inside the inlined body so the program's H1/H2
                # hierarchy isn't broken.
                demoted = re.sub(r"^## ", "#### ", sg_body, flags=re.MULTILINE)
                demoted = re.sub(r"^### ", "##### ", demoted, flags=re.MULTILINE)
                body.append(demoted)
                body.append("")
                file_stats["studiengang_inlines"] += 1

    # ── PO-versions ───────────────────────────────────────────────────
    if po_versions:
        body.append(f"## Prüfungsordnungs-Versionen ({len(po_versions)})")
        body.append("")
        for po in sorted(po_versions, key=lambda n: n["name"].lower()):
            title = _strip_inline_html(po["name"]).lstrip("- ").strip()
            body.append(f"### {title}")
            body.append("")
            body.append(f"- **Campo-Segment:** `{po['segment']}`")
            body.append(f"- **Campo-Permalink:** <{catalog_permalink(po, period_id)}>")
            pdfs = _po_pdfs_for_version(po, program, fau_index, out_root, md_path)
            if pdfs:
                body.append("- **Passende PO-PDFs (FAU.de):**")
                for label, link in pdfs:
                    body.append(f"  - [{label}]({link})")
            body.append("")
            file_stats["po_versions"] += 1

    # ── Courses ───────────────────────────────────────────────────────
    if course_pairs:
        body.append(f"## Veranstaltungen ({len(course_pairs)})")
        body.append("")
        for node, course in sorted(course_pairs, key=lambda p: p[0]["name"].lower()):
            body.append(_course_h3_section(node, course, period_id))
            file_stats["courses"] += 1

    # ── Lehramt fallback ──────────────────────────────────────────────
    if not has_studiengang:
        lehramt_pdfs = _lehramt_pdf_matches(program, fau_index)
        if lehramt_pdfs:
            body.append("## Lehramts-Prüfungsordnungen")
            body.append("")
            for pdf in lehramt_pdfs[:30]:
                link = _relative_link_from(md_path, pdf["rel_path"], out_root)
                body.append(f"- [{pdf['title']}]({link})")
            if len(lehramt_pdfs) > 30:
                body.append(
                    f"- … und {len(lehramt_pdfs)-30} weitere unter "
                    "`pruefungsordnungen/lehramt/lehramtsfaecher/`"
                )
            body.append("")
            file_stats["lehramt_pdfs"] = len(lehramt_pdfs)

    return "\n".join(fm + body).rstrip() + "\n", file_stats


def render_period_index_md(
    period_id: int,
    period_name: str,
    by_segment: dict[str, dict],
    by_section: dict[str, list[dict]],
    program_filenames: dict[str, str],
) -> str:
    """Top-level INDEX for a period — programs grouped by section heading."""
    fm = [
        "---",
        f"period_id: {period_id}",
        f"period_name: {json.dumps(period_name, ensure_ascii=False)}",
        f"program_count: {sum(len(v) for v in by_section.values())}",
        "---",
        "",
    ]
    body: list[str] = [
        f"# {period_name} — Studiengänge",
        "",
        "Dieses Verzeichnis enthält pro Campo-Studiengang **eine** Markdown-Datei "
        "mit allen Prüfungsordnungs-Versionen, Veranstaltungen und der zugehörigen "
        "FAU.de-Studiengang-Seite *inline*. Die großen PO-PDF-Volltexte liegen separat "
        "unter [`../pruefungsordnungen/`](../pruefungsordnungen/INDEX.md) und sind aus "
        "den Programm-Dateien direkt verlinkt.",
        "",
    ]
    section_segments = sorted(
        by_section.keys(), key=lambda s: by_segment[s]["name"].lower()
    )
    for sec_seg in section_segments:
        sec_name = by_segment[sec_seg]["name"]
        progs = sorted(by_section[sec_seg], key=lambda p: p["name"].lower())
        body.append(f"## {sec_name}")
        body.append("")
        for p in progs:
            fname = program_filenames[p["segment"]]
            body.append(f"- [{_strip_inline_html(p['name'])}]({fname})")
        body.append("")
    return "\n".join(fm + body)


def _wipe_period_folder(base: Path) -> None:
    """Remove every previous render output under ``base`` so a re-render
    starts fresh — keeps the parent ``out/`` tree untouched."""
    if not base.exists():
        return
    for child in base.iterdir():
        if child.is_dir():
            shutil.rmtree(child)
        else:
            child.unlink()


def render_corpus(
    snapshot: dict, out_root: Path, *, courses: dict | None = None
) -> dict:
    """Write the merged-program corpus under ``out_root/{period-slug}/``.

    Layout (Entry 0013):
      * ``out/{period}/INDEX.md`` — programs grouped by section.
      * ``out/{period}/{program-slug-id}.md`` — one merged file per Campo
        depth-3 program, with FAU.de Studiengang inline + every PO-version
        + every course (Eckdaten + Termine + instructors).
    """
    period_id: int = snapshot["periodId"]
    period_name: str = snapshot["periodName"]
    period_slug = f"{period_id}-{slugify(period_name)}"
    base = out_root / period_slug
    _wipe_period_folder(base)
    base.mkdir(parents=True, exist_ok=True)

    by_segment: dict[str, dict] = {n["segment"]: n for n in snapshot["nodes"]}
    children_of: dict[str, list[dict]] = {}
    for n in snapshot["nodes"]:
        ps = n.get("parentSegment")
        if ps:
            children_of.setdefault(ps, []).append(n)

    courses_by_uid: dict[int, dict] = {}
    if courses:
        for c in courses.get("courses", []):
            courses_by_uid[int(c["unit_id"])] = c

    fau_index = load_fau_index(out_root)

    # Identify the "program" layer: every depth-3 node is a program — it's
    # the unit a user (and a RAG) thinks about as a single thing.
    programs = [n for n in snapshot["nodes"] if len(n["path"]) == 3]

    # Group programs by their section (depth-2 parent) for the period INDEX.
    by_section: dict[str, list[dict]] = {}
    program_filenames: dict[str, str] = {}
    for p in programs:
        section_seg = p["path"][1]
        by_section.setdefault(section_seg, []).append(p)
        program_filenames[p["segment"]] = f"{node_basename(p)}.md"

    stats = {
        "programs": 0,
        "po_versions": 0,
        "courses_embedded": 0,
        "studiengang_inlines": 0,
        "lehramt_pdf_blocks": 0,
    }

    # Render every program
    for program in programs:
        md_path = base / program_filenames[program["segment"]]
        content, fstats = render_program_md(
            program,
            by_segment,
            children_of,
            courses_by_uid,
            fau_index,
            out_root,
            md_path,
            period_id,
            period_name,
        )
        md_path.write_text(content, encoding="utf-8")
        stats["programs"] += 1
        stats["po_versions"] += fstats["po_versions"]
        stats["courses_embedded"] += fstats["courses"]
        stats["studiengang_inlines"] += fstats["studiengang_inlines"]
        if fstats["lehramt_pdfs"]:
            stats["lehramt_pdf_blocks"] += 1

    # Top-level period INDEX
    index_md = render_period_index_md(
        period_id, period_name, by_segment, by_section, program_filenames
    )
    (base / "INDEX.md").write_text(index_md, encoding="utf-8")

    return stats


# ── CLI ─────────────────────────────────────────────────────────────────────


def main(argv: Iterable[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument(
        "--in",
        dest="inp",
        type=Path,
        required=True,
        help="path to a JSON snapshot produced by scrape.py",
    )
    p.add_argument(
        "--out",
        type=Path,
        required=True,
        help="output root (period-slug subfolder will be created beneath it)",
    )
    p.add_argument(
        "--courses",
        type=Path,
        default=None,
        help="optional JSON from fetch_courses.py — embeds course content in leaves",
    )
    args = p.parse_args(list(argv) if argv else None)

    snapshot = json.loads(args.inp.read_text(encoding="utf-8"))
    courses = (
        json.loads(args.courses.read_text(encoding="utf-8")) if args.courses else None
    )
    stats = render_corpus(snapshot, args.out, courses=courses)
    print(
        f"rendered period {snapshot['periodId']} {snapshot['periodName']!r} "
        f"into {args.out}: programs={stats['programs']} "
        f"po_versions={stats['po_versions']} courses={stats['courses_embedded']} "
        f"studiengang_inlines={stats['studiengang_inlines']} "
        f"lehramt_blocks={stats['lehramt_pdf_blocks']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
