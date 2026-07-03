"""Tests for ``shard_walk`` — the depth-3 → N-checkpoint splitter.

The output of shard_walk must be a valid input to scrape.py's
``_load_checkpoint``, so these tests double-check the shape against
what scrape.py reads (see ``scraper/scrape.py`` — ``_load_checkpoint``
and the ``resume_from`` branch of ``walk_tree``).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR))

from shard_walk import main as shard_walk_main  # noqa: E402
from shard_walk import shard_snapshot  # noqa: E402


def _make_node(
    segment: str,
    name: str,
    path: list[str],
    parent_segment: str | None,
    children: list[str] | None = None,
    unit_id: int | None = None,
) -> dict:
    """Mirror :meth:`schema.CatalogNode.to_dict`'s output shape."""
    kind, node_id = segment.split(":", 1)
    return {
        "segment": segment,
        "kind": kind,
        "nodeId": int(node_id),
        "name": name,
        "path": list(path),
        "parentSegment": parent_segment,
        "children": list(children or []),
        "unitId": unit_id,
    }


def _shallow_snapshot(n_programs: int = 10) -> dict:
    """Build a synthetic depth-3 walk output: root + 2 sections + N programs."""
    root_seg = "title:1000"
    sec_a = "title:2000"
    sec_b = "title:2001"

    root = _make_node(root_seg, "FAU Root", [root_seg], None, [sec_a, sec_b])
    section_a_programs = [
        f"title:{3000 + i}" for i in range(n_programs // 2)
    ]
    section_b_programs = [
        f"title:{3500 + i}" for i in range(n_programs - n_programs // 2)
    ]
    sec_a_node = _make_node(
        sec_a, "Faculty A", [root_seg, sec_a], root_seg, section_a_programs
    )
    sec_b_node = _make_node(
        sec_b, "Faculty B", [root_seg, sec_b], root_seg, section_b_programs
    )

    programs = []
    for seg in section_a_programs:
        programs.append(
            _make_node(seg, f"Program {seg}", [root_seg, sec_a, seg], sec_a)
        )
    for seg in section_b_programs:
        programs.append(
            _make_node(seg, f"Program {seg}", [root_seg, sec_b, seg], sec_b)
        )

    return {
        "periodId": 589,
        "periodName": "Sommersemester 2026",
        "scrapedAt": "2026-04-01T12:00:00+00:00",
        "rootSegment": root_seg,
        "maxDepth": 3,
        "nodes": [root, sec_a_node, sec_b_node, *programs],
    }


def test_shard_snapshot_produces_expected_file_names(tmp_path):
    """3 shards → 3 files with the right names next to each other."""
    inp = tmp_path / "589-shallow.json"
    inp.write_text(json.dumps(_shallow_snapshot(10)), encoding="utf-8")
    out_dir = tmp_path / "shards"

    rc = shard_walk_main(
        ["--in", str(inp), "--shards", "3", "--out-dir", str(out_dir)]
    )
    assert rc == 0

    files = sorted(out_dir.glob("*.checkpoint.json"))
    assert [f.name for f in files] == [
        "589-shallow-shard-0.json.checkpoint.json",
        "589-shallow-shard-1.json.checkpoint.json",
        "589-shallow-shard-2.json.checkpoint.json",
    ]


def test_shard_files_have_valid_checkpoint_shape(tmp_path):
    """Each shard file must be JSON that _load_checkpoint accepts."""
    inp = tmp_path / "589-shallow.json"
    inp.write_text(json.dumps(_shallow_snapshot(10)), encoding="utf-8")
    out_dir = tmp_path / "shards"

    shard_walk_main(
        ["--in", str(inp), "--shards", "3", "--out-dir", str(out_dir)]
    )

    for f in sorted(out_dir.glob("*.checkpoint.json")):
        ckpt = json.loads(f.read_text(encoding="utf-8"))

        # Mandatory keys used by scrape._load_checkpoint + walk_tree(resume_from=…):
        assert "rootSegment" in ckpt and ckpt["rootSegment"] == "title:1000"
        assert ckpt["periodId"] == 589
        assert ckpt["periodName"] == "Sommersemester 2026"

        # 'nodes' MUST be a dict keyed by segment (see resume_from branch).
        assert isinstance(ckpt["nodes"], dict)
        for seg, node in ckpt["nodes"].items():
            assert node["segment"] == seg
            assert "path" in node

        # 'queue' MUST be a list of {"path": [...], "depth": int}.
        assert isinstance(ckpt["queue"], list)
        for item in ckpt["queue"]:
            assert isinstance(item["path"], list)
            assert isinstance(item["depth"], int)
            assert item["depth"] == len(item["path"])


def test_shards_union_covers_all_programs(tmp_path):
    """Union of queues across all shards == the depth-3 program set."""
    inp = tmp_path / "589-shallow.json"
    inp.write_text(json.dumps(_shallow_snapshot(10)), encoding="utf-8")
    out_dir = tmp_path / "shards"

    shard_walk_main(
        ["--in", str(inp), "--shards", "3", "--out-dir", str(out_dir)]
    )

    seen_segments: set[str] = set()
    for f in sorted(out_dir.glob("*.checkpoint.json")):
        ckpt = json.loads(f.read_text(encoding="utf-8"))
        for item in ckpt["queue"]:
            seen_segments.add(item["path"][-1])

    snap = json.loads(inp.read_text(encoding="utf-8"))
    expected = {n["segment"] for n in snap["nodes"] if len(n["path"]) == 3}
    assert seen_segments == expected
    assert len(seen_segments) == 10


def test_shards_include_full_node_table(tmp_path):
    """Each shard's `nodes` dict must contain every node from the input.

    Rationale: workers merging results back need to know the shallow
    tree exists so they don't re-fetch it.
    """
    inp = tmp_path / "589-shallow.json"
    inp.write_text(json.dumps(_shallow_snapshot(10)), encoding="utf-8")
    out_dir = tmp_path / "shards"

    shard_walk_main(
        ["--in", str(inp), "--shards", "3", "--out-dir", str(out_dir)]
    )

    snap = json.loads(inp.read_text(encoding="utf-8"))
    expected_segments = {n["segment"] for n in snap["nodes"]}

    for f in sorted(out_dir.glob("*.checkpoint.json")):
        ckpt = json.loads(f.read_text(encoding="utf-8"))
        assert set(ckpt["nodes"].keys()) == expected_segments


def test_sharding_is_deterministic(tmp_path):
    """Two independent runs of shard_walk must yield identical queues."""
    inp = tmp_path / "589-shallow.json"
    inp.write_text(json.dumps(_shallow_snapshot(10)), encoding="utf-8")

    out_a = tmp_path / "a"
    out_b = tmp_path / "b"
    shard_walk_main(["--in", str(inp), "--shards", "3", "--out-dir", str(out_a)])
    shard_walk_main(["--in", str(inp), "--shards", "3", "--out-dir", str(out_b)])

    for i in range(3):
        a = json.loads(
            (out_a / f"589-shallow-shard-{i}.json.checkpoint.json").read_text()
        )
        b = json.loads(
            (out_b / f"589-shallow-shard-{i}.json.checkpoint.json").read_text()
        )
        # savedAt differs (timestamp), so compare the deterministic fields.
        assert a["queue"] == b["queue"]
        assert a["nodes"] == b["nodes"]
        assert a["rootSegment"] == b["rootSegment"]
        assert a["periodId"] == b["periodId"]


def test_round_robin_split_is_balanced(tmp_path):
    """10 programs across 3 shards → sizes 4, 3, 3 in sorted-segment order."""
    inp = tmp_path / "589-shallow.json"
    inp.write_text(json.dumps(_shallow_snapshot(10)), encoding="utf-8")
    out_dir = tmp_path / "shards"

    shard_walk_main(
        ["--in", str(inp), "--shards", "3", "--out-dir", str(out_dir)]
    )

    sizes = []
    for i in range(3):
        ckpt = json.loads(
            (out_dir / f"589-shallow-shard-{i}.json.checkpoint.json").read_text()
        )
        sizes.append(len(ckpt["queue"]))
    assert sizes == [4, 3, 3]


def test_more_shards_than_programs_leaves_empty_bins(tmp_path):
    """N > programs → some shards have empty queues, and that's fine."""
    inp = tmp_path / "589-shallow.json"
    inp.write_text(json.dumps(_shallow_snapshot(3)), encoding="utf-8")
    out_dir = tmp_path / "shards"

    shard_walk_main(
        ["--in", str(inp), "--shards", "5", "--out-dir", str(out_dir)]
    )

    queue_lens = []
    for i in range(5):
        ckpt = json.loads(
            (out_dir / f"589-shallow-shard-{i}.json.checkpoint.json").read_text()
        )
        queue_lens.append(len(ckpt["queue"]))
    # First 3 get 1 each; last 2 empty.
    assert queue_lens == [1, 1, 1, 0, 0]


def test_no_depth_3_nodes_raises_loudly(tmp_path):
    """A snapshot with only root + section (no depth-3) must fail with hint."""
    snap = {
        "periodId": 589,
        "periodName": "S26",
        "scrapedAt": "2026-04-01T00:00:00+00:00",
        "rootSegment": "title:1000",
        "maxDepth": 2,
        "nodes": [
            _make_node("title:1000", "Root", ["title:1000"], None, ["title:2000"]),
            _make_node("title:2000", "Sec", ["title:1000", "title:2000"], "title:1000"),
        ],
    }
    inp = tmp_path / "589-shallow.json"
    inp.write_text(json.dumps(snap), encoding="utf-8")

    with pytest.raises(ValueError, match="no depth-3 program nodes"):
        shard_snapshot(snap, shards=3)


def test_max_depth_override(tmp_path):
    """--max-depth stamps that value on each output checkpoint."""
    inp = tmp_path / "589-shallow.json"
    inp.write_text(json.dumps(_shallow_snapshot(6)), encoding="utf-8")
    out_dir = tmp_path / "shards"

    shard_walk_main(
        [
            "--in", str(inp),
            "--shards", "2",
            "--out-dir", str(out_dir),
            "--max-depth", "9",
        ]
    )
    for i in range(2):
        ckpt = json.loads(
            (out_dir / f"589-shallow-shard-{i}.json.checkpoint.json").read_text()
        )
        assert ckpt["maxDepth"] == 9


def test_queue_paths_carry_depth_3(tmp_path):
    """Each seed's depth must equal len(path) == 3.

    Guards the walker: on resume, the BFS pops (path, depth) and
    fetches children at depth+1. Miswriting depth here would either
    stall the walk (if too high) or double-fetch (if too low).
    """
    inp = tmp_path / "589-shallow.json"
    inp.write_text(json.dumps(_shallow_snapshot(6)), encoding="utf-8")
    out_dir = tmp_path / "shards"

    shard_walk_main(
        ["--in", str(inp), "--shards", "2", "--out-dir", str(out_dir)]
    )

    for i in range(2):
        ckpt = json.loads(
            (out_dir / f"589-shallow-shard-{i}.json.checkpoint.json").read_text()
        )
        for item in ckpt["queue"]:
            assert item["depth"] == 3
            assert len(item["path"]) == 3
