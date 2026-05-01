"""Parse a Campo course-detail page (``detailView-flow``) into a ``Course``.

The Campo detail page is a JSF tabbed view with five tabs: *Termine*
(default, schedule), *Inhalte* (description), *Vorlesungsverzeichnis*
(catalogue placement), *Module / Studiengänge* (which programmes use it),
*Dokumente*. Switching tabs requires JSF AJAX postbacks. For the corpus
v0 we extract everything visible on the **default Termine page** plus the
basic-data block at the top, which is rendered regardless of tab.

Field strategy: most fields are rendered as ``<label>NAME</label>`` next
to a value cell; we use that label as the anchor and slurp the text up
to the next label or block boundary. The schedule sits in a stable
``appointmentSeriesTableTable`` ``<tbody>`` we can parse row-by-row.
"""
from __future__ import annotations

import html as _html
import re
from typing import Optional

from schema import Appointment, Course


CAMPO_BASE = "https://www.campo.fau.de"
DETAIL_URL = f"{CAMPO_BASE}/qisserver/pages/startFlow.xhtml?_flowId=detailView-flow"


# ── helpers ────────────────────────────────────────────────────────────────


_WS_RE = re.compile(r"\s+")
_TAG_RE = re.compile(r"<[^>]+>")


def _text(html: str) -> str:
    return _WS_RE.sub(" ", _TAG_RE.sub(" ", html)).strip()


_LABEL_BLOCK_RE_TPL = (
    r"<label\b[^>]*>\s*{lbl}\b[^<]*</label>"
    r"(?P<after>.*?)"
    r'(?=<label\b|<h\d\b|<div\s+class="block_|<fieldset\b|<section\b)'
)


def _label_html_block(html: str, label: str) -> Optional[str]:
    """Like ``_label_value`` but returns the *raw HTML* of the value cell.

    Useful when we want to walk the inner structure (e.g. a ``<ul><li>``
    instructor list) rather than just the flattened text."""
    pat = re.compile(
        _LABEL_BLOCK_RE_TPL.format(lbl=re.escape(label)),
        re.DOTALL | re.IGNORECASE,
    )
    m = pat.search(html)
    return m.group("after") if m else None


def _label_value(html: str, label: str) -> Optional[str]:
    """Slurp the text immediately after ``<label>LABEL…</label>``.

    The regex consumes the entire opening ``<label …>LABEL[ :…]</label>``
    so the captured ``after`` group starts at the value cell. Stops at the
    next ``<label>``, ``<h1>…</h6>``, or a ``<div class="block_…">`` —
    HISinOne uses these as section separators.
    """
    block = _label_html_block(html, label)
    if not block:
        return None
    text = _text(block)
    return text or None


# ── basic-data block ───────────────────────────────────────────────────────


_BASIC_LABELS = {
    "course_type": "Veranstaltungsart",
    "ects": "ECTS-Punkte",
    "language": "Unterrichtssprache",
    "turnus": "Turnus des Angebots",
    "short_text": "Kurztext",
    "org_unit": "Organisationseinheit",
}


def _parse_basic(html: str) -> dict:
    """Pull basic-data fields by their German labels."""
    out: dict = {}
    for key, label in _BASIC_LABELS.items():
        v = _label_value(html, label)
        if v is None:
            continue
        out[key] = v
    if "ects" in out:
        m = re.search(r"\d+(?:[.,]\d+)?", out["ects"])
        out["ects"] = float(m.group(0).replace(",", ".")) if m else None
    return out


# ── instructors (responsible / executing) ──────────────────────────────────


def _parse_instructors(html: str, label: str) -> list[str]:
    """Names listed under e.g. ``Verantwortliche/-r`` or ``Dozent/-in (durchführend)``.

    Each instructor is rendered as one ``<li>`` inside a ``<ul>``; we parse
    the list structurally so adjacent names never get glued into a single
    string. The ``title="Profil von {Name} anzeigen"`` attribute on the
    inner button/span is the cleanest source of the name. Falls back to a
    text-based splitter when no ``<li>`` is present.
    """
    block_html = _label_html_block(html, label)
    if not block_html:
        return []
    li_items = _LI_RE.findall(block_html)
    if li_items:
        return _instructors_from_cell(block_html)
    # No <li> structure — fall back to flattened text + naive split.
    text = _text(block_html)
    if not text:
        return []
    parts = re.split(r"\s{2,}|,\s+|;\s+", text)
    seen: set[str] = set()
    out: list[str] = []
    for p in parts:
        p = p.strip()
        if not p or p in seen:
            continue
        if re.search(r"(?i)\b(hilfe|anzeigen|zur\b|ein-?\s?ausklappen)", p):
            continue
        seen.add(p)
        out.append(p)
    return out


# ── schedule table ─────────────────────────────────────────────────────────


_TERMINE_TBODY_RE = re.compile(
    r'<tbody[^>]*\bid="[^"]*appointmentSeriesTableTable:tbody_element"[^>]*>'
    r"(?P<body>.*?)</tbody>",
    re.DOTALL,
)
_TR_RE = re.compile(r"<tr\b[^>]*>(?P<row>.*?)</tr>", re.DOTALL)
_TD_RE = re.compile(r"<td\b[^>]*>(?P<cell>.*?)</td>", re.DOTALL)
_LI_RE = re.compile(r"<li\b[^>]*>(?P<item>.*?)</li>", re.DOTALL)
# Each instructor <li> wraps a button/span whose title attribute is
# "Profil von {Name} anzeigen" — the cleanest source for the name.
_INSTRUCTOR_TITLE_RE = re.compile(
    r'\btitle="Profil von\s+([^"]+?)\s+anzeigen"', re.IGNORECASE
)


