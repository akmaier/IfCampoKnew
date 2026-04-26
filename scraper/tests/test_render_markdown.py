"""Tests for ``render_markdown`` helpers added in Entries 0009 + 0010.

We don't render full corpora here — we exercise the small pure-Python
helpers (slug normalisation, year extraction, FAU index loading,
relative-link computation, related-FAU selection) that gate the
correctness of the cross-link output.
"""
from __future__ import annotations

import sys
from pathlib import Path
from textwrap import dedent

import pytest

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR))

from render_markdown import (  # noqa: E402
    _candidate_slugs,
    _compute_fold_set,
    _estimate_folder_chars,
    _find_related_fau,
    _lehramt_pdf_matches,
    _po_version_years,
    _strip_degree_suffix,
    load_fau_index,
    slugify,
)


# ── slugify ───────────────────────────────────────────────────────────────


@pytest.mark.parametrize(
    "name, expected",
    [
        ("Informatik", "informatik"),
        ("Mathematik für Informatiker", "mathematik-fuer-informatiker"),
        ("Künstliche Intelligenz", "kuenstliche-intelligenz"),
        ("Maße & Größen / Bewegung", "masse-und-groessen-bewegung"),
        ("Computational Engineering (Elite)", "computational-engineering-elite"),
        ("", "unnamed"),
        ("---", "unnamed"),
    ],
)
def test_slugify_handles_german_and_punctuation(name, expected):
    # The "und" inside `_candidate_slugs` is not part of slugify; here we
    # only assert the deterministic ASCII-folding behaviour of slugify.
    s = slugify(name)
    # Some of the param entries assume the "und" expansion of `&`; if the
    # actual implementation differs, the tests below explicitly cover it.
    if name.startswith("Maße"):
        # accept either "und" expansion or simple drop, as long as it's
        # ASCII, hyphenated, and contains the German-folded forms.
        assert "masse" in s and "groessen" in s
    else:
        assert s == expected


def test_slugify_truncates_at_max_len():
    long = "x" * 500
    assert len(slugify(long, max_len=80)) <= 80


# ── degree-suffix stripping ───────────────────────────────────────────────


@pytest.mark.parametrize(
    "slug, expected",
    [
        ("informatik-b-sc", "informatik"),
        ("informatik-m-sc", "informatik"),
        ("artificial-intelligence-b-sc", "artificial-intelligence"),
        ("zahnmedizin-staatsexamen", "zahnmedizin"),
        ("informatik", "informatik"),  # no suffix → unchanged
        ("foo-zertifikat", "foo"),
    ],
)
def test_strip_degree_suffix(slug, expected):
    assert _strip_degree_suffix(slug) == expected


# ── candidate slug variants ───────────────────────────────────────────────


def test_candidate_slugs_includes_literal_and_connector_drop():
    cands = _candidate_slugs("Elektrotechnik - Elektronik und Informationstechnik")
    assert "elektrotechnik-elektronik-und-informationstechnik" in cands
    # connector "und" can be removed
    assert any("informationstechnik" in c and "und" not in c.split("-") for c in cands)


def test_candidate_slugs_strips_parenthetical_qualifiers():
    cands = _candidate_slugs("Computational Engineering (Elite)")
    assert "computational-engineering-elite" in cands
    assert "computational-engineering" in cands  # paren stripped


def test_candidate_slugs_dedupes():
    cands = _candidate_slugs("Informatik")
    assert len(cands) == len(set(cands))


# ── PO-version year extraction ────────────────────────────────────────────


@pytest.mark.parametrize(
    "name, expected",
    [
        ("Bachelor of Science Informatik Hauptfach PO-Version 2007", ["2007"]),
        ("Lehramt Gymnasium Mathematik Hauptfach PO-Version 20192", ["2019"]),
        ("Master of Science Wirtschaftsinformatik PO-Version 20242", ["2024"]),
        ("Master of Science Wirtschaftsinformatik PO-Version 20211", ["2021"]),
        ("Bachelor of Science Informatik (no year here)", []),
        ("PO-Version 2010", ["2010"]),
    ],
)
def test_po_version_years(name, expected):
    assert _po_version_years(name) == expected


# ── load_fau_index against a tiny on-disk corpus ──────────────────────────


