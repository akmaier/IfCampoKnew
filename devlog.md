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

