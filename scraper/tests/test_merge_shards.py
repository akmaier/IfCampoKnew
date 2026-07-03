"""Tests for ``merge_shards`` — the N-subtree-snapshot unioner."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR))

from merge_shards import main as merge_main  # noqa: E402
from merge_shards import merge_snapshots  # noqa: E402


def _node(
    segment: str,
    name: str = "",
    path: list[str] | None = None,
    parent_segment: str | None = None,
    children: list[str] | None = None,
    unit_id: int | None = None,
) -> dict:
    kind, node_id = segment.split(":", 1)
    return {
        "segment": segment,
        "kind": kind,
        "nodeId": int(node_id),
        "name": name,
        "path": list(path or [segment]),
        "parentSegment": parent_segment,
        "children": list(children or []),
        "unitId": unit_id,
    }


def _snapshot(
    *,
    period_id: int = 589,
    period_name: str = "S26",
    scraped_at: str = "2026-04-01T00:00:00+00:00",
    root_segment: str = "title:1000",
    max_depth: int = 9,
    nodes: list[dict] | None = None,
) -> dict:
    return {
        "periodId": period_id,
        "periodName": period_name,
        "scrapedAt": scraped_at,
        "rootSegment": root_segment,
        "maxDepth": max_depth,
        "nodes": nodes or [],
    }


def test_merge_unions_disjoint_subtrees(tmp_path):
    """Three shards with disjoint nodes → union with no duplicates."""
    a = _snapshot(nodes=[_node("title:1000"), _node("title:2000")])
    b = _snapshot(nodes=[_node("title:1000"), _node("title:3000")])
    c = _snapshot(nodes=[_node("title:1000"), _node("title:4000")])

    ap = tmp_path / "a.json"
    bp = tmp_path / "b.json"
    cp = tmp_path / "c.json"
    out = tmp_path / "merged.json"
    for p, s in [(ap, a), (bp, b), (cp, c)]:
        p.write_text(json.dumps(s), encoding="utf-8")

    rc = merge_main([
        "--in", str(ap), str(bp), str(cp), "--out", str(out),
    ])
    assert rc == 0

    merged = json.loads(out.read_text(encoding="utf-8"))
    segs = [n["segment"] for n in merged["nodes"]]
    assert segs == sorted(segs)  # deterministic segment order
    assert set(segs) == {"title:1000", "title:2000", "title:3000", "title:4000"}


def test_merge_uses_max_depth(tmp_path):
    """Output maxDepth = max across inputs."""
    a = _snapshot(max_depth=6, nodes=[_node("title:1000")])
    b = _snapshot(max_depth=9, nodes=[_node("title:1000")])
    c = _snapshot(max_depth=3, nodes=[_node("title:1000")])

    merged = merge_snapshots([a, b, c])
    assert merged["maxDepth"] == 9


def test_merge_takes_period_name_and_scraped_at_from_first(tmp_path):
    a = _snapshot(
        period_name="First",
        scraped_at="2026-04-01T00:00:00+00:00",
        nodes=[_node("title:1000")],
    )
    b = _snapshot(
        period_name="Second",
        scraped_at="2026-04-02T00:00:00+00:00",
        nodes=[_node("title:1000")],
    )
    merged = merge_snapshots([a, b])
    assert merged["periodName"] == "First"
    assert merged["scrapedAt"] == "2026-04-01T00:00:00+00:00"


def test_merge_period_mismatch_raises_system_exit(tmp_path):
    a = _snapshot(period_id=589, nodes=[_node("title:1000")])
    b = _snapshot(period_id=588, nodes=[_node("title:1000")])
    ap = tmp_path / "a.json"
    bp = tmp_path / "b.json"
    out = tmp_path / "merged.json"
    ap.write_text(json.dumps(a), encoding="utf-8")
    bp.write_text(json.dumps(b), encoding="utf-8")

    with pytest.raises(SystemExit) as ei:
        merge_main(["--in", str(ap), str(bp), "--out", str(out)])
    assert "periodId" in str(ei.value)


def test_merge_root_segment_mismatch_raises(tmp_path):
    a = _snapshot(root_segment="title:1000", nodes=[_node("title:1000")])
    b = _snapshot(root_segment="title:9999", nodes=[_node("title:9999")])
    ap = tmp_path / "a.json"
    bp = tmp_path / "b.json"
    out = tmp_path / "merged.json"
    ap.write_text(json.dumps(a), encoding="utf-8")
    bp.write_text(json.dumps(b), encoding="utf-8")

    with pytest.raises(SystemExit) as ei:
        merge_main(["--in", str(ap), str(bp), "--out", str(out)])
    assert "rootSegment" in str(ei.value)


def test_merge_prefers_record_with_more_children():
    """Collision: shard 0 saw title:2000 as a bare node (no children walked);
    shard 1's record has walked children → shard 1's record wins."""
    a = _snapshot(nodes=[_node("title:2000", name="X", children=[])])
    b = _snapshot(nodes=[
        _node("title:2000", name="X", children=["title:3000", "title:3001"])
    ])
    merged = merge_snapshots([a, b])
    node = next(n for n in merged["nodes"] if n["segment"] == "title:2000")
    assert node["children"] == ["title:3000", "title:3001"]


def test_merge_prefers_non_empty_name_on_children_tie():
    a = _snapshot(nodes=[_node("title:2000", name="", children=["title:3000"])])
    b = _snapshot(nodes=[_node("title:2000", name="Faculty A", children=["title:3000"])])
    merged = merge_snapshots([a, b])
    node = next(n for n in merged["nodes"] if n["segment"] == "title:2000")
    assert node["name"] == "Faculty A"


def test_merge_prefers_non_null_unit_id_on_children_and_name_tie():
    a = _snapshot(nodes=[_node("exam:5", name="X", unit_id=None)])
    b = _snapshot(nodes=[_node("exam:5", name="X", unit_id=42)])
    merged = merge_snapshots([a, b])
    node = next(n for n in merged["nodes"] if n["segment"] == "exam:5")
    assert node["unitId"] == 42


def test_merge_first_wins_on_full_tie():
    a = _snapshot(nodes=[
        _node("title:2000", name="A", children=["c"], unit_id=1)
    ])
    b = _snapshot(nodes=[
        _node("title:2000", name="B", children=["c"], unit_id=1)
    ])
    merged = merge_snapshots([a, b])
    node = next(n for n in merged["nodes"] if n["segment"] == "title:2000")
    assert node["name"] == "A"


def test_merge_output_shape_matches_snapshot_to_dict(tmp_path):
    """The output keys must line up with CatalogSnapshot.to_dict() so
    render_markdown.py can eat it without changes."""
    a = _snapshot(nodes=[_node("title:1000")])
    b = _snapshot(nodes=[_node("title:2000")])
    merged = merge_snapshots([a, b])
    assert set(merged.keys()) == {
        "periodId", "periodName", "scrapedAt",
        "rootSegment", "maxDepth", "nodes",
    }
    assert isinstance(merged["nodes"], list)


def test_merge_deterministic_node_order(tmp_path):
    """Nodes must be sorted by segment, regardless of input order."""
    a = _snapshot(nodes=[_node("title:5000"), _node("title:1000")])
    b = _snapshot(nodes=[_node("title:3000"), _node("title:2000")])
    merged = merge_snapshots([a, b])
    segs = [n["segment"] for n in merged["nodes"]]
    assert segs == ["title:1000", "title:2000", "title:3000", "title:5000"]


def test_merge_end_to_end_via_cli(tmp_path):
    """Full CLI: two files in, one file out with correct union content."""
    a = _snapshot(nodes=[_node("title:1000"), _node("title:2000")])
    b = _snapshot(nodes=[_node("title:1000"), _node("title:3000")])
    ap = tmp_path / "a.json"
    bp = tmp_path / "b.json"
    out = tmp_path / "merged.json"
    ap.write_text(json.dumps(a), encoding="utf-8")
    bp.write_text(json.dumps(b), encoding="utf-8")

    rc = merge_main(["--in", str(ap), str(bp), "--out", str(out)])
    assert rc == 0
    merged = json.loads(out.read_text(encoding="utf-8"))
    assert {n["segment"] for n in merged["nodes"]} == {
        "title:1000", "title:2000", "title:3000",
    }
    assert merged["periodId"] == 589
    assert merged["rootSegment"] == "title:1000"


def test_merge_empty_list_raises():
    with pytest.raises(ValueError):
        merge_snapshots([])
