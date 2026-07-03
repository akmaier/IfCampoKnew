"""Merge N per-shard Campo snapshots into one unified snapshot.

The companion to :mod:`shard_walk`. Each shard-worker runs
``scrape.py --resume`` on its assigned slice and emits a subtree
snapshot; this script unions those subtree snapshots into a single
snapshot in the exact shape :func:`schema.CatalogSnapshot.to_dict`
produces (which is what :mod:`render_markdown` expects as input).

Usage:

    python scraper/merge_shards.py \\
        --in tmp/589-shard-0.json tmp/589-shard-1.json ... \\
        --out tmp/589.json

Merge rules:

* All inputs must share the same ``periodId`` and ``rootSegment``
  (defensive check — a mismatch means somebody wired the wrong shard
  set together).
* ``periodName`` and ``scrapedAt`` are taken from the first input
  (arbitrary but deterministic).
* ``maxDepth`` = max across inputs.
* Nodes are unioned by ``segment``. On collision the winner is the
  record with (in order): more ``children``, non-empty ``name``,
  non-null ``unitId``. First-input wins on remaining ties. The
  ``children`` tie-breaker matters because shard 0 always sees the
  root & its immediate children in its shallow-node dump but has no
  reason to have walked them; a later shard that actually visited
  the same segment as its seed will have populated its ``children``
  list, so its record supersedes.
"""
from __future__ import annotations

import argparse
import json
import logging
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT_DIR))

log = logging.getLogger("campo.merge_shards")

def _pick_winner(existing: dict, incoming: dict) -> dict:
    """Return whichever node record is "richer" per the merge rules.

    See module docstring for the priority order. Ties resolve to
    ``existing`` (first-wins) since merges call this while streaming
    inputs left-to-right.
    """
    # Priority 1: more children wins.
    e_kids = len(existing.get("children") or [])
    i_kids = len(incoming.get("children") or [])
    if i_kids > e_kids:
        return incoming
    if i_kids < e_kids:
        return existing

    # Priority 2: non-empty name beats empty.
    e_name = bool(existing.get("name"))
    i_name = bool(incoming.get("name"))
    if i_name and not e_name:
        return incoming
    if e_name and not i_name:
        return existing

    # Priority 3: non-null unitId beats null.
    e_uid = existing.get("unitId")
    i_uid = incoming.get("unitId")
    if i_uid is not None and e_uid is None:
        return incoming
    if e_uid is not None and i_uid is None:
        return existing

    return existing

def merge_snapshots(snapshots: list[dict]) -> dict:
    """Merge ``snapshots`` (all in ``CatalogSnapshot.to_dict()`` shape).

    Raises ``ValueError`` if the inputs disagree on ``periodId`` or
    ``rootSegment``. The caller (``main``) converts that into a
    ``SystemExit`` with a helpful message per the brief.
    """
    if not snapshots:
        raise ValueError("no snapshots to merge")

    first = snapshots[0]
    period_id = first.get("periodId")
    root_segment = first.get("rootSegment")
    if period_id is None:
        raise ValueError("first snapshot has no periodId")
    if not root_segment:
        raise ValueError("first snapshot has no rootSegment")

    period_name = first.get("periodName", "")
    scraped_at = first.get("scrapedAt", "")
    max_depth = int(first.get("maxDepth") or 0)

    for i, s in enumerate(snapshots[1:], start=1):
        if s.get("periodId") != period_id:
            raise ValueError(
                f"snapshot #{i} periodId={s.get('periodId')!r} "
                f"≠ first snapshot's periodId={period_id!r}"
            )
        if s.get("rootSegment") != root_segment:
            raise ValueError(
                f"snapshot #{i} rootSegment={s.get('rootSegment')!r} "
                f"≠ first snapshot's rootSegment={root_segment!r}"
            )
        max_depth = max(max_depth, int(s.get("maxDepth") or 0))

    merged: dict[str, dict] = {}
    for i, s in enumerate(snapshots):
        raw_nodes = s.get("nodes")
        if not isinstance(raw_nodes, list):
            raise ValueError(
                f"snapshot #{i} 'nodes' must be a list, "
                f"got {type(raw_nodes).__name__}"
            )
        for n in raw_nodes:
            seg = n.get("segment")
            if not seg:
                log.warning("snapshot #%d: skipping node without segment: %r", i, n)
                continue
            if seg not in merged:
                merged[seg] = dict(n)
            else:
                merged[seg] = dict(_pick_winner(merged[seg], n))

    ordered = sorted(merged.values(), key=lambda n: n.get("segment", ""))

    return {
        "periodId": period_id,
        "periodName": period_name,
        "scrapedAt": scraped_at,
        "rootSegment": root_segment,
        "maxDepth": max_depth,
        "nodes": ordered,
    }

def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description=(
            "Union N per-shard Campo snapshots into a single snapshot "
            "in the shape scrape.py normally emits."
        )
    )
    p.add_argument(
        "--in",
        dest="in_paths",
        type=Path,
        nargs="+",
        required=True,
        help="per-shard snapshot files (as produced by scrape.py)",
    )
    p.add_argument(
        "--out",
        type=Path,
        required=True,
        help="output snapshot path (parent created if missing)",
    )
    p.add_argument("-v", "--verbose", action="count", default=0)
    args = p.parse_args(argv)

    level = logging.WARNING - 10 * args.verbose
    logging.basicConfig(
        level=max(level, logging.DEBUG),
        format="%(levelname)s %(name)s: %(message)s",
    )

    snapshots: list[dict] = []
    for path in args.in_paths:
        log.info("reading %s", path)
        snapshots.append(json.loads(path.read_text(encoding="utf-8")))

    try:
        merged = merge_snapshots(snapshots)
    except ValueError as e:
        raise SystemExit(f"merge_shards: {e}") from e

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(
        json.dumps(merged, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(
        f"wrote {args.out}: periodId={merged['periodId']} "
        f"nodes={len(merged['nodes'])} (max-depth {merged['maxDepth']})"
    )
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
