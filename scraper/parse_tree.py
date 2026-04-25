"""Parse a rendered Campo course-catalogue HTML page.

What we extract from one GET of ``showCourseCatalog-flow``:
  * The *current* node (the one addressed by ``path=``), including its name
    and ``title_id``.
  * Its immediate children: ``title_id``, name, and the full path from root.

How: Campo embeds a ``<textarea>`` with the node's permalink next to every
rendered node (current + children + optionally some already-expanded
descendants). Each permalink's ``path=`` parameter gives us the full id
chain. The node name is in the nearest preceding ``<h3>Permalink: …</h3>``.
"""
from __future__ import annotations

import html as _html
import re
import urllib.parse as _url
from dataclasses import dataclass
from typing import Optional


PERMALINK_TEXTAREA_RE = re.compile(
    # The <textarea> carries the node's permalink as its body and — critically —
    # the node's human-readable name in a ``data-page-permalink-title`` attribute.
    r"<textarea\b([^>]*?)>\s*(https?://[^<]*_flowId=showCourseCatalog-flow[^<]*?)\s*</textarea>",
    re.IGNORECASE | re.DOTALL,
)
PERMALINK_TITLE_ATTR_RE = re.compile(
    r'\bdata-page-permalink-title="([^"]+)"', re.IGNORECASE
)
PATH_PARAM_RE = re.compile(r"[?&]path=([^&\s\"']+)")
PERIOD_PARAM_RE = re.compile(r"[?&]periodId=(\d+)")


@dataclass
class ParsedNode:
    """A node found on the rendered page."""

    title_id: int
    name: str
    path: list[int]  # inclusive, from root to this node


def _decode_permalink(url: str) -> Optional[tuple[int, list[int]]]:
    """Return (periodId, path as ids) or None if the URL is malformed."""
    dec = _html.unescape(url)
    m_pid = PERIOD_PARAM_RE.search(dec)
    m_path = PATH_PARAM_RE.search(dec)
    if not m_pid:
        return None
    period_id = int(m_pid.group(1))
    if not m_path:
        # Root-most view: no path parameter — caller must know the root id.
        return period_id, []
    raw_path = _url.unquote(m_path.group(1))
    ids: list[int] = []
    for seg in raw_path.split("|"):
        seg = seg.strip()
        if not seg.startswith("title:"):
            continue
        try:
            ids.append(int(seg.split(":", 1)[1]))
        except ValueError:
            return None
    if not ids:
        return None
    return period_id, ids


def parse_nodes(html: str) -> list[ParsedNode]:
    """Extract every node-with-permalink from the rendered page, in order.

    Each permalink textarea has the node's full path in its body; the node's
    human-readable name sits in ``data-page-permalink-title="…"`` on the same
    tag. Duplicate ``title_id`` s are deduplicated (Campo emits two permalink
    textareas per node — inline + popup copy).
    """
    seen: set[int] = set()
    nodes: list[ParsedNode] = []
    for m in PERMALINK_TEXTAREA_RE.finditer(html):
        attrs, url = m.group(1), m.group(2)
        decoded = _decode_permalink(url)
        if decoded is None:
            continue
        _period_id, ids = decoded
        if not ids:
            continue
        title_id = ids[-1]
        if title_id in seen:
            continue
        seen.add(title_id)
        title_m = PERMALINK_TITLE_ATTR_RE.search(attrs)
        name = _html.unescape(title_m.group(1)).strip() if title_m else f"title:{title_id}"
        nodes.append(ParsedNode(title_id=title_id, name=name, path=ids))
    return nodes


def classify_nodes(
    all_nodes: list[ParsedNode], current_path: list[int]
) -> tuple[ParsedNode, list[ParsedNode]]:
    """Split the parsed nodes into (current, immediate_children).

    * The *current* node has ``path == current_path``.
    * *Immediate children* have ``path == current_path + [X]``.
    * Anything deeper is ignored (it appears only as side-effect of Campo's
      "expand ancestors and descendants of the current node" behaviour).
    """
    current: Optional[ParsedNode] = None
    children: list[ParsedNode] = []
    for n in all_nodes:
        if n.path == current_path:
            current = n
        elif (
            len(n.path) == len(current_path) + 1
            and n.path[: len(current_path)] == current_path
        ):
            children.append(n)
    if current is None:
        # Some root renderings omit the self-permalink; synthesise one.
        current = ParsedNode(
            title_id=current_path[-1] if current_path else 0,
            name="",
            path=list(current_path),
        )
    return current, children


PERIOD_OPTION_RE = re.compile(
    r'<option[^>]*\bvalue="(\d+)"[^>]*>\s*([^<]+?)\s*</option>'
)
PERIOD_SELECT_RE = re.compile(
    r'<select\b[^>]*\bid="[^"]*termSelection_input"[^>]*>(.*?)</select>',
    re.IGNORECASE | re.DOTALL,
)


def parse_periods(html: str) -> list[tuple[int, str]]:
    """Extract (period_id, period_name) pairs from the semester dropdown."""
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