def _instructors_from_cell(cell_html: str) -> list[str]:
    """Extract the list of instructor names from an instructor-column
    ``<td>``. Each instructor lives in its own ``<li>`` — we parse those
    structurally so two adjacent names never get concatenated into one
    string. The cleanest signal is the ``title="Profil von … anzeigen"``
    attribute on the inner button/span; if that's missing we fall back
    to the visible text of the ``<li>``.
    """
    items = _LI_RE.findall(cell_html)
    if not items:
        # No <li> at all — fall back to the previous-style splitter so a
        # single-instructor cell still works.
        text = _text(cell_html)
        return [p.strip() for p in re.split(r"[·•|]+|\n", text) if p.strip()]

    out: list[str] = []
    seen: set[str] = set()
    for li in items:
        # Prefer the explicit title="Profil von Name anzeigen"
        m = _INSTRUCTOR_TITLE_RE.search(li)
        if m:
            name = _html.unescape(m.group(1)).strip()
        else:
            name = _text(li).strip()
        if not name or name in seen:
            continue
        seen.add(name)
        out.append(name)
    return out


def _parse_appointments(html: str) -> list[Appointment]:
    """The Termine table — one row per scheduled appointment series."""
    m = _TERMINE_TBODY_RE.search(html)
    if not m:
        return []
    appts: list[Appointment] = []
    for row_m in _TR_RE.finditer(m.group("body")):
        cells_html = _TD_RE.findall(row_m.group("row"))
        if not cells_html:
            continue
        cells = [_text(c) for c in cells_html]
        appt = Appointment()
        # Column order observed on Campo (2026-04):
        #   0 rhythm, 1 weekday, 2 time, 3 cancelled-dates list,
        #   4 date-range, 5 (sometimes) note, 6 room, 7 instructors-list
        if len(cells) > 0: appt.rhythm = cells[0] or None
        if len(cells) > 1: appt.weekday = cells[1] or None
        if len(cells) > 2:
            tm = re.match(r"(\d{2}:\d{2})\s*[-–]\s*(\d{2}:\d{2})", cells[2])
            if tm:
                appt.time_from, appt.time_to = tm.group(1), tm.group(2)
        if len(cells) > 3 and cells[3]:
            appt.cancelled_dates = [d.strip() for d in re.split(r"[;,\s]+", cells[3]) if d.strip()]
        if len(cells) > 4 and cells[4]:
            dm = re.match(r"(\d{2}\.\d{2}\.\d{4})\s*[-–]\s*(\d{2}\.\d{2}\.\d{4})", cells[4])
            if dm:
                appt.date_from, appt.date_to = dm.group(1), dm.group(2)
            else:
                appt.date_from = cells[4]
        if len(cells) > 5 and cells[5]:
            appt.note = cells[5] or None
        if len(cells) > 6 and cells[6]:
            appt.room = cells[6] or None
        # instructors: parse the raw <li> structure of the cell HTML, not
        # the flattened text — see _instructors_from_cell.
        if len(cells_html) > 7:
            appt.instructors = _instructors_from_cell(cells_html[7])
        appts.append(appt)
    return appts


# ── permalink / title ──────────────────────────────────────────────────────


_PERMA_DETAIL_RE = re.compile(
    r"<textarea[^>]*>(https?://[^<]*?_flowId=detailView-flow[^<]*?)</textarea>",
    re.DOTALL,
)
_TITLE_FROM_PERMA_RE = re.compile(
    r'data-page-permalink-title="([^"]+)"', re.IGNORECASE
)


def _parse_permalink_and_title(html: str) -> tuple[Optional[str], Optional[str]]:
    """Return ``(permalink_url, title)`` from the share-permalink popup.

    Campo prefixes the title with the literal word "Elementdaten " — that's
    a Campo-internal section label, not part of the course name; we strip it.
    """
    m = re.search(
        r"<textarea\b([^>]*?)>(https?://[^<]*?_flowId=detailView-flow[^<]*?)</textarea>",
        html,
        re.DOTALL,
    )
    if not m:
        return None, None
    attrs, url = m.group(1), m.group(2)
    title_m = _TITLE_FROM_PERMA_RE.search(attrs)
    title = _html.unescape(title_m.group(1)).strip() if title_m else None
    if title and title.lower().startswith("elementdaten "):
        title = title[len("elementdaten "):].strip()
    return _html.unescape(url).strip(), title


# ── public API ─────────────────────────────────────────────────────────────


def parse_course_detail(
    html: str, *, unit_id: int, period_id: int, fallback_title: Optional[str] = None
) -> Course:
    """Build a :class:`Course` from the rendered detail HTML.

    ``fallback_title`` is used when Campo's permalink popup omits the title
    (rare but defensive — the catalog row already gave us a name).
    """
    permalink, title = _parse_permalink_and_title(html)
    if not permalink:
        permalink = f"{DETAIL_URL}&unitId={unit_id}&periodId={period_id}"
    title = title or fallback_title or f"unit:{unit_id}"

    basic = _parse_basic(html)
    course = Course(
        unit_id=unit_id,
        period_id=period_id,
        title=title,
        permalink=permalink,
        course_type=basic.get("course_type"),
        short_text=basic.get("short_text"),
        ects=basic.get("ects"),
        language=basic.get("language"),
        turnus=basic.get("turnus"),
        org_unit=basic.get("org_unit"),
        instructors_resp=_parse_instructors(html, "Verantwortliche/-r")
        or _parse_instructors(html, "Verantwortliche"),
        instructors_exec=_parse_instructors(html, "Dozent/-in (durchführend)")
        or _parse_instructors(html, "Durchführende"),
        appointments=_parse_appointments(html),
    )
    return course
