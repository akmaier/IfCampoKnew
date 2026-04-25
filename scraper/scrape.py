"""IfCampoKnew scraper — CLI entry point.

Walks the Campo course catalogue tree breadth-first and writes a JSON
snapshot. Tree segments are addressed by ``KIND:ID`` strings (typically
``title:NNN`` for sections/programs, ``exam:NNN`` for PO-versions); see
:mod:`parse_tree` for the full topology.

Usage:

    python scraper/scrape.py --period 589 --out data/589-tree.json [--max-depth 4]
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
    """Walk the catalogue BFS up to ``max_depth`` segments past the root.

    Depth is counted from root inclusive: ``max_depth=1`` means root only;
    ``max_depth=2`` adds root's immediate children; etc. ``max_depth=0`` is
    treated as "unlimited" with a hard cap at ``HARD_DEPTH_CAP`` for safety.
    """
    HARD_DEPTH_CAP = 12
    if max_depth <= 0:
        max_depth = HARD_DEPTH_CAP
    period_name = f"(period {period_id})"

    # 1) fetch root
    root_url = client.catalog_url(period_id)
    log.info("fetching root: %s", root_url)
    r = client.get(root_url)
    r.raise_for_status()
    root_html = r.text

    for pid, name in parse_periods(root_html):
        if pid == period_id:
            period_name = name
            break

    parsed = parse_nodes(root_html)
    if not parsed:
        raise RuntimeError("root page: no permalinks found")
    root = min(parsed, key=lambda n: len(n.path))
    root_path = list(root.path)
    log.info(
        "root segment=%s name=%r (depth-1 children seen: %d)",
        root.segment,
        root.name,
        sum(
            1
            for n in parsed
            if len(n.path) == len(root_path) + 1 and n.path[:-1] == root_path
        ),
    )

    nodes: dict[str, CatalogNode] = {}

    def record(p, parent_segment: str | None) -> CatalogNode:
        if p.segment not in nodes:
            nodes[p.segment] = CatalogNode(
                segment=p.segment,
                name=p.name,
                path=list(p.path),
                parent_segment=parent_segment,
                unit_id=p.unit_id,
            )
        else:
            existing = nodes[p.segment]
            if p.name and not existing.name:
                existing.name = p.name
            if p.unit_id and not existing.unit_id:
                existing.unit_id = p.unit_id
        return nodes[p.segment]

    # record root + its immediate children from the root page.
    record(root, None)
    _, root_children = classify_nodes(parsed, root_path)
    for ch in root_children:
        record(ch, root.segment)
        if ch.segment not in nodes[root.segment].children:
            nodes[root.segment].children.append(ch.segment)

    # 2) BFS deeper. Depth in queue = depth of `cur_path` (root_path is depth 1).
    if max_depth > 2:
        queue: list[tuple[list[str], int]] = [
            (ch.path, len(root_path) + 1) for ch in root_children
        ]
    else:
        queue = []
    while queue:
        cur_path, depth = queue.pop(0)
        if depth >= max_depth:
            continue
        url = client.catalog_url(period_id, cur_path)
        try:
            r = client.get(url, referer=root_url)
            r.raise_for_status()
        except Exception as e:  # noqa: BLE001
            log.warning("skip %s (%s)", cur_path, e)
            continue
        page_nodes = parse_nodes(r.text)
        current, kids = classify_nodes(page_nodes, cur_path)
        if current and current.name and not nodes[cur_path[-1]].name:
            nodes[cur_path[-1]].name = current.name
        for ch in kids:
            record(ch, cur_path[-1])
            if ch.segment not in nodes[cur_path[-1]].children:
                nodes[cur_path[-1]].children.append(ch.segment)
            queue.append((ch.path, depth + 1))
        log.info(
            "depth=%d path=%s children=%d total_nodes=%d",
            depth,
            "/".join(cur_path),
            len(kids),
            len(nodes),
        )

    return CatalogSnapshot(
        period_id=period_id,
        period_name=period_name,
        scraped_at=_dt.datetime.now(_dt.timezone.utc).isoformat(timespec="seconds"),
        root_segment=root.segment,
        max_depth=max_depth,
        nodes=list(nodes.values()),
    )


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Scrape the Campo course catalogue.")
    p.add_argument("--period", type=int, required=True, help="periodId, e.g. 589 for SoSe 2026")
    p.add_argument(
        "--out", type=Path, required=True, help="output JSON path (parent created if missing)"
    )
    p.add_argument(
        "--max-depth",
        type=int,
        default=4,
        help="max BFS depth, root inclusive (default 4 = root→section→program→PO-version; "
        "set 0 for unlimited, capped internally at 12 for safety)",
    )
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
        f"name={snap.period_name!r} nodes={len(snap.nodes)} (max-depth {snap.max_depth})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
