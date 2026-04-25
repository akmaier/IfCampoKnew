"""Tests for ``parse_tree``.

Fixtures are real HTML pages captured from www.campo.fau.de (anonymously)
so the tests guard against regressions in the regex contract Campo's
HISinOne instance hands us.
"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR))

from parse_tree import (  # noqa: E402
    _decode_permalink,
    classify_nodes,
    parse_nodes,
    parse_periods,
    parse_root_segment,
)

FIXTURES = Path(__file__).parent / "fixtures"


@pytest.fixture(scope="module")
def musi_html() -> str:
    return (FIXTURES / "musizieren.html").read_text(encoding="utf-8")


def test_decode_permalink_simple():
    pid, segs = _decode_permalink(
        "https://x/?_flowId=showCourseCatalog-flow&periodId=589&path=title:17593"
    )
    assert pid == 589
    assert segs == ["title:17593"]


def test_decode_permalink_url_encoded():
    pid, segs = _decode_permalink(
        "https://x/?_flowId=showCourseCatalog-flow&periodId=589&path=title%3A17593%7Ctitle%3A17601%7Cexam%3A14867623"
    )
    assert pid == 589
    assert segs == ["title:17593", "title:17601", "exam:14867623"]


def test_decode_permalink_html_entities():
    pid, segs = _decode_permalink(
        "https://x/?_flowId=showCourseCatalog-flow&amp;periodId=589&amp;path=title:17593"
    )
    assert pid == 589
    assert segs == ["title:17593"]


def test_decode_permalink_rejects_garbage():
    assert _decode_permalink("https://x/?nope=1") is None


def test_parse_nodes_musizieren_finds_course_leaves(musi_html):
    """The Musizieren parent page exposes 17 course-leaf rows.

    Each course leaf must (a) be an ``exam:`` segment and (b) carry the
    ``unit_id`` from its action-column ``detailView-flow`` link.
    """
    nodes = parse_nodes(musi_html)
    # course leaves under title:17991
    musi_kids = [
        n for n in nodes
        if len(n.path) == 4 and n.path[2] == "title:17991"
    ]
    assert len(musi_kids) >= 17
    for n in musi_kids:
        assert n.segment.startswith("exam:")
        assert n.unit_id is not None and n.unit_id > 0


def test_parse_nodes_finds_a_specific_course(musi_html):
    """Akademischer Chor row must yield exam:15688820 → unit_id=92769."""
    nodes = parse_nodes(musi_html)
    chor = next(
        (n for n in nodes if n.segment == "exam:15688820"), None
    )
    assert chor is not None
    assert chor.unit_id == 92769
    assert "Akademischer Chor" in chor.name


def test_parse_nodes_internal_nodes_have_no_unit_id(musi_html):
    """Internal title: nodes (non-leaves) must NOT carry a unit_id."""
    nodes = parse_nodes(musi_html)
    musi_root = next(n for n in nodes if n.segment == "title:17991")
    assert musi_root.unit_id is None


def test_classify_nodes_splits_correctly(musi_html):
    nodes = parse_nodes(musi_html)
    current_path = ["title:17593", "title:17598", "title:17991"]
    current, kids = classify_nodes(nodes, current_path)
    assert current is not None
    assert current.segment == "title:17991"
    assert len(kids) >= 17
    # all immediate kids are at depth+1
    assert all(len(k.path) == len(current_path) + 1 for k in kids)


def test_parse_periods_finds_sose_2026(musi_html):
    periods = parse_periods(musi_html)
    pid_to_name = dict(periods)
    assert pid_to_name.get(589) == "Sommersemester 2026"


def test_parse_root_segment(musi_html):
    assert parse_root_segment(musi_html) == "title:17593"
