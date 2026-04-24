# IfCampoKnew — Development Log

Chronological record of the prompts, decisions, and actions that produced this project. Each entry preserves the user's verbatim prompt (indented in a block quote), the time window, and a short summary of what was done.

Timestamps are in the local timezone of the machine where Claude Code ran (Europe/Berlin, CEST/CET).

---

## Entry 0001 — Project kickoff, Campo public-surface analysis

- **Start:** 2026-04-24 21:38 CEST
- **End:** 2026-04-24 21:49 CEST
- **Duration:** ~10 min
- **Actor:** user → Claude Code (Opus 4.7, 1M context)

**Prompt (verbatim):**

> Our Website "Campo" is more than slightly problematic. We never find anything that we are looking for. I would like to make an analysis of all information that can be queried without logging into the system:
>
> https://www.campo.fau.de/qisserver/pages/cs/sys/portal/hisinoneStartPage.faces
>
> We will start with the analysis. Then we will build a java-script based version of Campo that offers all this information with a much more friendly user interface.
>
> We will host this on github:
> https://github.com/akmaier/IfCampoKnew
> The repo is already set up. Connect directly to this Repo and work on it.
>
> The name is a pun on "if Siemens knew what Siemens knows".
>
> Later, the website should run as GitHub Page as a Demo.
>
> We will need a requirement anaysis (like in the vibe coding book). The main users are students, lecturers, administrators and and other university people. We will work on the requirements once we know what is currently exposed to public by Campo.
>
> Document also all our interactions how we created this Campo Helper. Keep track of all interactions in a dev log that can be analysed later. Insert time stamps how long interactions were and keep book of all prompts in the log.

**Actions:**

