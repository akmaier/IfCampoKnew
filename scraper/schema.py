"""Dataclasses describing the scraped Campo structures.

The same shapes are serialised to JSON and re-read by the UI at runtime.
Keep fields JSON-friendly (no sets, no tuples beyond simple ones).
"""
from __future__ import annotations

from dataclasses import dataclass, field, asdict
from typing import Optional


@dataclass
class CatalogNode:
    """One node in the Campo course catalogue tree.

    A node can be either an internal (subject/faculty) node or a leaf course.
    Leaf-ness is indicated by ``unit_id`` being set: internal nodes have
    ``unit_id is None`` and zero or more ``children``.
    """

    title_id: int
    name: str
    path: list[int]
    parent_title_id: Optional[int] = None
    children: list[int] = field(default_factory=list)
    unit_id: Optional[int] = None

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class CatalogSnapshot:
    """A complete per-semester catalogue tree."""

    period_id: int
    period_name: str
    scraped_at: str  # ISO-8601
    root_title_id: int
    nodes: list[CatalogNode]

    def to_dict(self) -> dict:
        return {
            "periodId": self.period_id,
            "periodName": self.period_name,
            "scrapedAt": self.scraped_at,
            "rootTitleId": self.root_title_id,
            "nodes": [n.to_dict() for n in self.nodes],
        }
