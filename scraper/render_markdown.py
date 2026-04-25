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


def _front_matter(period_id: int, period_name: str) -> str:
    return (
        "---\n"
        f"period_id: {period_id}\n"
        f"period_name: {json.dumps(period_name, ensure_ascii=False)}\n"
        "---\n\n"
    )


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


def render_corpus(snapshot: dict, out_root: Path) -> dict:
    """Write the whole markdown tree under ``out_root/{period-slug}/``.

    Returns a small stats dict for logging.
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

    stats = {"folders": 0, "leaf_files": 0, "index_files": 0}

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
            (folder / "INDEX.md").write_text(
                render_index_md(node, period_id, period_name, kids, child_targets(seg)),
                encoding="utf-8",
            )
            stats["index_files"] += 1
            for ch in kids:
                base_name = node_basename(ch)
                if children_of.get(ch["segment"]):
                    walk(ch["segment"], folder / base_name)
                else:
                    (folder / f"{base_name}.md").write_text(
                        render_leaf_md(ch, period_id, period_name),
                        encoding="utf-8",
                    )
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
    args = p.parse_args(list(argv) if argv else None)

    snapshot = json.loads(args.inp.read_text(encoding="utf-8"))
    stats = render_corpus(snapshot, args.out)
    print(
        f"rendered period {snapshot['periodId']} {snapshot['periodName']!r} "
        f"into {args.out}: folders={stats['folders']} index={stats['index_files']} "
        f"leaves={stats['leaf_files']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
