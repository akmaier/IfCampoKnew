# IfCampoKnew

*If Campo knew what Campo knows.*

An **AI-readable markdown corpus** built from the public parts of [FAU Campo](https://www.campo.fau.de/). The name riffs on the old Siemens saying "if Siemens knew what Siemens knows" — Campo already exposes a lot, but its JSF UI makes it hard to actually find anything. We turn that public surface into a hierarchical tree of markdown files an LLM agent can navigate.

**Status:** depth-4 catalogue skeleton committed for **Sommersemester 2026**. Course-level content (Termine, Inhalte, instructors) is the next milestone.

## What this repo is

A self-contained markdown corpus + the Python tooling that builds it. Browse on github.com or feed the files to an agent.

```
data/{period-slug}/
    INDEX.md                                   # root: links to all sections
    {section-slug-id}/
        INDEX.md                               # section: links to programs
        {program-slug-id}/
            INDEX.md                           # program: links to PO-versions
            {po-version-slug-id}.md            # leaf: course-level content (phase 2)
        {program-slug-id}.md                   # leaf-program (no PO sub-tree)
```

Slugs are Campo-faithful German with ASCII-folded umlauts (`ä→ae`, `ß→ss`); every basename ends in `-<segmentId>` so links survive Campo renames.

## Why a markdown corpus, not a website?

Original plan was a Web Components SPA on GitHub Pages. After analysis we realised: the LLM agent already does what an SPA's UI does. Drop the UI, ship the data in the form an agent eats best — markdown — and let agents (or `github.com`'s native renderer) be the front end. Web Components, FlexSearch, onboarding quiz, telemetry: all gone. The corpus *is* the product.

## Repository contents

| Path | What's in it |
|---|---|
| [`data/`](data/) | The corpus. One folder per scraped semester. **The deliverable.** |
| [`scraper/`](scraper/) | Python pipeline: catalogue walk → JSON intermediate → markdown render. See [`scraper/README.md`](scraper/README.md). |
| [`docs/campo-public-surface.md`](docs/campo-public-surface.md) | Inventory of every Campo page/flow reachable without logging in, plus the working POST recipe and deep-link patterns we use. |
| [`docs/requirements.md`](docs/requirements.md) | v2-locked requirements (markdown-corpus pivot, decisions log, open items). |
| [`devlog.md`](devlog.md) | Chronological log of every prompt → actions → findings → time spent. |
| [`tmp/`](tmp/) | *(gitignored)* JSON snapshots from the scraper, regenerated each run. |

## Quick start

```bash
# install
python3 -m venv scraper/.venv
scraper/.venv/bin/pip install -r scraper/requirements.txt

# scrape SoSe 2026 catalogue tree (≈12 GETs at 1 req/s ≈ 15 s for depth 4)
scraper/.venv/bin/python scraper/scrape.py \
    --period 589 --out tmp/589.json --max-depth 4 -v

# render to markdown
scraper/.venv/bin/python scraper/render_markdown.py \
    --in tmp/589.json --out data
```

Browse the result in `data/589-sommersemester-2026/`.

## Roadmap

| Phase | Status | What it covers |
|------|:------:|----------------|
| Public-surface analysis | ✅ done | What Campo exposes anonymously; HTTP/JSF mechanics; deep-link patterns. |
| Requirements (v1 → v2 pivot) | ✅ locked | v1 was a Web Components UI; v2 is the markdown corpus. |
| Catalogue skeleton (depth 4) | ✅ done | 1 895 nodes for SoSe 2026; folders + INDEX.md + leaf placeholders. |
| Full-depth catalogue walk | ⏳ next | `--max-depth 0` to bottom out every `exam:` chain; run via GitHub Action. |
| Course content attachment | ⏳ next | Fetch each course's *Termine + Inhalte + Module memberships*, embed in the corpus. |
| F-TOKEN bucket policy | ⏳ | Merge thin / split thick content files into 10–30 k-token chunks. |
| Weekly GitHub Action | ⏳ | Mondays 03:00 UTC: scrape, render, commit, cut a Release. |
| Archive prior years | later | `archive/{year-slug}/` per completed academic year. |

See [`docs/requirements.md` §9](docs/requirements.md) for the full plan and open items (token-counting library, course-association strategy, next semester's `periodId`).

## Scope

Only **public** Campo data is in scope. Anything that needs a FAU login (personal schedule, grades, exam registrations, enrolments) is explicitly out — and out forever, because the corpus is shipped publicly on GitHub.

## License

[MIT](LICENSE) © Andreas Maier.

The Campo data the corpus references (titles, schedules, descriptions) remains FAU's. Permalinks to Campo are preserved on every file so attribution and source-of-truth are one click away.
