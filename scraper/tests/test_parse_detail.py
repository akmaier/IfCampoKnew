"""Tests for ``parse_detail``.

Two real course-detail fixtures (saved 2026-04-25):

* ``detail_92769_chor.html`` — Akademischer Chor (Übung, weekly schedule).
* ``detail_86267_praktikum_mustererkennung.html`` — Block Praktikum (no
  fixed weekly slot).
"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR))

from parse_detail import parse_course_detail  # noqa: E402

FIXTURES = Path(__file__).parent / "fixtures"


@pytest.fixture(scope="module")
def chor_html() -> str:
    return (FIXTURES / "detail_92769_chor.html").read_text(encoding="utf-8")


@pytest.fixture(scope="module")
def mustererkennung_html() -> str:
    return (FIXTURES / "detail_86267_praktikum_mustererkennung.html").read_text(
        encoding="utf-8"
    )


def test_parse_chor_basic_data(chor_html):
    c = parse_course_detail(chor_html, unit_id=92769, period_id=589)
    assert c.title == "Akademischer Chor"
    assert c.course_type == "Übung"
    assert c.ects == 3.0
    assert c.language == "Deutsch"
    assert c.turnus == "in jedem Semester"
    assert c.permalink.startswith("https://www.campo.fau.de")
    assert "unitId=92769" in c.permalink


def test_parse_chor_appointments(chor_html):
    c = parse_course_detail(chor_html, unit_id=92769, period_id=589)
    assert len(c.appointments) == 1
    a = c.appointments[0]
    assert a.rhythm == "wöchentlich"
    assert a.weekday == "Mi"
    assert a.time_from == "19:30"
    assert a.time_to == "22:00"
    assert a.date_from == "15.04.2026"
    assert a.date_to == "15.07.2026"
    assert "Jan Dolezel" in a.instructors


def test_parse_mustererkennung_basic_data(mustererkennung_html):
    c = parse_course_detail(mustererkennung_html, unit_id=86267, period_id=589)
    assert c.title == "Praktikum Mustererkennung"
    assert c.course_type == "Praktikum"
    assert c.ects == 5.0
    assert c.language == "Deutsch oder Englisch"
    assert "Vincent Christlein" in (c.instructors_resp[0] if c.instructors_resp else "")


def test_parse_mustererkennung_no_fixed_appointments(mustererkennung_html):
    """A Block-Praktikum has no Termine rows."""
    c = parse_course_detail(mustererkennung_html, unit_id=86267, period_id=589)
    assert c.appointments == []


def test_fallback_title_used_when_permalink_omits_it():
    # Empty HTML — no permalink popup; the fallback should win.
    c = parse_course_detail(
        "<html></html>", unit_id=42, period_id=589, fallback_title="Dummy"
    )
    assert c.title == "Dummy"
    assert c.unit_id == 42


def test_chor_appointment_has_one_instructor(chor_html):
    """Regression for the multi-instructor concat bug: <li> structure must be
    preserved even when the instructor cell wraps text in nested elements."""
    c = parse_course_detail(chor_html, unit_id=92769, period_id=589)
    assert len(c.appointments) == 1
    insts = c.appointments[0].instructors
    # Should be exactly one — Jan Dolezel
    assert len(insts) == 1
    assert "Jan Dolezel" in insts[0]


def test_instructors_from_synthetic_two_li_cell():
    """Two instructors in two <li> tags must come out as two distinct
    entries — never one concatenated string."""
    from parse_detail import _instructors_from_cell  # noqa: WPS433
    cell_html = (
        '<ul><li><button title="Profil von Heinz Werner Höppel anzeigen">x</button></li>'
        '<li><button title="Profil von PD Dr. habil. Tobias Fey anzeigen">x</button></li>'
        '<li><button title="Profil von Dr.-Ing. Joachim Kaschta anzeigen">x</button></li>'
        '<li><button title="Profil von Michael Redel anzeigen">x</button></li></ul>'
    )
    out = _instructors_from_cell(cell_html)
    assert out == [
        "Heinz Werner Höppel",
        "PD Dr. habil. Tobias Fey",
        "Dr.-Ing. Joachim Kaschta",
        "Michael Redel",
    ]


def test_instructors_fallback_when_no_li():
    """Cells without <li> should fall back to the previous splitter
    (rare, but a single-instructor row sometimes lacks the list wrap)."""
    from parse_detail import _instructors_from_cell  # noqa: WPS433
    out = _instructors_from_cell("<span>Jan Dolezel</span>")
    assert out == ["Jan Dolezel"]


def test_basic_data_instructors_handle_multi_li():
    """Regression: the user reported "Heinz Werner Höppel PD Dr. habil. Tobias
    Fey Dr.-Ing. Joachim Kaschta Michael Redel" glued into one string. The
    course's "Verantwortliche/-r" block holds a <ul><li>...</li></ul> that
    the old `_parse_instructors` flattened to text. The new code must walk
    the <li> structurally."""
    from parse_detail import _parse_instructors  # noqa: WPS433
    html = """
    <fieldset>
      <label for="x">Verantwortliche/-r</label>
      <ul class="listStyleIconSimple">
        <li><span title="Profil von apl. Prof. Dr. Heinz Werner Höppel anzeigen">x</span></li>
        <li><span title="Profil von PD Dr. habil. Tobias Fey anzeigen">x</span></li>
        <li><span title="Profil von Dr.-Ing. Joachim Kaschta anzeigen">x</span></li>
        <li><span title="Profil von Michael Redel anzeigen">x</span></li>
      </ul>
      <label for="y">Nächstes Feld</label>
    </fieldset>
    """
    out = _parse_instructors(html, "Verantwortliche/-r")
    assert out == [
        "apl. Prof. Dr. Heinz Werner Höppel",
        "PD Dr. habil. Tobias Fey",
        "Dr.-Ing. Joachim Kaschta",
        "Michael Redel",
    ]
