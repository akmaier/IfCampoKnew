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
    # NB: "Organisationseinheit" is parsed separately via _parse_org_units —
    # it's a <ul><li> list with one entry per home-Lehrstuhl + one per
    # cross-listed Studiengang. The previous parser flattened this into a
    # single text blob that dropped row boundaries.
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

# ── Organisationseinheit list (home Lehrstuhl + cross-listed Studiengänge) ───

# Campo's Organisationseinheit value is a <ul> with one <li> per row. Each
# row is one of:
#   * a home Lehrstuhl,      e.g.  "Lehrstuhl für Informatik 5 (Mustererkennung) (Verantwortlicher)"
#   * a cross-listed program, e.g. "FAU Tech | Medizintechnik | Master of Science (Verantwortlicher)"
# Program rows always have a stable `Fakultät | Programm | Abschluss`
# pipe-separated shape; the role suffix in parens is optional. Faculty
# strings vary and Campo has re-styled them a few times:
#   * old  (through mid-2026):    TechFak / PhilFak / ReWiFak / NatFak / MedFak / TheolFak
#   * new  (2026-07+):            FAU Tech / FAU Phil / FAU ReWi / FAU Nat / FAU Med / FAU Theol
#   * always:                     FB Pharmazie / Fachbereich Theologie / ZUV / ZiWiS
# We accept both styles.
_FACULTY_ROW_RE = re.compile(
    r"""
    ^(?:
        FAU\s+(?:Tech|Phil|ReWi|Nat|Med|Theol|Wi)          # new-style prefix
        | [A-Za-z]+Fak                                       # old-style ...Fak
        | (?:FB|Fachbereich)\s+[A-Z]                         # FB Pharmazie / Fachbereich X
        | ZUV | ZiWiS                                        # institutional stems
    )\b
    """,
    re.VERBOSE,
)
_ROLE_PAREN_RE = re.compile(
    r"\s*\(\s*("
    r"Verantwortlicher|Verantwortliche|Verantwortliche/-r|Verantwortliche/r"
    r"|Durchführender|Durchführende|Durchf[üu]hrende(?:/-r|/r)?"
    r"|Begleitende(?:/-r|/r)?|Beteiligte(?:/-r|/r)?|Mitwirkende(?:/-r|/r)?"
    r"|Prüfende(?:/-r|/r)?"
    r")\s*\)\s*$",
    re.IGNORECASE,
)

def _parse_org_row(text: str) -> dict:
    """Classify one Organisationseinheit row.

    Returns a dict with at least:
      * ``raw``  — the original cleaned text,
      * ``role`` — the role-suffix (Verantwortlicher / Durchführender / …) if any,
      * ``kind`` — ``"program"`` if the row matches the
        ``Fakultät | Programm | Abschluss`` shape, else ``"org"``.
    For ``kind == "program"`` additionally:
      * ``faculty``, ``program``, ``degree`` — the three pipe-separated parts.
    For ``kind == "org"`` additionally:
      * ``name`` — the same as ``raw`` minus the role suffix (e.g. ``"Lehrstuhl für Informatik 5 (Mustererkennung)"``).
    """
    text = (text or "").strip()
    role_m = _ROLE_PAREN_RE.search(text)
    role = role_m.group(1) if role_m else None
    main = _ROLE_PAREN_RE.sub("", text).strip() if role else text
    parts = [p.strip() for p in main.split("|")]
    # A program row has exactly 3 pipe-separated parts where the first one
    # *looks* like a faculty token (e.g. "TechFak" old-style, "FAU Tech"
    # new-style, "FB Theologie", "Fachbereich Physik"). The regex above
    # covers both spellings; without a match the row stays classified as
    # "org" (a Lehrstuhl/Institut name that happens to contain pipes will
    # not start with a faculty stem).
    if len(parts) == 3 and _FACULTY_ROW_RE.match(parts[0]):
        return {
            "raw": text,
            "kind": "program",
            "role": role,
            "faculty": parts[0],
            "program": parts[1],
            "degree": parts[2],
        }
    return {
        "raw": text,
        "kind": "org",
        "role": role,
        "name": main,
    }

