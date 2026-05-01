# IfCampoKnew Corpus

This directory is an AI-readable markdown snapshot of FAU's public study data:

- the **Campo course catalogue** (one file per study program — see below);
- every linked **FAU.de Studiengang page** (inlined into the matching Campo program);
- every linked **Prüfungsordnung PDF**, converted to markdown and stored under
  [`pruefungsordnungen/`](pruefungsordnungen/INDEX.md) — the texts are typically
  10–30 k tokens each and are too large to inline, so program files reference
  them by relative link.

The corpus is regenerated weekly (Campo) and monthly (FAU.de), then attached
to a GitHub Release as a ZIP. See
[`https://github.com/akmaier/IfCampoKnew/releases/latest`](https://github.com/akmaier/IfCampoKnew/releases/latest).

## How a RAG system should consume this corpus

1. **Start at the period directory** — e.g. `589-sommersemester-2026/INDEX.md`.
   It groups every program by its Campo section ("Studiengänge der Technischen
   Fakultät", "Allgemeiner Wahlbereich", "FAU Scientia Gaststudium" …).
2. **One file per program is the unit of retrieval.** For example
   `589-sommersemester-2026/informatik-17949.md` is a self-contained answer
   surface for almost any question about the Informatik program in SoSe 2026:
   the FAU.de marketing page, every PO-version, every course event with its
   schedule and instructors, and links to the matching PO PDFs.
3. **The big regulation PDFs live separately.** When a user asks something
   that requires the legal text of a regulation (precise grading rules,
   admission requirements, allowed elective combinations) follow the link
   from the program file into the corresponding `pruefungsordnungen/…/*.md`.
4. **Every file carries source links** — both in the YAML front-matter
   (`campo_permalink`, `fau_studiengang_urls`, `pdf_source`) and inline as
   `<https://…>` Markdown autolinks. Use these to attribute answers and to
   send a curious user to the original source of truth.

### Stable identifiers

Every Campo node carries a `KIND:ID` segment. For programs and PO-versions
the segment is preserved on disk:
- file basename ends with `-<segmentId>` (e.g. `informatik-17949.md` for
  `title:17949`),
- the segment string is also in the front-matter (`campo_segment`).

This makes file paths stable across weekly scrapes — even if Campo renames
the program, the segment id (and hence the basename) does not change.

Course events carry `unit_id` instead. They appear inside program files as
`### Course Title — Type` sections with bullet lines that include
`Segment: exam:NNN`, `unitId: NNN`, and Campo / detail-view permalinks.

## Layout summary

```
.
├── README.md                          ← you are here
├── {period-slug}/                     ← one folder per scraped semester
│   ├── INDEX.md                       ← programs grouped by section
│   └── {program-slug-id}.md           ← one merged file per program
│                                        ┌── FAU.de Studiengang inline (Steckbrief, sections, links)
│                                        ├── PO-Versionen mit Permalinks + passenden PO-PDFs
│                                        ├── Veranstaltungen mit Eckdaten + Termine
│                                        └── Lehramts-Prüfungsordnungen (falls anwendbar)
├── pruefungsordnungen/                ← full PO regulation texts (one per PDF)
│   ├── INDEX.md
│   └── {faculty}/{program}/{po-slug}.md
├── studiengang/                       ← FAU.de Studiengang pages (raw, also inlined above)
│   ├── INDEX.md
│   └── {slug}.md
├── personen/                          ← aggregate of every Campo Lehrende
│   └── INDEX.md                       ← {N} unique person-strings × their courses
└── analyse/                           ← heuristic pre-computed analyses
    ├── pflichtveranstaltungen.md      ← Pflicht sections per PO + matched Campo courses
    └── lehrende-ohne-pflicht.md       ← Lehrende whose courses don't appear in any
                                          Pflicht-flagged set (Vergleich für RAG)
```

The two files in `analyse/` are **heuristic**. They exist as ground-truth
material for verifying RAG-driven answers to the same questions. If a RAG
agent and these files disagree, the agent is usually closer to truth
(it can reconcile naming variations PO-text → course-title that the
heuristic can't).

## Update cadence

| Source | Cron | Job |
|---|---|---|
| Campo catalogue + courses | Mondays 03:00 UTC | `.github/workflows/scrape-weekly.yml` |
| FAU.de Studiengang + PO PDFs | First of each month, 04:00 UTC | `.github/workflows/scrape-monthly-fau.yml` |

Each successful run pushes the regenerated corpus to `main`, cuts a Release
tagged `snapshot-YYYY-Www`, and uploads `ifcampoknew-corpus-{period-slug}.zip`
as the Release asset for direct download.

## Provenance

Built by the Python scraper in [`../scraper/`](../scraper/) — see that
directory's README for the underlying HTTP / JSF semantics and the
three-stage pipeline (`scrape.py` → `fetch_courses.py` →
`render_markdown.py`, plus `fau_corpus.py` for the FAU.de side).

The corpus content is FAU's. Permalinks back to Campo and FAU.de are on
every file; please honour the original sources when citing.
