"""Tests for ``merge_courses`` — the N-shard courses.json unioner.

The output must have the exact shape :func:`fetch_courses.fetch_courses`
writes so it can be fed to ``render_markdown.py --courses`` unchanged.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR))

from merge_courses import main as merge_main  # noqa: E402
from merge_courses import merge_courses  # noqa: E402


def _course(uid: int, title: str = "", **extras) -> dict:
    """Build a minimal Course.to_dict()-shaped payload."""
    return {
        "unit_id": uid,
        "period_id": 589,
        "title": title or f"Course {uid}",
        "permalink": f"https://www.campo.fau.de/qisserver/pages/foo?unitId={uid}",
        "course_type": None,
        "short_text": None,
        "ects": None,
        "language": None,
        "turnus": None,
        "instructors_resp": [],
        "instructors_exec": [],
        "appointments": [],
        "org_unit": None,
        "assigned_programs": [],
        "description": None,
        "extra_links": [],
        **extras,
    }


def _failure(uid: int, err: str = "boom") -> dict:
    return {"unitId": uid, "error": err}


def _shard(
    *,
    period_id: int = 589,
    period_name: str = "S26",
    courses: list[dict] | None = None,
    failures: list[dict] | None = None,
) -> dict:
    """Build one fetch_courses.py-shaped payload for one shard."""
    payload: dict = {
        "periodId": period_id,
        "periodName": period_name,
        "fetchedAt": "2026-04-01T00:00:00+00:00",
        "courses": list(courses or []),
    }
    if failures is not None:
        payload["failures"] = list(failures)
    return payload


def test_merge_unions_disjoint_courses(tmp_path):
    """Three shards with disjoint uids → union with all entries present."""
    a = _shard(courses=[_course(1000), _course(1003)])
    b = _shard(courses=[_course(1001), _course(1004)])
    c = _shard(courses=[_course(1002), _course(1005)])

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
    uids = [c["unit_id"] for c in merged["courses"]]
    assert uids == sorted(uids)  # deterministic uid-ascending order
    assert set(uids) == {1000, 1001, 1002, 1003, 1004, 1005}


def test_merge_takes_period_name_from_first():
    a = _shard(period_name="First", courses=[_course(1000)])
    b = _shard(period_name="Second", courses=[_course(1001)])
    merged = merge_courses([a, b])
    assert merged["periodName"] == "First"


def test_merge_period_mismatch_raises_system_exit(tmp_path):
    a = _shard(period_id=589, courses=[_course(1000)])
    b = _shard(period_id=588, courses=[_course(1001)])
    ap = tmp_path / "a.json"
    bp = tmp_path / "b.json"
    out = tmp_path / "merged.json"
    ap.write_text(json.dumps(a), encoding="utf-8")
    bp.write_text(json.dumps(b), encoding="utf-8")

    with pytest.raises(SystemExit) as ei:
        merge_main(["--in", str(ap), str(bp), "--out", str(out)])
    assert "periodId" in str(ei.value)


def test_merge_dedupes_courses_by_unit_id():
    """Same uid appearing in two shards → one entry (first-wins).

    Each uid should belong to exactly one shard in practice; this is
    defensive against the pathological case where the sharder
    misassigns.
    """
    a = _shard(courses=[_course(1000, title="From shard A")])
    b = _shard(courses=[_course(1000, title="From shard B")])
    merged = merge_courses([a, b])
    assert len(merged["courses"]) == 1
    assert merged["courses"][0]["title"] == "From shard A"


def test_merge_courses_sorted_by_unit_id():
    """Final courses list must be sorted by unit_id ascending."""
    a = _shard(courses=[_course(3000), _course(1000)])
    b = _shard(courses=[_course(4000), _course(2000)])
    merged = merge_courses([a, b])
    uids = [c["unit_id"] for c in merged["courses"]]
    assert uids == [1000, 2000, 3000, 4000]


def test_merge_unions_failures_and_dedupes(tmp_path):
    """Failures unioned across shards, deduped by unitId, first-wins."""
    a = _shard(
        courses=[_course(1000)],
        failures=[_failure(9000, "timeout"), _failure(9001, "500")],
    )
    b = _shard(
        courses=[_course(1001)],
        # 9000 is a dupe (first-wins → "timeout"). 9002 is new.
        failures=[_failure(9000, "different error"), _failure(9002, "404")],
    )
    merged = merge_courses([a, b])
    fail_uids = [f["unitId"] for f in merged["failures"]]
    assert fail_uids == [9000, 9001, 9002]
    err_by_uid = {f["unitId"]: f["error"] for f in merged["failures"]}
    assert err_by_uid[9000] == "timeout"  # first-wins
    assert err_by_uid[9002] == "404"


def test_merge_preserves_failure_input_order():
    """Failures from shard 0 come before shard 1's, etc.

    Not sorted by unitId — the operator scanning the failures list
    wants to see shard-0 problems first, then shard-1's.
    """
    a = _shard(courses=[], failures=[_failure(9005), _failure(9001)])
    b = _shard(courses=[], failures=[_failure(9003), _failure(9002)])
    merged = merge_courses([a, b])
    assert [f["unitId"] for f in merged["failures"]] == [9005, 9001, 9003, 9002]


def test_merge_output_shape_matches_fetch_courses(tmp_path):
    """Output keys must line up with fetch_courses.py's output so
    render_markdown --courses eats it without changes."""
    a = _shard(courses=[_course(1000)], failures=[])
    b = _shard(courses=[_course(1001)], failures=[])
    merged = merge_courses([a, b])
    assert set(merged.keys()) >= {
        "periodId", "periodName", "fetchedAt", "courses", "failures",
    }
    assert isinstance(merged["courses"], list)
    assert isinstance(merged["failures"], list)


def test_merge_missing_failures_key_is_ok(tmp_path):
    """A shard payload without a 'failures' key must merge cleanly.

    Real fetch_courses.py always writes the key, but be defensive
    against manual edits or legacy files.
    """
    # No 'failures' at all in either shard.
    a = _shard(courses=[_course(1000)])
    b = _shard(courses=[_course(1001)])
    del a["courses"]  # even 'courses' can be missing
    a["courses"] = []  # keep valid — this line simulates an empty shard
    merged = merge_courses([a, b])
    assert merged["failures"] == []
    assert {c["unit_id"] for c in merged["courses"]} == {1001}


def test_merge_empty_list_raises():
    with pytest.raises(ValueError):
        merge_courses([])


def test_merge_end_to_end_via_cli(tmp_path):
    """Full CLI: three files in, one file out, correct union & dedup."""
    a = _shard(
        courses=[_course(1000), _course(1001)],
        failures=[_failure(9000, "timeout")],
    )
    b = _shard(
        courses=[_course(1000), _course(1002)],  # 1000 dup → drops
        failures=[_failure(9001, "500")],
    )
    c = _shard(
        courses=[_course(1003)],
        failures=[_failure(9000, "dup ignored")],  # 9000 dup → drops
    )
    ap = tmp_path / "courses-0.json"
    bp = tmp_path / "courses-1.json"
    cp = tmp_path / "courses-2.json"
    out = tmp_path / "589-courses.json"
    ap.write_text(json.dumps(a), encoding="utf-8")
    bp.write_text(json.dumps(b), encoding="utf-8")
    cp.write_text(json.dumps(c), encoding="utf-8")

    rc = merge_main(
        ["--in", str(ap), str(bp), str(cp), "--out", str(out)]
    )
    assert rc == 0
    merged = json.loads(out.read_text(encoding="utf-8"))
    assert {c["unit_id"] for c in merged["courses"]} == {1000, 1001, 1002, 1003}
    assert merged["periodId"] == 589
    assert [f["unitId"] for f in merged["failures"]] == [9000, 9001]
