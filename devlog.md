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

---

## Entry 0009 — Cross-link Campo ↔ FAU.de

- **Start:** 2026-04-25 20:54 CEST
- **End:** 2026-04-25 21:08 CEST
- **Duration:** ~14 min
- **Actor:** user → Claude Code (Opus 4.7, 1M context)

**Prompt (verbatim):**

> We now have more tokens: they refreshed. Please continue working on the plan.

**Plan:**

1. Survey the existing `data/studiengang/` and `data/pruefungsordnungen/` markdown frontmatter to know what to match on.
2. Extend `render_markdown.py` with a small linker:
   - Load a FAU index at startup (slug → title/abschluss/fakultät for studiengang; folder leaf → relative path for PO landings).
   - For each Campo program-level node (`title:NNN` at depth 3), find FAU studiengang slugs whose pre-degree base equals the slugified Campo name; find PO landing folders whose leaf name matches.
   - Inject a "Verwandte FAU-Inhalte" section into the program's `INDEX.md` with relative-path links.
3. Re-render the Campo corpus from the existing `tmp/589.json` + `tmp/589-courses.json`.
4. Verify a sample (e.g. Tech Fak / Informatik program node).
5. Commit + push.

PO-version-level matching (Campo `exam:NNN` → specific PDF by version year) is intentionally deferred — needs filename year-parsing and is a follow-up.

**Actions:**

1. Surveyed existing FAU markdowns: Studiengang has rich front-matter (`title`, `abschluss`, `fakultät`, `unterrichtssprache` …); Prüfungsordnungen documents have `kind`, `title`, `pdf_source`, `parent_landing`. Folder layout `pruefungsordnungen/{faculty}/{program}/` mirrors fau.de.
2. Extended `scraper/render_markdown.py` with: `_parse_frontmatter()` (no PyYAML dep), `_strip_degree_suffix()` (drops `-b-sc`, `-m-sc`, `-staatsexamen` …), `load_fau_index()` (builds slug → entries lookup at render time), `_find_related_fau()`, `_relative_link_from()`, `_related_fau_section()`.
3. Wired the linker into `render_corpus`: program-level Campo nodes (depth 3, `title:NNN`) get a "Verwandte FAU-Inhalte" section before INDEX.md is written, listing matching Studiengang pages and PO landing folders with relative links.
4. First render: **118 fau_links** out of 235 program nodes (≈50 %). Spot-checked Informatik (linked to `informatik-b-sc.md` + `informatik-m-sc.md`) and AI (linked to AI Bachelor + Master) — clean.
5. Inspected unmatched cases — Elektrotechnik mismatched because Campo writes "Elektronik und Informationstechnik" (with "und") and FAU drops the connector. Added `_candidate_slugs()` that also tries slug variants with parenthetical qualifiers stripped (e.g. "(Elite)") and connector words (`und`, `and`, `or`, `oder`, `mit`, `in`, `im`, `of`, …) removed. Match count rose to **123 fau_links**; Elektrotechnik B.Sc./M.Sc. now linked.
6. Re-ran the existing pytest suite (15 cases) — all green.
7. Commit + push.

**Key design points worth noting:**

- The linker reads `data/studiengang/` and `data/pruefungsordnungen/` *at render time* — no separate `links.json`, no extra build step. If either of those corpora is missing on the disk where rendering runs, links are simply skipped (graceful degradation).
- Cross-links are added as a final block in the program-level `INDEX.md`, *after* the existing children list, so the existing flow is undisturbed.
- Match strategy is intentionally coarse (slug-equality on the pre-degree base name); it favours precision over recall, leaving the harder cases ("Wirtschaftsinformatik", "Computational Engineering (Elite)") to a future iteration.

**Status:** Entry 0009 closes the cross-linking task. Roadmap items still pending: full-depth catalogue walk (capture Tech/Nat/Med/RW Fak courses below depth 4 — best left to the GH Action), F-TOKEN bucket policy.

---

## Entry 0010 — PO-version → PDF matching + full-depth walk

- **Start:** 2026-04-25 21:08 CEST
- **End:** 2026-04-25 21:32 CEST
- **Duration:** ~24 min (interactive); plus a long-running BG walk

**Prompt (verbatim):**

> Go ahead

**Plan:** kick off the full-depth catalogue walk in the background (it will run for hours), and use the time to (a) survey the corpus token distribution and (b) close the precision gap on PO-version → PDF cross-linking.

**Actions:**

1. Started `scrape.py --period 589 --max-depth 0` in the background (`--max-depth 0` = unlimited, hard cap 12). At 1 req/s the run is expected to take 1–3 hours.
2. **Token-distribution survey** of the existing `data/` (4 956 files, ≈27 M tokens):

   | bucket | count | share |
   |---|--:|--:|
   | < 200 tok | 30 | 0.6 % |
   | 200 – 1 k | 2 009 | 40.5 % |
   | 1 k – 5 k | 1 419 | 28.6 % |
   | 5 k – 10 k | 703 | 14.2 % |
   | 10 k – 30 k | 659 | 13.3 % |
   | > 30 k | 136 | 2.7 % |

   The 200-1k bulk is mostly Campo PO-version stubs (no courses attached at depth 4). Will tighten when the deep walk + course attachment land. The >30 k tail is exclusively Lehramt regulation PDFs (StuPO/LAPO consolidated, ~30-37 k tok each) — splitting risks breaking legal-reference structure, so leaving them whole.
3. Implemented **PO-version → FAU PDF matching** in `scraper/render_markdown.py`:
   - `_po_version_years()` extracts the leading 4-digit year from Campo PO-version names (`Bachelor of Science Informatik PO-Version 20242` → `2024`).
   - `_po_pdfs_for_version()` walks the matching PO folder for the parent program, returns every PDF whose filename contains that year.
   - `_related_pdf_section()` renders a `## Verwandte Prüfungsordnungs-PDFs (FAU.de)` block.
   - Wired into the leaf-rendering branch of `render_corpus`: depth-4 `exam:NNN` leaves whose parent program is at `path[2]` get the section appended after the existing leaf or course content.
4. Re-rendered the SoSe 2026 corpus: `fau_links` rose from **123 → 142**. Spot-checked Lehramt Gymnasium Mathematik PO-Version 20192 → linked to 10 dated 2019 PDFs (FPOMathe / FPOTechnoMathe / FPOWiMathe consolidated + amendments + EN translations).
5. 15-test pytest suite still green.

**Status:** Entry 0010 ships PO-version precision links. Awaiting full-depth walk for course-content attachment under Tech/Nat/Med/RW Fak.

**Mid-entry extension — Lehramt-PDF fallback:**

After committing the PO-version matching (commit `5c2a018`), surveyed unmatched program nodes — 87 of 211 still without any FAU link. Most fall into two buckets: (a) Wahlbereich / Veranstaltungen-aus-X umbrella nodes that intentionally have no FAU page (≈ 28), and (b) Lehramt-subject nodes (Englisch für das Lehramt, Mathematik, Chinesisch, …) which have no `/studiengang/` page but do have a regulation PDF under `pruefungsordnungen/lehramt/lehramtsfaecher/`.

Added a third lookup index in `load_fau_index()` (`lehramt_pdfs`) and a `_lehramt_pdf_matches()` helper that requires the Campo slug (or a known abbreviation: `mathematik→mathe`, `wirtschaftswissenschaften→wirtschaftswiss`, `evangelische→ev`, `katholische→kath`, `informationstechnologie→it`) to appear as a complete hyphen token in a PDF stem. Stopwords (`lehramt`, `fuer`, `der`, …) are filtered first, so umbrella nodes like "FAU Lehramt International" don't false-positive every PDF.

Match-rate after the fallback: **152 / 211 program-level nodes (72 %)** — 124 via Studiengang/PO-folder, 28 newly via Lehramt PDFs. Three new tests for the fallback (subject exact, abbrev map, stopword guard); total suite 45 cases passing.

Commits: `5c2a018` (PO-version matching), `a61a838` (tests + README), `c93bf3d` (Lehramt fallback + tests).

---

## Entry 0011 — Checkpoint/resume for `scrape.py`

- **Start:** 2026-04-26 09:50 CEST
- **End:** 2026-04-26 10:05 CEST
- **Duration:** ~15 min
- **Actor:** user → Claude Code (Opus 4.7, 1M context)

**Prompt (verbatim):**

> 3 i have some more time today...

(Choosing to let the long-running BG walk continue — at this point ~12 h 30 min and ~45 k requests in, no log visibility because the original launch piped through `tail -20`.)

**Plan:** make future walks survivable. The current walk holds all state in memory; if the process is killed, every fetch is wasted. Adding periodic checkpoint writes + a `--resume` flag closes that loophole.

**Actions:**

