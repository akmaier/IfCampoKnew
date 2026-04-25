# scraper

Python tool that turns the public Campo portal into JSON snapshots consumed by the IfCampoKnew site.

## Quick start

```bash
python3 -m venv scraper/.venv
scraper/.venv/bin/pip install -r scraper/requirements.txt
scraper/.venv/bin/python scraper/scrape.py \
    --period 589 --out data/589-tree.json --max-depth 2 -v
```

- `--period`: Campo `periodId`. Discovered by inspecting the semester dropdown; `589` is *Sommersemester 2026*.
- `--max-depth`: BFS depth. `1` = root + children (no extra GETs); `2` = each top-level node fetched once; higher = deeper tree walk.
- `--interval`: minimum seconds between requests (default `1.0`). Do **not** lower below `0.5` without justification.
- `-v`/`-vv`: log level (WARNING → INFO → DEBUG).

## Module map

| File | Purpose |
|------|---------|
| `scrape.py`       | CLI entry point; orchestrates the BFS tree walk. |
| `campo_client.py` | HTTP session, rate limiting, retries. Starts a fresh JSESSIONID from the Campo start page. |
| `parse_tree.py`   | Regex-based parser for the catalogue HTML → `(title_id, name, path)` tuples. |
| `schema.py`       | Dataclasses `CatalogNode` and `CatalogSnapshot`; JSON (de-)serialisation. |

## Notes

- Campo is HISinOne (JSF + Spring Web Flow). Details on session hygiene, deep links, and POST mechanics live in [`docs/campo-public-surface.md`](../docs/campo-public-surface.md).
- The walker only uses **GETs**. No CSRF, no form state, no POSTs.
- Output JSON shape matches [`scraper/schema.py`](./schema.py) and is the contract with the site.
