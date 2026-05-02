"""Unit tests for ``scrape_tagesaktuelle.fetch_one_day`` HTML parsing."""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR))

from scrape_tagesaktuelle import (  # noqa: E402
    DETAIL_LINK_RE,
    ROW_TITLE_RE,
)


def test_detail_link_re_matches_html_encoded_amp():
    html = (
        '<a href="/qisserver/pages/startFlow.xhtml?_flowId=detailView-flow'
        "&amp;unitId=86267&amp;periodId=589&amp;navigationPosition=foo\">x</a>"
    )
    m = DETAIL_LINK_RE.search(html)
    assert m is not None
    assert m.group("uid") == "86267"
    assert m.group("pid") == "589"


def test_detail_link_re_matches_plain_amp():
    html = (
        "/qisserver/pages/startFlow.xhtml?_flowId=detailView-flow"
        "&unitId=92769&periodId=589"
    )
    m = DETAIL_LINK_RE.search(html)
    assert m is not None
    assert m.group("uid") == "92769"


def test_row_title_extracts_clean_name():
    html = (
        '<a title="Details für Veranstaltung Praktikum Mustererkennung anzeigen" '
        'href="...">x</a>'
    )
    m = ROW_TITLE_RE.search(html)
    assert m is not None
    assert m.group("title") == "Praktikum Mustererkennung"


def test_pairs_title_with_link_in_order():
    """fetch_one_day pairs title attributes with the *next* detail link."""
    from scrape_tagesaktuelle import fetch_one_day

    fragment = """
    <html><body>
      <a title="Details für Veranstaltung Vorlesung X anzeigen"
         href="/qisserver/pages/startFlow.xhtml?_flowId=detailView-flow&amp;unitId=111&amp;periodId=589">x</a>
      <a title="Details für Veranstaltung Übung Y anzeigen"
         href="/qisserver/pages/startFlow.xhtml?_flowId=detailView-flow&amp;unitId=222&amp;periodId=589">x</a>
    </body></html>
    """

    class _FakeClient:
        def get(self, url):
            class R:
                text = fragment

                def raise_for_status(self):
                    pass

            return R()

    import datetime as _dt

    out = fetch_one_day(_FakeClient(), _dt.date(2026, 5, 15), expected_period=589)
    assert out == {111: "Vorlesung X", 222: "Übung Y"}


def test_filters_wrong_period():
    from scrape_tagesaktuelle import fetch_one_day
    import datetime as _dt

    fragment = (
        '<a title="Details für Veranstaltung Foo anzeigen"'
        ' href="/x?_flowId=detailView-flow&amp;unitId=99&amp;periodId=999">x</a>'
    )

    class _FakeClient:
        def get(self, url):
            class R:
                text = fragment

                def raise_for_status(self):
                    pass

            return R()

    out = fetch_one_day(_FakeClient(), _dt.date(2026, 5, 15), expected_period=589)
    assert out == {}
