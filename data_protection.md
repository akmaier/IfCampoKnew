# Datenschutz / Data Protection

This repository publishes an AI-readable markdown corpus built from the
**public, non-authenticated** parts of FAU's Campo course catalogue,
the [fau.de Studiengang pages](https://www.fau.de/studium/studienangebot/alle-studiengaenge/),
and the [Prüfungsordnungen (PO)](https://www.fau.de/universitaet/universitaetsorganisation/rechtliche-grundlagen/pruefungsordnungen/).
Public availability of a source does **not** by itself remove GDPR
duties from the re-publisher — the aggregate is a separate processing
operation. This document records what we do and do not publish, and how
to reach us for erasure/rectification requests.

## Datenminimierung (Art. 5 Abs. 1 lit. c DSGVO)

The RAG use-case this corpus serves — answering questions about study
programs, modules, and Prüfungsordnungen — does not need personal
data. The scraper and its published output are therefore configured to
carry **no personal data by construction**:

* **No FAUdir Professor:innen-Index** is generated or published
  (formerly under `data/personen/`).
* **No aggregated teaching-load profiles** per person are generated or
  published (formerly `data/analyse/profs-pflichtlehre.md`,
  `data/analyse/lehrende-ohne-pflicht.md`,
  `data/analyse/pflichtveranstaltungen.md`).
* **No instructor names** are emitted inside course pages under
  `data/{period}/*.md`: the `## Lehrende` bullets
  (`Verantwortlich:` / `Durchführend:`) are omitted, and the
  `Dozent/-in` column of Termine tables is dropped.
* **No email addresses or phone numbers** are emitted anywhere in the
  corpus: `…@fau.de` / `…@uni-erlangen.de` and DE-format phone
  numbers are stripped from the entire tree.
* **No standalone contact-person lines** are emitted in
  `data/studiengang/*.md` (a standalone `Prof. Dr. …` line, typical
  of the FAU Studiengang contact block, is replaced with a
  placeholder). Prose mentions of names inside sentences are left
  alone so the meaning of the surrounding text survives.
* **PO regulation texts** under `data/pruefungsordnungen/**` retain
  their prose — official Bavarian legal texts routinely reference
  named office holders — but any email/phone in them is stripped.
* **Raw JSON intermediates** (`*-courses.json` from Campo) are
  no longer uploaded to GitHub Releases; they carry raw
  `instructors_resp` / `instructors_exec` / appointment-instructor
  fields.

The enforcement is layered so a future scraper change cannot silently
leak personal data:

1. `scraper/render_markdown.py` never emits instructor fields.
2. `scraper/sanitize_corpus.py` sweeps `data/**/*.md` after every
   render, then re-scans in `--check-only` mode; a hit fails the
   GitHub Actions job.
3. `scraper/tests/test_sanitize_corpus.py` unit-tests every rule.
4. The `data/personen/` folder and the person-oriented
   `data/analyse/*` files, plus the scripts that generated them
   (`scraper/faudir_scrape.py`, `scraper/people_index.py`,
   `scraper/analyze_pflicht.py`), have been removed from the working
   tree and from the git history.

## Aufbewahrung / Retention

* The corpus under `data/` is re-generated **weekly** (Campo scrape)
  and **monthly** (FAU.de / PO scrape). Each run replaces the
  previous week's or month's snapshot, so the working tree always
  reflects the latest run.
* No personal-data snapshots are retained. Historical git commits
  that pre-date the 2026-08 DSGVO sweep have been rewritten to remove
  the person-carrying files and the inlined names; historical GitHub
  Releases that included personal data have been re-cut without those
  assets.
* Any residual derived artefacts (workflow logs, cache blobs) are
  deleted at the latest **one year** after they were created.

## Rechtsgrundlage (Legal basis)

The processing is performed in the context of the University's public
task (Art. 6 Abs. 1 lit. e DSGVO in Verbindung mit dem Bayerischen
Hochschulinnovationsgesetz (BayHIG) und dem Bayerischen
Datenschutzgesetz (BayDSG)).

**Final confirmation of the concrete legal basis and this data
protection notice is subject to review by the FAU Datenschutz-
beauftragte / behördliche Datenschutzbeauftragte der FAU.**

## Kontakt / Contact for erasure & rectification

Verantwortlich für das Repository:

Prof. Dr. Person D  
Friedrich-Alexander-Universität Erlangen-Nürnberg  
E-Mail: <andreas.maier@fau.de>

Auskunfts-, Berichtigungs-, Löschungs- und Widerspruchsrechte
(Art. 15–21 DSGVO) können über diese Adresse ausgeübt werden.

Für die formal-rechtliche Datenschutz-Aufsicht der FAU:
Behördliche Datenschutzbeauftragte der FAU,
<https://www.datenschutz.fau.de/>.
