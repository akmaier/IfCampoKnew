# IfCampoKnew

*If Campo knew what Campo knows.*

An **AI-readable markdown corpus** built from the public parts of [FAU Campo](https://www.campo.fau.de/), [fau.de's Studiengang pages](https://www.fau.de/studium/studienangebot/alle-studiengaenge/), and FAU's [Prüfungsordnungen](https://www.fau.de/universitaet/universitaetsorganisation/rechtliche-grundlagen/pruefungsordnungen/) (PDFs converted to markdown). The name riffs on the old Siemens saying "if Siemens knew what Siemens knows" — Campo already exposes a lot, but its JSF UI makes it hard to actually find anything. We turn that public surface into a flat list of merged-per-program markdown files an LLM agent can navigate.

**Status:** SoSe 2026 corpus complete. **One merged file per Campo study program** (FAU.de Studiengang content + every PO-version + every course inlined), plus the full PO regulation texts as separate large files. Weekly + monthly crons keep it fresh.

## Download the corpus

Each weekly run cuts a [GitHub Release](https://github.com/akmaier/IfCampoKnew/releases/latest) tagged `snapshot-YYYY-Www` with **`ifcampoknew-corpus-{period-slug}.zip`** as the asset — a single self-contained markdown corpus ready to drop into a RAG system. Start with `README.md` inside the zip; it explains the layout and stable-id conventions to the agent.

## What this repo is

A self-contained markdown corpus + the Python tooling that builds it. Three public sources, **one merged corpus**:

```
data/
├── README.md                                 # RAG usage guide (also at the zip root)
├── {period-slug}/                            # Campo course catalogue per semester
│   ├── INDEX.md                              # programs grouped by section
│   └── {program-slug-id}.md                  # ★ ONE merged file per program:
│                                             #   • FAU.de Studiengang inline (Steckbrief, sections)
│                                             #   • every PO-version with permalinks + dated PDFs
│                                             #   • every course (Eckdaten + Termine + instructors)
│                                             #   • Lehramts-Prüfungsordnungen (when applicable)
├── studiengang/                              # FAU.de Studiengang pages (raw, also inlined above)
│   └── {slug}.md
└── pruefungsordnungen/                       # full PO regulation texts (10–30 k tok each)
    └── {faculty}/{program}/{po-slug}.md
```

Slugs are Campo/FAU-faithful German with ASCII-folded umlauts (`ä→ae`, `ß→ss`); every Campo basename ends in `-<segmentId>` so links survive renames. Every file carries `campo_permalink` / `source_url` / `pdf_source` in its YAML front-matter so a RAG can cite the original source.

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

# Campo (per-semester catalogue + course detail + merged-program render)
scraper/.venv/bin/python scraper/scrape.py        --period 589 --out tmp/589.json --max-depth 4 -v
scraper/.venv/bin/python scraper/fetch_courses.py --in tmp/589.json --out tmp/589-courses.json -v
scraper/.venv/bin/python scraper/render_markdown.py --in tmp/589.json --courses tmp/589-courses.json --out data

# FAU.de (programs + Prüfungsordnungen — single-script pipeline)
scraper/.venv/bin/python scraper/fau_corpus.py --out data --tmp tmp/fau-pdfs -v

# Re-render once you have FAU files on disk so they get inlined:
scraper/.venv/bin/python scraper/render_markdown.py --in tmp/589.json --courses tmp/589-courses.json --out data

# Build a corpus zip locally
( cd data && zip -r -q ../ifcampoknew-corpus.zip . )
```

Browse the result under `data/`.

## Roadmap

| Phase | Status | What it covers |
|------|:------:|----------------|
| Public-surface analysis | ✅ | What Campo exposes anonymously; HTTP/JSF mechanics; deep-link patterns. |
| Requirements (v1 → v2 pivot) | ✅ | v1 was a Web Components UI; v2 is the markdown corpus. |
| Catalogue scrape (Campo) | ✅ | depth-4 BFS: 1 895 nodes for SoSe 2026, with checkpoint/resume. |
| Course-content attachment | ✅ | Fetch every Course's *Termine + Eckdaten + Lehrende*; 683/683 for SoSe 2026. |
| FAU.de Studiengang corpus | ✅ | 222 programs scraped; content inlined into the matching Campo program file. |
| FAU.de Prüfungsordnungen corpus | ✅ | 36 landing pages + ~2 800 PDFs converted to markdown via PyMuPDF4LLM. |
| Cross-link Campo ↔ FAU.de | ✅ | Each program file inlines its FAU.de Studiengang page and references the matched dated PO-PDFs. |
| Merge into one file per program | ✅ | Entry 0013 redesign: 1 654 → 236 files for SoSe 2026; flat `{period}/{program}.md` layout, max 2 levels deep. |
| Weekly GitHub Action — Campo | ✅ | Mondays 03:00 UTC: scrape, render, commit, build zip, cut a Release with the zip + JSON intermediates. |
| Monthly GitHub Action — FAU.de | ✅ | First of each month, 04:00 UTC; the next weekly run inlines the new content. |
| Full-depth catalogue walk | ⏸ | `--max-depth 0` is technically supported but a single GH-Actions job hits the 6-h timeout. A daily-resume chain is the next available step if and when deeper data turns out to be needed. |
| Archive prior years | later | `archive/{year-slug}/` per completed academic year. |

See [`docs/requirements.md` §9](docs/requirements.md) for the full plan and open items (token-counting library, course-association strategy, next semester's `periodId`).

## Scope

Only **public** Campo data is in scope. Anything that needs a FAU login (personal schedule, grades, exam registrations, enrolments) is explicitly out — and out forever, because the corpus is shipped publicly on GitHub.

## License

[MIT](LICENSE) © Andreas Maier.

The Campo data the corpus references (titles, schedules, descriptions) remains FAU's. Permalinks to Campo are preserved on every file so attribution and source-of-truth are one click away.
