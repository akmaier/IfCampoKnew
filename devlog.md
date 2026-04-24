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
