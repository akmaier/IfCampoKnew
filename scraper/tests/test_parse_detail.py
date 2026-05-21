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
    assert "Person C" in a.instructors

def test_parse_mustererkennung_basic_data(mustererkennung_html):
    c = parse_course_detail(mustererkennung_html, unit_id=86267, period_id=589)
    assert c.title == "Praktikum Mustererkennung"
    assert c.course_type == "Praktikum"
    assert c.ects == 5.0
    assert c.language == "Deutsch oder Englisch"
    assert "Person B" in (c.instructors_resp[0] if c.instructors_resp else "")

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
    # Should be exactly one — Person C
    assert len(insts) == 1
    assert "Person C" in insts[0]

def test_instructors_from_synthetic_two_li_cell():
    """Two instructors in two <li> tags must come out as two distinct
    entries — never one concatenated string."""
    from parse_detail import _instructors_from_cell  # noqa: WPS433
    cell_html = (
        '<ul><li><button title="Profil von Fixture Person Alpha anzeigen">x</button></li>'
        '<li><button title="Profil von PD Dr. habil. Fixture Beta anzeigen">x</button></li>'
        '<li><button title="Profil von Dr.-Ing. Fixture Gamma anzeigen">x</button></li>'
        '<li><button title="Profil von Fixture Delta anzeigen">x</button></li></ul>'
    )
    out = _instructors_from_cell(cell_html)
    assert out == [
        "Fixture Person Alpha",
        "PD Dr. habil. Fixture Beta",
        "Dr.-Ing. Fixture Gamma",
        "Fixture Delta",
    ]

def test_instructors_fallback_when_no_li():
    """Cells without <li> should fall back to the previous splitter
    (rare, but a single-instructor row sometimes lacks the list wrap)."""
    from parse_detail import _instructors_from_cell  # noqa: WPS433
    out = _instructors_from_cell("<span>Person C</span>")
    assert out == ["Person C"]

def test_basic_data_instructors_handle_multi_li():
    """Regression: the user reported "Fixture Person Alpha PD Dr. habil. Tobias
    Fey Dr.-Ing. Fixture Gamma Fixture Delta" glued into one string. The
    course's "Verantwortliche/-r" block holds a <ul><li>...</li></ul> that
    the old `_parse_instructors` flattened to text. The new code must walk
    the <li> structurally."""
    from parse_detail import _parse_instructors  # noqa: WPS433
    html = """
    <fieldset>
      <label for="x">Verantwortliche/-r</label>
      <ul class="listStyleIconSimple">
        <li><span title="Profil von apl. Prof. Dr. Fixture Person Alpha anzeigen">x</span></li>
        <li><span title="Profil von PD Dr. habil. Fixture Beta anzeigen">x</span></li>
        <li><span title="Profil von Dr.-Ing. Fixture Gamma anzeigen">x</span></li>
        <li><span title="Profil von Fixture Delta anzeigen">x</span></li>
      </ul>
      <label for="y">Nächstes Feld</label>
    </fieldset>
    """
    out = _parse_instructors(html, "Verantwortliche/-r")
    assert out == [
        "apl. Prof. Dr. Fixture Person Alpha",
        "PD Dr. habil. Fixture Beta",
        "Dr.-Ing. Fixture Gamma",
        "Fixture Delta",
    ]

# ── Regression: Organisationseinheit list → assigned_programs ──────────────

@pytest.fixture(scope="module")
def llm_seminar_html() -> str:
    return (FIXTURES / "detail_136825_seminar_llm_medicine.html").read_text(
        encoding="utf-8"
    )

