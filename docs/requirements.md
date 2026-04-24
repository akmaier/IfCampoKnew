# IfCampoKnew — Requirements Analysis

> Status: **skeleton**. The actual requirements discussion happens in the next session, after reviewing `docs/campo-public-surface.md`. This file exists so that the requirements live alongside the analysis and can be filled in iteratively, in the spirit of the *vibe coding* book.

---

## 1. Vision

A friendly, browser-only front end over the *public* surface of FAU's Campo portal (https://www.campo.fau.de/). IfCampoKnew replaces the JSF-heavy UI with a fast, URL-shareable, filter-first experience, served as a static site on GitHub Pages.

## 2. Personas (primary)

| # | Persona | Main job-to-be-done | Top pain with current Campo |
|---|---------|---------------------|-----------------------------|
| P1 | **Student (enrolled)** | Find the right course / module / exam time / room. | Searches are deeply nested; no cross-facet filtering; permalinks rare. |
| P2 | **Lecturer** | See own and colleagues' schedules; find free rooms; look up module descriptions. | Multiple flows for closely-related tasks; no overview across courses. |
| P3 | **Administrator / staff** | Quick lookup of rooms, current events, study-program plans. | Having to log in for read-only tasks; fragmented filters. |
| P4 | **Other university people** (prospective students, guests, partners) | Browse study programs, find today's events on campus. | Navigation assumes insider terminology. |

*(To be refined: concrete job stories — "As a P1, I want to …, so that …" — based on what we found to be publicly reachable in section 3 of `campo-public-surface.md`.)*

## 3. Functional scope — candidates (to be prioritised)

Each candidate maps 1:1 to a public Campo flow (see analysis §2).

- [ ] **F1 — Course search** (maps to `searchCourseNonStaff-flow`). Facets: semester, subject, language, instructor, organisational unit, room, day/time.
- [ ] **F2 — Today's events / day view** (maps to `showEventsAndExaminationsOnDate-flow`). A date picker, a list of all events on campus with filters by building/lecturer.
- [ ] **F3 — Room finder** (maps to `searchRoomDetail-flow`). "Find a free room with ≥N seats on day D, slot T".
- [ ] **F4 — Room schedule** (maps to `searchRoomReservationSchedule-flow`). Week view per room.
- [ ] **F5 — Module catalog browser** (maps to flows 4 & 5). Filter by Abschluss/Fach/Vertiefung/language.
- [ ] **F6 — Study-program plan** (maps to `searchStudyCourseSchedule-flow`). "What does semester 3 of B.Sc. Informatik (PO 2020) look like?"
- [ ] **F7 — Lecturer schedule** (maps to `searchConflictSchedule-flow`). Public lookup: "what is Prof. X teaching this semester?"
- [ ] **F8 — Special-event search** (maps to `searchSpecialEventsOnlyDetails-flow`).
- [ ] **F9 — Course catalog tree** (maps to `showCourseCatalog-flow`). Full hierarchy browser, stable URLs per node.

## 4. Non-functional requirements (draft)

- **NFR-1 (Hosting)** Pure static site on GitHub Pages. No server at runtime.
- **NFR-2 (Freshness)** Data is a snapshot refreshed at most daily — acceptable for a demo.
- **NFR-3 (Shareability)** Every filter state has a URL (hash-based). Every course / module / room has a stable permalink.
- **NFR-4 (Performance)** First contentful paint < 1s on a cold cache on standard broadband. Search results < 200ms client-side on snapshots.
- **NFR-5 (Bilingual)** DE/EN interchangeable.
- **NFR-6 (Accessibility)** WCAG 2.1 AA: keyboard navigation, screen-reader labels, colour-contrast AA.
- **NFR-7 (Privacy)** No analytics, no cookies, no tracking. We only expose data already public on Campo.
- **NFR-8 (Reproducibility)** Scraper and snapshot pipeline live in-repo; anyone can re-run them.

## 5. Architecture hypothesis (to confirm)

```
┌──────────────────────┐       ┌──────────────────┐
│  scraper/  (Node?)   │ ───▶  │  data/  (JSON)   │  ◀── GitHub Actions cron
└──────────────────────┘       └──────────────────┘
                                         │
                                         ▼
                              ┌────────────────────────┐
                              │ site/  (vanilla JS SPA) │  ◀── served by GitHub Pages
                              └────────────────────────┘
```

Open: framework choice (vanilla / Preact / Svelte), scraper language (Node / Python / Playwright), index format (JSON array vs FlexSearch vs SQLite-WASM).

## 6. Out of scope (for this version)

- Any feature that requires a Campo login (grades, registrations, enrolments, personal schedule).
- Write-back to Campo.
- Authentication against IdM.

## 7. Decisions log

*(empty — populated as we make them.)*
