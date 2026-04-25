"""Parse a rendered Campo course-catalogue HTML page.

Tree topology learned from probing real Campo (2026-04-25):

  * Path segments come in two kinds:
      ``title:NNN`` — sections, faculties, study programs.
      ``exam:NNN``  — Prüfungsordnung (PO) versions and their sub-blocks.
  * Levels 1–3 are typically all ``title:`` nodes (root, section, program).
  * Level 4+ are typically ``exam:`` nodes — the PO chain may nest further.
  * Concrete courses (with a ``unit_id``) **do not** appear directly in the
    catalogue HTML; they are fetched through the search-flow keyed by
    ``unitId``. The catalogue is the structural index, not a course listing.

Each rendered node carries:

  * a ``<textarea>`` whose body is its permalink URL (encoding the full
    ``path=…`` chain) and whose ``data-page-permalink-title="…"`` attribute
    holds the human-readable name.
  * an inner JSF tree-position (``courseCatalog:0:5:16:0:t2g_0`` etc.) which
    is *only* useful as a uniqueness marker; we ignore it.
"""
from __future__ import annotations

import html as _html
import re
import urllib.parse as _url
from dataclasses import dataclass


# Build a permalink textarea with its attribute string + body in one match.
PERMALINK_TEXTAREA_RE = re.compile(
    r"<textarea\b([^>]*?)>\s*(https?://[^<]*?_flowId=showCourseCatalog-flow[^<]*?)\s*</textarea>",
    re.IGNORECASE | re.DOTALL,
)
PERMALINK_TITLE_ATTR_RE = re.compile(
    r'\bdata-page-permalink-title="([^"]+)"', re.IGNORECASE
)
PATH_PARAM_RE = re.compile(r"[?&]path=([^&\s\"']+)")
PERIOD_PARAM_RE = re.compile(r"[?&]periodId=(\d+)")
SEGMENT_RE = re.compile(r"^([a-z]+):(\d+)$", re.IGNORECASE)


@dataclass
class ParsedNode:
    """One node found on the page."""

    segment: str        # e.g. "title:17593" or "exam:14867623"
    name: str
    path: list[str]     # inclusive: from root to this node


def _decode_permalink(url: str) -> tuple[int, list[str]] | None:
    """Return (period_id, [segment, …]) or None if the URL is malformed.

    Accepts either URL-encoded or pre-decoded path parameters; segments are
    of the form ``KIND:ID`` with KIND ∈ {title, exam, …}.
    """
    dec = _html.unescape(url)
    m_pid = PERIOD_PARAM_RE.search(dec)
    m_path = PATH_PARAM_RE.search(dec)
    if not m_pid:
        return None
    period_id = int(m_pid.group(1))
    if not m_path:
        return period_id, []
    raw_path = _url.unquote(m_path.group(1))
    segments: list[str] = []
    for seg in raw_path.split("|"):
        seg = seg.strip()
        if not seg:
            continue
        if not SEGMENT_RE.match(seg):
            return None
        segments.append(seg)
    if not segments:
        return None
    return period_id, segments


def parse_nodes(html: str) -> list[ParsedNode]:
    """Extract every node-with-permalink from the rendered page.

    Each permalink ``<textarea>`` carries the full path in its body and the
    human-readable name in ``data-page-permalink-title``. The same node can
    appear in two textareas (inline + popup copy) — we deduplicate by
    terminal segment.
    """
    seen: set[str] = set()
    nodes: list[ParsedNode] = []
    for m in PERMALINK_TEXTAREA_RE.finditer(html):
        attrs, url = m.group(1), m.group(2)
        decoded = _decode_permalink(url)
        if decoded is None:
            continue
        _period_id, segments = decoded
        if not segments:
            continue
        terminal = segments[-1]
        if terminal in seen:
            continue
        seen.add(terminal)
        title_m = PERMALINK_TITLE_ATTR_RE.search(attrs)
        name = (
            _html.unescape(title_m.group(1)).strip()
            if title_m
            else terminal
        )
        nodes.append(ParsedNode(segment=terminal, name=name, path=segments))
    return nodes


def classify_nodes(
    all_nodes: list[ParsedNode], current_path: list[str]
) -> tuple[ParsedNode | None, list[ParsedNode]]:
    """Split the parsed nodes into (current, immediate_children).

    *Current* matches ``current_path`` exactly. *Immediate children* are
    nodes whose path is ``current_path`` plus exactly one segment.
    """
    current: ParsedNode | None = None
    children: list[ParsedNode] = []
    for n in all_nodes:
        if n.path == current_path:
            current = n
        elif (
            len(n.path) == len(current_path) + 1
            and n.path[: len(current_path)] == current_path
        ):
            children.append(n)
    return current, children


PERIOD_OPTION_RE = re.compile(
    r'<option[^>]*\bvalue="(\d+)"[^>]*>\s*([^<]+?)\s*</option>'
)
PERIOD_SELECT_RE = re.compile(
    r'<select\b[^>]*\bid="[^"]*termSelection_input"[^>]*>(.*?)</select>',
    re.IGNORECASE | re.DOTALL,
)


def parse_periods(html: str) -> list[tuple[int, str]]:
    """Extract ``(period_id, name)`` pairs from the semester ``<select>``."""
    m = PERIOD_SELECT_RE.search(html)
    if not m:
        return []
    options = PERIOD_OPTION_RE.findall(m.group(1))
    out: list[tuple[int, str]] = []
    for raw_id, raw_name in options:
        try:
            pid = int(raw_id)
        except ValueError:
            continue
        name = _html.unescape(raw_name).strip()
        if name and name != "---":
            out.append((pid, name))
    return out


def parse_root_segment(html: str) -> str | None:
    """The root permalink of the catalogue page, e.g. ``"title:17593"``."""
    nodes = parse_nodes(html)
    if not nodes:
        return None
    # The shortest path is always the root.
    return min(nodes, key=lambda n: len(n.path)).segment