1. Cloned https://github.com/akmaier/IfCampoKnew into the working directory (empty repo on `main`).
2. Initialised this dev log (`devlog.md`).
3. Fetched the Campo start page via `curl` with a cookie jar (WebFetch failed — Campo's JSF flow redirects exceed the 10-redirect limit).
4. Extracted all public `_flowId=*-flow` entry points from the start-page HTML — 10 distinct flows.
5. Fetched each of the 10 flows (~10 HTML files totalling ~2.8 MB) using the same cookie jar.
6. Parsed every page with a small Python helper to extract: headings, form fields with their human labels, select-option samples (up to 6 per dropdown), and table-header columns. This produced the raw material for the inventory.
7. Confirmed that the *Tagesaktuelle Veranstaltungen* flow serves **100 real events for today (2026-04-24)** on a single anonymous GET — making it the richest public data source.
8. Wrote [`docs/campo-public-surface.md`](docs/campo-public-surface.md): full public-surface inventory with per-flow filters, data fields, and architectural observations.
9. Wrote [`docs/requirements.md`](docs/requirements.md): skeleton requirements doc (personas, 9 functional candidates, 8 NFR drafts) — to be finalised in the next session.
10. Wrote [`README.md`](README.md) and [`.gitignore`](.gitignore).
11. (Pending) Local commit. **Not pushed** — awaiting user confirmation before the first push to `origin/main`.

**Key findings:**

- Campo is HIS eG HISinOne (JSF + Spring Web Flow). No JSON API; every read is a stateful flow.
- 10 public flows, covering course catalog/search, study-program plans, module descriptions/handbook search, detailed room search, room plans, today's events, special events, and lecturer-schedule lookup.
- No `robots.txt` published.
- Dropdown values alone enumerate 85+ degree types, 350+ subjects, 370+ room-use categories, 14+ campuses — a useful static reference by itself.
- A GitHub-Pages demo will need an offline scraper writing JSON snapshots into the repo (or a release artifact), since static hosting cannot drive the stateful JSF flow at runtime.

**Open questions for the next session** (full list in `docs/requirements.md` §3 and `docs/campo-public-surface.md` §7):

- Which of the 9 functional candidates are MVP?
- Stack: vanilla JS vs. Preact/Svelte? Scraper in Node vs. Python?
- DE-first, EN-first, or bilingual?

---

## Entry 0002 — Deeper analysis: run a real search, drill the catalog tree

- **Start:** 2026-04-24 22:00 CEST
- **End:** 2026-04-24 22:55 CEST
- **Duration:** ~55 min
- **Actor:** user → Claude Code (Opus 4.7, 1M context)

**Prompt (verbatim):**

> 2

(Shorthand for "option 2" offered at the end of Entry 0001 — i.e. *go deeper on analysis: actually run a search POST, or drill into the catalog tree*.)

**Plan:**

1. Start a fresh cookie-jar session; GET the course-search page.
2. Parse its JSF form state: `javax.faces.ViewState`, form action URL, all hidden inputs, and the generated name of the free-text "Suchbegriffe" field.
3. POST a real query and inspect the response.
4. Drill into the course-catalog tree: expand a faculty node and see what comes back.
5. If a result row has a detail link, follow it to see the course-detail page.
6. Document the mechanics (JSF partial responses? full HTML? AJAX behaviour?) in `docs/campo-public-surface.md` §8.

**Actions:**

1. GET startpage + search form in a fresh cookie jar; parsed the `genericSearchMask` form (15 hidden inputs incl. `authenticity_token`, `javax.faces.ViewState=e1s1`, `genericSearchMask_SUBMIT=1`; ~45 visible inputs).
2. Identified the `Suchbegriffe` free-text field by label-for mapping: `genericSearchMask:search_e4ff…:cm_exa_eventprocess_basic_data:fieldset:inputField_0_…:id1ad0…`.
3. First POST attempt **silently failed** — response was identical to the GET, same `e1s1` ViewState. Reason: stale session (reused cookie jar from Entry 0001 — 20+ min old). Debug trail included: diffing GET vs POST response (only `authenticity_token` rotated), checking field IDs (stable), checking session cookie (only one `JSESSIONID`, bound to `/qisserver`).
4. Restart in a **fresh session** (visit startpage → visit search form → POST) with all hidden inputs + MyFaces `SCROLL_TO_ANCHOR`/`DISABLE_AUTOSCROLL` extras + submit button name. POST succeeded: `e1s1` → `e1s2`, `<h2>Gefundene Veranstaltungen</h2>`, 2 hits for *Mustererkennung* (VL Prof. Maier, Praktikum Dr. Christlein).
5. Parsed result table — 9 columns per row, with Aktionen cells containing a plain `<a href>` to the course-detail deep-link `?_flowId=detailView-flow&unitId=86267&periodId=589`.
6. Fetched the detail page directly via the deep-link in a new flow (e2s1): 5 tabs visible (Termine / Inhalte / Vorlesungsverzeichnis / Module-Studiengänge / Dokumente), fields including ECTS=5.0, Unterrichtssprache, Verantwortliche/-r, plus the self-generated Perma-Link in a `<textarea>`.
7. Parsed the catalog permalink textareas — the catalog tree is deep-linkable via `&path=title:ROOT|title:CHILD|title:GRANDCHILD…`, which renders any sub-tree view in a fresh session with a single GET.
8. Verified the catalog deep-link by fetching `path=title:17593|title:17598` from a clean session — returned 222 KB HTML with 22 unique child paths and full H3 permalinks ("Sprachkenntnisse Latein", "Veranstaltungen aus der Philosophischen Fakultät", …).
9. Wrote `docs/campo-public-surface.md` §7a.1-7a.7: session recipe, POST recipe, result-table schema, deep-link patterns, course-detail tab list, absence of exports, and the resulting scraper architecture (catalog-walk via GETs, no POSTs needed for 95% of the data).
10. (Pending) Commit.

**Key findings:**

- **Deep-linking works.** Both `detailView-flow?unitId=…&periodId=…` and `showCourseCatalog-flow?periodId=…&path=title:…|title:…` render directly in a fresh session. This is the single biggest architectural unblocker — a scraper can walk the whole catalog with pure GETs.
- **Filtered search requires a full JSF+CSRF POST.** Recipe documented. But given deep-links, we can skip it entirely in the scraper and reproduce filtering client-side over the snapshot.
- **Session hygiene matters.** Must start from `hisinoneStartPage.faces`; cannot reuse a stale `JSESSIONID` across long gaps.
- **Course detail has 5 tabs**, incl. *Dokumente* (likely the hidden treasure of syllabi & slides) — requires tab-switch postback, left as a follow-up.
- **No iCal, no JSON, no PDF export** from the default views.

**Hypothesis for next session** (architecture is now clear):

1. Scraper is a Node or Python script that:
   - GETs the catalog root per semester, recursively walks via `path=`.
   - At each leaf, issues GETs to `detailView-flow?unitId=…&periodId=…`.
   - Writes `data/{periodId}/courses.json`, `tree.json`.
2. Site is vanilla JS + client-side filter/search over JSON. URL hash encodes filters.
3. GitHub Actions nightly cron re-runs the scraper and commits the snapshot.

**Status:** analysis now complete enough to start requirements.

---

## Entry 0003 — Requirements walk-through + MIT license

- **Start:** 2026-04-24 23:04 CEST
- **End:** 2026-04-24 23:30 CEST
- **Duration:** ~26 min
- **Actor:** user → Claude Code (Opus 4.7, 1M context)

**Prompts (verbatim, in order):**

> License is MIT. Walk me through the requiremens questions.

> Q1) F1 + F2 + F3
> Q2) P1
> Q3) A (historical can stay in Campo; Our Version will have updates, but only for each running semester, we keep backups of previous semesters (as old versions, Can github pages allow access to old versions?), all faculties please
> Q4) weekly scrape with github actions and update in version.
> Q5) EN is favored, DE as fallback
> Q6) I don't understand the question. Elaborate.

