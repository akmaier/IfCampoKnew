# IfCampoKnew

*If Campo knew what Campo knows.*

An **AI-readable markdown corpus** built from the public parts of [FAU Campo](https://www.campo.fau.de/). The name riffs on the old Siemens saying "if Siemens knew what Siemens knows" — Campo already exposes a lot, but its JSF UI makes it hard to actually find anything. We turn that public surface into a hierarchical tree of markdown files an LLM agent can navigate.

**Status:** depth-4 catalogue skeleton committed for **Sommersemester 2026**. Course-level content (Termine, Inhalte, instructors) is the next milestone.

## What this repo is

A self-contained markdown corpus + the Python tooling that builds it. Three sources, one corpus:

```
data/
├── {period-slug}/                            # Campo course catalogue per semester
│   ├── INDEX.md                              # root: links to all sections
│   ├── {section-slug-id}/
│   │   ├── INDEX.md                          # section: links to programs
│   │   └── {program-slug-id}/
│   │       ├── INDEX.md                      # program: links to PO-versions
│   │       ├── {po-or-course-slug-id}.md     # PO-version OR full course content
│   │       └── …
│   └── …
├── studiengang/                              # FAU.de program info pages (222 programs)
│   ├── INDEX.md
│   └── {slug}.md                             # ~3-5k tok per program
└── pruefungsordnungen/                       # FAU.de Prüfungsordnungen + PDFs
    ├── INDEX.md
    └── {faculty}/{program}/
        ├── INDEX.md                          # landing page (intro + PDF list)
        └── {pdf-slug}.md                     # converted PDF (10-30k tok typical)
```

Slugs are Campo/FAU-faithful German with ASCII-folded umlauts (`ä→ae`, `ß→ss`); every Campo basename ends in `-<segmentId>` so links survive renames.

## Why a markdown corpus, not a website?

Original plan was a Web Components SPA on GitHub Pages. After analysis we realised: the LLM agent already does what an SPA's UI does. Drop the UI, ship the data in the form an agent eats best — markdown — and let agents (or `github.com`'s native renderer) be the front end. Web Components, FlexSearch, onboarding quiz, telemetry: all gone. The corpus *is* the product.

## Repository contents

| Path | What's in it |
|---|---|
| [`data/{period-slug}/`](data/) | Campo per-semester corpus (catalogue tree + course detail). **The primary deliverable.** |
| [`data/studiengang/`](data/) | FAU.de Studiengang info — one markdown per program (222). |
| [`data/pruefungsordnungen/`](data/) | FAU.de regulations — landing pages + each PO converted from PDF. |
| [`scraper/`](scraper/) | Python pipeline. See [`scraper/README.md`](scraper/README.md). |
| [`docs/campo-public-surface.md`](docs/campo-public-surface.md) | Inventory of every Campo page/flow reachable without logging in, plus the working POST recipe and deep-link patterns we use. |
| [`docs/requirements.md`](docs/requirements.md) | v2-locked requirements (markdown-corpus pivot, decisions log, open items). |
| [`devlog.md`](devlog.md) | Chronological log of every prompt → actions → findings → time spent. |
| [`tmp/`](tmp/) | *(gitignored)* JSON snapshots and downloaded PDFs, regenerated each run. |

## Quick start

```bash
# install
python3 -m venv scraper/.venv
scraper/.venv/bin/pip install -r scraper/requirements.txt

# Campo (per-semester catalogue + course detail)
scraper/.venv/bin/python scraper/scrape.py        --period 589 --out tmp/589.json --max-depth 4 -v
scraper/.venv/bin/python scraper/fetch_courses.py --in tmp/589.json --out tmp/589-courses.json -v
scraper/.venv/bin/python scraper/render_markdown.py --in tmp/589.json --courses tmp/589-courses.json --out data

# FAU.de (programs + Prüfungsordnungen — single-script pipeline)
scraper/.venv/bin/python scraper/fau_corpus.py --out data --tmp tmp/fau-pdfs -v
```

Browse the result under `data/`.

## Roadmap

| Phase | Status | What it covers |
|------|:------:|----------------|
| Public-surface analysis | ✅ | What Campo exposes anonymously; HTTP/JSF mechanics; deep-link patterns. |
| Requirements (v1 → v2 pivot) | ✅ | v1 was a Web Components UI; v2 is the markdown corpus. |
| Catalogue skeleton (depth 4) | ✅ | 1 895 nodes for SoSe 2026; folders + INDEX.md + leaf placeholders. |
| Course content attachment | ✅ | Fetch each course's *Termine + Eckdaten + Lehrende*, embed in the corpus (683/683 ok for SoSe 2026). |
| Weekly GitHub Action — Campo | ✅ | Mondays 03:00 UTC: scrape, render, commit, cut a Release. |
| FAU.de Studiengang corpus | ✅ | 222 programs, one markdown per page, with Steckbrief + sections + external links. |
| FAU.de Prüfungsordnungen corpus | ✅ | 36 landing pages + every linked PDF converted to markdown via PyMuPDF4LLM. |
| Monthly GitHub Action — FAU.de | ✅ | First of each month, 04:00 UTC. |
| Full-depth catalogue walk | ⏳ | `--max-depth 0` to bottom out every `exam:` chain; capture Tech/Nat/Med/RW Fak courses (deeper than 4). |
| F-TOKEN bucket policy | ✅ | Thin program folders fold into one merged file; course-bearing folders fold up to ~30 k tok; per-leaf Eckdaten + Termine inlined. SoSe 2026 went 1 654 → 742 files. |
| Cross-link Campo ↔ FAU.de | ✅ | Each Campo program-level INDEX.md links to matching `studiengang/{slug}.md` + PO landing folder; each PO-version leaf links to dated `pruefungsordnungen/.../{pdf}.md` files (year-matched). |
| Archive prior years | later | `archive/{year-slug}/` per completed academic year. |

See [`docs/requirements.md` §9](docs/requirements.md) for the full plan and open items (token-counting library, course-association strategy, next semester's `periodId`).

## Scope

Only **public** Campo data is in scope. Anything that needs a FAU login (personal schedule, grades, exam registrations, enrolments) is explicitly out — and out forever, because the corpus is shipped publicly on GitHub.

## License

[MIT](LICENSE) © Andreas Maier.

The Campo data the corpus references (titles, schedules, descriptions) remains FAU's. Permalinks to Campo are preserved on every file so attribution and source-of-truth are one click away.
