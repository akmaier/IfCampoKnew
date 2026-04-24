# Campo — Public Surface Analysis

What information can an **anonymous visitor** (not logged in) query from FAU's Campo portal?

**Source:** https://www.campo.fau.de/qisserver/pages/cs/sys/portal/hisinoneStartPage.faces
**Method:** HTTP fetches with a cookie jar (Campo is a HIS eG *HISinOne* deployment using JSF web-flow — every page sets a `_flowExecutionKey`).
**Analysis date:** 2026-04-24

---

## 1. Technology the real Campo runs on

- **Vendor**: HIS eG · product: **HISinOne**.
- **Framework**: JSF (Jakarta Server Faces) + Spring Web Flow, rendered server-side.
- **Session model**: every visit — even anonymous — gets a `JSESSIONID` and a `_flowExecutionKey` per flow. Deep links carry `_flowId=<name>-flow`; state is server-side, so the same URL does not always render the same page.
- **No** `robots.txt` is published (404). Access is otherwise unrestricted for public flows.
- **No** JSON/REST API has been observed — interactions are form posts with `javax.faces.ViewState` tokens.

**Implication for IfCampoKnew.** We cannot simply proxy Campo from a static GitHub Pages site: the JSF flow system needs a stateful crawler/shim. The realistic architecture is an offline scraper that materialises Campo's public data into static JSON, served alongside the UI.

---

## 2. Public entry points (10 flows)

Every flow below is reachable *without* logging in.

| # | Flow ID | Purpose | Start URL (relative) |
|---|---------|---------|----------------------|
| 1 | `showCourseCatalog-flow` | Vorlesungsverzeichnis — hierarchical course catalog | `/qisserver/pages/cm/exa/coursecatalog/showCourseCatalog.xhtml` |
| 2 | `searchCourseNonStaff-flow` | Lehrveranstaltungen suchen — course search | `/qisserver/pages/startFlow.xhtml` |
| 3 | `searchStudyCourseSchedule-flow` | Studiengangspläne — per-study-program schedule | `/qisserver/pages/cm/exa/timetable/studyCourseSchedule.xhtml` |
| 4 | `searchCourseOfStudyForModuleDescription-flow` | Modulbeschreibungen — curriculum browser | `/qisserver/pages/cm/exa/curricula/genericRailsSearchUnitsSimple.xhtml` |
| 5 | `searchElementsInModuleDescription-flow` | In Modulhandbüchern suchen — free-text module search | `/qisserver/pages/cm/exa/curricula/moduleDescriptionSearch.xhtml` |
| 6 | `searchRoomDetail-flow` | Detaillierte Raumsuche — room search with filters | `/qisserver/pages/cm/exa/searchRoomDetail.xhtml` |
| 7 | `searchRoomReservationSchedule-flow` | Raumpläne — room reservation schedules | `/qisserver/pages/plan/raeume.xhtml` |
| 8 | `showEventsAndExaminationsOnDate-flow` | Tagesaktuelle Veranstaltungen — events on a date | `/qisserver/pages/cm/exa/timetable/currentLectures.xhtml` |
| 9 | `searchSpecialEventsOnlyDetails-flow` | Sonderveranstaltung suchen — special events | `/qisserver/pages/startFlow.xhtml` |
| 10 | `searchConflictSchedule-flow` | Pläne für Dozenten und Einrichtungen — date-conflict view | `/qisserver/pages/cm/exa/enrollment/allocation/enter.xhtml` |

**Not publicly reachable** (require login, confirmed by the HISinOne privilege model — not enumerated in this report):
- My exam registrations / grades, my schedule, my documents
- Person directory with private contact data
- Application / enrolment flows

---

## 3. Data available per flow

### 3.1 Vorlesungsverzeichnis (`showCourseCatalog-flow`)

- **Semester selector**: 9 semesters available, from *Wintersemester 2022/23* through *Sommersemester 2026*.
- **Hierarchy**: the catalog is a tree. Top-level nodes confirmed on 2026-04-24 load:
  - Allgemeiner Wahlbereich inklusive Schlüsselqualifikationen und Sprachkurse
  - Studiengänge der Philosophischen Fakultät und des Fachbereichs Theologie
  - Studiengänge der Rechts- und Wirtschaftswissenschaftlichen Fakultät
  - *(+ 4 more faculties not enumerated above but addressed in the catalog)*
- **Per-node actions**: **Permalink** (shareable URL for every node — great for stable deep links).
- **Drill-down**: rendered via AJAX POSTs that expand rows; result is a tree of courses.

### 3.2 Lehrveranstaltungen suchen (`searchCourseNonStaff-flow`)

