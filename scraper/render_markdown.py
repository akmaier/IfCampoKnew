"""Render a Campo catalogue snapshot as a hierarchical markdown corpus.

Each catalogue node becomes either a folder + ``INDEX.md`` (if it has
children) or a single ``<slug>.md`` file (leaf, in the parent folder).
Slug language is Campo-faithful (German, ASCII-folded with umlaut
expansion: ä→ae, ö→oe, ü→ue, ß→ss). The terminal segment ID is appended
to every name so file paths stay stable across weekly scrapes.

The output is intended for consumption by LLM-based agents (an agent
walks INDEX.md → child INDEX.md → content). Plain humans browsing on
github.com get a passable secondary view because GitHub renders .md
natively.

Layout per period:

    out/{period-slug}/
        INDEX.md                                   # root overview
        {section-slug-id}/                         # one folder per section
            INDEX.md
            {program-slug-id}/                     # one per program (if it has POs)
                INDEX.md
                {po-version-slug-id}.md            # leaf
            {program-slug-id}.md                   # leaf-program (no PO sub-tree)
        ...
"""
from __future__ import annotations

import argparse
import json
import re
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

    Returns a dict with two indexes keyed by *slugified base name*:
      * ``studiengang``: name → list of {slug, title, fakultaet, rel_path}
      * ``po_folders``:   name → list of {rel_dir, name (faculty/program)}
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

    return {
        "studiengang": studiengang_by_base,
        "po_folders": po_folders_by_leaf,
    }


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
    if not rel["studiengang"] and not rel["po_folders"]:
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


def render_corpus(
    snapshot: dict, out_root: Path, *, courses: dict | None = None
) -> dict:
    """Write the whole markdown tree under ``out_root/{period-slug}/``.

    If ``courses`` (the JSON produced by ``fetch_courses.py``) is given,
    every leaf with a ``unitId`` is rendered with full course detail
    instead of the placeholder text.
    """
    period_id: int = snapshot["periodId"]
    period_name: str = snapshot["periodName"]
    period_slug = f"{period_id}-{slugify(period_name)}"
    base = out_root / period_slug
    base.mkdir(parents=True, exist_ok=True)

    by_segment: dict[str, dict] = {n["segment"]: n for n in snapshot["nodes"]}
    children_of: dict[str, list[dict]] = {}
    for n in snapshot["nodes"]:
        ps = n.get("parentSegment")
        if ps:
            children_of.setdefault(ps, []).append(n)

    root_seg: str = snapshot.get("rootSegment") or next(
        n["segment"] for n in snapshot["nodes"] if not n.get("parentSegment")
    )
    root = by_segment[root_seg]

    courses_by_uid: dict[int, dict] = {}
    if courses:
        for c in courses.get("courses", []):
            courses_by_uid[int(c["unit_id"])] = c

    fau_index = load_fau_index(out_root)

    stats = {
        "folders": 0,
        "leaf_files": 0,
        "index_files": 0,
        "courses_embedded": 0,
        "fau_links": 0,
    }

    def child_targets(parent_seg: str) -> dict[str, str]:
        out: dict[str, str] = {}
        for ch in children_of.get(parent_seg, []):
            base_name = node_basename(ch)
            if children_of.get(ch["segment"]):
                out[ch["segment"]] = f"{base_name}/"
            else:
                out[ch["segment"]] = f"{base_name}.md"
        return out

    def walk(seg: str, folder: Path) -> None:
        node = by_segment[seg]
        kids = children_of.get(seg, [])
        if kids:
            folder.mkdir(parents=True, exist_ok=True)
            stats["folders"] += 1
            content = render_index_md(
                node, period_id, period_name, kids, child_targets(seg)
            )
            # Cross-link Campo program-level nodes (depth 3, title:NNN) to
            # matching FAU.de Studiengang and PO landing pages.
            if (
                len(node["path"]) == 3
                and node["segment"].startswith("title:")
            ):
                fau_section = _related_fau_section(
                    node, fau_index, folder / "INDEX.md", out_root
                )
                if fau_section:
                    content = content.rstrip() + "\n\n" + fau_section
                    stats["fau_links"] += 1
            (folder / "INDEX.md").write_text(content, encoding="utf-8")
            stats["index_files"] += 1
            for ch in kids:
                base_name = node_basename(ch)
                if children_of.get(ch["segment"]):
                    walk(ch["segment"], folder / base_name)
                else:
                    leaf_file = folder / f"{base_name}.md"
                    course = courses_by_uid.get(int(ch.get("unitId") or 0))
                    if course:
                        content = render_course_md(ch, course, period_id, period_name)
                        stats["courses_embedded"] += 1
                    else:
                        content = render_leaf_md(ch, period_id, period_name)

                    # PO-version → matching FAU PO PDF: only for depth-4
                    # exam:NNN leaves whose parent program node we can resolve.
                    if (
                        len(ch["path"]) == 4
                        and ch["segment"].startswith("exam:")
                    ):
                        program_seg = ch["path"][2]
                        program_node = by_segment.get(program_seg)
                        if program_node:
                            pdf_section = _related_pdf_section(
                                ch, program_node, fau_index, out_root, leaf_file
                            )
                            if pdf_section:
                                content = content.rstrip() + "\n\n" + pdf_section
                                stats["fau_links"] += 1
                    leaf_file.write_text(content, encoding="utf-8")
                    stats["leaf_files"] += 1
        else:
            # Root with no children — degenerate but keep the file.
            (folder / "INDEX.md").write_text(
                render_leaf_md(node, period_id, period_name), encoding="utf-8"
            )
            stats["index_files"] += 1
    walk(root_seg, base)
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
        f"into {args.out}: folders={stats['folders']} index={stats['index_files']} "
        f"leaves={stats['leaf_files']} courses_embedded={stats['courses_embedded']} "
        f"fau_links={stats['fau_links']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