_ORG_UL_RE = re.compile(
    r'<ul\b[^>]*\bclass="[^"]*\blistStyleIconSimple\b[^"]*"[^>]*>'
    r"(?P<body>.*?)</ul>",
    re.DOTALL,
)
_ORG_LABEL_RE = re.compile(
    r"<label\b[^>]*>\s*Organisationseinheit\b[^<]*</label>",
    re.IGNORECASE,
)
_NEXT_LABEL_RE = re.compile(r"<label\b[^>]*>\s*(?!Organisationseinheit)", re.IGNORECASE)
# Inside a popup, Campo emits a draggable "<h3 class=mouseMoveTitle>" which
# the plain label-block matcher treats as a section boundary. The popup's
# own heading is not a section break — so we use a wider capture here and
# rely on the `<ul class="listStyleIconSimple">` shape to find every
# Organisationseinheit row (visible list + popup-expanded list).

def _parse_org_units(html: str) -> tuple[Optional[str], list[dict]]:
    """Return ``(home_org_unit, assigned_programs)`` from the Organisationseinheit list.

    Campo renders this field as a small visible ``<ul>`` plus, when the
    list overflows, a "Mehr…" popup containing the *complete* list in a
    second ``<ul class="listStyleIconSimple">``. We slurp a wide window
    starting at the ``Organisationseinheit`` label, find every such
    ``<ul>`` until the next labelled field, and union the ``<li>`` rows
    (de-duplicated by raw text).

    ``home_org_unit`` is the *text* of the first non-program row (typically
    the home Lehrstuhl), preserved for backwards compatibility with
    ``Course.org_unit``. ``assigned_programs`` is the structured list of
    cross-listed Studiengänge, each a dict from ``_parse_org_row``.
    """
    m = _ORG_LABEL_RE.search(html)
    if not m:
        return None, []
    after = html[m.end():]
    # Cut at the next labelled field so we don't bleed into the rest of the
    # detail page. A generous 20 kB window comfortably covers Campo's
    # popup HTML for courses with many cross-listings.
    nxt = _NEXT_LABEL_RE.search(after)
    window = after[: nxt.start() if nxt else min(20_000, len(after))]

    seen_raw: set[str] = set()
    rows: list[dict] = []
    for ul_m in _ORG_UL_RE.finditer(window):
        for li_html in _LI_RE.findall(ul_m.group("body")):
            # Skip the popup-wrapper <li> — it just holds the "Mehr..." button
            # and re-emits the same list inside a nested <ul>. Non-greedy
            # _LI_RE would otherwise capture this wrapper's opening text
            # ("Mehr...") plus content up to the first inner </li>, producing
            # a duplicate row prefixed with "Mehr...".
            if "popupDismissable" in li_html or "showPopup" in li_html:
                continue
            text = _text(li_html).strip()
            if not text or text in seen_raw:
                continue
            seen_raw.add(text)
            rows.append(_parse_org_row(text))

    if not rows:
        # No <ul> structure at all — fall back to the flattened text.
        flat = _text(window[:2000])
        return flat or None, []

    home_rows = [r for r in rows if r["kind"] == "org"]
    program_rows = [r for r in rows if r["kind"] == "program"]
    home_org = home_rows[0]["raw"] if home_rows else None
    return home_org, program_rows

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

_TERMINE_TABLE_RE = re.compile(
    r'<table[^>]*\bid="[^"]*appointmentSeriesTableTable"[^>]*>'
    r"(?P<table>.*?)</table>",
    re.DOTALL,
)
_TERMINE_TBODY_RE = re.compile(
    r'<tbody[^>]*\bid="[^"]*appointmentSeriesTableTable:tbody_element"[^>]*>'
    r"(?P<body>.*?)</tbody>",
    re.DOTALL,
)
_TERMINE_THEAD_RE = re.compile(
    r"<thead\b[^>]*>(?P<head>.*?)</thead>",
    re.DOTALL,
)
_TH_RE = re.compile(r"<th\b[^>]*>(?P<cell>.*?)</th>", re.DOTALL)
_TR_RE = re.compile(r"<tr\b[^>]*>(?P<row>.*?)</tr>", re.DOTALL)
_TD_RE = re.compile(r"<td\b[^>]*>(?P<cell>.*?)</td>", re.DOTALL)
_LI_RE = re.compile(r"<li\b[^>]*>(?P<item>.*?)</li>", re.DOTALL)
# Each instructor <li> wraps a button/span whose title attribute is
# "Profil von {Name} anzeigen" — the cleanest source for the name.
_INSTRUCTOR_TITLE_RE = re.compile(
    r'\btitle="Profil von\s+([^"]+?)\s+anzeigen"', re.IGNORECASE
)