Search fields exposed **without** login:

- *Grunddaten*: Suchbegriffe (free-text), Semesterunabhängiger Titel, Kurztext, Semesterabhängiger Titel, Semester, Veranstaltungsart (Vorlesung / Seminar / Übung / …), Unterrichtssprache.
- *Struktur*: Organisationseinheit, Studiengang, Modul.
- *Dozent, Ort und Termine*: Dozenten/Dozentinnen, Raum, dates/times (not fully enumerated here; full field list in the raw HTML).

This is the core "find me a course by …" search and is the most direct replacement target for the UI we want to build.

### 3.3 Studiengangspläne (`searchStudyCourseSchedule-flow`)

Search fields: **Suchbegriffe, Abschluss, Fach, Vertiefung, Fachkennzeichen, Prüfungsordnungsversion, Studientyp**. Result is a per-semester plan view of a study program (what courses a student in *Abschluss=Bachelor, Fach=Informatik, Prüfungsordnungsversion=2020, Semester=3* is expected to take).

### 3.4 Modulbeschreibungen / Modulhandbücher (flows 4 & 5)

Two overlapping flows:
- Flow 4 browses module descriptions from the *curriculum* side (Abschluss → Fach → Vertiefung → PO-Version).
- Flow 5 is a direct search: **Titel, Nummer, Unterrichts- und Prüfungssprache, Abschluss, Fach, Vertiefung, Fachkennzeichen, Prüfungsordnungsversion, Studientyp, Lehrende oder Verantwortliche**.

Notable: the dropdowns reveal the full FAU catalogues:

- **Abschluss**: 85+ distinct degrees (Staatsexamen, Promotion, Zertifikat Grundschulen, etc.).
- **Fach**: 350+ subjects (Advanced Healthcare, Advanced Optical Technologies, …, Zahnmedizin).
- **Unterrichts- und Prüfungssprache**: 27+ variants including "Deutsch oder Englisch: Nach Wahl der Lehrveranstaltung durch die Studierenden".

These dropdowns alone are gold: they enumerate FAU's full set of study programs and their attributes.

### 3.5 Raumsuche (`searchRoomDetail-flow`)

Filters:
- **Raumname**, **Gesetzlich erlaubte Anzahl Sitzplätze** (capacity), **Ausstattung** (equipment — free text).
- **Raumnutzungsart** (room-use type; 370+ options, incl. Abfallverbrennungsraum, Abstellraum, …).
- **Typ**, checkboxes *für Veranstaltungen geeignet* / *als Büroraum geeignet*.
- **Gültig von/bis** (validity).
- **Zugehörige Organisationseinheit** (owning org unit).
- **Wochentag, Uhrzeit von/bis, Rhythmus, Datum von/bis** — i.e. *"find a free room on Tuesdays 10-12 with ≥50 seats"* works without login.

### 3.6 Raumpläne (`searchRoomReservationSchedule-flow`)

Filters: Bezeichnung, Raumnutzungsart, *Campus* (Bamberg, ER Großstadtbereich, ER Innenstadt, ER Südgelände, ER Tennenlohe, Fürth, + ~8 more), *Gebäude*. Output is the room's booking calendar.

### 3.7 Tagesaktuelle Veranstaltungen (`showEventsAndExaminationsOnDate-flow`)

The flagship *"what's happening today"* view.

- **Filters**: *Datum* (date), *Alle Termine* / *Termine mit Änderungen* / *Ausfalltermine*, rows-per-page up to 300.
- **Columns**: Titel, Beginn, Ende, Nummer, Parallelgruppe, Veranstaltungsart, Dozent/-in (verantwortlich), Dozent/-in (durchführend), Räume (Gebäude), Semester, Bemerkung, Aktionen.
- On 2026-04-24 the initial load returned **100 events** with all columns populated, e.g. *"Spieleabend FSI Mathe/Physik/DS SoSe 2026, 00:00–06:00, Clara Marie Linke, 12801.01.250 (Felix-Klein-Gebäude)"*. Dates back/forward are reachable via single-click links (`Veranstaltungen am 23./25. April 2026 anzeigen`).

This page is the single richest public dataset in Campo — real-time, day-addressable, with room + instructor + time.

### 3.8 Sonderveranstaltung suchen (`searchSpecialEventsOnlyDetails-flow`)

Filters: Titel, Organisationseinheit, Raum, Mehrfachraumbuchung (ja/nein), Veranstaltungsdatum. Useful for one-off events (guest talks, conferences).

### 3.9 Pläne für Dozenten und Einrichtungen (`searchConflictSchedule-flow`)

