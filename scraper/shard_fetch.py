"""Split a merged Campo snapshot into N per-shard fetch inputs.

Stage 2.5 of the scraper pipeline — sandwiched between the sharded
depth-9 walk (``shard_walk.py`` + N × ``scrape.py --resume`` +
``merge_shards.py``) and the ``fetch_courses.py`` course-detail step.

Rationale: at depth-9 the merged snapshot contains ~2× the unit-id
volume of the previous depth-6 output, and a single
``fetch_courses.py --parallel 2 --interval 0.2`` run no longer fits in
GitHub Actions' 6h per-job cap (proven by run 28668392916). Solution:
also shard the fetch across a matrix of jobs.

This script takes a merged ``CatalogSnapshot.to_dict()``-shaped file
(``nodes`` is a list, produced by ``scrape.py`` or ``merge_shards.py``)
and produces N sub-snapshots. Each sub-snapshot has the same top-level
keys as the input, but its ``nodes`` list contains only that shard's
assigned subset of the unit-id-bearing "course event" leaves.

``fetch_courses.py`` already fetches all unit-id-bearing nodes from its
input snapshot (see :func:`fetch_courses.collect_unit_ids`), so each
shard worker can be invoked verbatim on its slice with no code changes.

Split algorithm: leaves are sorted by ``unitId`` ascending for
determinism, then dealt round-robin into ``--shards`` bins. Node at
sorted index ``i`` goes to shard ``i % N``.

Usage::

    python scraper/shard_fetch.py \\
        --in tmp/589.json \\
        --shards 8 \\
        --out-dir tmp/fetch-shards/
"""
from __future__ import annotations

import argparse
import json
import logging
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT_DIR))

log = logging.getLogger("campo.shard_fetch")


def _course_leaves(snapshot: dict) -> list[dict]:
    """Return every node from ``snapshot`` whose ``unitId`` is a non-null int.

    These are the "course event" leaves — the nodes that
    :func:`fetch_courses.collect_unit_ids` would pick up. Sorted by
    ``unitId`` ascending so the round-robin split is deterministic.
    """
    raw_nodes = snapshot.get("nodes")
    if not isinstance(raw_nodes, list):
        raise ValueError(
            "input snapshot 'nodes' must be a list "
            "(as produced by scrape.py / merge_shards.py); got "
            f"{type(raw_nodes).__name__}"
        )
    leaves: list[dict] = []
    for n in raw_nodes:
        uid = n.get("unitId")
        if isinstance(uid, int) and uid > 0:
            leaves.append(n)
    leaves.sort(key=lambda n: int(n["unitId"]))
    return leaves


def shard_snapshot(snapshot: dict, *, shards: int) -> list[dict]:
    """Split ``snapshot`` into ``shards`` sub-snapshots.

    Each sub-snapshot is a valid input to ``fetch_courses.py``: it has
    the same top-level keys as the input (``rootSegment``, ``periodId``,
    ``periodName``, ``scrapedAt``, ``maxDepth``) and its ``nodes`` list
    contains only that shard's assigned course-event leaves.

    Raises ``ValueError`` if the input has zero unit-id-bearing nodes
    (nothing to shard — probably wrong input file).
    """
    if shards < 1:
        raise ValueError(f"--shards must be >= 1, got {shards}")

    course_nodes = _course_leaves(snapshot)
    if not course_nodes:
        raise ValueError(
            "input snapshot has no nodes with a non-null unitId "
            "— nothing to shard for fetching; check that the input is "
            "a depth-9+ merged snapshot rather than a shallow tree"
        )

    period_id = snapshot.get("periodId")
    period_name = snapshot.get("periodName", "")
    root_segment = snapshot.get("rootSegment", "")
    scraped_at = snapshot.get("scrapedAt", "")
    max_depth = snapshot.get("maxDepth", 0)

    bins: list[list[dict]] = [[] for _ in range(shards)]
    for i, node in enumerate(course_nodes):
        bins[i % shards].append(node)

    log.info(
        "sharded %d course-nodes into %d shards; shard sizes: %s",
        len(course_nodes),
        shards,
        [len(b) for b in bins],
    )

    return [
        {
            "periodId": period_id,
            "periodName": period_name,
            "scrapedAt": scraped_at,
            "rootSegment": root_segment,
            "maxDepth": max_depth,
            "nodes": list(b),
        }
        for b in bins
    ]


def _shard_output_path(out_dir: Path, in_stem: str, idx: int) -> Path:
    """Return the file path for shard ``idx``."""
    return out_dir / f"{in_stem}-fetch-shard-{idx}.json"


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description=(
            "Split a merged Campo snapshot into N sub-snapshots, one per "
            "fetch shard. Each sub-snapshot lists only that shard's "
            "assigned unit-id nodes and is a valid input to fetch_courses.py."
        )
    )
    p.add_argument(
        "--in",
        dest="in_path",
        type=Path,
        required=True,
        help="input merged snapshot (as produced by scrape.py or merge_shards.py)",
    )
    p.add_argument(
        "--shards",
        type=int,
        required=True,
        help="number of shards to produce (typically the CI fetch matrix size)",
    )
    p.add_argument(
        "--out-dir",
        type=Path,
        required=True,
        help="directory to write shard snapshot files into (created if missing)",
    )
    p.add_argument("-v", "--verbose", action="count", default=0)
    args = p.parse_args(argv)

    level = logging.WARNING - 10 * args.verbose
    logging.basicConfig(
        level=max(level, logging.DEBUG),
        format="%(levelname)s %(name)s: %(message)s",
    )

    snapshot = json.loads(args.in_path.read_text(encoding="utf-8"))

    sub_snapshots = shard_snapshot(snapshot, shards=args.shards)

    args.out_dir.mkdir(parents=True, exist_ok=True)
    stem = args.in_path.stem  # foo.json -> foo

    written: list[Path] = []
    for i, sub in enumerate(sub_snapshots):
        out_path = _shard_output_path(args.out_dir, stem, i)
        out_path.write_text(
            json.dumps(sub, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        written.append(out_path)
        log.info(
            "wrote fetch-shard %d/%d: %s (nodes=%d)",
            i,
            args.shards,
            out_path,
            len(sub["nodes"]),
        )

    total = sum(len(s["nodes"]) for s in sub_snapshots)
    print(
        f"wrote {len(written)} fetch-shard(s) into {args.out_dir}: "
        f"course-nodes={total} periodId={snapshot.get('periodId')}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
