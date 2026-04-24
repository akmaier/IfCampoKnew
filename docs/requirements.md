# IfCampoKnew — Requirements Analysis

> Status: **v1 locked** (2026-04-24). Decisions taken in Entry 0003 of [`devlog.md`](../devlog.md). This file is authoritative for v1 scope; open items are explicitly flagged.

---

## 1. Vision

A friendly, browser-only front end over the *public* surface of FAU's Campo portal (https://www.campo.fau.de/). IfCampoKnew replaces Campo's JSF-heavy UI with a fast, filter-first, URL-shareable experience, served as a static site on GitHub Pages and embeddable in WordPress.

## 2. Personas

| # | Persona | Priority | Main job-to-be-done | Top pain with current Campo |
|---|---------|:-------:|---------------------|-----------------------------|
| **P1** | **Student (enrolled)** | **★ primary** | Find the right course / module / exam time / room for my program. | Searches are deeply nested; no cross-facet filtering; hard-to-share permalinks; unfamiliar terminology. |
| P2 | Lecturer | secondary | See own and colleagues' schedules; find free rooms; look up module descriptions. | Multiple flows for related tasks; no overview across courses. |
| P3 | Administrator / staff | secondary | Quick lookup of rooms, events, study-program plans. | Login required for read-only tasks; fragmented filters. |
| P4 | Other university people (prospective students, guests, partners) | tertiary | Browse study programs; find today's events on campus. | Navigation assumes insider terminology. |

**Rule of thumb** when UX decisions conflict: optimise for P1 Student. Everyone else rides on the same pages without blocking students.

## 3. Functional scope — v1 (locked)

Three features ship in v1. Each maps 1:1 to a public Campo flow (see [`campo-public-surface.md` §2](campo-public-surface.md)).

### F1 — Course search ★
Maps to `searchCourseNonStaff-flow`. Facets: **semester, subject, language, instructor, organisational unit, room, weekday, time-window**. All facets combinable, results updated instantly (client-side, no server round-trip). Every result has an "Open in Campo" deep-link via `?_flowId=detailView-flow&unitId=…&periodId=…`.

### F2 — Today's events / day view ★
Maps to `showEventsAndExaminationsOnDate-flow`. Date picker plus a list of all events on campus on that day, filterable by building/lecturer/type. Back/forward date arrows. Semester-bounded.

