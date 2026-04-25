# scraper

Three-stage Python pipeline that turns the public Campo portal into the **markdown corpus** under [`../data/`](../data/) consumed by IfCampoKnew's downstream agents and tooling.

```
Campo HTML ─▶ scrape.py        ─▶ tmp/<period>.json
              fetch_courses.py ─▶ tmp/<period>-courses.json
              render_markdown  ─▶ data/<period-slug>/
                                  (committed)
```

The JSON files are internal intermediates only — they live in `tmp/` and are regenerated on every run. The deliverable is the markdown tree.

## Quick start

```bash
# 1. one-time
python3 -m venv scraper/.venv
scraper/.venv/bin/pip install -r scraper/requirements.txt

# 2. scrape the catalogue tree to JSON (4 levels = root → section → program → PO-version)
scraper/.venv/bin/python scraper/scrape.py \
    --period 589 --out tmp/589.json --max-depth 4 -v

# 3. fetch every course-detail page referenced from the tree
scraper/.venv/bin/python scraper/fetch_courses.py \
    --in tmp/589.json --out tmp/589-courses.json -v

# 4. render the JSON into the hierarchical markdown corpus
scraper/.venv/bin/python scraper/render_markdown.py \
    --in tmp/589.json --courses tmp/589-courses.json --out data
```

Result: `data/589-sommersemester-2026/INDEX.md` + nested folders/files for every catalogue node, with course-leaves carrying full Eckdaten + Termine + Organisation tables.

### Subset run (testing)

`fetch_courses.py --path-contains title:17991` only fetches courses whose catalogue path includes that segment — handy for working on a single section (e.g. `title:17991` = *Musizieren an der Universität*) without hitting Campo for the full set.

### Going deeper

```bash
scraper/.venv/bin/python scraper/scrape.py \
    --period 589 --out tmp/589-deep.json --max-depth 0 -v   # 0 = unlimited (hard cap 12)
```

Walks until every branch hits its true leaf (the deepest `exam:` sub-section). Expect **hundreds of GETs**, possibly an hour at the polite 1 req/s. Best run via the weekly GitHub Action, not interactively.

## CLI reference

### `scrape.py`

| flag | default | what it does |
|------|---------|--------------|
| `--period` | required | Campo `periodId` (e.g. `589` = Sommersemester 2026). |
| `--out` | required | path of the JSON snapshot. |
| `--max-depth` | `4` | BFS cap, root inclusive. `1` = root only, `4` = PO-versions, `0` = unlimited (hard-capped at 12 internally). |
| `--interval` | `1.0` | minimum seconds between requests. **Don't go below `0.5`** — it's the FAU-polite rate. |
| `-v` / `-vv` | — | log level: WARNING → INFO → DEBUG. |

### `render_markdown.py`

| flag | what it does |
|------|--------------|
| `--in` | path to a JSON snapshot from `scrape.py`. |
| `--out` | output root; the renderer creates `<out>/<period-slug>/…` underneath it. |

## Module map

| File | Purpose |
|------|---------|
| `campo_client.py`     | HTTP session bootstrap (start-page → JSESSIONID) + 1 req/s rate limit + 5xx retry. |
| `parse_tree.py`       | Catalogue HTML → `ParsedNode`s; pairs each leaf with its `unit_id` from the action-column `detailView` link. |
| `parse_detail.py`     | Course-detail HTML → `Course` (Eckdaten + Termine + instructors + org-units). |
| `schema.py`           | `CatalogNode`, `CatalogSnapshot`, `Course`, `Appointment` dataclasses + JSON shape. |
| `scrape.py`           | CLI: BFS walk of the catalogue. |
| `fetch_courses.py`    | CLI: GETs every unique `unit_id` referenced in the tree, parses to `Course`. |
| `render_markdown.py`  | JSON snapshots → hierarchical markdown corpus with stable, ASCII-folded German slugs. |
| `tests/`              | pytest fixtures (real Campo HTML) + unit tests for both parsers. Run with `pytest scraper/tests/`. |
| `requirements.txt`    | `requests`, `lxml`. |
| `requirements-dev.txt`| Adds `pytest`. |

## Notes for AI consumers / agents

- Every folder has an `INDEX.md` listing its children with one-line descriptions and Campo permalinks.
- Every catalogue node knows its `segment` (`title:17593`, `exam:14867623`) and full `path` from root.
- File slugs are deterministic — `<asciified-german-name>-<terminal-id>` — so links between files don't break across weekly scrapes when Campo renames a node.
- See [`../docs/campo-public-surface.md`](../docs/campo-public-surface.md) for the underlying HTTP / JSF semantics.