# Role annotations Campo appends to the visible instructor name in some
# views (e.g. "Prof. Dr. Person D (Zuständigkeit: Verantwortliche/-r)").
# These are not part of the person's identity — the same prof rendered with
# vs. without the suffix used to land in two separate by_person buckets in
# downstream tools. Strip them at parse time so the JSON intermediate is
# clean and every consumer benefits.
_ROLE_SUFFIX_RE = re.compile(
    r"\s*\((?:Zust[äa]ndigkeit:\s*)?"
    r"(?:Verantwortliche|Durchf[üu]hrende|Begleitende|Beteiligte|Mitwirkende|Pr[üu]fende)"
    r"(?:[/-]+(?:r|in))?"
    r"\s*\)\s*$",
    re.IGNORECASE,
)

def _strip_role_suffix(s: str) -> str:
    return _ROLE_SUFFIX_RE.sub("", s).strip()

def _instructors_from_cell(cell_html: str) -> list[str]:
    """Extract the list of instructor names from an instructor-column
    ``<td>``. Each instructor lives in its own ``<li>`` — we parse those
    structurally so two adjacent names never get concatenated into one
    string. The cleanest signal is the ``title="Profil von … anzeigen"``
    attribute on the inner button/span; if that's missing we fall back
    to the visible text of the ``<li>``. Role-suffix annotations like
    ``(Zuständigkeit: Verantwortliche/-r)`` are stripped here so the
    JSON intermediate carries clean person identities.
    """
    items = _LI_RE.findall(cell_html)
    if not items:
        # No <li> at all — fall back to the previous-style splitter so a
        # single-instructor cell still works.
        text = _text(cell_html)
        return [_strip_role_suffix(p) for p in re.split(r"[·•|]+|\n", text) if p.strip()]

    out: list[str] = []
    seen: set[str] = set()
    for li in items:
        # Prefer the explicit title="Profil von Name anzeigen"
        m = _INSTRUCTOR_TITLE_RE.search(li)
        if m:
            name = _html.unescape(m.group(1)).strip()
        else:
            name = _text(li).strip()
        name = _strip_role_suffix(name)
        if not name or name in seen:
            continue
        seen.add(name)
        out.append(name)
    return out

def _detect_termine_columns(table_html: str) -> dict[str, int]:
    """Map Campo's Termine-table headers to column indices.

    Campo's column layout has drifted over time and is not fixed-width:
    different course detail pages can have 8, 9, or 10 columns
    (e.g. an "Änderungen" column at the front, an "Erw. Tn." column for
    expected attendees, a "Bemerkung" column, ...). The previous parser
    used a positional comment from "2026-04" that mapped col 6 to room
    and col 7 to instructors — by 2026-05 the room cell at col 6 was
    actually the *capacity* (e.g. ``350`` for Deep Learning) and the
    real room sat at col 9 with full identifiers like
    ``11907.01.040 (H18)``.

    This helper parses the ``<thead>`` and returns a dict of
    ``{semantic_name: col_index}`` for the headers we care about. Caller
    falls back to no-op if a column isn't present.
    """
    out: dict[str, int] = {}
    thead_m = _TERMINE_THEAD_RE.search(table_html)
    if not thead_m:
        return out
    th_cells = _TH_RE.findall(thead_m.group("head"))
    for i, th in enumerate(th_cells):
        label = _text(th).strip().lower()
        # The header text often has "[Sortierbare Spalte]" tail noise;
        # drop it before keyword matching.
        label = re.sub(r"\[.*?\]", "", label).strip()
        if "rhythmus" in label:
            out.setdefault("rhythm", i)
        elif "wochentag" in label:
            out.setdefault("weekday", i)
        elif "von" in label and "bis" in label:
            out.setdefault("time", i)
        elif "ausfalltermin" in label:
            out.setdefault("cancelled", i)
        elif ("startdatum" in label and "enddatum" in label) or label == "datum von – bis":
            out.setdefault("daterange", i)
        elif "bemerkung" in label:
            out.setdefault("note", i)
        elif "durchführende" in label or "dozent" in label or "lehrende" in label:
            out.setdefault("instructors", i)
        elif label == "raum" or label.startswith("raum"):
            out.setdefault("room", i)
        # Erw. Tn. / capacity is captured but unused (kept for future).
        elif "erw" in label and "tn" in label:
            out.setdefault("capacity", i)
    return out