### F3 — Room finder ★
Maps to `searchRoomDetail-flow`. "Find a free room with ≥N seats on day D between T1 and T2, optionally filtered by building or equipment." Equipment filter free-text (Campo's `Ausstattung` column is free-text in the source data too).

### F10 — Onboarding quiz + saved profile ★ **(new, session 0003)**
First-visit flow tailors the UI to the user without requiring a login:

1. **Role**: Student / Lecturer / Staff / Guest.
2. If Student: **Abschluss**, **Fach**, **Prüfungsordnungsversion**, **current semester #**.
3. If Lecturer/Staff: **Organisationseinheit**, **role** (teaching / admin / both).
4. Confirmation screen; answers stored in `localStorage` *and* encoded in URL-hash (`#profile=<base64>`).

Tailored home:
- **Students**: their program's current-semester courses first; optional "jump to semester N".
- **Lecturers/Staff**: their own org unit's events + rooms + colleagues' schedules first.

A always-visible **"Show me everything"** link bypasses the tailoring. Every entity has an **"Open in Campo"** deep-link.

### Deferred (not v1, explicit backlog)

| ID | Feature | Reason to defer |
|---|---|---|
| F4 | Room schedule (week view per room) | Subsumed by F3 "free-room" search for v1; add if users request. |
| F5 | Module catalog browser (Abschluss/Fach/Vertiefung filter) | Overlap with F1+F10 when student-program is known. |
| F6 | Study-program plan ("semester 3 of B.Sc. Informatik") | F10's saved profile does 80% of this; full reconstruction is v2. |
| F7 | Lecturer schedule lookup | F1 with "Dozent/-in" facet does most of this. |
| F8 | Special-event search | Low-traffic, add if demanded. |
| F9 | Catalog tree browser | F1 covers search; tree is a v2 add for discovery. |

## 4. Non-functional requirements

- **NFR-1 (Hosting)** Pure static site on GitHub Pages. No server at runtime. Data comes from bundled JSON snapshots.
- **NFR-2 (Freshness)** Weekly scrape via GitHub Actions cron. Each run writes `data/*.json` *and* cuts a GitHub **Release** tagged `snapshot-YYYY-Www` with the JSON as release assets.
- **NFR-3 (Shareability)** Every filter state has a URL (hash-based). Every course / room / day view has a stable permalink. Onboarding profile is URL-hash shareable.
- **NFR-4 (Performance)** First contentful paint < 1 s on a cold cache on standard broadband. Search results < 200 ms client-side on snapshots. Initial JS budget ≤ 80 KB gz (FlexSearch ~30 KB + app ~50 KB).
- **NFR-5 (Language)** **English primary, German fallback**. All UI strings and labels exist in both; string file is EN-authoritative, DE from Campo source where possible. Language toggle in the header; default inferred from `Accept-Language`.
- **NFR-6 (Accessibility)** WCAG 2.1 AA: keyboard navigation, screen-reader labels, colour contrast AA, focus ring visible.
- **NFR-7 (Privacy & feedback)** **Consent-light telemetry strategy:**
  - **T1 — Feedback button**: prominent "💡 Send feedback" link that opens a pre-filled GitHub Issue with the user's current route, filter state, and localStorage profile (without any PII). Zero tracking.
  - **T2 — Anonymous aggregate analytics**: cookieless, GDPR-clean analytics ([GoatCounter](https://www.goatcounter.com/) or [Plausible](https://plausible.io/) — TBD). Collects only: visited routes, quiz-answer bucket (role + Fach only), referrer. No IPs stored, no cross-site identifiers. Visible privacy note + opt-out link in footer.
  - **No cookies, no local accounts, no server-side session.** The onboarding profile lives in `localStorage` on the user's device only.
- **NFR-8 (Reproducibility)** Scraper and snapshot pipeline live in-repo; anyone can `python scraper/scrape.py --period 589` and get the same JSON.
- **NFR-9 (Embeddability)** UI ships as **Web Components** (custom elements with Shadow DOM). Drop `<ifcampoknew-app></ifcampoknew-app>` (or `<ifcampoknew-search>` / `<ifcampoknew-day>` / `<ifcampoknew-rooms>`) into any HTML page — including a WordPress shortcode block — and it boots self-contained, with its own CSS isolated from the host.
- **NFR-10 (Archival)** Each completed academic year is snapshotted into `archive/{year-slug}/` as a full copy of the site (HTML + JS + data JSON) at that point in time. GitHub Pages serves these alongside the live site.
- **NFR-11 (Licensing)** MIT. Code only — the Campo data itself is FAU's and stays subject to FAU's terms.

## 5. Architecture (locked)

```
┌────────────────────────┐        ┌──────────────────┐
│ scraper/  (Python)     │ ─────▶ │ data/*.json      │
│  requests + lxml       │        │  + releases      │
└────────────────────────┘        └──────────────────┘
         ▲                                 │
         │                                 ▼
   GitHub Actions cron               ┌──────────────────────────────┐
    (weekly, Monday 03:00 UTC)       │ site/  — Vite build          │
                                     │   Web Components (vanilla JS)│
                                     │   FlexSearch client index    │
                                     └──────────────────────────────┘
                                                 │
                                                 ▼
                                     ┌──────────────────────────────┐
                                     │ GitHub Pages                 │
                                     │  /               live v1     │
                                     │  /archive/{year-slug}/ older │
                                     └──────────────────────────────┘
```

### Repository layout (planned)

```
IfCampoKnew/
├── scraper/
│   ├── scrape.py             # entry point: --period 589 --out ../data
│   ├── parse_detail.py
│   ├── parse_tree.py
│   ├── schema.py             # dataclasses → JSON schema
│   ├── requirements.txt
│   └── tests/
├── data/                     # committed JSON snapshots
│   ├── 589.json              # SoSe 2026 (current)
│   ├── 589-tree.json
│   ├── 590.json              # WiSe 2026/27 (next)
│   └── 590-tree.json
├── site/
│   ├── index.html
│   ├── src/
│   │   ├── main.ts
│   │   ├── components/
│   │   │   ├── ifcampoknew-app.ts        # <ifcampoknew-app>
│   │   │   ├── ifcampoknew-search.ts     # F1
│   │   │   ├── ifcampoknew-day.ts        # F2
│   │   │   ├── ifcampoknew-rooms.ts      # F3
│   │   │   └── ifcampoknew-onboard.ts    # F10
│   │   ├── i18n/
│   │   │   ├── en.json
│   │   │   └── de.json
│   │   └── styles.css
│   ├── public/
│   └── vite.config.ts         # library mode → single JS + CSS bundle
├── archive/                   # prior-year snapshots (full site copies)
│   └── ws-2024-25/
├── docs/
│   ├── campo-public-surface.md
│   └── requirements.md
├── .github/workflows/
│   ├── scrape-weekly.yml      # cron → commit + Release
│   └── pages-deploy.yml       # build + deploy to Pages on main
├── devlog.md
├── README.md
├── LICENSE
└── .gitignore
```

### Data model sketch

```ts
// Scraper output, also the client-side runtime type
type Snapshot = {
  periodId: number;            // e.g. 589
  periodName: string;           // "Sommersemester 2026"
  scrapedAt: string;            // ISO 8601
  tree: CatalogNode[];          // nested tree from showCourseCatalog path=…
  courses: Course[];            // from detailView-flow?unitId=…
  rooms: Room[];                // from searchRoomDetail-flow
  orgUnits: OrgUnit[];
};

type Course = {
  unitId: number;
  titleStable: string;
  titleSemester?: string;
  shortText?: string;
  type: string;                 // Vorlesung/Seminar/Übung/…
  ects?: number;
  language?: string;
  orgUnitId?: number;
  instructorsResp: string[];
  instructorsExec: string[];
  catalogPaths: string[];       // "17593|17598|…"
  dates: Date[];                // parallel groups flattened
  permalink: string;
};
```

## 6. Out of scope (v1)

- Anything requiring a Campo login (grades, registrations, enrolments, personal schedule, exams).
- Write-back to Campo.
- Authentication against FAU IdM / Shibboleth.
- Server-side sessions, user accounts, cross-device sync.
- Deferred features F4–F9 (see §3).
- Native mobile apps (PWA is reachable in v1 but not prioritised).

## 7. Decisions log

| Date | Decision | Rationale |
|------|----------|-----------|
| 2026-04-24 | **License: MIT.** | Simple, permissive, compatible with any future FAU-hosted deployment. Code-only scope; Campo data remains FAU's. |
| 2026-04-24 | **v1 scope = F1 + F2 + F3 + F10.** | Covers the student's "find a course", the universal "what's on today", the lecturer pain "where do I teach", and the personalisation that makes the UI feel usable on first contact. |
| 2026-04-24 | **Primary persona = P1 Student.** | Biggest cohort, loudest Campo pain. Lecturers ride on the same pages without blocking. |
| 2026-04-24 | **Data scope = current + next semester, all faculties.** | Keeps scrape size realistic (~few thousand courses) while showing forward planning. Historical data stays in Campo itself. |
| 2026-04-24 | **Versioning = subfolder archive (`/archive/{year-slug}/`) per completed academic year.** | Preserves UI+data together. GitHub Pages serves it at no extra cost. |
| 2026-04-24 | **Scrape cadence = weekly via GitHub Actions; every run = a GitHub Release.** | Low load on Campo, explicit version per snapshot, Release API gives programmatic access to history. |
| 2026-04-24 | **Language = EN primary, DE fallback.** | Serves international students first; DE labels come from Campo data for free. |
| 2026-04-24 | **UI = Vanilla JS + Vite, packaged as Web Components (custom elements, Shadow DOM).** | Zero framework weight, clean WordPress embeddability, smallest viable attack surface. |
| 2026-04-24 | **Scraper = Python (`requests` + `lxml` + `pydantic`-ish dataclasses).** | Matches FAU-scientist tooling culture; best HTML parsing libraries. |
| 2026-04-24 | **Client search = FlexSearch.** | 30 KB gz, facets + boosting; right fit for ≤10 k courses. |
| 2026-04-24 | **Privacy posture = T1 (GitHub-issue feedback) + T2 (cookieless aggregate analytics — Plausible or GoatCounter).** | Keeps privacy story clean while still giving us signal to improve the UI. Final analytics vendor pinned before first deploy. |

## 8. Open items (to decide before first deploy)

- **O1** — Pick analytics vendor: Plausible vs GoatCounter. (Both free for small OSS projects; difference is mostly UI preference.)
- **O2** — Confirm WordPress target page (which FAU WP instance will embed the Web Component?) — affects CSP headers and the final bundle loading snippet.
- **O3** — Decide naming: `<ifcampoknew-…>` vs `<campo-…>` custom-element prefix.
- **O4** — Cron day-of-week and time (proposal: Mondays 03:00 UTC = 04:00/05:00 CE(S)T, off-peak for Campo).
- **O5** — Determine the `periodId` for WiSe 2026/27 (not yet known — first weekly scrape will discover it by walking the semester dropdown).
- **O6** — Sketch the F10 quiz flow visually (wireframe) before coding.

## 9. Next session — implementation start

Proposal for Entry 0004:

1. Bootstrap the repo skeleton: `scraper/`, `site/`, `.github/workflows/`.
2. Write the scraper's first pass: catalog-tree walk for `periodId=589`, extract all `unitId`s. No course-detail fetch yet.
3. Smoke-test against live Campo with a polite rate limit (e.g. 1 req/s).
4. Output a first `data/589-tree.json`.

*Implementation only starts after alignment on §8 open items where they block day-one work (O3, O4, O6 probably yes).*
