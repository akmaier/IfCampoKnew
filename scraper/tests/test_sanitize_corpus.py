"""Tests for the DSGVO sanitiser.

Each rule in :mod:`sanitize_corpus` has a positive (input hit → replaced)
and a preservation (input near-miss → unchanged) case.
"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR))

from sanitize_corpus import (  # noqa: E402
    _drop_dozent_column,
    _drop_last_cell,
    sanitize_bytes,
    sanitize_text,
)

# ── Termine table column drop ─────────────────────────────────────────────

def test_drop_last_cell_basic():
    row = "| a | b | c |"
    assert _drop_last_cell(row) == "| a | b |"

def test_drop_last_cell_alignment_row():
    assert _drop_last_cell("|---|---|---|") == "|---|---|"

def test_drop_dozent_column_full_table():
    md = (
        "| Rhythmus | Tag | Zeit | Datum von–bis | Raum | Dozent/-in |\n"
        "|---|---|---|---|---|---|\n"
        "| wöchentlich | Mo | 10:00–11:00 | 01.04.–01.07. | R1 | Prof. Dr. Foo |\n"
        "| wöchentlich | Di | 12:00–13:00 | 02.04.–02.07. | R2 | Alice |\n"
        "\n"
        "next section\n"
    )
    out = _drop_dozent_column(md)
    assert "Dozent" not in out
    assert "Prof. Dr. Foo" not in out
    assert "Alice" not in out
    # Structural cells preserved
    assert "wöchentlich | Mo | 10:00–11:00 | 01.04.–01.07. | R1 |" in out
    assert "wöchentlich | Di | 12:00–13:00 | 02.04.–02.07. | R2 |" in out
    # Non-table content preserved
    assert "next section" in out

def test_drop_dozent_column_leaves_unrelated_tables_alone():
    md = (
        "| Foo | Bar |\n"
        "|---|---|\n"
        "| 1 | 2 |\n"
    )
    assert _drop_dozent_column(md) == md

# ── Personal-role bullets ─────────────────────────────────────────────────

@pytest.mark.parametrize(
    "line",
    [
        "- **Verantwortlich:** Prof. Dr. Foo Bar",
        "- **Durchführend:** Alice Smith, Bob Jones",
        "- **Modulverantwortlich:** Dr. X Y",
        "- **Ansprechpartner:** Dr. Q",
        "- **Kontakt:** [E-Mail entfernt]",
    ],
)
def test_personal_bullets_stripped(line):
    out = sanitize_text(line + "\n")
    assert "Prof" not in out
    assert "Dr." not in out
    assert "Alice" not in out
    assert "[E-Mail entfernt]" not in out

def test_lehrende_heading_removed_when_block_empties_out():
    md = (
        "## Lehrende\n"
        "\n"
        "- **Verantwortlich:** Prof. Dr. Foo\n"
        "- **Durchführend:** Alice\n"
        "\n"
        "## Termine\n"
    )
    out = sanitize_text(md)
    assert "Lehrende" not in out
    assert "Prof" not in out
    assert "## Termine" in out

def test_ordinary_bullets_are_not_stripped():
    md = "- **Segment:** `title:1000`\n- **Kurztext:** foo\n"
    assert sanitize_text(md) == md

# ── Email + phone redaction ────────────────────────────────────────────────

@pytest.mark.parametrize(
    "given, expect_contained",
    [
        ("Kontakt: [E-Mail entfernt]", "[E-Mail entfernt]"),
        ("via [E-Mail entfernt] please", "[E-Mail entfernt]"),
        ("legacy: [E-Mail entfernt]", "[E-Mail entfernt]"),
    ],
)
def test_emails_stripped(given, expect_contained):
    out = sanitize_text(given)
    assert "@fau.de" not in out
    assert "@physik.uni-erlangen.de" not in out
    assert expect_contained in out

def test_dsgvo_contact_email_preserved():
    # The repo-owner contact address in ``data_protection.md`` must
    # survive the sweep — it is the documented erasure contact.
    md = "E-Mail: <andreas.maier@fau.de>"
    assert sanitize_text(md) == md

def test_other_domain_emails_preserved():
    # We only strip @fau.de and @…uni-erlangen.de. Third-party emails
    # in official public regulations (rare, but possible) stay so the
    # regulation text isn't corrupted.
    md = "Kontakt bei Konsortialpartner: partner@example.com"
    assert sanitize_text(md) == md

@pytest.mark.parametrize(
    "given",
    [
        "Tel.: [Telefon entfernt]",
        "[Telefon entfernt]",
        "Rufnummer [Telefon entfernt]",
        "Kontakt ([Telefon entfernt]",
    ],
)
def test_phones_stripped(given):
    out = sanitize_text(given)
    assert "9131" not in out
    assert "[Telefon entfernt]" in out

def test_short_numbers_preserved():
    # A four-digit room code shouldn't trigger the phone regex.
    md = "Raum 05.012 im Gebäude 11907"
    assert sanitize_text(md) == md

# ── Standalone studiengang name lines ─────────────────────────────────────

def test_standalone_name_line_replaced_in_studiengang():
    md = "Studienberatung\n\nProf. Dr. Robert Freitag\n\nWeitere Infos.\n"
    out = sanitize_text(md, path="data/studiengang/deutsch-franzoesisches-recht-ll-m.md")
    assert "Robert Freitag" not in out
    assert "[Kontaktperson entfernt]" in out
    assert "Weitere Infos" in out

def test_name_in_prose_preserved_in_studiengang():
    # Names inside sentences describe official roles / authorship; leaving
    # them keeps the surrounding text meaningful. The line here is not a
    # standalone name-line so the regex must not fire.
    md = "Prof. Dr. Robert Freitag ist verantwortlich für das Programm.\n"
    out = sanitize_text(md, path="data/studiengang/x.md")
    assert out == md

def test_standalone_name_line_preserved_outside_studiengang():
    # PO files and other roots keep name-lines intact.
    md = "Prof. Dr. Robert Freitag\n"
    out = sanitize_text(md, path="data/pruefungsordnungen/rw/foo.md")
    assert out == md

# ── Whole-file idempotence ────────────────────────────────────────────────

def test_sanitize_is_idempotent():
    md = (
        "## Lehrende\n\n"
        "- **Verantwortlich:** Prof. Dr. Foo\n\n"
        "## Termine\n\n"
        "| Rhythmus | Tag | Zeit | Datum von–bis | Raum | Dozent/-in |\n"
        "|---|---|---|---|---|---|\n"
        "| wöchentlich | Mo | 10:00–11:00 | 01.04.–01.07. | R1 | Alice |\n"
        "\n"
        "Kontakt: [E-Mail entfernt] · Tel.: [Telefon entfernt]\n"
    )
    once = sanitize_text(md)
    twice = sanitize_text(once)
    assert once == twice

def test_sanitize_bytes_utf8_strips_personal_data():
    text = "- **Verantwortlich:** Prof. Dr. Foo\n"
    out = sanitize_bytes(text.encode("utf-8"), path="data/x.md")
    # Personal data gone, and the blob shrank (idempotence of an empty
    # trailing newline isn't asserted — the callback only needs to
    # guarantee removal of the sensitive substring).
    assert b"Prof" not in out
    assert b"Verantwortlich" not in out
    assert len(out) < len(text)

def test_sanitize_bytes_binary_passthrough():
    # Non-UTF-8 blob (e.g. a stray binary attachment) passes through
    # unchanged so we never corrupt non-markdown.
    binary = bytes(range(200, 220))
    assert sanitize_bytes(binary, path="data/x.md") == binary

def test_sanitize_bytes_non_md_passthrough():
    # Non-.md path is left alone even if utf-8-decodable and matching.
    text = "- **Verantwortlich:** Prof. Dr. Foo\n"
    assert (
        sanitize_bytes(text.encode("utf-8"), path="data/x.txt")
        == text.encode("utf-8")
    )