def _parse_appointments(html: str) -> list[Appointment]:
    """The Termine table — one row per scheduled appointment series.

    Columns are detected from the ``<thead>`` so a future Campo layout
    change doesn't silently mis-map fields (the previous positional
    parser read the "Erw. Tn." capacity column as the room — yielding
    e.g. ``350`` instead of ``11907.01.040 (H18)`` for Deep Learning).
    """
    table_m = _TERMINE_TABLE_RE.search(html)
    body_m = _TERMINE_TBODY_RE.search(html)
    if not body_m:
        return []
    col_idx = _detect_termine_columns(table_m.group("table")) if table_m else {}
    appts: list[Appointment] = []
    for row_m in _TR_RE.finditer(body_m.group("body")):
        cells_html = _TD_RE.findall(row_m.group("row"))
        if not cells_html:
            continue
        cells = [_text(c) for c in cells_html]

        def cell(name: str, fallback_idx: int | None = None) -> str | None:
            idx = col_idx.get(name)
            if idx is None:
                idx = fallback_idx
            if idx is None or idx >= len(cells):
                return None
            return cells[idx] or None

        appt = Appointment()
        appt.rhythm = cell("rhythm", 0)
        appt.weekday = cell("weekday", 1)
        time_text = cell("time", 2)
        if time_text:
            tm = re.match(r"(\d{2}:\d{2})\s*[-–]\s*(\d{2}:\d{2})", time_text)
            if tm:
                appt.time_from, appt.time_to = tm.group(1), tm.group(2)
        cancelled = cell("cancelled", 3)
        if cancelled:
            appt.cancelled_dates = [
                d.strip() for d in re.split(r"[;,\s]+", cancelled) if d.strip()
            ]
        date_text = cell("daterange", 4)
        if date_text:
            dm = re.match(
                r"(\d{2}\.\d{2}\.\d{4})\s*[-–]\s*(\d{2}\.\d{2}\.\d{4})", date_text,
            )
            if dm:
                appt.date_from, appt.date_to = dm.group(1), dm.group(2)
            else:
                appt.date_from = date_text
        note = cell("note", 5)
        if note:
            appt.note = note
        room = cell("room", 6)
        if room:
            appt.room = room
        # instructors: parse the raw <li> structure of the cell HTML, not
        # the flattened text — see _instructors_from_cell.
        instr_idx = col_idx.get("instructors")
        if instr_idx is None:
            instr_idx = 7 if len(cells_html) > 7 else None
        if instr_idx is not None and instr_idx < len(cells_html):
            appt.instructors = _instructors_from_cell(cells_html[instr_idx])
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
    home_org, assigned_programs = _parse_org_units(html)
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
        org_unit=home_org,
        assigned_programs=assigned_programs,
        instructors_resp=_parse_instructors(html, "Verantwortliche/-r")
        or _parse_instructors(html, "Verantwortliche"),
        instructors_exec=_parse_instructors(html, "Dozent/-in (durchführend)")
        or _parse_instructors(html, "Durchführende"),
        appointments=_parse_appointments(html),
    )
    return course
