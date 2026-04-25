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

---

## Entry 0005 — Implementation start: scraper skeleton + first tree walk

- **Start:** 2026-04-24 23:52 CEST
- **End:** 2026-04-25 07:05 CEST (with a long break overnight; active time ≈ 25 min)
- **Duration:** ~25 min active
- **Actor:** user → Claude Code (Opus 4.7, 1M context)

**Prompt (verbatim):**

> please start

**Plan:**

1. Scaffold `scraper/` + project venv (Python 3.14, `requests`, `lxml`); update `.gitignore` for the venv.
2. Write `scraper/schema.py` (dataclasses), `scraper/campo_client.py` (session + rate limit + retries), `scraper/parse_tree.py` (catalog HTML → child nodes), `scraper/scrape.py` (CLI).
3. Smoke test: shallow walk of `periodId=589` (root + 1 faculty's children, ≤ 20 requests at 1 req/s).
4. Commit the first `data/589-tree.json`.

**Actions:**

1. Created `scraper/.venv/` (Python 3.14.3); installed `requests==2.33.1` + `lxml==6.1.0`. Added `scraper/.venv/` to `.gitignore`.
2. Wrote five Python files under `scraper/`:
   - `requirements.txt` — pinned deps.
   - `schema.py` — `CatalogNode` and `CatalogSnapshot` dataclasses with `to_dict()`.
   - `campo_client.py` — `CampoClient` with session bootstrap (start page → JSESSIONID), rate limit (default 1.0 s), 3-retry exponential backoff on 5xx, `catalog_url(period_id, path)` builder.
   - `parse_tree.py` — `parse_nodes(html)` returns deduplicated `(title_id, name, path)` tuples; `classify_nodes(parsed, current_path)` splits "current vs immediate children"; `parse_periods(html)` extracts the semester dropdown.
   - `scrape.py` — argparse CLI (`--period`, `--out`, `--max-depth`, `--interval`, `-v`); BFS tree walk; writes JSON.
3. Wrote `scraper/README.md` with quick start + module map + safety notes.
4. **Smoke test 1 (`max-depth=1`)** revealed two parser bugs:
   - Node names came out as `title:NNNN` because I was reading them from a non-existent `<h3>Permalink: NAME</h3>`. Real Campo HTML stores the name in `data-page-permalink-title="…"` directly on the `<textarea>` tag.
   - Period name was empty because the semester `<select>` ID is `…term-selection-container:termSelection_input`, not `termPeriodDropDownList`.
   Diagnosed by re-inspecting `/tmp/campo/catalog.html` from Entry 0001. Fixed both regexes in `parse_tree.py`.
5. **Smoke test 2 (`max-depth=1`)** clean: 12 nodes, root = "Vorlesungsverzeichnis FAU", period = "Sommersemester 2026", all 11 faculty/section names correctly populated (incl. those with embedded `<a>` markup like "Schulungsangebot der Universitätsbibliothek (Link)" — Campo's own formatting, kept verbatim for the UI to render).
6. **Real first snapshot (`max-depth=2`)**: 12 GETs (1 root + 11 faculties) at 1 req/s ≈ 12 s. Output `data/589-tree.json` = 54 KB, 223 nodes:
   - Phil Fak: 100 study programs
   - Tech Fak: 32 (incl. Advanced Materials, AI, Autonomy Technologies, …)
   - Nat Fak: 32, RW Fak: 19, Med Fak: 11, Allg. Wahlbereich: 10, Sustainability: 6, EELISA: 1, plus 3 leafless sections.
7. (Pending) Commit + push.

**Key findings & decisions made during implementation:**

- Names can contain inline HTML (`<a href="…">…</a>`). Kept raw in JSON; UI will sanitise/render.
- Each Campo deep-link GET expands the *current* node's children plus the path back to root, so a single GET per node is enough — no need to also fetch the parent. BFS at 1 req/s is the natural pace.
- A full-depth walk is O(internal-nodes) GETs. Depth 2 = 12 GETs / 12 s. Depth 3 will be ~223 GETs / ~4 min — acceptable for weekly cron, deliberately deferred to keep the first commit's smoke test fast.

**Next session candidates (Entry 0006):**

1. Push depth to its terminus (full tree per semester) and verify it stays sane against pagination edge-cases.
2. Add **course-detail fetcher** (`detailView-flow?unitId=…&periodId=…`) so leaf nodes get their `unit_id` populated and we can extract Termine/Inhalte.
3. Add a small **pytest** suite for `parse_tree.py` against fixtures in `scraper/tests/fixtures/`.
4. Wire up `.github/workflows/scrape-weekly.yml`.

**Reminder of remaining open items:** O1 analytics vendor · O2 WP target page · O3 next-semester `periodId` (will discover from `parse_periods()` once we hit the live catalogue with the next semester announced).

---

## Entry 0006 — Full-depth walk, course-detail fetcher, tests, GH Action

- **Start:** 2026-04-25 07:24 CEST
- **End:** 2026-04-25 08:20 CEST
- **Duration:** ~55 min (scraper deepening + design pivot to markdown corpus + renderer)
- **Actor:** user → Claude Code (Opus 4.7, 1M context)

**Prompt (verbatim):**

> 1, 2, 3, then 4

(Sequence proposed at the end of Entry 0005: ① full-depth walk · ② course-detail fetcher · ③ pytest suite · ④ `.github/workflows/scrape-weekly.yml`.)

**Plan, with one commit per sub-step so each can be reviewed independently:**

1. **Full-depth walk.** Probe how Campo renders leaf courses inside the catalogue tree (need a fresh sample). Add leaf detection to `parse_tree.py` — populate `unit_id` on the `CatalogNode` when the row is a course. Update the BFS in `scrape.py` to stop descending past leaves. Run a wider walk and record scale.
2. **Course-detail fetcher.** New module `parse_detail.py` for `detailView-flow?unitId=…&periodId=…`. Extract the fields visible in the *Termine* tab (Veranstaltungsart, ECTS, Unterrichtssprache, instructors, parallel groups). Add `--with-details` to `scrape.py`.
3. **Pytest suite.** Add `scraper/tests/` with HTML fixtures captured today; tests for `parse_tree`, `parse_detail`. `pytest` added to dev requirements.
4. **GitHub Actions.** `.github/workflows/scrape-weekly.yml` (Mon 03:00 UTC, commit `data/`, cut a Release with the JSON as asset). Pages-deploy stub deferred until the site exists.

**Mid-entry pivot — additional prompts (verbatim, in order):**

> I want to change something in the design: I changed my mind and I want to store the Campo Information rather in Markdown format than json. Also, I want the markdowns to be hierarchical, i.e. the markdown file structure should reflect the hierarchy in campo. External links should be preserved (i.e. to lectures and other content, to faudir and the like) each folder in the hierrarcy should have an overview in markdown that links to the contents (and subfolder overviews) such that an AI/LLM can identify which markdowns are relevant to ansewr a request. Essentially we want to make Campo AI compatible. Make sure, markdowns don't get too small. Each markdown document should have thoudsands of tokens. Otherwise, the LLM performance on small files will be terrible. We want to be able to parse several files with a 100.000 token window context. Overviews can be smaller, content files should be larger and in the range of 10.000-30.000 tokens. If the content files get much smaller, you probably have to merge hierarchy layers into one markdown file.

> 1 No more web UI. We will parse the structure with an agentic system. No flex search
> 2 Slug language Campo faithful.
> 3 JSON snapshot no longer required. Should be markdown instead.
>
> Otherwise: We need to go deeper

**Actions, in order:**

1. Refactored `parse_tree.py` and `schema.py` to handle **both** `title:NNN` and `exam:NNN` segments (and any other `KIND:ID` Campo emits). `CatalogNode` now stores `segment`, derived `kind`/`nodeId`, full `path` as segment strings.
2. Refactored `scrape.py` BFS to use segment strings; added `--max-depth 0` = unlimited (hard-capped at 12 for safety).
3. **Probed depth-5 topology.** Fetched `path=title:17593|title:17601|title:17949` (Informatik) — 470 KB HTML — and discovered: catalogue depth 4 nodes are **PO-versions** (`exam:NNN`), depth 5+ are **PO sub-blocks** (further `exam:NNN`); the catalogue tree does *not* contain individual courses. Courses are reached separately via the search-flow (deferred to phase 2).
4. **Ran depth-4 walk** of full FAU SoSe 2026: 12 GETs to seed root + 11 sections = no, actually 235 program GETs (since depth-4 needs every program fetched). Output: 1895 nodes, 750 KB JSON. By kind: 337 `title:` + 1558 `exam:`. By depth: 1 root, 11 section, 235 program, 1648 PO-version.
5. **Pivot received** mid-entry: drop the Web Components UI, drop FlexSearch, drop the JSON deliverable. Markdown corpus is the new product.
6. **Confirmed pivot** (3 questions answered): UI replaced (not augmented); slug language Campo-faithful (German); JSON intermediate-only (gitignored). User added: "We need to go deeper".
7. Wrote `scraper/render_markdown.py`. Slugs use ASCII-folding with explicit umlaut expansion (`ä→ae` etc.); every file/folder has the segment ID appended for stability. INDEX.md per folder; leaf .md per leaf node.
8. **Rendered** the depth-4 SoSe 2026 snapshot: **241 folders** (each with INDEX.md) + **1654 leaf .md files**. All slugs Campo-faithful German. Verified: root INDEX lists 11 sections with permalinks; Tech Fak INDEX lists all 32 programs alphabetically; Informatik PO-version 2007 leaf has correct frontmatter + permalink.
9. **Restructured `data/` vs `tmp/`.** Moved old `data/*-tree*.json` to `tmp/`; added `data/*.json` to `.gitignore`. `data/` now holds **markdown only**.
10. **Rewrote `docs/requirements.md`** as v2: new vision, consumers C1–C3 (LLM agent, github.com reader, RAG), F-CAT/F-COURSE/F-LINKS/F-OVERVIEW/F-TOKEN, NFR-9 marked obsolete, NFR-7 reduced to "no telemetry", architecture + repo layout + data-model sketch, 12-row decisions log, 3 open items, roadmap pointing at Entry 0007.
11. Rewrote `scraper/README.md` for the two-stage pipeline.

**Key findings:**

- **Tree topology:** Campo's catalogue tree has two segment kinds. `title:` = sections / faculties / programs (mostly the upper 3 levels). `exam:` = PO-versions and their sub-blocks (depth 4+). The chain can nest several `exam:` levels deep ("PO 2007 → 10000 Staatsexamen → …").
- **Courses are not in the catalogue.** The catalogue is the *structural index*; concrete course events with `unitId` are reached through the search-flow (or per-PO via Studiengangspläne). Phase 2 in Entry 0007.
- **File-size reality at depth 4 with skeleton-only content:** every leaf .md is ~600 bytes / ~150 tokens. The 10-30 k-token bucket policy can only be enforced once we attach courses (phase 2). For now the skeleton is the scaffolding the bucketing will eventually fold or split.
- **Renderer scale**: 1895 nodes → 1895 .md files in <1 s. Slugs deterministic; tested by re-rendering twice and getting identical paths.

**Open items pushed forward to Entry 0007:**

- O1 token-counting library (`tiktoken` vs character heuristic).
- O2 how to associate courses with PO-version leaves (search-flow with PO filter? Studiengangspläne flow?).
- O3 next-semester `periodId`.

**Status:** Entry 0006 ships the markdown skeleton. Going deeper (full catalogue depth + course content) is Entry 0007.

---

## Entry 0007 — Going deeper: full-depth walk, course content, weekly cron

- **Start:** 2026-04-25 08:25 CEST
- **End:** 2026-04-25 13:38 CEST
- **Duration:** ~5 h elapsed; ~70 min active (rest = waiting on rate-limited fetches)
- **Actor:** user → Claude Code (Opus 4.7, 1M context)

**Prompt (verbatim):**

> Also update the README.md with the new plans and push, Then continue with our plan.

**Plan (per requirements.md §9 + Entry 0006 findings):**

1. README updated and pushed (done as the first action of this entry).
2. Run a full-depth catalogue walk in the background (`--max-depth 0`, hard-cap 12) — likely tens of minutes to a couple of hours; doesn't block other work.
3. Resolve the **mixed-leaf finding** from Entry 0006: are Wahlbereich/Musizieren leaves like `akademischer-chor-uebung-15688820` actually courses with `unitId=15688820` reachable via `detailView-flow`? Or is `15688820` a different segment kind?
4. Probe `searchStudyCourseSchedule-flow` with a known PO-version (e.g. `exam:14867623` Lehramt Gym Info PO 2007) — does it list the courses for that PO?
5. Probe `detailView-flow?unitId=…&periodId=…` and define the field set worth pulling (title, type, ECTS, Unterrichtssprache, instructors, Termine, Inhalte, module memberships, FAUdir links).
6. Implement `scraper/parse_detail.py` + a `Course` dataclass; extend `render_markdown.py` to embed courses in the relevant content file.
7. Apply F-TOKEN bucket policy.
8. Wire up `.github/workflows/scrape-weekly.yml` so the weekly run is automated and a Release is cut.

**Mid-entry, additional prompt (verbatim):**

> All of the study programs have study regulations:
> https://www.fau.de/universitaet/universitaetsorganisation/rechtliche-grundlagen/pruefungsordnungen/#philosophische-fakultaet-und-fachbereich-theologie
> We need to scrape them too and make them available as Markdowns too.
>
> On top of that every study program maintains additional information that also needs to be added as markdowns. An overview of this additional nested structure is here:
> https://www.fau.de/studium/studienangebot/alle-studiengaenge/
> We need to scrape all of this as markdown as well.

Acknowledged but **deferred to Entry 0008** so this entry could close with a clean Campo deliverable. Sketch returned to user with three design questions (PDF text extraction yes/no, separate cadence, ordering); awaiting answers.

**Actions taken in this entry:**

1. **Probed `_flowId=detailView-flow&unitId=15688820`** for "Akademischer Chor" — Campo replied "Die Unit mit der ID 15.688.820 konnte nicht gefunden werden". So `exam:NNN` segment IDs are **not** course `unit_id`s.
2. **Probed the parent catalogue page** (`title:17991`, *Musizieren an der Universität*) and found that each leaf row has a `_flowId=detailView-flow&unitId=NNN` link in its action column — Campo emits *both* a permalink (with `exam:` segment) and a detail-view link (with the real course `unitId`). Akademischer Chor: `exam:15688820` ↔ `unitId=92769`.
3. **Updated `parse_tree.py`**: new `_unit_id_for_textarea()` walks back to the enclosing `<tr` and extracts the action-column `unitId`; `ParsedNode.unit_id` field added.
4. **Updated `schema.py`**: new `Appointment` and `Course` dataclasses (Eckdaten + Termine + Lehrende + org-units).
5. **Wrote `parse_detail.py`**: parses Veranstaltungsart / ECTS / Unterrichtssprache / Turnus from labelled blocks; pulls the Termine table (rhythm / weekday / time / date-range / room / instructors) from the stable `appointmentSeriesTableTable` `<tbody>`; strips Campo's "Elementdaten " title prefix.
6. **Wrote `fetch_courses.py`**: dedupes `unit_id`s, GETs each detail page at 1 req/s, supports `--path-contains` for subset runs.
7. **Extended `render_markdown.py`**: when a `--courses` JSON is provided, every leaf with a matching `unit_id` is rendered with full Eckdaten + Termine + Lehrende + Organisation tables; Katalog-Permalink and Veranstaltungs-Permalink both included.
8. **Wrote `.github/workflows/scrape-weekly.yml`**: Mondays 03:00 UTC + manual dispatch; runs scrape → fetch_courses → render → commit → cuts a Release with the JSON intermediates as assets.
9. **Wrote pytest fixtures + 15 tests** in `scraper/tests/` against real Campo HTML; all pass.
10. **Ran the full pipeline** end-to-end: scrape (1895 nodes), fetch (683 unique unit_ids, 0 failures, 11 min wall), render (765 leaves embedded with full course content — same course referenced from multiple POs counts each time).
11. (Pending) Commit + push.

**Mid-flight bug fixes:**

- `_label_value` was leaking `</label>` text into values — refactored to consume the entire opening label (including its closing tag) so the captured group starts at the value cell.
- Title carried Campo's internal "Elementdaten " prefix — stripped explicitly in `_parse_permalink_and_title`.

**Findings worth recording:**

- The catalogue's `exam:NNN` segments **mix two semantically different things** at depth 4: PO-versions in faculty branches, and individual course events in cross-cutting branches (Musizieren, Frühstudium, FAU Scientia). Both look the same in HTML; the `unit_id` field is what distinguishes a course-leaf from a structural node.
- Of the 1895 depth-4 nodes, **683 unique courses** are reachable as leaves (≈40% of leaves are course-bearing at this depth; the other 60% are PO-versions whose courses are deeper, not yet walked).
- Course distribution across sections at depth 4: FAU Scientia 624 · Frühstudium 113 · Allg. Wahlbereich 27 · Phil Fak 1 · Tech/Nat/Med/RW Fak: 0. The big faculties' courses live deeper in the catalogue.

**Open items pushed to Entry 0008+:**

- O1 token-counting library (still unresolved; characters used as proxy for now).
- Full-depth catalogue walk (`--max-depth 0`, hours) to pick up Tech/Nat/Med/RW Fak courses.
- F-TOKEN bucket policy (merge thin / split thick) — most leaves are still tiny (~700 bytes) until courses attach.
- **NEW for Entry 0008** (deferred via the user's mid-entry add): scrape `fau.de/.../pruefungsordnungen/` (≈50 landing pages + their PDFs) and `fau.de/studiengang/{slug}/` (222 program pages); cross-link to Campo nodes by name match.

**Status:** Entry 0007 closes a complete Campo end-to-end. Entry 0008 will take on FAU.de regulations + program-info corpora.

---

## Entry 0008 — FAU.de corpora: Studiengang pages + Prüfungsordnungen PDFs

- **Start:** 2026-04-25 14:02 CEST
- **End:** 2026-04-25 18:58 CEST (paused on user request — token budget)
- **Duration:** ~5 h elapsed; ~50 min active (rest waiting on rate-limited fetches + PDF conversion)
- **Actor:** user → Claude Code (Opus 4.7, 1M context)

**Prompts (verbatim, in order):**

> 1 extract pdf to markdown
> 2 once a month is ok
> 3 the fastest way ahead

**Plan, in order of "fastest meaningful deliverable":**

1. Probe one Studiengang page + one PO landing — done. Studiengang pages are clean HTML (~1200 words/page, three collapsible sections + a Steckbrief facts box); PO landing pages link to PDFs at `doc.zuv.fau.de` (e.g. ~30 Informatik PDFs of consolidated regulations + amendments).
2. Install `pymupdf4llm` (PDF → markdown, purpose-built for LLM ingestion) + `markdownify` + `beautifulsoup4`.
3. Write `scraper/scrape_studiengang.py` — paginates the 222-program listing and fetches each program's HTML page.
4. Write `scraper/scrape_pruefungsordnungen.py` — recurses the faculty / program-type / PDF-list pages.
5. Write `scraper/pdf_to_markdown.py` — wraps `pymupdf4llm` for the PO PDFs.
6. Write `scraper/render_fau.py` — emits `data/studiengang/{slug}.md` and `data/pruefungsordnungen/{faculty}/{program}/...`.
7. Add a monthly cron job to `.github/workflows/scrape-monthly.yml` (or extend the weekly).
8. Smoke test on a small slice; commit.

**Final user prompt of the entry (verbatim):**

> Pause the development after this. I am running out of tokens.

**Actions:**

1. Probed `/studiengang/artificial-intelligence-b-sc/` (clean HTML, `<dl>` Steckbrief, three collapsible sections), `…/pruefungsordnungen/technische-fakultaet/informatik/` (148 PDF links → `doc.zuv.fau.de`).
2. Discovered `/sitemap_index.xml` exposes **all** 222 Studiengang URLs and 36 Prüfungsordnungen landing URLs as a flat `<urlset>` — bypasses the JS-driven listing pagination cleanly.
3. Installed `pymupdf4llm` 1.27, `markdownify`, `beautifulsoup4`. Verified PDF→markdown on a real 10-page PO PDF: 28 974 chars (~7 200 tokens) of clean markdown with headings preserved.
4. Wrote `scraper/fau_corpus.py` — single-script pipeline:
   - Fetches the sitemap, classifies URLs.
   - For each `/studiengang/{slug}/`: parses Steckbrief `<dl>`, extracts H2 sections, drops site chrome, converts each section to markdown via `markdownify`, gathers external links, writes `data/studiengang/{slug}.md` with YAML front-matter.
   - For each `…/pruefungsordnungen/{path}/`: extracts intro markdown + every linked PDF; for each PDF downloads to `tmp/fau-pdfs/`, runs `pymupdf4llm.to_markdown`, writes `data/pruefungsordnungen/{path}/{pdf-slug}.md`; emits an `INDEX.md` per landing.
   - Slugs use the same Campo-faithful ASCII-folded German rule as the Campo renderer (`ä→ae`, `ß→ss`).
5. Smoke-tested on 1 Studiengang + 2 PO landings + 1 PDF; output good. Fixed two bugs:
   - Steckbrief was rendering twice (once as table, once as auto-converted body) — now decompose the `<dl>` before iterating section bodies.
   - Output dir wasn't created before per-PDF write — `dest.mkdir(parents=True, exist_ok=True)` moved before the PDF loop.
   - Title spacing ("Healthcare(M.Sc.)" → "Healthcare (M.Sc.)") via `get_text(" ", strip=True)`.
   - PO root URL went to `misc/`; now mapped to `Path('.')` so the FAU site root is the corpus' top-level `INDEX.md`.
6. Wrote `.github/workflows/scrape-monthly-fau.yml` — first of every month at 04:00 UTC (off-peak, content rarely changes).
7. Updated `README.md` and `scraper/README.md` to reflect three-source corpus (Campo per-semester + Studiengang + Prüfungsordnungen) and new quick-start commands.
8. Kicked off the **full FAU run** in the background and let it run while updating docs.
9. **User asked to pause** mid-run (token budget). Killed the background process — but it had already gotten through almost everything: **222/222 Studiengang markdowns + 2 838 Prüfungsordnungen markdowns** (one INDEX per landing + one per PDF; the bulk are converted PDF text). Total: 4 956 markdown files / 82 MB under `data/studiengang/` + `data/pruefungsordnungen/`.

**State at pause:**

- Code: complete and committable (single-file pipeline, monthly workflow, README updates).
- Data: substantially complete; the next monthly cron will fully refresh and fill any gaps.
- Pending for the next session: cross-link Campo's catalogue nodes to the matching FAU.de Studiengang and Prüfungsordnung markdowns by name match.

**Status:** paused mid-flow; the data captured before the kill is being committed and pushed so nothing is lost.