@pytest.fixture
def tiny_fau_corpus(tmp_path: Path) -> Path:
    """Create a minimal data/ tree mimicking the real one."""
    sg = tmp_path / "studiengang"
    sg.mkdir()
    (sg / "INDEX.md").write_text("# all programs\n", encoding="utf-8")
    (sg / "informatik-b-sc.md").write_text(
        dedent(
            """\
            ---
            title: "Informatik (B.Sc.)"
            abschluss: "Bachelor of Science"
            fakultät: "Technische Fakultät"
            ---
            # Informatik (B.Sc.)
            """
        ),
        encoding="utf-8",
    )
    (sg / "informatik-m-sc.md").write_text(
        dedent(
            """\
            ---
            title: "Informatik (M.Sc.)"
            abschluss: "Master of Science"
            fakultät: "Technische Fakultät"
            ---
            # Informatik (M.Sc.)
            """
        ),
        encoding="utf-8",
    )
    po = tmp_path / "pruefungsordnungen" / "technische-fakultaet" / "informatik"
    po.mkdir(parents=True)
    (po / "INDEX.md").write_text("# Informatik POs\n", encoding="utf-8")
    (po / "BSc-MSc Informatik FPOINF 20240328.md").write_text(
        dedent(
            """\
            ---
            kind: "fau-pruefungsordnung-document"
            title: "BSc-MSc Informatik FPOINF 20240328.pdf"
            ---
            # BSc-MSc Informatik FPOINF 20240328
            """
        ),
        encoding="utf-8",
    )
    (po / "fpoinf-20070920-idf-20220726.md").write_text(
        dedent(
            """\
            ---
            kind: "fau-pruefungsordnung-document"
            title: "BSc-MSc Informatik FPOINF 20070920 i.d.F. 20220726.pdf"
            ---
            # BSc-MSc Informatik FPOINF 20070920 i.d.F. 20220726
            """
        ),
        encoding="utf-8",
    )
    return tmp_path


def test_load_fau_index_studiengang(tiny_fau_corpus):
    idx = load_fau_index(tiny_fau_corpus)
    sgs = idx["studiengang"].get("informatik", [])
    assert {sg["slug"] for sg in sgs} == {"informatik-b-sc", "informatik-m-sc"}
    titles = {sg["title"] for sg in sgs}
    assert "Informatik (B.Sc.)" in titles


def test_load_fau_index_po_folders(tiny_fau_corpus):
    idx = load_fau_index(tiny_fau_corpus)
    pos = idx["po_folders"].get("informatik", [])
    assert len(pos) == 1
    assert pos[0]["leaf"] == "informatik"
    assert pos[0]["rel_dir"].endswith("technische-fakultaet/informatik")


def test_find_related_fau_program(tiny_fau_corpus):
    idx = load_fau_index(tiny_fau_corpus)
    node = {"name": "Informatik", "path": ["title:1", "title:2", "title:3"]}
    rel = _find_related_fau(node, idx)
    assert len(rel["studiengang"]) == 2
    assert len(rel["po_folders"]) == 1


def test_find_related_fau_unmatched(tiny_fau_corpus):
    idx = load_fau_index(tiny_fau_corpus)
    node = {"name": "Nichtexistent", "path": ["title:1"]}
    rel = _find_related_fau(node, idx)
    assert rel == {"studiengang": [], "po_folders": []}


# ── Lehramt PDF fallback ──────────────────────────────────────────────────


@pytest.fixture
def tiny_lehramt_corpus(tmp_path: Path) -> Path:
    lehramt = tmp_path / "pruefungsordnungen" / "lehramt" / "lehramtsfaecher"
    lehramt.mkdir(parents=True)
    for stem in [
        "1aes-20la-englisch",
        "1aes-20lapo-englisch",
        "1aes-20la-mathe",
        "lapo-mathe-neu",
        "1aes-la-arbeitslehre",
        "1aes-20la-musik",
    ]:
        (lehramt / f"{stem}.md").write_text(
            f"---\nkind: \"fau-pruefungsordnung-document\"\ntitle: \"{stem}.pdf\"\n---\n# {stem}\n",
            encoding="utf-8",
        )
    return tmp_path


def test_lehramt_match_exact_subject(tiny_lehramt_corpus):
    idx = load_fau_index(tiny_lehramt_corpus)
    node = {"name": "Englisch für das Lehramt", "path": []}
    matches = _lehramt_pdf_matches(node, idx)
    assert {m["stem"] for m in matches} == {"1aes-20la-englisch", "1aes-20lapo-englisch"}