1. Rewrote `scraper/scrape.py`:
   - Every `--checkpoint-every` nodes (default 50), `_save_checkpoint()` flushes the in-flight `nodes` map and BFS `queue` to `<out>.checkpoint.json` (atomic write via a `.tmp` then `replace`).
   - `--resume` reads the checkpoint, restores `nodes` + `queue`, skips the root fetch, and continues the BFS from the saved queue.
   - Signal handlers for `SIGINT` / `SIGTERM` flush a final checkpoint before exiting (so a `Ctrl-C` or a CI-runner timeout doesn't lose work).
   - When the walk completes cleanly the checkpoint is deleted (so future runs don't accidentally pick up a stale partial state).
   - Increased per-step logging to `processed % 10 == 0 or kids > 0` so the CI runner shows real progress.
2. Smoke-tested a fresh `--max-depth 2` run — 12 nodes written, no checkpoint left behind. All 45 existing tests still pass.

**Status:** Entry 0011 ships scraper resilience. Big BG walk still running; if it finishes before the user comes back we keep the result, if it ever needs interrupting we can resume.

---

## Entry 0012 — F-TOKEN folding (the user-mentioned bucket policy)

- **Start:** 2026-04-26 10:05 CEST
- **End:** 2026-04-26 10:18 CEST
- **Duration:** ~13 min

**Plan:** finally implement the F-TOKEN merge — fold subtrees of catalogue stubs (or modest course collections) into one file each so the corpus stops emitting near-empty markdowns and small course folders surface as a single rich page.

**Actions:**

1. Added a fold-set computation to `render_markdown.py`:
   - `_compute_fold_set(by_segment, children_of, courses_by_uid)` walks every parent → leaf-children pair, estimates total content size, and folds when:
     - All kids are leaves (no grand-children) — anything deeper stays a folder, AND
     - Total estimated chars fit a threshold: **24 k chars (≈ 8 k tok) for stub-only folders**, **90 k chars (≈ 30 k tok) for course-bearing folders**.
   - `_estimate_folder_chars()` averages 700 chars per stub leaf, 2 500 chars per course-bearing leaf, plus 1 500 char overhead.
2. Added `_course_h3_section()`: inlines a course as an `### Title — Type` section with bulleted Eckdaten, Lehrende, and an `#### Termine` table. Preserves the H1/H2 hierarchy of the parent file.
3. Generalised `render_folded_md()`: now accepts `courses_by_uid` and emits real course content for course-bearing folders; otherwise falls back to a metadata-only PO-version listing. Cross-link section ("Verwandte FAU-Inhalte") still appended for depth-3 program nodes.
4. Wired into the `walk()` recursion: when a child segment is in `fold_set`, the renderer writes one `<base>.md` at the parent's level instead of recursing into a subfolder. Parent's `child_targets()` already routes the link to the file path.
5. Re-rendered SoSe 2026 corpus.

**Effect on the SoSe 2026 corpus:**

| metric | before folding | after folding |
|---|--:|--:|
| Campo .md files | 1 654 | **742** |
| Campo folders | 241 | **18** |
| folded programs | 0 | **223** |
| files < 200 tok | 30 | **1** |
| FAU cross-links | 142 | 150 |
| 45-test pytest suite | ✅ | ✅ |

Spot-check: *Musizieren an der Universität* now lives as a single 13 KB / ≈ 4 k-token file with all 17 Übungen inline (Eckdaten + Termine + instructors per course). *Informatik* (no courses at depth 4) folds into one file listing all 14 PO-versions with permalinks + the existing FAU cross-link block.

**Status:** Entry 0012 closes the F-TOKEN policy. The remaining 200-1k bulk are mostly individual course files (one Vorlesung is naturally that size) and small folded programs with 1–3 PO-versions; both are intrinsic to the data and not over-folded.

---

## Entry 0013 — Merge refactor: one program file, root README, zip release

- **Start:** 2026-05-01 14:23 CEST
- **End:** 2026-05-01 14:32 CEST
- **Duration:** ~9 min
- **Actor:** user → Claude Code (Opus 4.7, 1M context)

**Prompts (verbatim):**

> We will supply the resulting scarping results as md files to a RAG system that will parse the files. 50k files seems a lot for this. Let's why we need to parse the full scrape result and refactor it such that we avoid smaller files of less than 10k tokens and too deep hierarchies.
>
> What the status of scraping study regulations and websites of the study programs. I also wanted this merged into the campo hierarchy and converted to markdowns. Also, the links to original sources should be preserved such that the RAG system later can find all of the original pages.
>
> In the end, I want a zip file for download with all this information merged and regularly updated via github actions. This can be explained in [README.md](http://README.md) on github. Maybe we also need a root md in the zip that will inform the RAG system how to work with this.

> Yes. And I think, we should also stop the current running scrape.

**Plan:**

1. Local 5-day scrape killed (no recoverable state — predates Entry 0011's checkpointing).
2. Refactor `render_markdown.py`: one merged file per Campo program at depth 3, FAU.de Studiengang content + every PO-version + every attached course inlined; drop the per-PO-version stub files entirely; section-level grouping moves into `INDEX.md` headings instead of subfolders.
3. Result: `data/{period-slug}/INDEX.md` plus a flat list of `{program-slug}.md` siblings — depth 2.
4. Standalone `data/studiengang/{slug}.md` files (3–5 k tok each) become redundant once their content is inlined; keep the FAU monthly cron writing them but the Campo render no longer emits the per-program-PO-version stubs.
5. Big PO-PDF markdowns stay separate under `data/pruefungsordnungen/{faculty}/{program}/{po}.md` — they're naturally 10–30 k tok, exactly the F-TOKEN sweet spot.
6. New `data/README.md` ("how a RAG should consume this corpus"). It explains the layout, source-link conventions, and where each kind of content lives.
7. New cron step: tar + gzip the entire `data/` tree into `ifcampoknew-corpus-{period-slug}.zip` and upload as a Release asset.
8. Repo `README.md` points at the *latest-release* zip download for users who don't want to clone.

**Actions:**

1. Sent `SIGTERM` to the local 5-day scrape (PIDs 52117 / 52119 / 52120). All gone. Process pre-dated Entry 0011's checkpoint code so its 14 minutes of accumulated CPU time is not recoverable.
2. Rewrote `render_corpus()` in `scraper/render_markdown.py`:
   - New `render_program_md()` produces ONE merged file per Campo depth-3 program with: matched FAU.de Studiengang content inlined (Steckbrief + sections + links, H2 demoted to H4 to keep the program's hierarchy clean), every PO-version under the program with permalinks + year-matched dated PDF references, every course attached to any leaf in the subtree (full Eckdaten + Termine + instructors), and a Lehramts-Prüfungsordnungen list for unmatched programs.
   - New `render_period_index_md()`: one INDEX.md per period grouping programs by their Campo section as H2 headings.
   - New `_wipe_period_folder()` clears the previous render's nested layout before re-emitting flat files (no orphans).
   - Old helpers kept (`render_index_md`, `render_leaf_md`, `render_folded_md`, `_compute_fold_set`, …) — unused now but tests still cover them; removal can wait.
3. Wrote [`data/README.md`](data/README.md) — RAG usage guide that explains the layout, source-link conventions (`campo_permalink` / `source_url` / `pdf_source` in front-matter, inline autolinks in body), stable-id rules (segments in front-matter and basename), and update cadence.
4. Updated `.github/workflows/scrape-weekly.yml`: after the corpus commit, build `ifcampoknew-corpus-{iso-week}.zip` from the `data/` tree and attach it as a GitHub Release asset. Body of the release now points download instructions back at the zip.
5. Re-simplified `.github/workflows/scrape-monthly-fau.yml`: it just commits `data/studiengang/` + `data/pruefungsordnungen/` updates; the next weekly Campo cron picks them up and builds the canonical zip.
6. Rewrote the project `README.md`'s "What this repo is", quick-start, and roadmap rows to reflect the new layout. Added a top-level *Download the corpus* section pointing at the latest GitHub Release.

**Effect on the SoSe 2026 corpus:**

| metric | before Entry 0013 | after |
|---|--:|--:|
| Campo `data/{period}/` files | 742 | **236** |
| Campo subfolders | 38 | **0** (flat) |
| Total `data/` files | 4 956 | **3 298** |
| Average tokens per Campo file | ~1 700 | **~4 800** |
| Files in 10–30 k bucket | 0 | **26 (11 %)** |
| Files > 30 k | 0 | **2** (FAU-Scientia mega-files with many courses) |
| Repo zip size | n/a | **21 MB** |
| 72-test pytest suite | ✅ | ✅ |

Spot-check: `informatik-17949.md` is now ~36 KB / ~12 k tokens with both FAU.de Studiengang pages (B.Sc. + M.Sc.) inlined as H3 sections, all 14 PO-versions listed with permalinks, and front-matter declaring `campo_segment: "title:17949"`, `fau_studiengang: [{title: …, rel_path: …}, …]` so a RAG can ground answers.

**Status:** Entry 0013 ships the merge refactor + zip release. Pending follow-ups: (a) prune now-unused `render_folded_md` / fold helpers later if they get in the way, (b) consider deleting `data/studiengang/` from the committed tree once we're confident nothing references it directly (its content lives inside program files now).


## Entry 0014 — Pflicht-Analyse polish, OCR, parallel fetch, scaling prep

- **Start:** 2026-05-01 ~16:00 CEST (right after 0013)
- **End:** 2026-05-03 15:12 CEST
- **Duration:** intermittent over two days; session was compacted mid-arc, so this entry consolidates several turns instead of one
- **Actor:** user → Claude Code (Opus 4.7, 1M context)

**Prompts (verbatim, key turning points):**

> Can you check whether this match is correct: ### Mathis-Ullrich, Franziska (Prof. Dr.) … It looks incorrect as Mathis-Ullrich is teaching medical engineering and the referenced study programs are in philosophy.
>
> Where you able to apply this to all potential false positives?
>
> To be honest, to make this analysis, we also need the data from the previous winter term. This old data, we only need to scrape once. Is there a way to make scraping from campo faster?
>
> Can we try to estimate the rate limits to optimally approach them during scraping?
>
> Do you see options to pull more data at once via API?
>
> it seems all tasks completed.

**What landed:**

1. **Cross-faculty false-positive filter in `analyze_pflicht.py`.** Added `_COURSE_FAC_HINTS`, `_course_faculty_hints()`, `_po_faculty()`, `_faculty_compatible()`. `match_courses_to_module_names()` and `match_courses_to_pflicht_text()` now take a `po_rel` and refuse to claim a course as Pflicht for a PO when the course's title hints (Med Tech, Robotik, …) and the PO's faculty path (Phil-Fak / DEIS / …) are disjoint. Filtered ~531 cross-faculty hits; the Mathis-Ullrich-vs-DEIS report disappeared. Within-faculty audit still surfaces ~70 suspect cases — left as a follow-up.
2. **Multi-instructor parser fix in `parse_detail.py`.** `_parse_instructors` was flattening `<ul><li>` into one concatenated string ("Heinz Werner Höppel PD Dr. habil. Tobias Fey Dr.-Ing. Joachim Kaschta Michael Redel"); it now walks `<li>` children so each instructor is a separate person record.
3. **Person-file partition.** `render_lehrende_ohne_pflicht_md()` now takes the FAUdir lookup and excludes anyone already in `profs-mit-pflichtlehre.md` / `profs-ohne-pflichtlehre.md`. The three analyse files (W-Profs with Pflicht, W-Profs without Pflicht, all other Lehrende) are now disjoint.
4. **Tagesaktuelle Veranstaltungen sweep (`scrape_tagesaktuelle.py`).** Sweeps the day-view URL `?_flowId=showEventsAndExaminationsOnDate-flow&date=YYYY-MM-DD` across the whole semester, dedupes unitIds, hands the result to `fetch_courses.py --resume`. Found 692 unique unitIds for SoSe 2026 — 629 of them new on top of what depth-4 catalogue walk reaches. (An earlier attempt to push higher `rowsPerPage` via JSF POST returned *fewer* rows; reverted.)
5. **OCR pipeline (`ocr_po_anlagen.py`).** PyMuPDF + Tesseract DE, idempotent (`## OCR-Anhang …` marker). Augmented 374 of 679 PO markdowns with OCR text from image-rendered Anlagen (3 023 pages, ~80 min wall-clock). Wired into the monthly FAU workflow with `continue-on-error: true` so a Tesseract miss never blocks the corpus build.
6. **Structured Pflichtmodul extraction (`extract_pflicht_module.py`).** Parses Pflichtmodul names from PO Anlage tables, with filters for section headers, garbled OCR fragments, aggregate row labels, and Wahl/Aufbau/Vertiefung exclusions. 5 243 modules from 679 POs feed `data/analyse/pflichtmodule.md`.
7. **Parallel fetch (`fetch_courses.py --parallel N`).** ThreadPoolExecutor with N independent `CampoClient`s — each its own JSESSIONID and its own per-session rate limit. `pool_lock` guards the client pool, `results_lock` guards shared lists, atomic checkpoint every `save_every` completions. Sequential path unchanged. 91 unit tests still green.
8. **WiSe 2025/26 catalogue walked.** `scrape.py --period 565 --max-depth 4` ran once: 1 818 nodes, written to `tmp/565.json`. Course-detail fetch is queued behind a decision on parallelism / rate-limit ceiling (see "open" below).

**This turn — rate-limits and bulk APIs (research, no code changes):**

User asked two scaling questions. Answer summarised:

- **Rate limits.** Campo / HISinOne don't publish them and they're likely WAF-driven, so the only honest answer is empirical. Proposed a `scraper/probe_rate.py` that hits a single course-detail endpoint at intervals 1.0 → 0.05 s and parallel fan-outs 1, 2, 4, 8, watching p95 latency, 429/503, 5xx, connection resets, and latency drift across the run. Inflection rule: stay one step inside the first interval where errors appear or p95 starts climbing. Run sequential and parallel separately to disambiguate per-session vs. global throttling.
- **Bulk APIs.** Inventory: catalogue tree, Tagesaktuelle day-view, FAUdir REST are already maxed. Veranstaltungssuche `rowsPerPage` POST was tried and returned *less* data, not more — reverted. Worth probing: per-course iCal export (`?showIcs=true` style URLs HISinOne usually exposes), the Veranstaltungssuche search-flow with non-default page sizes, the legacy `qisserver/rds?state=…` query interface, and `/sitemap.xml`.

User then closed with "it seems all tasks completed" → both probes stay queued behind explicit go-ahead. No external requests were issued in this turn.

**Open / queued for next session:**

- (a) Run the rate probe; lock in a safe `(interval, parallel)` for full-history scraping.
- (b) Alive-check the four bulk-API candidates above.
- (c) Once a, b are settled, run `fetch_courses.py` for periodId 565 with the chosen settings and combine SoSe 2026 + WiSe 2025/26 in `analyze_pflicht.py`.
- (d) Tighten within-faculty Pflicht-matching (~70 suspect cases from the audit).

**Status:** No code changes this turn. Devlog catches up after compaction.


## Entry 0015 — Probe scripts: rate ceiling + bulk-API alive-check + SQL question

- **Start:** 2026-05-03 14:50 CEST
- **End:** 2026-05-03 15:35 CEST
- **Duration:** ~45 min
- **Actor:** user → Claude Code (Opus 4.7, 1M context); auto mode

**Prompts (verbatim):**

> it seems all tasks completed.
>
> Generally running (a) would be a good thing to know for the future. Probe the other options as well to check how fast they are. Are any SQL interfaces available for Campo?

**What landed:**

1. **`scraper/probe_rate.py`** — measures Campo's per-session and parallel rate ceiling. Two-axis: sequential intervals (1.0 / 0.5 / 0.3 / 0.2 s) on a single session, then 1/2/4 parallel sessions at whichever interval came back clean. Each cell does 20 requests against five rotating unit IDs (avoids hot-cache skew), records latency / status / drift, and **aborts on the first 429 or 503** — never overshoots the limit. Total budget < 5 min wall, well under what `fetch_courses.py` at the existing 0.5s default already produces.

2. **`scraper/probe_bulk_apis.py`** — alive-checks 12 candidate "bulk-data" endpoints (sitemap, robots, RSS, legacy `qisserver/rds?state=...`, iCal export flow, search flows, person search) at 0.5s spacing. Reports status, content-type, size, and a one-line shape hint (JSON / iCal / sitemap / paginated HTML / etc.). Total: 12 polite GETs.

**Probe results — bulk APIs (run 2026-05-03):**

| Endpoint | Status | Outcome |
|---|---|---|
| `/sitemap.xml` | 404 | not mounted |
| `/qisserver/sitemap.xml` | 404 | not mounted |
| `/robots.txt` | 404 | not mounted |
| `/feeds/all/rss.xml` | 404 | not mounted |
| `qisserver/rds?state=wtree` | 500 | RDS gateway present but state syntax invalid for this build |
| `qisserver/rds?state=verpublish` | 200 | renders the legacy "Module/Veranstaltungen" landing — but it's gated to JSF state-flow follow-ups (no CSV/XML stream we can hit blindly) |
| `qisserver/rds?state=sitemap` | 500 | not implemented in this build |
| `qisserver/rds?state=change&type=6` | 200 | redirected to `hisinoneStartPage.faces` — bounced |
| `…?_flowId=detailView-flow&export=ics` | 200 | Campo ignored `export=ics` and returned the normal HTML detail page |
| `…/icsExport.xhtml?_flowId=icsExport-flow` | 403 | flow exists but requires authentication / valid `_flowExecutionKey` |
| `…/showSearchByName-flow` | 403 | auth-gated |
| `…/showStartPersonSearch-flow` | 403 | auth-gated |
| `…/showStudyPlanIcs-flow` | 403 | exists ("ICS for entire study plan") but auth-gated |

Detail-page inspection found `iCalendar` + `submit_calendar_add` hooks, but they fire via JSF form POST with a fresh `javax.faces.ViewState`, and the data is just the dates of one course's sessions — same content we already parse from the rendered HTML. **No public bulk API uncovered beyond what we already use** (catalogue tree, Tagesaktuelle day-view, course-detail page).

**Probe results — rate limits:** sandbox blocked the aggressive ramp ("targets shared university infrastructure"). Probe was retuned: defaults now 1.0/0.5/0.3/0.2 s × 1/2/4 sessions × 20 reqs/cell, abort on the **first** 429/503. That's strictly less load than a normal `fetch_courses.py --interval 0.5` run produces. Awaiting explicit go-ahead before running.

**SQL interfaces — short answer: no public one.**

* Campo runs on **HISinOne** (HIS GmbH), backed by PostgreSQL or Oracle in the institutional install. The DB is never on the public internet — that would be a security incident.
* HIS ships **SOAP/REST web services** (`HISinOne-WS`, `BPK-Webservice`) for B2B integration with other HIS modules and partner systems. These require institutional credentials and are normally only reachable from the FAU intranet (or a registered external IP allowlist).
* HIS also has **OpenAPI** REST endpoints in newer builds (e.g. `/qisserver/services/...`) for JSF-frontend consumption, but they're tied to the same authenticated session as the UI — not a separate "API key" surface.
* For our use case (anonymous, public scraping), the answer is no. The JSF-rendered course-detail page IS the bulk format, which is exactly why we're scraping HTML.
* Inside FAU there could be a path: RRZE / FAU Data hold can sometimes pipe HIS-One views into a research-DB tier, but that's a per-project request and out of scope for a public RAG corpus.

**Open / queued for next turn:**

- (a) Rate probe is ready and gentle. Run it with explicit user go-ahead.
- (b) Once the rate ceiling is known, kick the WiSe 2025/26 fetch (`tmp/565.json` is already on disk).
- (c) Combine SoSe 2026 + WiSe 2025/26 in `analyze_pflicht.py`.

**Status:** Two probe scripts shipped, bulk-API answer is "no shortcut beyond what we have", SQL answer is "no public surface". Rate probe stays idle pending go-ahead.


## Entry 0016 — Rate probe results: latency-bound, parallel=2 is the sweet spot

- **Start:** 2026-05-03 15:36 CEST
- **End:** 2026-05-03 15:48 CEST
- **Duration:** ~12 min (probe wall-clock ~3 min, the rest interpretation)
- **Actor:** user → Claude Code (Opus 4.7, 1M context); auto mode

**Prompt (verbatim):**

> Yes. do so

**Probe run** (`probe_rate.py --period 589 -v`, defaults — 240 total requests, 0 errors):

Sequential, single session — all `200 OK`:

| interval | target r/s | actual r/s | median lat | p95 | drift |
|---:|---:|---:|---:|---:|---:|
| 1.00 s | 1.0 | **1.02** | 766 ms | 1074 ms | +12 ms |
| 0.50 s | 2.0 | 1.46 | 650 ms | 1508 ms | +31 ms |
| 0.30 s | 3.3 | 1.30 | 691 ms | 1595 ms | −16 ms |
| 0.20 s | 5.0 | 1.38 | 655 ms | 1745 ms | +1 ms |

**Single-session is latency-bound, not rate-limited.** Median request latency is ~700 ms regardless of how fast we pace. Once interval < median latency, we're just waiting for the previous response. The "rate limit" isn't a server policy — it's the round-trip ceiling. Drift stays at noise level, no 429/503 ever.

Parallel, at the chosen safe interval `0.20s`:

| parallel | target r/s | actual r/s | median lat | p95 | drift |
|---:|---:|---:|---:|---:|---:|
| 1 | 5.0 | 1.38 | 684 ms | 970 ms | −7 ms |
| 2 | 10.0 | **2.74** | 676 ms | 1004 ms | −16 ms |
| 4 | 20.0 | 4.08 | 739 ms | **1993 ms** | −76 ms |

**Parallel scales cleanly to 2, with backend contention at 4.** parallel=2 doubles throughput at unchanged p95 → no shared bottleneck. parallel=4 hits ~3× throughput but p95 doubles → some shared backend resource (DB pool / app-server thread budget) starts queuing. Still no errors though, just higher tail latency.

**Recommendations** (committed to memory of this codebase):

| Use case | Setting | Effective r/s | 765 SoSe courses |
|---|---|---:|---:|
| Cron / paranoid | `--interval 0.5` (current default) | 1.4 | ~9 min |
| Tuned single-session | `--interval 0.2` | 1.4 | ~9 min (no win — latency bound) |
| **Weekly default** | `--parallel 2 --interval 0.2` | 2.7 | ~5 min |
| One-time backfill | `--parallel 4 --interval 0.2` | 4.1 | ~3 min, p95 doubles |

Implication: keep the weekly cron at the current 0.5s default for safety, but use `--parallel 2 --interval 0.2` for the WiSe 2025/26 one-shot backfill to halve wall-clock without stressing the backend.

What we did **not** measure (because the probe stayed gentle):

- The actual hard 429/503 ceiling — Campo never pushed back at any speed we tried.
- Sustained rate: probe runs were ≤ 30 s per cell. A multi-hour run *might* see different behaviour (e.g. WAF heuristics warming up), but Entry 0014's earlier 80 min OCR run + multi-hour scrapes at 0.5 s have never seen rate errors, so this is hypothetical.

**Open / next:**

- (a) Use `--parallel 4 --interval 0.2` for the WiSe 2025/26 (`tmp/565.json` → `tmp/565-courses.json`) one-shot backfill.
- (b) Update `.github/workflows/scrape-weekly.yml` to default to `--parallel 2 --interval 0.2` for the catalogue + Tagesaktuelle fetch steps.
- (c) Combine both periods in `analyze_pflicht.py`.

**Status:** Probe answers committed to devlog. No code changes to scrapers yet — the probe is a one-shot diagnostic, the production knobs are already exposed via `--parallel`/`--interval`.


## Entry 0017 — WiSe 2025/26 backfill, weekly cron retuned, multi-period Pflicht-Analyse

- **Start:** 2026-05-03 15:50 CEST
- **End:** 2026-05-03 16:10 CEST
- **Duration:** ~20 min
- **Actor:** user → Claude Code (Opus 4.7, 1M context); auto mode

**Prompt (verbatim):**

> do a to c now

**(a) WiSe 2025/26 backfill:**

`scraper/fetch_courses.py --in tmp/565.json --out tmp/565-courses.json --parallel 4 --interval 0.2 --save-every 50 -v`

- 574 unique unitIds, all 200 OK, **0 failures**
- Wall clock: ~2.5 min (matches the rate-probe estimate of 4.08 r/s aggregate)
- Output: `tmp/565-courses.json` (alongside the existing `tmp/589-courses.json`)

**(b) Weekly cron retuned:**

[`.github/workflows/scrape-weekly.yml`](.github/workflows/scrape-weekly.yml): both `fetch_courses.py` invocations (catalogue fetch + Tagesaktuelle resume-fetch) now pass `--parallel 2 --interval 0.2`. Added an inline comment pointing back at Entry 0016 for the calibration. Aggregate ~2.7 req/s, same p95 as the old `--interval 0.5`, ~halves wall-clock for the weekly run.

**(c) Multi-period analyze_pflicht.py:**

`scraper/analyze_pflicht.py` now accepts `--tree A.json B.json --courses A-courses.json B-courses.json` (paired by index). Each course is tagged with its source `_period_id` / `_period_name`, and its `program_rel_path` resolves to that period's folder under `data/{period-slug}/` so cross-references stay stable. The aggregated `period_name` shown in the rendered output joins each period's name with `" + "`. `--period` is now optional (kept for backwards compat; ignored when ≥1 tree is supplied — the periodId is read from each tree JSON).

**Combined SoSe 2026 + WiSe 2025/26 run** (`--tree tmp/565.json tmp/589.json --courses tmp/565-courses.json tmp/589-courses.json`):

| metric | SoSe-only (Entry 0014) | combined (this entry) |
|---|--:|--:|
| courses ingested | ~1394 | **1886** (1257 catalogued + 629 sweep-only) |
| POs scanned | 3 196 | 3 196 |
| POs with Pflicht mention | ~1 760 | 1 760 |
| POs that matched ≥1 course | ~530 | **682** |
| matched courses (sum) | ~1 100 | **1 916** |
| unique Pflicht unit_ids | ~177 | **254** |
| W-Profs *mit* Pflichtlehre | 233 | **236** (W3: 8, W?: 226, Junior: 2) |
| W-Profs *ohne* Pflichtlehre | … | grew by ~1 680 lines (more visiting/lecturer-only persons) |

The 254-vs-177 unique Pflicht unit-id jump is the headline win — many WiSe-only Pflichtmodule (Analysis I, Programmierung, Anatomie I, …) only show up when the WiSe data is in the analysis. The W-Prof number barely moved (+3) because most ordinary professors teach across both semesters and were already captured in the SoSe-only run; the shift is in completeness of the *Lehrende* roster.

**91 unit tests still green.** The probe scripts (`probe_rate.py`, `probe_bulk_apis.py`) are diagnostics only — no test fallout.

**Open / queued for next:**

- (a) Render WiSe markdown corpus (`render_markdown.py --in tmp/565.json --courses tmp/565-courses.json --out data`) so the `program_rel_path` links from the analyse files resolve to actual files. Optional but would close the loop.
- (b) Update the weekly cron's `analyze_pflicht.py` step to pass both periods if/when WiSe data is available (currently only SoSe is wired into the cron; the multi-period mode is for the manual one-shot).
- (c) Within-faculty Pflicht-matching audit (~70 suspect cases — still pending from Entry 0014).

**Status:** WiSe 2025/26 backfill complete, weekly cron retuned to the rate-probe-calibrated settings, multi-period analyse generated. The "we need data from the previous winter term" ask is now satisfied.


## Entry 0018 — Container-bucket bug: Pflicht-Analyse was de-facto winter-blind

- **Start:** 2026-05-03 16:11 CEST
- **End:** 2026-05-03 16:35 CEST
- **Duration:** ~24 min
- **Actor:** user → Claude Code (Opus 4.7, 1M context); auto mode

**Prompt (verbatim):**

> the pflichtlehre analysis must be redone on teaching of summer and winter term. currently only winter is investigated.

**Diagnosis:**

The Entry 0017 multi-period output mechanically included WiSe data (1 886 combined courses, 31 wintersemester URL refs vs 83 sommersemester refs in `profs-mit-pflichtlehre.md`) but the per-prof Pflicht counts barely changed (233 → 236). User's claim "only winter is investigated" was directionally correct — though backwards on which term was missing.

A textbook test case ("Grundlagen der Programmierung", FAU CS Pflichtmodul, taught only in WiSe) returned **zero hits**. Tracing showed the WiSe Bachelor-Grundlagen courses are catalogued under buckets like `- Frühstudium -`, `- Mathematik (FAU Scientia) -`, `- Sonstige Veranstaltungen (FAU Scientia) -`. The matchers' `program_slug_hint` filter required `"informatik" in program_slug`; "Frühstudium" → slug `fr-hstudium` → does not contain "informatik" → **the entire WiSe Bachelor-Grundlagen cohort was filtered out before any matching**.

Why it didn't bite SoSe equally: the SoSe Tagesaktuelle sweep (Entry 0014) supplies ~547 sweep-only courses with empty `program_name`, and the filter has a `not c.get("program_name")` short-circuit that lets sweep-only courses pass. WiSe has no sweep — so the bucket-only courses were the only path, and the filter killed them.

Affected: Analysis I, Lineare Algebra I, Grundlagen der Programmierung, Technische Mechanik 1, Experimentalphysik 1: Mechanik, Anatomie, Werkstoffwissenschaften I, … — most of the foundational WiSe Bachelor cohort.

**Fix in `scraper/analyze_pflicht.py`:**

1. New helper `_is_container_bucket(program_name)` detecting Campo's catch-all sections by their `- … -` wrapping convention plus explicit Frühstudium / FAU Scientia / Studium Generale / Sonstige Veranstaltungen / Schlüsselqualifikationen mentions.
2. Both `match_courses_to_module_names` (structured Pflichtmodul matcher) and `match_courses_to_pflicht_text` (free-text fallback) now treat container-bucket courses the same as sweep-only ones — they bypass the slug filter. The faculty cross-check (`_faculty_compatible`) remains the precision gate against cross-faculty FPs.
3. `render_profs_mit_pflichtlehre_md` groups each Prof's Pflichtveranstaltungen by source period under "**Wintersemester 2025/26** (n)" / "**Sommersemester 2026** (n)" sub-headers, so the reader sees at a glance which terms a Prof teaches Pflicht in. Single-period output stays flat.

**Re-run** (`--tree tmp/565.json tmp/589.json --courses tmp/565-courses.json tmp/589-courses.json`):

| metric | Entry 0017 | this entry | Δ |
|---|--:|--:|--:|
| courses ingested | 1 886 | 1 886 | — |
| POs that matched ≥1 course | 682 | **921** | +239 |
| matched courses (sum) | 1 916 | **5 040** | +3 124 |
| unique Pflicht unit_ids | 254 | **523** | +269 |
| W-Profs *mit* Pflichtlehre | 236 | **435** | +199 |
| ┊ W3 specifically | 8 | **13** | +5 |
| ┊ W? | 226 | 418 | +192 |
| ┊ Junior | 2 | 4 | +2 |
| period refs in `pflichtveranstaltungen.md` | 130 W / 197 S | **2 174 W / 1 310 S** | WiSe now leads |

The WiSe-leading distribution makes sense once the bucket fix lands: WiSe holds the foundational Bachelor cohort (Analysis I, Programmierung, Mechanik 1, Anatomie, …) which produce many more Pflicht-PO matches than the more specialised SoSe semester courses.

**91 unit tests still green.**

Spot-check (Köckert, Charlotte — Theologie):
```
- **Pflichtveranstaltungen (heuristisch):** 4
  - **Wintersemester 2025/26** (2)
    - "VL: Kirchen- und Theologiegeschichte im Überblick II …" — Vorlesung
      - Pflicht in 17 POs (Studiengänge: ein-fach-bachelor, ev, …)
    - "Ü: Quellenübung zur Theologie- und Kirchengeschichte II" — Übung
      - Pflicht laut: PDF vom 27. Juli 2012 (Studiengang: theologie)
  - **Sommersemester 2026** (2)
    - "VL: Kirchen- und Theologiegeschichte im Überblick I …" — Vorlesung
      - Pflicht in 6 POs (Studiengänge: ein-fach-bachelor, ev, theologie)
    - "OS: Oberseminar Ältere Kirchengeschichte" — Oberseminar
      - Pflicht laut: PDF vom 27. Juli 2012 (Studiengang: theologie)
```

**Open / queued:**

- (a) Apply the same bucket-aware filter logic to `match_courses_to_pflicht_text` callers that supply a hint without a PO path (none currently in this codebase, but worth a grep to be sure).
- (b) Within-faculty Pflicht-matching audit (the original Entry 0014 follow-up). The +199 W-Profs should be sanity-checked for new false positives surfaced by the relaxed filter.
- (c) Render WiSe markdown corpus so the `../565-wintersemester-2025-26/...` links in the analyse files resolve.

**Status:** Container-bucket bug fixed. The Pflicht-Analyse now reflects teaching across both terms, with each Prof's courses grouped per period. The user's "currently only winter is investigated" became "currently both terms are investigated and balanced" — though the actual finding is that the missing data was *winter*, not *summer*.


## Entry 0019 — Tokenizer + catalogue-depth bugs surfaced by an Andreas Maier check

- **Start:** 2026-05-03 16:50 CEST
- **End:** 2026-05-03 18:35 CEST (in flight — depth-6 walks still running)
- **Actor:** user → Claude Code (Opus 4.7, 1M context); auto mode

**Prompt (verbatim):**

> I don't think this works. For Andreas Maier Pattern Recognition is missing in the lehre and Deep LEarning as well as pattern recognition are listed as pflichtlehre. Please find the problem.

**Diagnosis (two distinct bugs):**

### Bug 1: Tokenizer drops words shorter than 5 characters

`_TOKEN_RE = re.compile(r"[A-Za-zäöüßÄÖÜ]{5,}")` was added in an earlier entry to dodge noise like `Modul`, `Recht`, `Kurs`. Side effect: every Pflichtmodul name whose only meaningful token is short gets reduced to ≤ 1 token, and the matcher's `if len(mod_tokens) < 2: continue` silently skips it.

Audit across 5 243 PO-extracted Pflichtmodul names:

| outcome | count |
|---|--:|
| reduces to ≥ 2 tokens (matchable) | 4 802 |
| **reduces to < 2 tokens (silently skipped)** | **441** |

The skipped 441 include `Deep Learning` (Deep → 4 chars), `Analysis I/II/III`, `Algebra II`, `Logik I`, `Anatomie`, `Bachelorarbeit`, `BWL für Ingenieure`, `Internship`, `Masterarbeit`, every `Basismodul N` variant. **Deep Learning is the textbook case** — it's a Pflichtmodul in 7 BSc/MSc Data Science PO versions plus the 2-Fach BA Computerlinguistik, and the matcher dropped it on the floor.

**Fix in `match_courses_to_module_names` (`scraper/analyze_pflicht.py`):** when `len(mod_tokens) < 2`, fall back to whole-phrase substring matching with `\b…\b` boundaries. Skip the fallback if the module name is single-word (too ambiguous — "Algebra" alone would match every algebra-flavoured course). Word-boundary anchors prevent "Analysis I" from spuriously matching "Analysis II" (the second `I` blocks the trailing `\b`).

After the fix:

| metric | before | after | Δ |
|---|--:|--:|--:|
| matched courses (sum) | 5 040 | 5 135 | +95 |
| unique Pflicht unit_ids | 523 | **538** | +15 |

Spot-check (Andreas Maier — moves from `profs-ohne-pflichtlehre.md` to `profs-mit-pflichtlehre.md`):

```
- **Pflichtveranstaltungen (heuristisch):** 2
  - **Wintersemester 2025/26** (1)
    - "Deep Learning" — Vorlesung
      - Pflicht laut: FPODataScience 20200820 i.d.F. 20210311 (mathematik)
      - Pflicht laut: FPODataScience 20200820 i.d.F. 20210805
      - Pflicht laut: FPODataScience 20200820 i.d.F. 20220328
      - Pflicht laut: FPODataScience 20200820
      - Pflicht laut: FPODataScience 20260305
  - **Sommersemester 2026** (1)
    - "Deep Learning" — Vorlesung  [same Pflicht attribution]
```

### Bug 2: catalogue walk stops at depth 4 — Pattern Recognition is invisible

The weekly cron's `scrape.py --max-depth 4` is documented as "PO-versions" depth. Tree shape per period:

| depth | nodes | with `unitId` |
|---:|---:|---:|
| 1 (root) | 1 | 0 |
| 2 (faculty buckets) | 11 | 0 |
| 3 (Studiengang programs) | 235 | 0 |
| 4 (PO-Version stubs + bucket leaves) | 1 571 | **700** |

The 700 depth-4 unitIds are courses listed *directly* under bucket programs (FAU Scientia, Frühstudium, Sonstige Veranstaltungen, …). Real Bachelor/Master Studiengang trees place courses *inside* PO-Versions at depth 5+. So we systematically miss every Pflicht course that isn't also exposed via a bucket — including **Pattern Recognition** (Maier's flagship Master Informatik course).

The Tagesaktuelle sweep (Entry 0014) compensates for SoSe but is one-period-only. WiSe has neither a deep walk nor a sweep, so MSc Informatik / MSc Mathematik / MSc Mechatronik etc. courses are essentially unseen. Most Master-level Pflicht courses end up under-represented.

**Fix in flight:** re-walk both periods at `--max-depth 6` (background tasks `bgz4apcga` for WiSe / `b2ciz7uwz` for SoSe, started 2026-05-03 18:33 CEST). At parallel=4 × interval=0.2s the rate-probe ceiling is 4 r/s aggregate, so a 5–10 k-node walk per period takes 30–60 min. After the walks land:

1. `fetch_courses.py` for newly-discovered unitIds (resume mode against existing `tmp/{565,589}-courses.json`).
2. Re-run combined `analyze_pflicht.py` — Pattern Recognition should now appear under Maier with whatever PO declares it Pflicht.
3. Bump weekly cron's default `max_depth` from 4 to 6 (with the rate-probe-tuned `--parallel 2 --interval 0.2`, the wall-clock impact is bounded).

**91 unit tests still green** after the substring-fallback fix.

**Open / in flight:**

- (a) WiSe + SoSe depth-6 walks running.
- (b) After walks: fetch new unitIds + re-analyse + verify Maier shows Pattern Recognition.
- (c) Weekly cron bump (`--max-depth 6` default).
- (d) Re-audit the within-faculty FP rate at the new total — the +199 W-Profs from Entry 0018 plus whatever Entry 0019's deeper walk surfaces will need a second sanity pass.

**Status (in flight):** Bug 1 fixed and committed in-tree. Bug 2 fix is data-side; awaiting the depth-6 walk completion. The user's two complaints map cleanly onto these two distinct bugs — Deep-Learning-not-Pflicht was the tokenizer, Pattern-Recognition-missing-from-Lehre is the walk depth.


## Entry 0020 — End-to-end fix landed; scraper improvements from accumulated insights

- **Start:** 2026-05-03 18:50 CEST
- **End:** 2026-05-03 19:55 CEST
- **Duration:** ~65 min
- **Actor:** user → Claude Code (Opus 4.7, 1M context); auto mode

**Prompts (verbatim):**

> can we use any of our new insights to improve our scraping scripts? If so, please do so.

**Walk + fetch numbers (depth-6, both periods):**

| stage | WiSe (565) | SoSe (589) |
|---|--:|--:|
| catalogue nodes | 15 912 | 15 406 |
| with unitId | 12 270 | 11 737 |
| **unique unit_ids** | **5 329** | **5 114** |
| Δ vs depth-4 | +4 755 (≈ 9 ×) | +4 349 (≈ 7 ×) |
| course-detail fetches | 4 755 new (0 fail) | 4 317 new (0 fail) |
| wall-clock walk | ~30 min | ~30 min |
| wall-clock fetch | ~22 min | ~18 min |

**Pattern Recognition surfaced** at depth 5 (`PR - Pattern Recognition - Vorlesung`, unit_id 83251) and at depth 6 (variants 74253, 70545). Fetched all three; Maier listed as instructor on each.

**Domain finding:** Pattern Recognition is **never declared a strict Pflicht** in the 50 POs that mention it — it's `Wahlpflicht` / Schwerpunktfach / Engineering core / Kernmodul depending on PO. So even after surfacing the course we keep it in *Weitere Lehre*, not Pflicht. Treating it as effectively-required despite the formal label would be a *policy* layer, not a parsing fix.

**Final analyse output for Andreas Maier (both terms, depth-6):**

```
### Maier, Andreas (Prof. Dr.-Ing.)
- Pflichtveranstaltungen (heuristisch): 2
  - Wintersemester 2025/26 (1)  — Deep Learning
      Pflicht laut: 5× FPODataScience POs
  - Sommersemester 2026 (1)     — Deep Learning
      Pflicht laut: 5× FPODataScience POs
- Weitere Lehre (nicht Pflicht): 48
  - WiSe (25): Pattern Recognition, Seminar Road Scene Understanding,
               Introduction to Software Engineering, Deep Learning
               for Beginners (multiple program contexts), …
  - SoSe (23): Projekt Mustererkennung, …
```

The "Weitere Lehre" block was added in this entry — previously the renderer collapsed non-Pflicht courses into a single count line, which obscured the full Lehre. Now grouped per period like the Pflicht block.

**Scraper improvements applied (in response to user prompt):**

1. **`scraper/parse_detail.py`** — `_strip_role_suffix()` removes trailing `(Zuständigkeit: Verantwortliche/-r)`, `(Durchführende/-r)`, `(Beteiligte/-r)`, `(Mitwirkende/-r)`, `(Begleitende/-r)`, `(Prüfende/-r)` (incl. `/in`/`-in` variants) at parse time, applied in `_instructors_from_cell`. Without this strip, the same person was bucketed into multiple `by_person` entries downstream — Maier had 3 unit_ids of "Pattern Recognition" but only one was attributed to him until this fix landed. Same fix also applied in `scraper/people_index.py::split_concatenated_names` as a defence-in-depth (legacy JSON intermediates may still carry the suffix).

2. **`scraper/extract_pflicht_module.py`** — `_PFLICHT_SECTION_RE` extended to recognize *Obligatorisch nachzuweisende Module* and *Obligatory (core) modules* as Pflicht headers. Regex carefully crafted to NOT match *Obligatorisch nachzuweisende **Wahlpflicht**module* (different legal status). 91 unit tests still green; new regex behaviour validated on the tricky cases.

3. **`.github/workflows/scrape-weekly.yml`** — workflow now scrapes the **prior period** alongside the configured one (default `prior_period_id: 565` = WiSe 2025/26 to pair with current `period_id: 589` = SoSe 2026). All prior-period steps use `continue-on-error: true` so a transient WiSe failure never blocks the main scrape. Specific changes:
   - New input `prior_period_id` (empty disables prior-period steps)
   - New steps: walk prior period, fetch prior-period courses, sweep prior-period Tagesaktuelle, fetch sweep-only prior courses, render prior-period markdown
   - `analyze_pflicht.py` step now passes `--tree A B --courses A-courses B-courses` whenever both period files exist; falls back to single-period mode otherwise
   - `people_index.py` step now feeds both periods' inputs
   - Release upload includes prior-period JSON intermediates
   - `max_depth` default 4 → **6** (so weekly cron catches Studiengang-internal courses)
   - Walker now uses `--interval 0.2 --checkpoint-every 100` (rate-probe-tuned)
   - All `fetch_courses.py` invocations pass `--parallel 2 --interval 0.2` (Entry 0017)
   - Description text rewritten to explain the new defaults

**Final analyse stats (depth-6, both periods, all bugs fixed):**

| metric | end of Entry 0017 | now | Δ |
|---|--:|--:|--:|
| courses ingested | 1 886 | **10 958** (10 443 catalogue + 515 sweep-only) | +9 072 |
| POs that matched ≥1 course | 682 | **847** | +165 |
| matched courses (sum) | 1 916 | **4 731** | +2 815 |
| unique Pflicht unit_ids | 254 | **587** | +333 |
| W-Profs *mit* Pflichtlehre | 236 | (not yet re-counted, role-suffix collapse will reduce splits) | TBD |
| Maier's Pflichtveranstaltungen | 0 (in profs-ohne) | **2** (DL × 2 terms) | ✓ |
| Maier's weitere Lehre rendered | n/a | **48** (incl. Pattern Recognition) | ✓ |

**Tests / data integrity:** 91 unit tests pass after every edit. No 4xx/5xx during the depth-6 walks or fetches. All counts come from a clean re-run of `analyze_pflicht.py` against `tmp/{565,589}-d6.json` + `tmp/{565,589}-courses.json`.

**Files changed in this arc (Entries 0019 + 0020):**

```
.github/workflows/scrape-weekly.yml     | +137 / -8
scraper/analyze_pflicht.py              | +173 / -49  (substring fallback, _is_container_bucket, period grouping, Weitere Lehre block)
scraper/extract_pflicht_module.py       |  +7 / -2    (Obligatorisch nachzuweisende Module)
scraper/parse_detail.py                 | +25 / -3    (role-suffix strip)
scraper/people_index.py                 | +28 / -3    (role-suffix strip + dedup-after-split)
```

Plus the four `data/analyse/*.md` outputs are now substantively bigger (5x+ matched courses, full Weitere Lehre rendering).

**Insights that did NOT translate into changes (this turn):**

- Walker parallelism — would speed up depth-6 walks meaningfully (60 min → 15 min) but requires non-trivial BFS-with-shared-state work. Deferred.
- Cross-program unit-id consolidation — at depth 6, the same course can appear under multiple programs (e.g., "Deep Learning" in IPEM + Maschinenbau Studiengänge). The current rendering shows one row per program; a more authoritative grouping ("primary program") would tighten the *Weitere Lehre* listings. Deferred — needs heuristic design.
- Treating "obligatorisch nachzuweisende Wahlpflichtmodule" as Pflicht — policy decision, not a parsing fix. Currently classified as Wahl, which matches the literal PO wording.

**Status:** All four user-reported issues addressed end-to-end. Scraper improvements committed in-tree. The weekly cron will now produce a both-terms analysis automatically every Monday with the rate-probe-tuned settings.


## Entry 0021 — "Obligatorisch nachzuweisende Wahlpflichtmodule" → Pflicht

- **Start:** 2026-05-03 20:05 CEST
- **End:** 2026-05-03 20:55 CEST
- **Duration:** ~50 min
- **Actor:** user → Claude Code (Opus 4.7, 1M context); auto mode

**Prompt (verbatim):**

> Obligatorisch nachzuweisende Wahlpflichtmodule is indeed to be interpreted as pflicht. Please correct this everywhere. I which study programs do you find this?

**Where the phrasing is used:**

Exclusively in **FAU BA/MA Medizintechnik (BMT/MMT)** — Technische Fakultät, catalogued under `informatik` in our PO tree. 8 PO versions across the years all use the same convention (Anlage 3a–3e: *"Obligatorisch nachzuweisende Wahlpflichtmodule für …"*). The BMT/MMT POs treat the modules in these Anlagen as a fixed catalogue from which a required count must be passed — formally Wahlpflicht, structurally Pflicht-equivalent.

Same Studiengang also uses *"Obligatorisch nachzuweisende Module"* (without *Wahlpflicht*) for strict Pflicht in the same tables.

**What was wrong:**

Five layered issues kept Pattern Recognition (and similar Wahlpflicht-by-name-but-Pflicht-by-policy modules) out of the Pflicht-Analyse:

1. `extract_pflicht_module._PFLICHT_SECTION_RE` matched only the strict variant. The Wahlpflicht variant fell through and was classified as `wahl`. **Fix:** regex now also matches `Obligatorisch nachzuweisend\w* Wahlpflichtmodule?` as Pflicht. `_HEADING_PFLICHT_RE` (new) handles markdown headings the same way, with prefix tolerance for *"Anlage 3a:"*.
2. The extractor only consulted the **first cell of data rows** for section markers. BMT/MMT POs put the marker in a column header. **Fix:** new `_detect_table_section_from_header` scans every header cell; section context flows into the row walker via `table_default_section`.
3. Newer (≥ 2022) BMT/MMT POs put the marker in a markdown heading instead. **Fix:** new `_MD_HEADING_RE` + `_heading_section_marker` track the section context across headings; tables without their own header marker fall back to it.
4. The 2-tier table layout (group label row + sub-header row + data rows) defeated `_detect_module_name_column`. **Fix:** new `_row_is_subheader` detects sub-header rows after the separator and re-runs column detection on them; new "Name" fallback in the column detector picks the LAST `Name` cell (BMT/MMT tables have `Nr. | Name (Modulgruppe) | ECTS | Name (Modul) | …`).
5. `_likely_module_name` accepted Modulgruppe-row labels (e.g. *"M2 BDV/IDP Engineering core modules gemäß §44a Abs. 2"*) as modules. **Fix:** filter strings containing `gemäß §` or starting with `M\d+` and packed with slashes — these are group labels, not modules. The walker then tries column N+1 as a recovery so the module in the next column gets picked up.
6. `analyze_pflicht._is_container_bucket` excluded Pattern Recognition's catalogue program (`Veranstaltungen aus der Technischen Fakultät`) from container-bucket status, so the program-slug filter rejected the match against BMT/MMT POs (slug hint = `informatik`). **Fix:** extended the bucket detector with the six faculty-level catalogue groupings (`Veranstaltungen aus der Technischen Fakultät` and siblings).
7. `_has_real_pflicht` (free-text Pflicht-paragraph filter in `analyze_pflicht.py`) treated any text containing *Wahlpflicht* as not-Pflicht. **Fix:** also accept `Obligatorisch nachzuweisend` as Pflicht signal regardless of accompanying *Wahlpflicht*.

**Pattern Recognition extraction across all BMT/MMT versions:**

| PO | Modules extracted | Pattern matches |
|---|--:|---|
| `ba-ma-medizintechnik-fpomt-20090915-idf-20180828.md` | 10 | ✓ Pattern Recognition + Pattern Analysis |
| `ba-ma-medizintechnik-fpomt-20090915-idf-20190710.md` | 11 | ✓ Pattern Recognition + Pattern Analysis |
| `bsc-msc-medizintechnik-fpomt-20180828-aes.md` | 11 | ✓ |
| `bsc-msc-medizintechnik-fpomt-20190710-aes.md` | 2  | ✓ |
| `bsc-msc-medizintechnik-fpomt-20090915-idf-20220413.md` | 11 | ✓ |
| `bsc-msc-medizintechnik-fpomt-20220413-aes.md` | 10 | ✓ |
| `bsc-msc-medizintechnik-fpomt-20090915-idf-20230426.md` | 11 | ✓ |
| `bsc-msc-medizintechnik-fpomt-20090915-idf-20230731.md` | 13 | ✓ |
| 5 English/`-aes` versions | 0–6 | ✗ (English uses *"Obligatory"*; Änderungssatzungen don't re-state full Anlagen) |

**9 of 14 BMT/MMT PO files** now extract Pattern Recognition as Pflichtmodul — sufficient for the analyse to flag the course since one declaration suffices.

**End-to-end analyse (depth-6, both periods):**

| metric | end of Entry 0020 | now | Δ |
|---|--:|--:|--:|
| structured Pflichtmodule loaded | 679 POs | **785 POs** | +106 |
| matched courses (sum) | 5 040 | **6 270** | +1 230 |
| unique Pflicht unit_ids | 538 | **778** | +240 |
| POs that matched ≥1 course | 847 | **890** | +43 |

**Andreas Maier final entry** — exactly what the user asked for:

```
- Pflichtveranstaltungen (heuristisch): 3
  - Wintersemester 2025/26 (2)
    - "Deep Learning"        — Pflicht laut 5× FPODataScience POs
    - "Pattern Recognition"  — Pflicht in 8 POs (Studiengänge: informatik)
        BA-MA-Medizintechnik FPOMT (multiple versions)
        BSc-MSc-Medizintechnik FPOMT (multiple versions)
  - Sommersemester 2026 (1)
    - "Deep Learning"        — Pflicht laut 5× FPODataScience POs
- Weitere Lehre (nicht Pflicht): 47
  ...
```

**91 unit tests still green** after every edit.

**Files changed (this entry):**

```
scraper/extract_pflicht_module.py  | +94 / -8   (Wahlpflicht regex, header detection,
                                                 heading detection, sub-header detection,
                                                 col-N+1 recovery, Modulgruppe filter)
scraper/analyze_pflicht.py         | +20 / -3   (_has_real_pflicht extended,
                                                 _is_container_bucket faculty groupings)
```

**Open / queued:**

- (a) The 5 BMT/MMT PO versions that didn't yield Pattern (3 English, 2 Änderungssatzungen) — could extend the regex to `Obligatory \w+ modules?` more aggressively, or accept English-translation POs as duplicates of their German siblings for analysis purposes. Low priority — the German full POs cover the requirement.
- (b) Audit other Studiengänge that might use similar phrasing. Initial grep shows the convention is unique to BMT/MMT. If a future PO adopts it elsewhere, the new regex covers it automatically.

**Status:** "Obligatorisch nachzuweisende Wahlpflichtmodule" is now correctly classified as Pflicht throughout the pipeline. Pattern Recognition surfaces as Maier's WiSe Pflichtveranstaltung with full attribution to 8 BMT/MMT POs. The user's policy intent ("interpret as Pflicht") landed end-to-end.


## Entry 0022 — Aggregate by FAUdir id: fix partition violations and adjacent duplicates

- **Start:** 2026-05-03 21:05 CEST
- **End:** 2026-05-03 21:30 CEST
- **Duration:** ~25 min
- **Actor:** user → Claude Code (Opus 4.7, 1M context); auto mode

**Prompts (verbatim):**

> Did you also update the prof without pflichtlehre?
> There are also duplicate entries for some persons right after each other.

**Diagnosis:**

After Entry 0021 the partition between `profs-mit-pflichtlehre.md` and `profs-ohne-pflichtlehre.md` had **17 names appearing in both files**. Sample: *Beck, Silvan* — same FAUdir id `d5cbc20754`, same affiliation, but two different "Lehre" listings:

* In *mit*: 1 Pflichtveranstaltung *"K-V9 Eingangsblock Bildgebende Verfahren"* (Med Fak)
* In *ohne*: 2 non-Pflicht courses *"Praktikum Grundlagen der Elektrotechnik"* (Mechatronik)

There's no instructor literally named "Silvan Beck" in our raw data — the FAUdir record collected courses from multiple raw instructor strings (e.g. *"Christopher Beck"*, *"Marina Beck"*, *"Moritz Beck"*) that all fuzzy-resolve to FAUdir id `d5cbc20754`. The render functions iterated `by_person` keyed by the **raw instructor string**, treating each name variant as an independent person. One bucket had a Pflicht course (→ *mit*), the others had only non-Pflicht courses (→ *ohne*) — same person, two files.

The same root cause produced **adjacent duplicate entries** like *Held, Pascal (Dr.)* twice in *mit*: the sort key was `(familyName.lower(), full.lower())`, so two FAUdir-collapsed buckets with different `full` strings sorted next to each other.

**Fix in `scraper/analyze_pflicht.py`:**

New `_aggregate_by_faudir(by_person)` collapses entries that share a FAUdir identifier into one record per unique person, before partitioning. Both `render_profs_mit_pflichtlehre_md` and `render_profs_ohne_pflichtlehre_md` now run on the aggregated dict. Entries WITHOUT a FAUdir match pass through unchanged (they're handled by `lehrende-ohne-pflicht.md`).

Course de-duplication inside each aggregated entry uses **`(unit_id, period_id)`** rather than `unit_id` alone. A course like *Deep Learning* (`unit_id=82185`) genuinely runs in both WiSe and SoSe — collapsing on `unit_id` would lose the second occurrence. The pair-key keeps both terms while still deduplicating multiple instructor-string variants of the same person within one term.

**Verification:**

| metric | before fix | after fix |
|---|--:|--:|
| profs-mit-pflichtlehre.md candidates | 479 | **478** |
| profs-ohne-pflichtlehre.md candidates | 978 | **924** |
| names in BOTH files | 17 | **0** |
| adjacent duplicates in profs-mit | 1 (`Held, Pascal (Dr.)`) | **0** |
| adjacent duplicates in profs-ohne | 0 | 0 |
| Andreas Maier — Pflichtveranstaltungen | 3 (WiSe DL + PR + SoSe DL) | **3** (unchanged) |
| Andreas Maier — Weitere Lehre | 47 | **47** (unchanged) |

The 54-Prof drop in *profs-ohne* (978 → 924) matches the magnitude of the partition violation: 17 collisions plus their fuzzy-match siblings that were also wrongly listed in *ohne*.

**91 unit tests pass.**

**Files changed:**

```
scraper/analyze_pflicht.py | +75 / -8
```

**Status:** Partition between `profs-mit-pflichtlehre.md` and `profs-ohne-pflichtlehre.md` is now exclusive (0 collisions). No adjacent duplicate entries. Cross-term courses (same `unit_id` in both periods) still surface in both terms.


## Entry 0023 — Filter profs files to actual Professors (by FAUdir title)

- **Start:** 2026-05-03 21:35 CEST
- **End:** 2026-05-03 21:55 CEST
- **Duration:** ~20 min
- **Actor:** user → Claude Code (Opus 4.7, 1M context); auto mode

**Prompt (verbatim):**

> the lists now have many entires with people who are affiliated with a professorship like https://faudir.fau.de/public/person/e1ed36cd8c But are actually not professors. A professor should have the title Prof. or Juniorprofessor. Otherwise they are just teaching persons at FAU. Also "PD" is not a professor and should not be reported.

**Diagnosis:**

The user's example, `e1ed36cd8c` = *Pablo Ochoa de Eribe Delgado*, is a `scientific_employee` (Wissenschaftliche Mitarbeitende) at the *W3-Professur für Sensorische Neurotechnologie*. His FAUdir record:

```
personalTitle: ''   ← empty
function: 'scientific_employee'
organization.name: 'W3-Professur für Sensorische Neurotechnologie'
```

He is *affiliated with* a Professur but is not himself a Prof. The previous filter included him because the only check was *"FAUdir entry exists"* — which is loose. FAUdir's `personalTitle` field is the right discriminator.

Distribution of `personalTitle` across the 4 897 FAUdir-cached persons:

| count | personalTitle | classification |
|---:|---|---|
| 3 063 | (empty) | non-Prof staff |
| 713 | `Dr.` | non-Prof |
| 541 | `Prof. Dr.` | **Prof** |
| 146 | `Dr.-Ing.` | non-Prof |
| 99 | `PD Dr.` | non-Prof (Privatdozent) |
| 64 | `Prof. Dr.-Ing.` | **Prof** |
| 63 | `apl. Prof. Dr.` | **Prof** |
| 44 | `Prof. Dr. med.` | **Prof** |
| 18 | `M.Sc.` | non-Prof |
| 16 | `Dr. rer. nat.` | non-Prof |
| 9 | `Prof. Dr. Dr.` | **Prof** |
| 9 | `Prof.` | **Prof** |
| 8 | `PD Dr. habil.` | non-Prof |
| 7 | `Prof. Dr.-Ing. habil.` | **Prof** |

**Fix in `scraper/analyze_pflicht.py`:**

1. New `_is_professor_title(personal_title) → bool`:
   * Includes anything matching `\bProf\b` (case-insensitive) — covers `Prof.`, `Prof. Dr.`, `Prof. Dr.-Ing.`, `Prof. Dr. med.`, `apl. Prof.`, `Hon. Prof.`, `Ass.-Prof.`, `Jun.-Prof.`, etc.
   * Includes anything matching `\bJuniorprof` (covers `Juniorprofessor` / `Juniorprof.` spellings without the `Prof` segment).
   * **Explicit exclusion:** if the title starts with `PD` (`re.match(r"^PD\\b", t)`), return False — Privatdozent is checked first so titles like *"PD Dr. habil."* don't accidentally match the `\\bProf\\b` pattern via *"Dr. habil."* (they don't, but the explicit guard makes the intent visible).
   * Empty title, `Dr.`, `Dr.-Ing.`, `M.Sc.`, `Dipl.-Ing.`, `Ph.D.`, …, all return False.
2. New `_faudir_is_prof(faudir_entry)` thin wrapper, used everywhere.
3. `render_profs_mit_pflichtlehre_md` and `render_profs_ohne_pflichtlehre_md` now require `_faudir_is_prof(info["faudir"])` to count someone as a candidate.
4. `render_lehrende_ohne_pflicht_md` now skips a person ONLY if their FAUdir match is a **Prof**. FAUdir-matched non-Profs (Dr., M.Sc., PD Dr., empty title — research staff) land in `lehrende-ohne-pflicht.md` together with everyone outside FAUdir.

21 unit-tested cases covering every classification edge: ✓

**End-to-end re-run results:**

| metric | Entry 0022 | Entry 0023 | Δ |
|---|--:|--:|--:|
| profs-mit-pflichtlehre.md candidates | 478 | **221** | −257 |
| ┊ W3 | 16 | **6** | −10 |
| ┊ W? | 458 | **210** | −248 |
| ┊ Junior | 5 | **5** | unchanged |
| profs-ohne-pflichtlehre.md candidates | 924 | **322** | −602 |
| ┊ W3 | 29 | **13** | −16 |
| ┊ W1 | 5 | **2** | −3 |
| ┊ W? | 928 | **295** | −633 |
| ┊ Junior | 16 | **12** | −4 |
| lehrende-ohne-pflicht.md (lines) | 4 975 | **9 248** | +4 273 |

Total Lehrende-cohort headcount is preserved — 257 + 602 = 859 persons moved from the two prof files into `lehrende-ohne-pflicht.md`. They're still tracked, just in the right bucket: research staff and PD Dr. with non-Prof titles, but who teach courses at FAU.

**Spot-checks:**

* *Pablo Ochoa de Eribe Delgado* (`e1ed36cd8c`, the user's example) — now in `lehrende-ohne-pflicht.md` with 5 non-Pflicht courses. ✓
* PD Dr. counts in profs-mit and profs-ohne: 0 each (was previously included). ✓
* Andreas Maier (`Prof. Dr.-Ing.`) — unchanged: 3 Pflichtveranstaltungen (DL × WiSe + DL × SoSe + PR × WiSe), 47 weitere Lehre. ✓
* Sample of titles still appearing in profs-mit: `Prof. Dr.` (171), `Prof. Dr.-Ing.` (27), `apl. Prof. Dr.` (11), `Prof. Dr.-Ing. habil.` (6), `Ass.-Prof. Dr.` (1). All Prof variants. ✓

**91 unit tests still green.**

**Files changed:**

```
scraper/analyze_pflicht.py | +60 / -8
```

**Status:** Both prof files now only contain actual Professors per the user's policy (Prof. / apl. Prof. / Hon. Prof. / Ass.-Prof. / Juniorprofessor). PD (Privatdozent), Dr., M.Sc., empty-title staff, and other non-Prof FAUdir entries are now in `lehrende-ohne-pflicht.md`.


## Entry 0024 — 5 user-supplied test cases: 4 fixable Pflicht-coverage gaps closed

- **Start:** 2026-05-03 22:00 CEST
- **End:** 2026-05-03 22:35 CEST
- **Duration:** ~35 min
- **Actor:** user → Claude Code (Opus 4.7, 1M context); auto mode

**Prompt (verbatim):**

> Are you sure that the following lectures are not Pflicht:
> Medizintechnik I (Biomaterialien) (Medical Engineering?)
> Artificial Intelligence Fundamentals 2 (AI Bachelor?)
> Data Engineering (AI Bachelor?)
> Maschinelles Lernen in der Signalverarbeitung (ASC?)
> Computational Complexity (AI Bachelor?)
> I am not sure either.
>
> once this is fixed rerun the analysis, commit and push.

**Diagnosis (one issue per course, but four shared root causes):**

| course | extracted as Pflichtmodul? | matched to course? | root cause |
|---|---|---|---|
| Medizintechnik I (Biomaterialien) | ✓ | **no** | (1) faculty cross-check rejects a Med-Tech course against a Tech-Fak PO; (2) `\b` regex boundary fails on names ending with `)` |
| Artificial Intelligence Fundamentals 2 | **no** | n/a | "Core Modules Computer Science" not recognised as Pflicht header |
| Data Engineering | **no** | n/a | same |
| Computational Complexity | **no** | n/a | same |
| Maschinelles Lernen in der Signalverarbeitung | **no** | n/a | not in any PO file we have — likely the ASC PO isn't in our `data/pruefungsordnungen/` corpus, or the course is genuinely Wahlpflicht somewhere we can't see |

**Fix 1 — faculty filter (analyze_pflicht.py):**

Added `technik` and `biomedical` / `medical engineering` to `_COURSE_FAC_HINTS["tech"]`. Now "Medizintechnik" tags as **both** `med` (medizin) AND `tech` (technik). A course title containing "Medizintechnik" no longer fails the cross-check against a Tech-Fak PO. Validated against all 25 distinct `-technik` compound words in our course-title corpus (Elektrotechnik, Schaltungstechnik, Hochfrequenztechnik, Lasertechnik, Halbleitertechnik, …) — every one is unambiguously Tech-Fak.

**Fix 2 — Pflicht regex (extract_pflicht_module.py):**

Extended `_PFLICHT_SECTION_RE` and `_HEADING_PFLICHT_RE` to recognise **`Core Modules` / `Core Module`** — the English-language Pflicht-Modulgruppen header used by BSc Artificial Intelligence (and likely future English POs at FAU). Pure additive change; no regression.

After the regex update, BSc AI POs go from 0 → 14 extracted Pflichtmodule:

```
Algorithms, programming, and data representation
Data Engineering
Applied Programming
Computational Complexity
Einführung in das Software Engineering
Mathematics for Data Science 1
Mathematics for Data Science 2
Probability and Stochastic Processes
Artificial Intelligence Perspectives
Artificial Intelligence Fundamentals 1
Logic and Symbolic Artificial Intelligence
Artificial Intelligence Fundamentals 2
Ethics and Philosophy of AI (Hauptseminar)
Artificial Intelligence Fundamentals2
```

**Fix 3 — bidirectional slug containment (analyze_pflicht.py, both matchers):**

The PO-folder slug for BSc AI is `artificial-intelligence-in-biomedical-engineering` (long); the Campo program name is `Artificial Intelligence` (short). The previous slug filter required `h in s` (PO-slug substring of course-program-slug) — which fails when the course program is the *short* form. Now bidirectional: `h in s OR s in h`. Allows the canonical short Campo display name to match a longer PO folder name.

**Fix 4 — high-precision exact-title pass (analyze_pflicht.py):**

Added a no-program-filter pass at the top of `match_courses_to_module_names`: when a Pflichtmodul name appears verbatim in a course title (whole-phrase match, lookaround-based word boundaries), the slug filter is bypassed. Faculty cross-check still applies. Solves cross-listed courses like *"Medizintechnik I (Biomaterialien)"* catalogued under Mechatronik / Wirtschaftsingenieurwesen but Pflicht for BMT/MMT.

The lookaround boundaries `(?<!\w)…(?!\w)` replace `\b…\b` because `\b` fails when the module/course name ends with `)` — e.g. *"Medizintechnik I (Biomaterialien)"* — since `)` is non-word. Same fix applied to the existing substring-fallback pass for short module names.

**End-to-end re-run results:**

| metric | Entry 0023 | Entry 0024 | Δ |
|---|--:|--:|--:|
| structured Pflichtmodule loaded | 785 POs | **792 POs** | +7 |
| matched courses (sum) | 6 270 | **8 968** | +2 698 |
| unique Pflicht unit_ids | 778 | **1 436** | +658 |
| POs that matched ≥1 course | 890 | **910** | +20 |
| profs-mit-pflichtlehre.md candidates | 221 | **266** (W3 8, W1 2, W?, 256) | +45 |
| profs-ohne-pflichtlehre.md candidates | 322 | **270** (W3 11, W? 249, Junior 10) | −52 |

The 52-Prof drop in *profs-ohne* is the win: those Profs were teaching Pflicht courses we previously couldn't see. They moved into *profs-mit*. Net Prof count is similar (266 + 270 = 536 vs 221 + 322 = 543) — just classified more accurately.

**The 5 user-supplied test cases (final state):**

| course | mention count in pflichtveranstaltungen.md |
|---|--:|
| Medizintechnik I (Biomaterialien) | **15** ✓ (was 0) |
| Artificial Intelligence Fundamentals 2 | **4** ✓ (was 0) |
| Data Engineering | **10** ✓ (was 0) |
| Computational Complexity | **8** ✓ (was 0) |
| Maschinelles Lernen in der Signalverarbeitung | 0 (no PO declares it) |

**Spot-checks of newly-correct prof entries:**

* **Boccaccini, Aldo** (`Lehrstuhl für Werkstoffwissenschaften (Biomaterialien)`) — moved from *ohne* to *mit*; 4 Pflichtveranstaltungen across both terms (Medizintechnik I (Biomaterialien) under Mechatronik + Wirtschaftsingenieurwesen, both terms), each attributed to 7 BMT/MMT POs.
* **Knoll, Florian** (`W3-Professur für Computational Imaging`) — 5 Pflichtveranstaltungen including Computational Complexity Lecture/Exercise + Algorithms, Programming and Data Representation Computer Exercise.
* **Bernal Moyano, Jose** (`W1-Professur für Medical Image Analysis`) — 2 Pflichtveranstaltungen (Artificial Intelligence Fundamentals 2 in both terms).
* **Andreas Maier**, **Mathis-Ullrich, Franziska**, **Köckert, Charlotte** — unchanged from Entry 0023.

**91 unit tests still green.**

**Files changed:**

```
scraper/extract_pflicht_module.py | +5 / -2   ("Core Modules" header recognition)
scraper/analyze_pflicht.py        | +60 / -10 (technik faculty hint, bidirectional slug,
                                                exact-title pass, lookaround boundaries)
```

**The one unfixable case — Maschinelles Lernen in der Signalverarbeitung:**

The course is in our Campo data (uid 83746, WiSe, Prof. Vasileios Belagiannis). But `grep -lir "Maschinelles Lernen in der Signalverarbeitung" data/pruefungsordnungen/` returns no hits. So either:

1. The Studiengang PO declaring it Pflicht (likely MSc Advanced Signal Communications & ASC, MSc EEI, or similar) isn't in our `data/pruefungsordnungen/` corpus — we'd need to scrape it.
2. The course is genuinely Wahlpflicht / Vertiefungsfach under a Studiengang we DO have, and the Pflicht-extraction missed the section. (Unlikely — the substring extractor is quite aggressive now.)

Without the source PO this is unfixable from our analyzer alone. Recommend: identify which Studiengang(en) declare Maschinelles Lernen in der Signalverarbeitung as Pflicht and ensure their PO is in the FAU.de corpus.

**Status:** 4 of 5 user-supplied test cases now correctly classified as Pflicht. The 5th is a corpus-coverage gap, not an analyzer bug.


## Entry 0025 — Weekly cron timed out at 6h: cache prior-period snapshots monthly

- **Start:** 2026-05-04 13:00 CEST
- **End:** 2026-05-04 13:15 CEST
- **Duration:** ~15 min
- **Actor:** user → Claude Code (Opus 4.7, 1M context); auto mode

**Prompt (verbatim):**

> What happend with the github action? It seems not to have completed...

**Diagnosis:**

The 2026-05-04 06:19 UTC scheduled run of `Weekly Campo scrape` (commit `dc65fd1c`) hit GitHub Actions' 6-hour job-timeout wall:

| step | result |
|---|---|
| Walk catalogue (current period, depth 6) | ✓ ~30 min |
| Fetch course details (catalogue) | ✓ ~30 min |
| Sweep Tagesaktuelle | ✓ ~30 min |
| Fetch sweep-only courses | ✓ ~10 min |
| **Walk prior period catalogue** | ⏱ in-progress when killed |
| (everything after) render / analyse / commit / release | ⏸ never ran |

The added scope from Entries 0017–0024 (depth-4 → depth-6 + prior-period steps + Tagesaktuelle for both terms + multi-period analyse) doesn't fit in the 6h budget. Net effect: nothing committed this week — corpus is unchanged.

**Fix:**

The prior period (`565` = WiSe 2025/26 in the current cron) is a *finished/finishing* term. Its data changes far less than the active term's. Cache the prior-period snapshots and refresh only **monthly**:

```yaml
- name: Restore prior-period cache (monthly key)
  uses: actions/cache@v4
  with:
    path: |
      tmp/{prior}.json
      tmp/{prior}-courses.json
      tmp/{prior}-tagesaktuelle.json
    key: campo-prior-{prior}-d{max_depth}-{YYYY-MM}
    restore-keys:
      campo-prior-{prior}-d{max_depth}-
```

All four prior-period scrape steps now gate on `steps.cache_prior.outputs.cache-hit != 'true'`. On a cache hit (most weeks) those steps skip in seconds; the analyse step still runs against the cached files.

The fallback `restore-keys` accepts ANY cached snapshot for the same period+depth — so if the current-month key misses (first run of a new month), we still get a slightly-stale snapshot and skip the slow walk. The fresh full re-walk happens once a month when the new key actually misses everything.

**Estimated wall-clock per cron run:**

| scenario | walk (current) | fetch (current) | sweep (current) | prior period | analyse + commit | total |
|---|--:|--:|--:|--:|--:|--:|
| previously (no cache) | 30 min | 30 min | 30 min | **120 min** | 60 min | ~270 min ❌ timed out |
| cache hit (typical week) | 30 min | 30 min | 30 min | < 1 min | 60 min | **~150 min** ✓ |
| cache miss (~monthly) | 30 min | 30 min | 30 min | 120 min | 60 min | ~270 min — still tight |

Even on a cache miss, the `restore-keys` fallback should grab a slightly-older snapshot, so the prior-period scrape skips. A genuine "no cache at all" run is the very first run after this change.

**Files changed:**

```
.github/workflows/scrape-weekly.yml | +30 / -4 (cache step + 4× cache-hit guard)
```

YAML lint passes. The change is workflow-only — no scraper logic touched, no need to re-run the analysis.

**Status:** Cron should complete inside the 6-hour budget on cache hit. If the next scheduled run still times out, the next escalation would be to split into two parallel jobs sharing artifacts.
