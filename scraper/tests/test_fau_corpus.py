"""Tests for ``fau_corpus`` — the FAU.de scraper.

We exercise the pure helpers (slugify, _clean_md, relpath_for_po) plus
the two HTML→dict parsers (parse_studiengang, parse_po_landing) against
real FAU.de pages captured into ``scraper/tests/fixtures/``. These tests
are completely offline.
"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR))

from fau_corpus import (  # noqa: E402
    _clean_md,
    parse_po_landing,
    parse_studiengang,
    relpath_for_po,
    slugify,
)

FIXTURES = Path(__file__).parent / "fixtures"


# ── slugify ───────────────────────────────────────────────────────────────


@pytest.mark.parametrize(
    "name, expected",
    [
        ("Informatik", "informatik"),
        ("Künstliche Intelligenz", "kuenstliche-intelligenz"),
        ("Maße & Größen", "masse-groessen"),  # `&` collapses to a single hyphen
        ("Studiengang (B.Sc.)", "studiengang-b-sc"),
        ("", "unnamed"),
        ("---", "unnamed"),
    ],
)
def test_slugify_basic(name, expected):
    assert slugify(name) == expected


def test_slugify_strips_html_tags():
    assert slugify("<a href='x'>Hello & World</a>") == "hello-world"


def test_slugify_truncates():
    assert len(slugify("x" * 500, max_len=80)) <= 80


# ── _clean_md ────────────────────────────────────────────────────────────


def test_clean_md_collapses_blank_runs():
    out = _clean_md("a\n\n\n\nb")
    assert out == "a\n\nb\n"


def test_clean_md_strips_trailing_whitespace_lines():
    out = _clean_md("a\n   \nb")
    assert out == "a\n\nb\n"


def test_clean_md_always_ends_in_newline():
    assert _clean_md("foo").endswith("\n")
    assert _clean_md("foo\n").endswith("\n")


# ── relpath_for_po ───────────────────────────────────────────────────────


@pytest.mark.parametrize(
    "url, expected",
    [
        (
            "https://www.fau.de/universitaet/universitaetsorganisation/rechtliche-grundlagen/pruefungsordnungen/",
            ".",
        ),
        (
            "https://www.fau.de/universitaet/universitaetsorganisation/rechtliche-grundlagen/pruefungsordnungen/sprachpruefungen/",
            "sprachpruefungen",
        ),
        (
            "https://www.fau.de/universitaet/universitaetsorganisation/rechtliche-grundlagen/pruefungsordnungen/technische-fakultaet/informatik/",
            "technische-fakultaet/informatik",
        ),
        (
            "https://www.fau.de/universitaet/universitaetsorganisation/rechtliche-grundlagen/pruefungsordnungen/lehramt/lehramtsfaecher",
            "lehramt/lehramtsfaecher",
        ),
    ],
)
def test_relpath_for_po(url, expected):
    assert str(relpath_for_po(url)) == expected


# ── parse_studiengang against a real fixture ─────────────────────────────


@pytest.fixture(scope="module")
def ai_bsc_page() -> tuple[str, str]:
    url = "https://www.fau.de/studiengang/artificial-intelligence-b-sc/"
    html = (FIXTURES / "fau_studiengang_ai-bsc.html").read_text(encoding="utf-8")
    return url, html


def test_parse_studiengang_extracts_title(ai_bsc_page):
    url, html = ai_bsc_page
    data = parse_studiengang(url, html)
    assert "Artificial Intelligence" in data["title"]
    assert "B.Sc." in data["title"]
    assert data["url"] == url


def test_parse_studiengang_steckbrief_keys(ai_bsc_page):
    url, html = ai_bsc_page
    data = parse_studiengang(url, html)
    keys = {k for k, _ in data["steckbrief"]}
    # The Steckbrief always carries Abschluss + Fakultät + Unterrichtssprache.
    assert "Abschluss" in keys
    assert "Fakultät" in keys
    assert "Unterrichtssprache" in keys


def test_parse_studiengang_has_sections(ai_bsc_page):
    url, html = ai_bsc_page
    data = parse_studiengang(url, html)
    section_labels = {label for label, _ in data["sections"]}
    # Site chrome should be filtered out.
    assert "Website-Menü" not in section_labels
    assert "Steckbrief" not in section_labels  # Steckbrief is in its own field
    # At least one substantive section should survive.
    assert any(len(body) > 200 for _, body in data["sections"])


def test_parse_studiengang_external_links_dedupe_and_filter(ai_bsc_page):
    url, html = ai_bsc_page
    data = parse_studiengang(url, html)
    hrefs = [h for _, h in data["links"]]
    # No duplicates
    assert len(hrefs) == len(set(hrefs))
    # No FAU site-chrome links (impressum, datenschutz, etc.)
    chrome = [h for h in hrefs if "/impressum/" in h or "/datenschutz/" in h]
    assert chrome == []
    # No social-network links
    social = [h for h in hrefs if "facebook.com" in h or "twitter.com" in h]
    assert social == []


# ── parse_po_landing ─────────────────────────────────────────────────────


@pytest.fixture(scope="module")
def sprachpruefungen_page() -> tuple[str, str]:
    url = "https://www.fau.de/universitaet/universitaetsorganisation/rechtliche-grundlagen/pruefungsordnungen/sprachpruefungen/"
    html = (FIXTURES / "fau_po_sprachpruefungen.html").read_text(encoding="utf-8")
    return url, html


def test_parse_po_landing_title(sprachpruefungen_page):
    url, html = sprachpruefungen_page
    data = parse_po_landing(url, html)
    assert data["url"] == url
    assert data["title"]  # non-empty


def test_parse_po_landing_finds_pdfs(sprachpruefungen_page):
    url, html = sprachpruefungen_page
    data = parse_po_landing(url, html)
    pdfs = data["pdfs"]
    assert len(pdfs) >= 1, "expected at least one PDF link on the Sprachprüfungen landing"
    for pdf in pdfs:
        assert pdf["url"].lower().endswith(".pdf")
        assert pdf["url"].startswith("http")
        assert pdf["title"]  # human-readable label


def test_parse_po_landing_intro_present(sprachpruefungen_page):
    url, html = sprachpruefungen_page
    data = parse_po_landing(url, html)
    # Some intro markdown should make it through markdownify.
    assert len(data["intro_md"]) > 100
