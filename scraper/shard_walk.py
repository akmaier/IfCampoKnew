"""Split a shallow Campo catalogue snapshot into N resumable-walk shards.

Depth-9 walks don't fit in GitHub Actions' 6h per-job cap as a single
:mod:`scrape` invocation, so we shard the work across a matrix of jobs:

1. A cheap depth-3 walk (``scrape.py --max-depth 3``) enumerates the
   ~200 program nodes (nodes whose ``path`` has length 3).
2. This script splits those programs round-robin into ``--shards`` bins.
3. For each bin, it writes a checkpoint file at
   ``{out-dir}/{stem}-shard-{i}.json.checkpoint.json``.
4. Each shard-worker invokes ``scrape.py --resume`` with the matching
   ``--out`` path; the resume machinery loads our pre-seeded checkpoint
   and picks up the BFS at the assigned programs, walking each subtree
   the rest of the way (typically depth 3 → 9).

Each shard's checkpoint has the *full* shallow node table (so the
worker starts with full knowledge of the shallow tree, no re-discovery
races) but only its own slice of the depth-3 seeds on the queue. The
file shape mirrors what :func:`scrape._save_checkpoint` writes so it
loads verbatim in :func:`scrape._load_checkpoint`.

Usage:

    python scraper/shard_walk.py --in tmp/589-shallow.json \\
        --shards 8 --out-dir tmp/shards/
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

log = logging.getLogger("campo.shard_walk")


def _build_shard_checkpoint(
    *,
    period_id: int,
    period_name: str,
    root_segment: str,
    max_depth: int,
    all_nodes_by_segment: dict[str, dict],
    seed_programs: list[dict],
) -> dict:
    """Assemble one shard's checkpoint payload.

    The shape matches :func:`scrape._save_checkpoint` byte-for-byte so
    :func:`scrape._load_checkpoint` accepts it without modification.
    """
    queue = [
        {"path": list(p["path"]), "depth": len(p["path"])}
        for p in seed_programs
    ]
    return {
        "version": 1,
        "savedAt": _dt.datetime.now(_dt.timezone.utc).isoformat(timespec="seconds"),
        "periodId": period_id,
        "periodName": period_name,
        "maxDepth": max_depth,
        "rootSegment": root_segment,
        "nodes": dict(all_nodes_by_segment),
        "queue": queue,
    }


def shard_snapshot(
    snapshot: dict, *, shards: int, max_depth: int | None = None
) -> list[dict]:
    """Split ``snapshot`` into ``shards`` pre-seeded checkpoint dicts.

    The depth-3 program nodes (``len(path) == 3``) are sorted by segment
    for determinism and dealt round-robin into shard bins. Each bin's
    checkpoint carries the full node table plus its own slice of the
    programs on the resume-queue.

    ``max_depth`` overrides the depth stamped on the checkpoint (defaults
    to the input snapshot's ``maxDepth``); production usage typically
    passes 9 here because the input snapshot is a shallow depth-3 walk
    but the shard walk itself needs to reach depth 9.
    """
    if shards < 1:
        raise ValueError(f"--shards must be >= 1, got {shards}")

    try:
        period_id = int(snapshot["periodId"])
    except (KeyError, TypeError, ValueError) as e:
        raise ValueError(f"input snapshot missing/invalid periodId: {e}") from e
    period_name = snapshot.get("periodName", f"(period {period_id})")
    root_segment = snapshot.get("rootSegment", "")
    if not root_segment:
        raise ValueError("input snapshot missing rootSegment")

    raw_nodes = snapshot.get("nodes")
    if not isinstance(raw_nodes, list):
        raise ValueError(
            "input snapshot 'nodes' must be a list "
            "(as produced by scrape.py); got "
            f"{type(raw_nodes).__name__}"
        )

    all_nodes_by_segment: dict[str, dict] = {}
    for n in raw_nodes:
        seg = n.get("segment")
        if not seg:
            log.warning("skipping node without segment: %r", n)
            continue
        all_nodes_by_segment[seg] = n

    programs = [
        n for n in raw_nodes
        if isinstance(n.get("path"), list) and len(n["path"]) == 3
    ]
    if not programs:
        raise ValueError(
            "input snapshot has no depth-3 program nodes "
            "(nodes with len(path) == 3); did you run scrape.py "
            "with --max-depth >= 3?"
        )

    programs.sort(key=lambda p: p["segment"])

    if max_depth is None:
        max_depth = int(snapshot.get("maxDepth") or 0)

    bins: list[list[dict]] = [[] for _ in range(shards)]
    for i, prog in enumerate(programs):
        bins[i % shards].append(prog)

    log.info(
        "sharded %d depth-3 programs into %d bins (sizes=%s)",
        len(programs),
        shards,
        [len(b) for b in bins],
    )

    return [
        _build_shard_checkpoint(
            period_id=period_id,
            period_name=period_name,
            root_segment=root_segment,
            max_depth=max_depth,
            all_nodes_by_segment=all_nodes_by_segment,
            seed_programs=b,
        )
        for b in bins
    ]


def _shard_output_path(out_dir: Path, in_stem: str, idx: int) -> Path:
    """Return the checkpoint path for shard ``idx``.

    The name follows scrape.py's ``_checkpoint_path`` convention: given
    an ``--out foo.json`` invocation, the checkpoint is
    ``foo.json.checkpoint.json``. So our file
    ``{stem}-shard-{i}.json.checkpoint.json`` corresponds to a worker
    invocation ``scrape.py --out {out-dir}/{stem}-shard-{i}.json``.
    """
    return out_dir / f"{in_stem}-shard-{idx}.json.checkpoint.json"


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description=(
            "Split a shallow Campo snapshot into N pre-seeded "
            "checkpoint files for parallel resumable walks."
        )
    )
    p.add_argument(
        "--in",
        dest="in_path",
        type=Path,
        required=True,
        help="input shallow snapshot (typically a depth-3 scrape.py output)",
    )
    p.add_argument(
        "--shards",
        type=int,
        required=True,
        help="number of shards to produce (typically the CI matrix size)",
    )
    p.add_argument(
        "--out-dir",
        type=Path,
        required=True,
        help="directory to write shard checkpoint files into (created if missing)",
    )
    p.add_argument(
        "--max-depth",
        type=int,
        default=None,
        help=(
            "override the maxDepth stamped on the checkpoints (defaults to "
            "the input snapshot's maxDepth; production sets this to 9)"
        ),
    )
    p.add_argument("-v", "--verbose", action="count", default=0)
    args = p.parse_args(argv)

    level = logging.WARNING - 10 * args.verbose
    logging.basicConfig(
        level=max(level, logging.DEBUG),
        format="%(levelname)s %(name)s: %(message)s",
    )

    snapshot = json.loads(args.in_path.read_text(encoding="utf-8"))

    checkpoints = shard_snapshot(
        snapshot, shards=args.shards, max_depth=args.max_depth
    )

    args.out_dir.mkdir(parents=True, exist_ok=True)
    stem = args.in_path.stem  # foo.json -> foo

    written: list[Path] = []
    for i, ckpt in enumerate(checkpoints):
        out_path = _shard_output_path(args.out_dir, stem, i)
        out_path.write_text(
            json.dumps(ckpt, ensure_ascii=False), encoding="utf-8"
        )
        written.append(out_path)
        log.info(
            "wrote shard %d/%d: %s (queue=%d nodes=%d)",
            i,
            args.shards,
            out_path,
            len(ckpt["queue"]),
            len(ckpt["nodes"]),
        )

    print(
        f"wrote {len(written)} shard(s) into {args.out_dir}: "
        f"programs={sum(len(c['queue']) for c in checkpoints)} "
        f"nodes-each={len(checkpoints[0]['nodes'])}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