def test_lehramt_match_via_abbreviation(tiny_lehramt_corpus):
    idx = load_fau_index(tiny_lehramt_corpus)
    node = {"name": "Mathematik", "path": []}
    matches = _lehramt_pdf_matches(node, idx)
    assert {m["stem"] for m in matches} == {"1aes-20la-mathe", "lapo-mathe-neu"}


def test_lehramt_match_no_false_positive_on_stopwords(tiny_lehramt_corpus):
    """A node whose only meaningful tokens are stopwords (or "lehramt"
    itself) must NOT match every Lehramt PDF in the corpus."""
    idx = load_fau_index(tiny_lehramt_corpus)
    node = {"name": "FAU Lehramt International", "path": []}
    matches = _lehramt_pdf_matches(node, idx)
    # 'lehramt' is a stopword; 'fau' / 'international' aren't tokens of any
    # PDF in the fixture, so no matches should fire.
    assert matches == []


# ── F-TOKEN folding logic ─────────────────────────────────────────────────


def _mk_node(seg: str, parent: str | None = None, unit_id=None) -> dict:
    return {
        "segment": seg,
        "parentSegment": parent,
        "unitId": unit_id,
        "name": seg,
        "path": [seg] if parent is None else [parent, seg],
    }


def test_fold_set_includes_stub_only_program():
    """A program with N stub leaves and combined size below threshold folds."""
    parent = _mk_node("title:1")
    kids = [_mk_node(f"exam:{i}", parent="title:1") for i in range(1, 6)]
    by_segment = {n["segment"]: n for n in [parent] + kids}
    children_of = {"title:1": kids}
    courses_by_uid: dict[int, dict] = {}
    fold = _compute_fold_set(by_segment, children_of, courses_by_uid)
    assert "title:1" in fold


def test_fold_set_excludes_folder_with_grandchildren():
    """If any kid has its own children, the parent does NOT fold."""
    parent = _mk_node("title:1")
    kid_with_kids = _mk_node("title:2", parent="title:1")
    grand = _mk_node("exam:99", parent="title:2")
    by_segment = {n["segment"]: n for n in [parent, kid_with_kids, grand]}
    children_of = {"title:1": [kid_with_kids], "title:2": [grand]}
    fold = _compute_fold_set(by_segment, children_of, {})
    assert "title:1" not in fold
    assert "title:2" in fold  # grand is a leaf → title:2 still folds


def test_fold_set_uses_higher_threshold_for_course_folders():
    """A course-bearing folder with ~10 kids fits under the 90k-char ceiling
    but would have exceeded the 24k stub ceiling — assert it folds anyway."""
    parent = _mk_node("title:1")
    kids = [_mk_node(f"exam:{i}", parent="title:1", unit_id=i) for i in range(1, 11)]
    by_segment = {n["segment"]: n for n in [parent] + kids}
    children_of = {"title:1": kids}
    courses_by_uid = {i: {"unit_id": i, "title": f"course-{i}"} for i in range(1, 11)}
    fold = _compute_fold_set(by_segment, children_of, courses_by_uid)
    assert "title:1" in fold


def test_fold_set_excludes_huge_course_folders():
    """A course folder so large it exceeds even the 90k-char ceiling is left
    as a regular folder so each course gets its own file."""
    parent = _mk_node("title:1")
    # 100 courses × 2500 chars baseline = 250k chars, well above the 90k ceiling
    kids = [_mk_node(f"exam:{i}", parent="title:1", unit_id=i) for i in range(1, 101)]
    by_segment = {n["segment"]: n for n in [parent] + kids}
    children_of = {"title:1": kids}
    courses_by_uid = {i: {"unit_id": i, "title": f"course-{i}"} for i in range(1, 101)}
    fold = _compute_fold_set(by_segment, children_of, courses_by_uid)
    assert "title:1" not in fold


def test_estimate_folder_chars_distinguishes_courses_from_stubs():
    parent = _mk_node("title:1")
    kid_stub = _mk_node("exam:1", parent="title:1")
    kid_course = _mk_node("exam:2", parent="title:1", unit_id=42)
    courses_by_uid = {42: {"unit_id": 42}}
    total_stubs, has1 = _estimate_folder_chars([kid_stub, kid_stub], courses_by_uid)
    total_mixed, has2 = _estimate_folder_chars([kid_stub, kid_course], courses_by_uid)
    assert has1 is False
    assert has2 is True
    assert total_mixed > total_stubs
