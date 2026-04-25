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
class Appointment:
    """One row of the *Termine* (schedule) table on a course-detail page."""

    rhythm: Optional[str] = None  # "wöchentlich", "einmalig", "Block", …
    weekday: Optional[str] = None  # "Mo", "Di", "Mi", …
    time_from: Optional[str] = None  # "HH:MM"
    time_to: Optional[str] = None  # "HH:MM"
    date_from: Optional[str] = None  # "DD.MM.YYYY"
    date_to: Optional[str] = None  # "DD.MM.YYYY"
    room: Optional[str] = None
    instructors: list[str] = field(default_factory=list)
    cancelled_dates: list[str] = field(default_factory=list)
    note: Optional[str] = None

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class Course:
    """One course event (Lehrveranstaltung) with its public detail data.

    Mirrors the Termine tab of Campo's ``detailView-flow`` page; richer
    tabs (Inhalte, Module/Studiengänge, Dokumente) are filled in only
    when the renderer asks for them.
    """

    unit_id: int
    period_id: int
    title: str
    permalink: str
    course_type: Optional[str] = None  # Vorlesung / Seminar / Übung / Praktikum
    short_text: Optional[str] = None
    ects: Optional[float] = None
    language: Optional[str] = None
    turnus: Optional[str] = None
    instructors_resp: list[str] = field(default_factory=list)
    instructors_exec: list[str] = field(default_factory=list)
    appointments: list[Appointment] = field(default_factory=list)
    org_unit: Optional[str] = None
    description: Optional[str] = None  # Inhalte tab — filled if available
    extra_links: list[tuple[str, str]] = field(default_factory=list)  # (label, url)

    def to_dict(self) -> dict:
        d = asdict(self)
        # appointments serialise themselves
        d["appointments"] = [a.to_dict() for a in self.appointments]
        return d


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
