# scraper

Two-stage Python pipeline that turns the public Campo portal into the **markdown corpus** under [`../data/`](../data/) consumed by IfCampoKnew's downstream agents and tooling.

```
Campo HTML ─▶ scrape.py ─▶ tmp/<period>.json ─▶ render_markdown.py ─▶ data/<period-slug>/
                            (gitignored)                                   (committed)
```

The JSON file is an internal intermediate only — it lives in `tmp/` and is regenerated on every run. The deliverable is the markdown tree.

## Quick start

```bash
# 1. one-time
python3 -m venv scraper/.venv
scraper/.venv/bin/pip install -r scraper/requirements.txt

# 2. scrape the catalogue tree to JSON (4 levels = root → section → program → PO-version)
scraper/.venv/bin/python scraper/scrape.py \
    --period 589 --out tmp/589.json --max-depth 4 -v

# 3. render the JSON into the hierarchical markdown corpus
scraper/.venv/bin/python scraper/render_markdown.py \
    --in tmp/589.json --out data
```

Result: `data/589-sommersemester-2026/INDEX.md` + nested folders/files for every catalogue node.

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
| `campo_client.py`   | HTTP session bootstrap (start-page → JSESSIONID) + 1 req/s rate limit + 5xx retry. |
| `parse_tree.py`     | Catalogue HTML → `ParsedNode`s. Handles both `title:NNN` and `exam:NNN` segments. |
| `parse_detail.py`   | *(phase 2)* Course-detail HTML → `Course`. |
| `schema.py`         | `CatalogNode`, `CatalogSnapshot`, `Course` dataclasses + JSON shape. |
| `render_markdown.py`| JSON snapshot → hierarchical markdown corpus with stable, ASCII-folded German slugs. |
| `scrape.py`         | CLI: BFS walk of the catalogue. |
| `tests/`            | *(phase 2)* pytest fixtures + parser unit tests. |

## Notes for AI consumers / agents

- Every folder has an `INDEX.md` listing its children with one-line descriptions and Campo permalinks.
- Every catalogue node knows its `segment` (`title:17593`, `exam:14867623`) and full `path` from root.
- File slugs are deterministic — `<asciified-german-name>-<terminal-id>` — so links between files don't break across weekly scrapes when Campo renames a node.
- See [`../docs/campo-public-surface.md`](../docs/campo-public-surface.md) for the underlying HTTP / JSF semantics.
