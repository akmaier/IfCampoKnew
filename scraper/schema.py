"""Dataclasses describing the scraped Campo structures.

The same shapes are serialised to JSON and re-read by the UI at runtime.
Keep fields JSON-friendly (no sets, no tuples beyond simple ones).
"""
from __future__ import annotations

from dataclasses import dataclass, field, asdict
from typing import Optional


@dataclass
class CatalogNode:
    """One node in the Campo course-catalogue tree.

    Campo identifies tree nodes by *segments* of the form ``"title:NNN"`` for
    title/program nodes and ``"exam:NNN"`` for examination-regulation
    (Prüfungsordnung) nodes. We keep the raw segment string and expose its
    parts (``kind``, ``node_id``) for convenience.

    A node is a *leaf* in the catalogue when ``len(children) == 0``. It can
    additionally have a ``unit_id`` if the catalogue links it to a concrete
    course event — but in practice the FAU catalogue bottoms out at PO
    sections, and courses are reached via the search-flow.
    """

    segment: str
    name: str
    path: list[str]
    parent_segment: Optional[str] = None
    children: list[str] = field(default_factory=list)
    unit_id: Optional[int] = None

    @property
    def kind(self) -> str:
        return self.segment.split(":", 1)[0]

    @property
    def node_id(self) -> int:
        return int(self.segment.split(":", 1)[1])

    def to_dict(self) -> dict:
        return {
            "segment": self.segment,
            "kind": self.kind,
            "nodeId": self.node_id,
            "name": self.name,
            "path": list(self.path),
            "parentSegment": self.parent_segment,
            "children": list(self.children),
            "unitId": self.unit_id,
        }


@dataclass
class CatalogSnapshot:
    """A complete per-semester catalogue tree."""

    period_id: int
    period_name: str
    scraped_at: str  # ISO-8601
    root_segment: str
    max_depth: int  # the depth limit used (1 = root only)
    nodes: list[CatalogNode]

    def to_dict(self) -> dict:
        return {
            "periodId": self.period_id,
            "periodName": self.period_name,
            "scrapedAt": self.scraped_at,
            "rootSegment": self.root_segment,
            "maxDepth": self.max_depth,
            "nodes": [n.to_dict() for n in self.nodes],
        }
