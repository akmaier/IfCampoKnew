"""IfCampoKnew scraper — CLI entry point.

Walks the Campo course catalogue tree breadth-first and writes a JSON
snapshot. Tree segments are addressed by ``KIND:ID`` strings (typically
``title:NNN`` for sections/programs, ``exam:NNN`` for PO-versions); see
:mod:`parse_tree` for the full topology.

The walker is **resumable**: every ``--checkpoint-every`` nodes the
in-flight state is flushed to ``<out>.checkpoint.json`` so an interrupted
run (CI timeout, machine reboot, manual ``Ctrl-C``) does not lose any
work. Re-invoke with ``--resume`` and the queue + node table are read
back and the walk continues from where it stopped.

Usage:

    python scraper/scrape.py --period 589 --out tmp/589.json [--max-depth 4]
    python scraper/scrape.py --period 589 --out tmp/589.json --resume   # continue
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import logging
import signal
import sys
from pathlib import Path
from typing import Optional

ROOT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT_DIR))

from campo_client import CampoClient  # noqa: E402
from parse_tree import classify_nodes, parse_nodes, parse_periods  # noqa: E402
from schema import CatalogNode, CatalogSnapshot  # noqa: E402

log = logging.getLogger("campo.scrape")


def _checkpoint_path(out: Path) -> Path:
    return out.with_suffix(out.suffix + ".checkpoint.json")


def _save_checkpoint(
    ckpt: Path,
    period_id: int,
    period_name: str,
    max_depth: int,
    root_segment: str,
    nodes: dict[str, CatalogNode],
    queue: list[tuple[list[str], int]],
) -> None:
    payload = {
        "version": 1,
        "savedAt": _dt.datetime.now(_dt.timezone.utc).isoformat(timespec="seconds"),
        "periodId": period_id,
        "periodName": period_name,
        "maxDepth": max_depth,
        "rootSegment": root_segment,
        "nodes": {seg: n.to_dict() for seg, n in nodes.items()},
        "queue": [{"path": p, "depth": d} for p, d in queue],
    }
    tmp = ckpt.with_suffix(ckpt.suffix + ".tmp")
    tmp.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")
    tmp.replace(ckpt)


def _load_checkpoint(ckpt: Path) -> Optional[dict]:
    if not ckpt.exists():
        return None
    try:
        return json.loads(ckpt.read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        log.warning("checkpoint %s unreadable (%s) — starting fresh", ckpt, e)
        return None


def _node_from_dict(d: dict) -> CatalogNode:
    return CatalogNode(
        segment=d["segment"],
        name=d.get("name", ""),
        path=list(d.get("path") or []),
        parent_segment=d.get("parentSegment"),
        children=list(d.get("children") or []),
        unit_id=d.get("unitId"),
    )


def walk_tree(
    client: CampoClient,
    period_id: int,
    max_depth: int,
    *,
    checkpoint_path: Optional[Path] = None,
    checkpoint_every: int = 50,
    resume_from: Optional[dict] = None,
) -> CatalogSnapshot:
    """Walk the catalogue BFS up to ``max_depth`` segments past the root.

    Depth is counted from root inclusive: ``max_depth=1`` means root only;
    ``max_depth=2`` adds root's immediate children; etc. ``max_depth=0`` is
    treated as "unlimited" with a hard cap at ``HARD_DEPTH_CAP`` for safety.

    If ``resume_from`` is a previously-saved checkpoint dict, the BFS
    resumes from its queue + node table (the root fetch is skipped).
    """
    HARD_DEPTH_CAP = 12
    if max_depth <= 0:
        max_depth = HARD_DEPTH_CAP

    nodes: dict[str, CatalogNode] = {}
    queue: list[tuple[list[str], int]] = []
    period_name = f"(period {period_id})"
    root_segment: str = ""
    root_url = client.catalog_url(period_id)

    if resume_from:
        # ── resume path ────────────────────────────────────────────────
        if int(resume_from.get("periodId", -1)) != period_id:
            raise RuntimeError(
                f"checkpoint periodId={resume_from.get('periodId')!r} "
                f"≠ requested period {period_id}"
            )
        period_name = resume_from.get("periodName") or period_name
        root_segment = resume_from.get("rootSegment", "")
        for d in resume_from.get("nodes", {}).values():
            n = _node_from_dict(d)
            nodes[n.segment] = n
        queue = [
            (list(item["path"]), int(item["depth"]))
            for item in resume_from.get("queue", [])
        ]
        log.info(
            "resumed: nodes=%d queue=%d root=%s",
            len(nodes),
            len(queue),
            root_segment,
        )
    else:
        # ── fresh start: fetch root and seed the queue ─────────────────
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
        root_segment = root.segment
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

        nodes[root.segment] = CatalogNode(
            segment=root.segment,
            name=root.name,
            path=list(root.path),
            parent_segment=None,
            unit_id=root.unit_id,
        )
        _, root_children = classify_nodes(parsed, root_path)
        for ch in root_children:
            if ch.segment not in nodes:
                nodes[ch.segment] = CatalogNode(
                    segment=ch.segment,
                    name=ch.name,
                    path=list(ch.path),
                    parent_segment=root.segment,
                    unit_id=ch.unit_id,
                )
            if ch.segment not in nodes[root.segment].children:
                nodes[root.segment].children.append(ch.segment)
        if max_depth > 2:
            queue = [(ch.path, len(root_path) + 1) for ch in root_children]

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

    # ── catch SIGTERM / SIGINT so a ^C still flushes a checkpoint ──────
    interrupted = {"flag": False}

    def _flush_and_exit(signum, _frame):  # noqa: ARG001
        interrupted["flag"] = True
        if checkpoint_path:
            _save_checkpoint(
                checkpoint_path,
                period_id,
                period_name,
                max_depth,
                root_segment,
                nodes,
                queue,
            )
            log.warning("signal %d — checkpoint flushed; exiting", signum)
        sys.exit(130)

    if checkpoint_path:
        signal.signal(signal.SIGINT, _flush_and_exit)
        signal.signal(signal.SIGTERM, _flush_and_exit)

    processed = 0
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

        processed += 1
        if processed % 10 == 0 or len(kids) > 0:
            log.info(
                "depth=%d path=%s children=%d total_nodes=%d queue=%d",
                depth,
                "/".join(cur_path),
                len(kids),
                len(nodes),
                len(queue),
            )
        if checkpoint_path and processed % checkpoint_every == 0:
            _save_checkpoint(
                checkpoint_path,
                period_id,
                period_name,
                max_depth,
                root_segment,
                nodes,
                queue,
            )
            log.debug("checkpoint @ processed=%d nodes=%d", processed, len(nodes))

    return CatalogSnapshot(
        period_id=period_id,
        period_name=period_name,
        scraped_at=_dt.datetime.now(_dt.timezone.utc).isoformat(timespec="seconds"),
        root_segment=root_segment,
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
    p.add_argument(
        "--checkpoint-every",
        type=int,
        default=50,
        help="flush a checkpoint to <out>.checkpoint.json every N nodes (default 50; 0 disables)",
    )
    p.add_argument(
        "--resume",
        action="store_true",
        help="if <out>.checkpoint.json exists, load it and continue the walk",
    )
    p.add_argument("-v", "--verbose", action="count", default=0)
    args = p.parse_args(argv)

    level = logging.WARNING - 10 * args.verbose
    logging.basicConfig(level=max(level, logging.DEBUG), format="%(levelname)s %(name)s: %(message)s")

    ckpt: Optional[Path] = (
        _checkpoint_path(args.out) if args.checkpoint_every > 0 else None
    )
    resume_state: Optional[dict] = None
    if args.resume and ckpt:
        resume_state = _load_checkpoint(ckpt)
        if resume_state is None:
            log.warning("no checkpoint at %s — starting fresh", ckpt)

    client = CampoClient(min_interval=args.interval)
    snap = walk_tree(
        client,
        period_id=args.period,
        max_depth=args.max_depth,
        checkpoint_path=ckpt,
        checkpoint_every=args.checkpoint_every,
        resume_from=resume_state,
    )

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(snap.to_dict(), ensure_ascii=False, indent=2), encoding="utf-8")

    # Walk completed cleanly — drop the checkpoint.
    if ckpt and ckpt.exists():
        try:
            ckpt.unlink()
        except OSError:
            pass

    print(
        f"wrote {args.out}: periodId={snap.period_id} "
        f"name={snap.period_name!r} nodes={len(snap.nodes)} (max-depth {snap.max_depth})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
