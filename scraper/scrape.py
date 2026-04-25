"""IfCampoKnew scraper — CLI entry point.

Usage:
  python scraper/scrape.py --period 589 --out data/589-tree.json [--max-depth 2]

The tree walk is BFS with a configurable max depth (1 = root's children only).
Rate limit defaults to 1.0 req/s; override with ``--interval``.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import logging
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT_DIR))

from campo_client import CampoClient  # noqa: E402
from parse_tree import classify_nodes, parse_nodes, parse_periods  # noqa: E402
from schema import CatalogNode, CatalogSnapshot  # noqa: E402

log = logging.getLogger("campo.scrape")


def walk_tree(
    client: CampoClient,
    period_id: int,
    max_depth: int,
) -> CatalogSnapshot:
    """Walk the catalogue BFS, starting at the semester's root.

    ``max_depth`` is measured from the root's children:
      * 0 = discover root only (no GETs beyond the initial one).
      * 1 = fetch root, list children (no further GETs).
      * 2 = fetch root and each child (children-of-children visible).
    """
    period_name = f"(period {period_id})"

    # 1) fetch root
    root_url = client.catalog_url(period_id)
    log.info("fetching root: %s", root_url)
    r = client.get(root_url)
    r.raise_for_status()
    root_html = r.text

    periods = parse_periods(root_html)
    for pid, name in periods:
        if pid == period_id:
            period_name = name
            break

    all_parsed = parse_nodes(root_html)
    if not all_parsed:
        raise RuntimeError("root page: no permalinks found")
    root_node = all_parsed[0]  # first permalink = current node = root
    root_path = list(root_node.path)
    log.info(
        "root: title_id=%s name=%r children-seen=%d",
        root_node.title_id,
        root_node.name,
        sum(
            1
            for n in all_parsed
            if len(n.path) == len(root_path) + 1 and n.path[:-1] == root_path
        ),
    )

    nodes: dict[int, CatalogNode] = {}

    def record(parsed, parent_title_id: int | None) -> CatalogNode:
        if parsed.title_id not in nodes:
            nodes[parsed.title_id] = CatalogNode(
                title_id=parsed.title_id,
                name=parsed.name,
                path=list(parsed.path),
                parent_title_id=parent_title_id,
            )
        return nodes[parsed.title_id]

    # record root + its children from the root HTML
    record(root_node, None)
    _, root_children = classify_nodes(all_parsed, root_path)
    for ch in root_children:
        record(ch, root_node.title_id)
        nodes[root_node.title_id].children.append(ch.title_id)

    # 2) BFS deeper
    queue: list[tuple[list[int], int]] = [(ch.path, 1) for ch in root_children]
    while queue:
        cur_path, depth = queue.pop(0)
        if depth >= max_depth:
            continue
        url = client.catalog_url(period_id, cur_path)
        r = client.get(url, referer=root_url)
        try:
            r.raise_for_status()
        except Exception as e:  # noqa: BLE001
            log.warning("skip node %s (%s)", cur_path, e)
            continue
        parsed = parse_nodes(r.text)
        current, children = classify_nodes(parsed, cur_path)
        if current.name and nodes[cur_path[-1]].name == f"title:{cur_path[-1]}":
            nodes[cur_path[-1]].name = current.name
        for ch in children:
            record(ch, cur_path[-1])
            if ch.title_id not in nodes[cur_path[-1]].children:
                nodes[cur_path[-1]].children.append(ch.title_id)
            queue.append((ch.path, depth + 1))
        log.info(
            "depth=%d path=%s children=%d total_nodes=%d",
            depth,
            cur_path,
            len(children),
            len(nodes),
        )

    return CatalogSnapshot(
        period_id=period_id,
        period_name=period_name,
        scraped_at=_dt.datetime.now(_dt.timezone.utc).isoformat(timespec="seconds"),
        root_title_id=root_node.title_id,
        nodes=list(nodes.values()),
    )


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Scrape the Campo course catalogue.")
    p.add_argument("--period", type=int, required=True, help="periodId, e.g. 589 for SoSe 2026")
    p.add_argument(
        "--out", type=Path, required=True, help="output JSON path (parent created if missing)"
    )
    p.add_argument("--max-depth", type=int, default=2, help="max BFS depth (default: 2)")
    p.add_argument("--interval", type=float, default=1.0, help="min seconds between requests")
    p.add_argument("-v", "--verbose", action="count", default=0)
    args = p.parse_args(argv)

    level = logging.WARNING - 10 * args.verbose
    logging.basicConfig(level=max(level, logging.DEBUG), format="%(levelname)s %(name)s: %(message)s")

    client = CampoClient(min_interval=args.interval)
    snap = walk_tree(client, period_id=args.period, max_depth=args.max_depth)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(snap.to_dict(), ensure_ascii=False, indent=2), encoding="utf-8")
    print(
        f"wrote {args.out}: periodId={snap.period_id} "
        f"name={snap.period_name!r} nodes={len(snap.nodes)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