A broad "show plans for lecturer X or facility Y" search: Typ, Titel, Nummer, Semester, Organisationseinheit, Dozent/-in, Veranstaltungsart, Prüfungsform, Prüfer/-in, Prüfungsperiode. Effectively a **public lecturer-schedule lookup** — no login needed to see what a professor is teaching.

---

## 4. What's **not** available to the public (confirmed or strongly indicated)

- Individual student data (grades, registrations, study progress).
- Person directory with email/phone (names appear as event data, but there's no "search for a person" flow in the public menu).
- Exam registration status, seat counts, waiting lists.
- Document downloads behind the Mein Studium section.

---

## 5. Observations that will shape the UI rewrite

1. **The data is there, the UI is the problem.** Every user-facing complaint ("I can never find anything") is plausible given the forms: 20-40 visible input fields per flow, many with opaque IDs and no visible labels until you tab into them.
2. **Tree + filter + day-view is the universal pattern.** Catalog (tree), search (filter), today's events (day-addressable) cover 80% of real use.
3. **Deep links almost work.** Campo permalinks exist for catalog nodes, but search results cannot be bookmarked (state lives in the flow execution key). A sensible demo site can *do better* by encoding filter state in the URL hash.
4. **Cross-search is impossible.** A student cannot say "all Informatik-Bachelor 3rd-semester courses taught in English on Tuesday mornings" without running 3 separate searches and mentally joining them.
5. **Semester coverage is 9 semesters** (2022 W through 2026 S). That's the practical horizon for any static snapshot.

---

## 6. Data collection plan (for the GitHub Pages demo)

A static-site demo cannot call Campo live. Two options:

1. **Cached snapshot**: crontab-driven scraper that materialises a JSON dump (courses, rooms, module descriptions, today's events) and checks it into the repo or a release artifact. Demo loads the JSON.
2. **Live proxy via a serverless function**: not compatible with pure GitHub Pages; skip unless we adopt Vercel/Cloudflare Workers.

Recommended: **(1) snapshot**, with a `scraper/` subfolder (Node or Python) that writes into `data/`, and a `site/` subfolder with vanilla JS + a single JSON-index. Decision deferred to the requirements phase.

---

## 7a. How to actually scrape Campo (tested 2026-04-24)

### 7a.1 Session prerequisites

- **A fresh session is mandatory.** Any client must first `GET` `hisinoneStartPage.faces` to receive a `JSESSIONID` bound to `/qisserver`. Reusing a stale cookie (even <24h old) causes silent POST rejection — the form re-renders but no flow advance happens.
- `_flowExecutionKey` is assigned per-flow; it is the literal value of `javax.faces.ViewState` in that flow.
- An `authenticity_token` (Rails-style CSRF token) is embedded in every form and rotates per request.
- After a successful submit, both `_flowExecutionKey` and `javax.faces.ViewState` increment (`e1s1` → `e1s2`).

### 7a.2 Course search — POST recipe (tested, works)

1. Fresh session: GET `hisinoneStartPage.faces`.
2. GET `startFlow.xhtml?_flowId=searchCourseNonStaff-flow` to receive the search form (ViewState `e1s1`).
3. Parse the `genericSearchMask` form: ~15 hidden inputs (incl. `authenticity_token`, `navigationPosition`, `javax.faces.ViewState`, `genericSearchMask_SUBMIT=1`), ~45 visible inputs/selects.
4. POST to the form action with: all hidden inputs, all visible inputs (using current values), plus `SCROLL_TO_ANCHOR=`, `DISABLE_AUTOSCROLL=true`, and the submit button `genericSearchMask:search=Suchen`.
5. Headers: `Content-Type: application/x-www-form-urlencoded`, a realistic `User-Agent`, `Referer` of the form URL, `Origin: https://www.campo.fau.de`.
6. Response (200, same URL with `_flowExecutionKey=e1s2`) contains `<h2>Gefundene Veranstaltungen</h2>` + a result table.

Verified with `Suchbegriffe=Mustererkennung`: returned 2 hits — *Mustererkennung* (Prof. Andreas Maier) and *Praktikum Mustererkennung* (Dr. Vincent Christlein).

### 7a.3 Result-table columns

Per-row fields (8 data columns + 2 action cells):

| Col | Content |
|-----|---------|
| 0 | Actions-left (quick menu with detail button) |
| 1 | **Semesterunabhängiger Titel** (stable course title) |
| 2 | **Kurztext** (short code, e.g. `PME`) |
| 3 | **Semesterabhängiger Titel** (semester-specific title) |
| 4 | **Veranstaltungsart** (Vorlesung / Seminar / Übung / Praktikum / …) |
| 5 | **Dozent/-in (verantwortlich)** |
| 6 | **Dozent/-in (durchführend)** |
| 7 | **Organisationseinheit** |
| 8 | Actions-right (detail button with `unitId` + `periodId`) |

### 7a.4 Deep links (the gold find)

Campo exposes **stable deep-links** for every course and every catalog node. These work with *only a fresh session cookie* — no ViewState, no CSRF token:

- **Course detail:**
  ```
  /qisserver/pages/startFlow.xhtml?_flowId=detailView-flow&unitId={unitId}&periodId={periodId}
  ```
  Example: `unitId=86267&periodId=589` → *Praktikum Mustererkennung* (SoSe 2026).

- **Catalog tree node:**
  ```
  /qisserver/pages/startFlow.xhtml?_flowId=showCourseCatalog-flow&periodId={periodId}&path=title:{rootId}|title:{lvl1Id}|title:{lvl2Id}…
  ```
  The full hierarchy is encoded in the `path=` parameter, pipe-separated (`|` URL-encoded as `%7C`, `:` as `%3A` when strict). Root `title:17593` has faculty-level children; each deeper level adds another `|title:NNNN`.

  Both the GET-only catalog browser (root node via `_flowId=showCourseCatalog-flow` with no `path`) and any sub-node permalink were verified to render directly in a fresh session.

### 7a.5 Course detail — available tabs

The detail page (tested on `unitId=86267`) exposes 5 tabs, loaded via JSF postback:

1. **Termine** (default) — schedule, time slots, rooms, parallel groups.
2. **Inhalte** — description, learning goals, literature.
3. **Vorlesungsverzeichnis** — where the course sits in the catalog tree.
4. **Module / Studiengänge** — which study programs and modules use this course.
5. **Dokumente** — file attachments (syllabus, etc.).

Data fields already visible on the default tab (sample): Veranstaltungsart, Turnus des Angebots (*jedem Semester*), ECTS-Punkte (`5.0`), Unterrichtssprache (`Deutsch oder Englisch`), Verantwortliche/-r.

### 7a.6 No direct exports (confirmed)

- No iCal/`.ics` download links on course detail or today's events.
- No PDF download on course detail (though *Dokumente* tab may hold them).
- No JSON API endpoints observed.
- `robots.txt` returns 404 — so Campo has no published crawl policy; defensive scraping etiquette is our responsibility (slow, cached, weekly).

### 7a.7 Scraper implications

A scraper for IfCampoKnew becomes *much* simpler than expected:

1. Walk the catalog tree via `path=` deep-links (pure GETs).
2. At each leaf, a `unitId` is exposed → fetch the course detail (pure GET).
3. Parse the Termine tab HTML for schedule/room/instructor data.
4. Per semester (`periodId`) this is ≈ O(n) courses * 2 GETs each.

The only operation requiring a full JSF POST-with-CSRF is the **filtered course search**. We can skip it entirely in the scraper: if we have the catalog tree + all course detail pages, any filter is a client-side operation.

**Target data model:**

```jsonc
{
  "periodId": 589,
  "periodName": "Sommersemester 2026",
  "tree":   [ /* nested catalog nodes with titleId, name, parent */ ],
  "courses": [
    {
      "unitId": 86267,
      "titleStable": "Praktikum Mustererkennung",
      "titleSemester": "Praktikum Mustererkennung",
      "shortText": "PME",
      "type": "Praktikum",
      "ects": 5.0,
      "language": "Deutsch oder Englisch",
      "orgUnit": "Lehrstuhl für Informatik 5 (Mustererkennung)",
      "instructorsResp": ["Andreas Maier"],
      "instructorsExec": ["Vincent Christlein"],
      "catalogPaths": [ "17593|17598|17...", /* ... */ ],
      "termine": [ /* parallel groups with weekday/time/room/dates */ ],
      "permalink": "https://www.campo.fau.de/qisserver/pages/startFlow.xhtml?_flowId=detailView-flow&unitId=86267&periodId=589"
    }
  ]
}
```

## 7b. Open questions for the requirements session

- Do we want to replicate *all 10* public flows, or focus on 2-3 that cover the top pain points?
- Should the demo be English-first, German-first, or bilingual?
- Do we care about historical semesters, or only the current + next?
- Is it acceptable that data is ~24h stale (scraper runs nightly) on the demo?
- Which persona gets priority: the student hunting for a course, or the lecturer checking who else is teaching at the same time?
- Given deep-linking works (§7a.4), is the scraper's first output a full **snapshot per semester** (all courses + tree + rooms), or do we demo with a single faculty first?