def test_llm_seminar_assigned_programs_complete(llm_seminar_html):
    """Saved 2026-05-21 — `Seminar Large Language Models in Medicine` is
    cross-listed under 5 Studiengängen. Four are in the visible <ul>; the
    fifth (Computerlinguistik, BA 2 Fächer) only appears in the "Mehr…"
    popup. The parser must surface all five.
    """
    c = parse_course_detail(llm_seminar_html, unit_id=136825, period_id=589)
    assert c.title == "Seminar Large Language Models in Medicine"
    assert c.org_unit == "Lehrstuhl für Informatik 5 (Mustererkennung) (Verantwortlicher)"
    programs = [(p["faculty"], p["program"], p["degree"]) for p in c.assigned_programs]
    assert ("TechFak", "Medizintechnik", "Master of Science") in programs
    assert ("TechFak", "Artificial Intelligence", "Master of Science") in programs
    assert ("NatFak", "Data Science", "Master of Science") in programs
    assert ("PhilFak", "English Studies", "Master of Arts") in programs
    # Computerlinguistik lives in the popup only — guards against any
    # future regression where the parser only scrapes the visible <ul>.
    assert (
        "PhilFak",
        "Computerlinguistik",
        "Bachelor of Arts (2 Fächer)",
    ) in programs
    assert len(programs) == 5

def test_org_row_classifier_program_vs_lehrstuhl():
    """The classifier separates pipe-shaped program rows from free-form
    Lehrstuhl/Institut rows, even when the Lehrstuhl name contains
    parentheses (which look like a role suffix to a naive parser).
    """
    from parse_detail import _parse_org_row  # noqa: WPS433

    # Program row
    r = _parse_org_row(
        "TechFak | Medizintechnik | Master of Science (Verantwortlicher)"
    )
    assert r["kind"] == "program"
    assert r["faculty"] == "TechFak"
    assert r["program"] == "Medizintechnik"
    assert r["degree"] == "Master of Science"
    assert r["role"] == "Verantwortlicher"

    # ReWiFak — the faculty token list is a `\w+Fak` regex, not a fixed
    # allowlist. This test pins that change in place.
    r = _parse_org_row("ReWiFak | Economics | Master of Science (Verantwortlicher)")
    assert r["kind"] == "program"
    assert r["faculty"] == "ReWiFak"

    # Lehrstuhl with parens in the name + role suffix in parens at the end
    r = _parse_org_row(
        "Lehrstuhl für Informatik 5 (Mustererkennung) (Verantwortlicher)"
    )
    assert r["kind"] == "org"
    # Role suffix is stripped from `name`, but the parenthetical
    # disambiguator inside the Lehrstuhl name is preserved.
    assert r["name"] == "Lehrstuhl für Informatik 5 (Mustererkennung)"
    assert r["role"] == "Verantwortlicher"

# ── Regression: Termine-table column detection ─────────────────────────────

def test_termine_column_detection_room_is_real_room_not_capacity():
    """Saved fixture from 2026-05-15 Deep Learning detail page.

    Campo's appointments table has up to 10 columns:
    ``Änderungen | Rhythmus | Wochentag | Von-Bis | Ausfalltermin |
    Startdatum-Enddatum | Erw. Tn. | Bemerkung | Durchführende | Raum``

    The "Erw. Tn." (expected attendees) column at index 6 used to be
    read as the room. That returned ``350`` (the capacity) for Deep
    Learning instead of the actual room
    ``11907.01.040 (H18) 11906.01.030 (H21)``. Header-based detection
    makes the parser robust to column reordering.
    """
    from parse_detail import _parse_appointments  # noqa: WPS433

    fixture = (FIXTURES / "termine_deep_learning_2026.html").read_text(
        encoding="utf-8"
    )
    appts = _parse_appointments(fixture)
    assert len(appts) == 1
    a = appts[0]
    # Room contains the real Raum identifier(s), NOT the capacity 350.
    assert "H18" in (a.room or "")
    assert "11907.01.040" in (a.room or "")
    assert a.room and "350" not in a.room
    # Sanity-check the other columns came through correctly too.
    assert a.weekday == "Fr"
    assert a.time_from == "12:15"
    assert a.time_to == "13:45"
    assert a.rhythm == "wöchentlich"
    # The instructors column moved too (now col 8, not col 7).
    assert any("Person D" in n for n in a.instructors)
