"""Tests for ``shard_fetch`` — the merged-snapshot → N-sub-snapshot splitter.

Each output file must be a valid input to ``fetch_courses.py`` — same
shape as ``scrape.py`` writes (``nodes`` is a list, top-level keys
``rootSegment``, ``periodId``, ``periodName``, ``scrapedAt``,
``maxDepth``).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR))

from shard_fetch import main as shard_fetch_main  # noqa: E402
from shard_fetch import shard_snapshot  # noqa: E402


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


def _snapshot_with_leaves(unit_ids: list[int]) -> dict:
    """Build a synthetic merged snapshot: root + a section + N course-leaves.

    Non-leaves have unitId=None; the N leaves have unitId set from
    ``unit_ids``. ``fetch_courses.collect_unit_ids`` picks exactly the
    leaves.
    """
    root_seg = "title:1000"
    sec_seg = "title:2000"
    leaves = [
        _make_node(
            f"exam:{5000 + i}",
            f"Course {uid}",
            [root_seg, sec_seg, f"exam:{5000 + i}"],
            sec_seg,
            unit_id=uid,
        )
        for i, uid in enumerate(unit_ids)
    ]
    root = _make_node(
        root_seg, "FAU Root", [root_seg], None, [sec_seg]
    )
    sec = _make_node(
        sec_seg,
        "Section",
        [root_seg, sec_seg],
        root_seg,
        [n["segment"] for n in leaves],
    )
    return {
        "periodId": 589,
        "periodName": "Sommersemester 2026",
        "scrapedAt": "2026-04-01T12:00:00+00:00",
        "rootSegment": root_seg,
        "maxDepth": 9,
        "nodes": [root, sec, *leaves],
    }


def test_shard_fetch_produces_expected_files(tmp_path):
    """3 shards → 3 files with the right names next to each other."""
    inp = tmp_path / "test.json"
    inp.write_text(
        json.dumps(_snapshot_with_leaves(list(range(1000, 1010)))),
        encoding="utf-8",
    )
    out_dir = tmp_path / "fetch-shards"

    rc = shard_fetch_main(
        ["--in", str(inp), "--shards", "3", "--out-dir", str(out_dir)]
    )
    assert rc == 0

    files = sorted(out_dir.glob("*.json"))
    assert [f.name for f in files] == [
        "test-fetch-shard-0.json",
        "test-fetch-shard-1.json",
        "test-fetch-shard-2.json",
    ]


def test_shard_files_have_fetch_courses_shape(tmp_path):
    """Each shard file must have the fetch_courses.py input shape."""
    inp = tmp_path / "test.json"
    inp.write_text(
        json.dumps(_snapshot_with_leaves(list(range(1000, 1010)))),
        encoding="utf-8",
    )
    out_dir = tmp_path / "fetch-shards"

    shard_fetch_main(
        ["--in", str(inp), "--shards", "3", "--out-dir", str(out_dir)]
    )

    for f in sorted(out_dir.glob("*.json")):
        sub = json.loads(f.read_text(encoding="utf-8"))

        # Mandatory top-level keys carried through from the input.
        assert "rootSegment" in sub and sub["rootSegment"] == "title:1000"
        assert sub["periodId"] == 589
        assert sub["periodName"] == "Sommersemester 2026"

        # 'nodes' MUST be a list (scrape.py-shape, not a dict as in
        # checkpoint files) — fetch_courses.collect_unit_ids iterates
        # over snapshot["nodes"] and reads each node's dict fields.
        assert isinstance(sub["nodes"], list)
        for node in sub["nodes"]:
            assert "unitId" in node
            assert isinstance(node["unitId"], int)
            assert node["unitId"] > 0


def test_shards_cover_all_unit_ids(tmp_path):
    """Union of assigned unit_ids across all shards == the full leaf set."""
    inp = tmp_path / "test.json"
    inp.write_text(
        json.dumps(_snapshot_with_leaves(list(range(1000, 1010)))),
        encoding="utf-8",
    )
    out_dir = tmp_path / "fetch-shards"

    shard_fetch_main(
        ["--in", str(inp), "--shards", "3", "--out-dir", str(out_dir)]
    )

    seen: set[int] = set()
    for f in sorted(out_dir.glob("*.json")):
        sub = json.loads(f.read_text(encoding="utf-8"))
        for n in sub["nodes"]:
            seen.add(int(n["unitId"]))

    assert seen == set(range(1000, 1010))
    assert len(seen) == 10


def test_round_robin_split_by_sorted_unit_id(tmp_path):
    """Deterministic round-robin: sorted-uid index i → shard i % N.

    10 uids (1000..1009) into 3 shards →
      shard 0 = {1000, 1003, 1006, 1009}
      shard 1 = {1001, 1004, 1007}
      shard 2 = {1002, 1005, 1008}
    """
    inp = tmp_path / "test.json"
    inp.write_text(
        json.dumps(_snapshot_with_leaves(list(range(1000, 1010)))),
        encoding="utf-8",
    )
    out_dir = tmp_path / "fetch-shards"

    shard_fetch_main(
        ["--in", str(inp), "--shards", "3", "--out-dir", str(out_dir)]
    )

    def uids(i: int) -> set[int]:
        sub = json.loads(
            (out_dir / f"test-fetch-shard-{i}.json").read_text(encoding="utf-8")
        )
        return {int(n["unitId"]) for n in sub["nodes"]}

    assert uids(0) == {1000, 1003, 1006, 1009}
    assert uids(1) == {1001, 1004, 1007}
    assert uids(2) == {1002, 1005, 1008}


def test_split_is_deterministic_across_input_order(tmp_path):
    """Same input in a different node order → identical shards.

    The sort by unitId ensures the split is order-independent.
    """
    uids = list(range(1000, 1010))
    snap = _snapshot_with_leaves(uids)

    # Shuffle the nodes list into reverse order — the leaves' unitIds
    # are still the same, so the split must be identical.
    shuffled = dict(snap)
    shuffled["nodes"] = list(reversed(snap["nodes"]))

    inp_a = tmp_path / "a.json"
    inp_b = tmp_path / "b.json"
    inp_a.write_text(json.dumps(snap), encoding="utf-8")
    inp_b.write_text(json.dumps(shuffled), encoding="utf-8")

    out_a = tmp_path / "out-a"
    out_b = tmp_path / "out-b"
    shard_fetch_main(["--in", str(inp_a), "--shards", "3", "--out-dir", str(out_a)])
    shard_fetch_main(["--in", str(inp_b), "--shards", "3", "--out-dir", str(out_b)])

    for i in range(3):
        a = json.loads((out_a / f"a-fetch-shard-{i}.json").read_text())
        b = json.loads((out_b / f"b-fetch-shard-{i}.json").read_text())
        assert [n["unitId"] for n in a["nodes"]] == [n["unitId"] for n in b["nodes"]]


def test_split_is_deterministic_across_runs(tmp_path):
    """Two independent runs of shard_fetch must yield identical outputs."""
    inp = tmp_path / "test.json"
    inp.write_text(
        json.dumps(_snapshot_with_leaves(list(range(1000, 1010)))),
        encoding="utf-8",
    )

    out_a = tmp_path / "a"
    out_b = tmp_path / "b"
    shard_fetch_main(["--in", str(inp), "--shards", "3", "--out-dir", str(out_a)])
    shard_fetch_main(["--in", str(inp), "--shards", "3", "--out-dir", str(out_b)])

    for i in range(3):
        a = json.loads((out_a / f"test-fetch-shard-{i}.json").read_text())
        b = json.loads((out_b / f"test-fetch-shard-{i}.json").read_text())
        assert a == b


def test_empty_unit_ids_raises_loudly(tmp_path):
    """A snapshot with no unitId-bearing nodes must fail with a clear message.

    Guards against wiring a shallow (walk-only) snapshot into the fetch
    pipeline; the shard_fetch stage would silently emit N empty shards
    otherwise and the operator would only notice after 8 CI jobs
    fetched nothing.
    """
    root_seg = "title:1000"
    snap = {
        "periodId": 589,
        "periodName": "S26",
        "scrapedAt": "2026-04-01T00:00:00+00:00",
        "rootSegment": root_seg,
        "maxDepth": 3,
        "nodes": [
            _make_node(root_seg, "Root", [root_seg], None, ["title:2000"]),
            _make_node("title:2000", "Sec", [root_seg, "title:2000"], root_seg),
        ],
    }
    with pytest.raises(ValueError, match="non-null unitId"):
        shard_snapshot(snap, shards=3)


def test_more_shards_than_leaves_writes_empty_shards(tmp_path):
    """N > leaves → some shards empty but files still written.

    Fine because fetch_courses.py on an empty snapshot just fetches
    nothing (collect_unit_ids returns []). We don't want to silently
    write fewer files than requested; the caller may be relying on the
    file count for a matrix.
    """
    inp = tmp_path / "test.json"
    inp.write_text(
        json.dumps(_snapshot_with_leaves([1000, 1001, 1002])),
        encoding="utf-8",
    )
    out_dir = tmp_path / "fetch-shards"

    shard_fetch_main(
        ["--in", str(inp), "--shards", "5", "--out-dir", str(out_dir)]
    )

    sizes = []
    for i in range(5):
        sub = json.loads(
            (out_dir / f"test-fetch-shard-{i}.json").read_text(encoding="utf-8")
        )
        sizes.append(len(sub["nodes"]))
    assert sizes == [1, 1, 1, 0, 0]


def test_shard_nodes_only_include_course_leaves(tmp_path):
    """A shard's nodes list must NOT contain intermediate (unitId=None) nodes.

    fetch_courses.collect_unit_ids skips them anyway, but keeping the
    files small and easy to eyeball matters for CI-artifact review.
    """
    inp = tmp_path / "test.json"
    inp.write_text(
        json.dumps(_snapshot_with_leaves([1000, 1001, 1002, 1003])),
        encoding="utf-8",
    )
    out_dir = tmp_path / "fetch-shards"

    shard_fetch_main(
        ["--in", str(inp), "--shards", "2", "--out-dir", str(out_dir)]
    )

    for i in range(2):
        sub = json.loads(
            (out_dir / f"test-fetch-shard-{i}.json").read_text(encoding="utf-8")
        )
        for n in sub["nodes"]:
            assert n["unitId"] is not None


def test_invalid_shards_arg_raises():
    """--shards must be >= 1."""
    snap = _snapshot_with_leaves([1000, 1001, 1002])
    with pytest.raises(ValueError, match=">= 1"):
        shard_snapshot(snap, shards=0)


def test_nodes_must_be_a_list():
    """A checkpoint-shape input (dict nodes) must be rejected clearly."""
    bad = {
        "periodId": 589,
        "periodName": "S26",
        "scrapedAt": "2026-04-01T00:00:00+00:00",
        "rootSegment": "title:1000",
        "maxDepth": 3,
        "nodes": {"title:1000": {"segment": "title:1000"}},  # dict, not list
    }
    with pytest.raises(ValueError, match="must be a list"):
        shard_snapshot(bad, shards=3)
