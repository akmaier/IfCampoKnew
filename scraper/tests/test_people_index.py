"""Tests for ``people_index``'s helper functions."""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR))

from people_index import split_concatenated_names, split_title  # noqa: E402


# ── split_title ──────────────────────────────────────────────────────────


@pytest.mark.parametrize(
    "full, expected_title, expected_name",
    [
        ("Andreas Maier", "", "Andreas Maier"),
        ("Prof. Dr.-Ing. Andreas Maier", "Prof. Dr.-Ing.", "Andreas Maier"),
        ("PD Dr. habil. Tobias Fey", "PD Dr. habil.", "Tobias Fey"),
        ("Dr. Stefan Weber", "Dr.", "Stefan Weber"),
        ("apl. Prof. Dr. Christian Lange", "apl. Prof. Dr.", "Christian Lange"),
    ],
)
def test_split_title_strips_known_prefixes(full, expected_title, expected_name):
    title, name = split_title(full)
    assert title == expected_title
    assert name == expected_name


# ── split_concatenated_names — the fix for the user-reported bug ─────────


def test_split_user_reported_concat():
    """Reproducer for the bug the user reported in lehrende-ohne-pflicht.md.

    Three of the four people are recoverable — Michael Redel has no title
    before it so it stays glued to the previous Dr.-Ing. block. That's a
    known, documented limitation; the proper fix is the upstream parser
    in parse_detail (which now extracts each <li> separately)."""
    out = split_concatenated_names(
        "Heinz Werner Höppel PD Dr. habil. Tobias Fey Dr.-Ing. Joachim Kaschta Michael Redel"
    )
    assert out == [
        "Heinz Werner Höppel",
        "PD Dr. habil. Tobias Fey",
        "Dr.-Ing. Joachim Kaschta Michael Redel",
    ]


def test_split_keeps_compound_titles_together():
    """`Prof. Dr. h.c.` is one title sequence — no split inside."""
    out = split_concatenated_names("Prof. Dr. h.c. Anna Müller PD Dr. Bertram Schmidt")
    assert out == ["Prof. Dr. h.c. Anna Müller", "PD Dr. Bertram Schmidt"]


def test_split_passes_through_single_name():
    assert split_concatenated_names("Andreas Maier") == ["Andreas Maier"]
    assert split_concatenated_names("Prof. Dr.-Ing. Andreas Maier") == [
        "Prof. Dr.-Ing. Andreas Maier"
    ]


def test_split_handles_empty_and_whitespace():
    assert split_concatenated_names("") == []
    assert split_concatenated_names("   ") == []


def test_split_does_not_break_dr_ing_inside_one_name():
    out = split_concatenated_names("Prof. Dr.-Ing. Vincent Christlein")
    assert out == ["Prof. Dr.-Ing. Vincent Christlein"]