> Q3) C
> Q6a) W1
> Q4) ok
> Q6b) ok
>
> T1 + T2
>
> [+ new question about onboarding quiz / tailored UI per study program / feedback-data collection]

**Actions:**

1. Added [`LICENSE`](LICENSE) (MIT) and updated the README's license line.
2. Posed six requirements questions in the chat with rec + main tradeoff for each: Q1 MVP scope, Q2 primary persona, Q3 data scope + versioning, Q4 scrape cadence, Q5 language, Q6 tech stack (UI / scraper / index).
3. Clarified Q3's "C" choice (subfolder archive for completed academic years) and Q6a's W1 choice (Web Components for WordPress embeddability). Explained the three sub-questions of Q6 in plain terms after user requested elaboration.
4. User raised a **new requirement**: onboarding quiz tailoring the UI per study program / user type, with "show me everything" escape hatch, an "Open in Campo" fallback on every entity, and feedback-data collection to improve the UI over time.
5. Proposed three privacy postures for telemetry (T1 GH-issue feedback, T2 cookieless aggregate analytics, T3 self-hosted endpoint). User chose **T1 + T2**.
6. Rewrote [`docs/requirements.md`](docs/requirements.md) from "skeleton" to **v1-locked**: §3 scope (F1, F2, F3, **+ new F10 onboarding quiz**), §4 NFRs including **NFR-9 Web Components embeddability** and **NFR-10 subfolder archive**, §5 full architecture diagram + planned repo layout + data-model sketch, §7 decisions log with 11 rows, §8 six remaining open items (O1–O6), §9 proposed first implementation session.
7. (Pending) Commit LICENSE + README + requirements.md + this devlog entry as one coherent "requirements locked" commit.

**Final decisions (from Q&A):**

| # | Decision |
|---|---|
| License | **MIT** (`LICENSE` file, © Andreas Maier) |
| Scope v1 | **F1 course search + F2 today-view + F3 room finder + F10 onboarding quiz** |
| Primary persona | **P1 Student** |
| Data scope | **Current + next semester, all faculties.** Historical stays in Campo. |
| Versioning | **Subfolder archive** `/archive/{year-slug}/` per completed academic year |
| Scrape cadence | **Weekly** GitHub Actions cron → **GitHub Release** per run |
| Language | **EN primary, DE fallback** (both always present) |
| UI stack | **Vanilla JS + Vite**, packaged as **Web Components** (custom elements + Shadow DOM) for WordPress embeddability |
| Scraper | **Python** (`requests` + `lxml`) |
| Client search | **FlexSearch** |
| Privacy | **T1 (GitHub-issue feedback) + T2 (Plausible or GoatCounter, cookieless)** |

**Open items to resolve before first deploy:** O1 analytics vendor · O2 WP target page · O3 custom-element prefix · O4 cron slot · O5 next semester's `periodId` · O6 F10 wireframe.

**Proposed next session (Entry 0004):** repo skeleton + first scraper pass (catalog tree walk for `periodId=589`, polite rate limit, write `data/589-tree.json`). Implementation only starts after O3/O4/O6 are resolved.

---

## Entry 0004 — Resolve blocking open items (O3/O4/O6)

- **Start:** 2026-04-24 23:45 CEST
- **End:** 2026-04-24 23:48 CEST
- **Duration:** ~3 min
- **Actor:** user → Claude Code (Opus 4.7, 1M context)

**Prompt (verbatim):**

> Q3 <campo-search>
> Q4 OK
> Q6 F10 ok

(User answers map to open items **O3**, **O4**, **O6** from §8 of `docs/requirements.md`; the "Q" prefix is recycled from the earlier walk-through.)

**Actions:**

1. **O3 locked — custom-element prefix is `campo-`.** Updated `docs/requirements.md` NFR-9 and §5 repo layout to use `<campo-app>`, `<campo-search>`, `<campo-day>`, `<campo-rooms>`, `<campo-onboard>` (shorter than the `ifcampoknew-` alternative; still unambiguous because of Shadow DOM isolation).
2. **O4 locked — cron = Mondays 03:00 UTC** (= 04:00 CET / 05:00 CEST). Recorded in §5 architecture block and §7 decisions log.
3. **O6 locked — F10 wireframe added inline to §3.** Three ASCII screens: role pick → role-specific details (student / lecturer-staff / guest) → confirm. Student path accommodates PO-version uncertainty with a "latest / don't know" default. Guest path skips straight to confirm.
4. Removed O3/O4/O6 from §8 open items; they're now in §7 decisions log. Remaining open items (renumbered O1/O2/O3): analytics vendor, WP target page, next semester's `periodId`.
5. (Pending) Commit.

**Decisions added to §7 log:** custom-element prefix = `campo-`; cron = Mondays 03:00 UTC; F10 wireframe pinned.

**Unblocked** — the next session can start with implementation (repo skeleton + Python scraper's tree-walk pass).


