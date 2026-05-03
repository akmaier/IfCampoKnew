"""Aggregate Campo instructor strings into a single ``data/personen/INDEX.md``.

For each unique instructor name in the courses-JSON we have on disk:
  * heuristically split off the title prefix (``Prof. Dr.``, ``Dr.-Ing.``, …);
  * count the courses they teach and list them with relative links to the
    program file that inlines the course;
  * include the period(s) they teach in.

Why this exists: the user wants W1/W2/W3 / academic-rank classification
ultimately, but FAUdir is a JS SPA whose API is auth-gated. As a first
useful step we surface every instructor with their teaching activity so
a RAG agent can ground answers about *who teaches X* without further
scraping. A FAUdir-driven enrichment will be merged on top in a later
step (see ``faudir_scrape.py`` once it lands).
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import logging
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Iterable

ROOT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT_DIR))

from render_markdown import slugify, node_basename  # noqa: E402

log = logging.getLogger("campo.people_index")


# Title tokens we recognise as academic / honorific prefixes.
_TITLE_TOKENS_RE = re.compile(
    r"^(?:"
    r"Prof\.?(?:in)?|"          # Prof., Prof.in
    r"Univ\.?-Prof\.?(?:in)?|"  # Univ.-Prof.
    r"Hon\.?-?Prof\.?(?:in)?|"  # Hon. Prof.
    r"PD|"                      # PD (Privatdozent)
    r"apl\.?|"                  # apl. Prof.
    r"em\.?|"                   # em. Prof.
    r"Dr\.?(?:-Ing\.?|\s*med\.?|\s*phil\.?|\s*rer\.?\s*nat\.?|\s*habil\.?|\s*hc\.?)*|"
    r"Dipl\.?(?:-Ing\.?)?|"
    r"M\.?Sc\.?|B\.?Sc\.?|MBA"
    r")\b\.?",
    re.IGNORECASE,
)


def split_title(full: str) -> tuple[str, str]:
    """Pull leading academic/honorific title tokens off ``full``.

    Returns ``(title, name)`` — both stripped.
    """
    s = full.strip()
    title_parts: list[str] = []
    while True:
        m = _TITLE_TOKENS_RE.match(s)
        if not m:
            break
        title_parts.append(m.group(0))
        s = s[m.end():].lstrip()
    return " ".join(title_parts), s


# A title token *anywhere* in a string. When we see one mid-string, the
# preceding word(s) belong to a previous person — Campo's renderer
# concatenates several `<li>` instructors and the parser used to flatten
# them into one big string. We split on each title-prefix start so the
# names emerge as separate entries.
_TITLE_TOKEN_ANY_RE = re.compile(
    r"\b(?:"
    r"Prof\.?(?:in)?|"
    r"Univ\.?-Prof\.?(?:in)?|"
    r"Hon\.?-?Prof\.?(?:in)?|"
    r"PD|"
    r"apl\.?-?Prof\.?(?:in)?|"
    r"em\.?-?Prof\.?(?:in)?|"
    r"Dr\.?(?:-Ing\.?|\s+habil\.?|\s+med\.?|\s+phil\.?|\s+rer\.?\s*nat\.?|\s+hc\.?)?|"
    r"Dipl\.?(?:-Ing\.?)?"
    r")\b\.?"
)


# Role-suffix annotations that Campo appends to a name in some contexts:
# "Prof. Dr.-Ing. Andreas Maier (Zuständigkeit: Verantwortliche/-r)",
# "Dr. Foo Bar (Durchführende/-r)", "Müller, Hans (Beteiligte/-r)" etc.
# These are role tags, not part of the person's identity — strip them so
# the same person doesn't get split into multiple by-name buckets.
_ROLE_SUFFIX_RE = re.compile(
    r"\s*\((?:Zust[äa]ndigkeit:\s*)?"
    r"(?:Verantwortliche|Durchf[üu]hrende|Begleitende|Beteiligte|Mitwirkende|Pr[üu]fende)"
    # Optional gender/role inflection: "/-r", "/-in", "/r", "/in", "-r", "-in"
    r"(?:[/-]+(?:r|in))?"
    r"\s*\)\s*$",
    re.IGNORECASE,
)


def _strip_role_suffix(s: str) -> str:
    """Remove a trailing role annotation like ``(Zuständigkeit: Verantwortliche/-r)``."""
    return _ROLE_SUFFIX_RE.sub("", s).strip()


def split_concatenated_names(s: str) -> list[str]:
    """Split a Campo instructor string that holds *multiple* persons.

    The historical bug: the Termine instructor cell rendered each instructor
    as one ``<li>``, but the parser flattened the cell to text — so
    ``"Heinz Werner Höppel PD Dr. habil. Tobias Fey Dr.-Ing. Joachim Kaschta"``
    came out as one string. The new parser (`parse_detail._instructors_from_cell`)
    emits each ``<li>`` separately; this function is the post-processing
    fallback that catches legacy JSON intermediates and any edge case the
    parser might still miss.

    Heuristic: a string is split BEFORE each occurrence of an academic
    title token (Prof., PD, Dr., Dr.-Ing., …) when that token is *not*
    at the very start. The first segment may therefore be a title-less
    name (e.g. *Heinz Werner Höppel*). Adjacent title-less names cannot
    be separated by this heuristic; they stay together (rare in practice
    once the parser is fixed).
    """
    s = (s or "").strip()
    # Strip the trailing role annotation BEFORE splitting so it doesn't
    # interfere with title-token detection and so each split-out person
    # also gets stripped (we re-strip per part below as belt-and-braces).
    s = _strip_role_suffix(s)
    if not s:
        return []
    starts: list[int] = []
    for m in _TITLE_TOKEN_ANY_RE.finditer(s):
        # Don't split at position 0 — the prefix at the very start belongs
        # to the first name.
        if m.start() == 0:
            continue
        # Don't split if the preceding char is a hyphen / dot / period or
        # we're inside another title sequence (e.g. "Prof. Dr." stays one).
        prev = s[m.start() - 1]
        if prev in "-.":
            continue
        # Don't split if the previous non-space token is itself a title
        # token (e.g. inside "Prof. Dr. h.c.").
        before = s[: m.start()].rstrip()
        prev_word = re.search(r"\S+$", before)
        if prev_word and _TITLE_TOKEN_ANY_RE.fullmatch(prev_word.group(0).rstrip(".")):
            continue
        starts.append(m.start())
    if not starts:
        return [s]
    parts: list[str] = []
    last = 0
    for pos in starts:
        chunk = s[last:pos].strip()
        if chunk:
            parts.append(_strip_role_suffix(chunk))
        last = pos
    parts.append(_strip_role_suffix(s[last:].strip()))
    return [p for p in parts if p]


def _short_filename_for_program_path(period_slug: str, program_seg_id: int, program_name: str) -> str:
    """Mirror the Campo renderer's filename for a program (``slug-id.md``)."""
    fake_node = {"name": program_name, "nodeId": program_seg_id}
    return f"{period_slug}/{node_basename(fake_node)}.md"


def collect_people_for_period(
    snapshot: dict, courses: dict
) -> tuple[dict[str, list[dict]], str, str]:
    """Build ``{full_name: [{title, name, period, period_slug, course_title,
    course_type, program_name, program_seg, program_node_id}, …]}``.
    """
    period_id = int(snapshot["periodId"])
    period_name = snapshot.get("periodName", f"period-{period_id}")
    period_slug = f"{period_id}-{slugify(period_name)}"

    by_segment = {n["segment"]: n for n in snapshot["nodes"]}

    # Map unit_id → program node (depth-3 ancestor).
    unit_to_program: dict[int, dict] = {}
    for n in snapshot["nodes"]:
        if not n.get("unitId"):
            continue
        if len(n["path"]) < 3:
            continue
        program_seg = n["path"][2]
        program = by_segment.get(program_seg)
        if program:
            unit_to_program[int(n["unitId"])] = program

    out: dict[str, list[dict]] = defaultdict(list)
    for c in courses.get("courses", []):
        uid = int(c["unit_id"])
        program = unit_to_program.get(uid)
        # Sweep-only courses (Tagesaktuelle-Veranstaltungen) lack a catalogue
        # parent — keep them with synthetic program info so their instructors
        # don't get dropped from the people-index.
        if program is None:
            program_name = "(nicht im Katalog auf Tiefe 4)"
            program_segment = ""
            program_node_id = 0
        else:
            program_name = program["name"]
            program_segment = program["segment"]
            program_node_id = int(program["segment"].split(":", 1)[1])
        names: set[str] = set()
        # Each raw instructor string may be a concatenation of several
        # persons (parser-bug history) — split first.
        for raw in (c.get("instructors_resp") or []) + (c.get("instructors_exec") or []):
            for n in split_concatenated_names(raw):
                names.add(n.strip())
        for a in c.get("appointments") or []:
            for raw in a.get("instructors") or []:
                for n in split_concatenated_names(raw):
                    names.add(n.strip())
        for n in names:
            if not n:
                continue
            title, plain = split_title(n)
            out[n].append(
                {
                    "title": title,
                    "name": plain,
                    "period_id": period_id,
                    "period_name": period_name,
                    "period_slug": period_slug,
                    "course_title": c.get("title", ""),
                    "course_type": c.get("course_type") or "",
                    "course_unit_id": uid,
                    "program_name": program_name,
                    "program_segment": program_segment,
                    "program_node_id": program_node_id,
                }
            )
    return out, period_slug, period_name


def render_people_md(
    people: dict[str, list[dict]],
    out_root: Path,
    sources: list[tuple[str, str]],
) -> str:
    """Single ``data/personen/INDEX.md`` aggregating every instructor.

    Sorting: by surname (last word of the name-without-title) so the doc
    reads alphabetically.
    """
    def sort_key(item: tuple[str, list[dict]]) -> tuple:
        full = item[0]
        _title, name = split_title(full)
        if not name:
            return ("￿", full.lower())
        last = name.split()[-1].lower() if name.split() else full.lower()
        return (last, name.lower())

    lines: list[str] = []
    lines.append("---")
    lines.append('kind: "campo-personen-aggregate"')
    lines.append(f"unique_persons: {len(people)}")
    total_teaching = sum(len(v) for v in people.values())
    lines.append(f"teaching_assignments: {total_teaching}")
    lines.append(
        f"scraped_at: {_dt.datetime.now(_dt.timezone.utc).isoformat(timespec='seconds')}"
    )
    if sources:
        lines.append("sources:")
        for label, src in sources:
            lines.append(f'  - {label}: {json.dumps(src, ensure_ascii=False)}')
    lines.append("---")
    lines.append("")
    lines.append("# Personen — Lehrende aus Campo")
    lines.append("")
    lines.append(
        "Diese Datei aggregiert jede Dozent/-in-Nennung aus den Campo-Veranstaltungs-"
        "Detailseiten zu einem Eintrag pro eindeutigem Namens-String. Pro Person "
        "werden Titel-Präfix (heuristisch abgespalten) und alle gelehrten "
        "Veranstaltungen (mit Programm-Datei verlinkt) aufgeführt."
    )
    lines.append("")
    lines.append("## Vorbehalte")
    lines.append("")
    lines.append(
        "* **Akademischer Rang (W1/W2/W3) ist hier _nicht_ enthalten.** Campo "
        "liefert nur den Namens-String; das genaue Rang-Niveau steht in FAUdir, "
        "dessen REST-Schnittstelle authentifiziert ist. Eine separate Datei "
        "(`personen/faudir-INDEX.md`) wird ergänzt, sobald die FAUdir-Anbindung "
        "steht."
    )
    lines.append(
        "* **Eindeutigkeits-Heuristik:** Personen werden über den exakten Namens-"
        "String aus Campo dedupliziert. Wenn dieselbe Person in einem Kurs als "
        "*Prof. Dr. Foo* und in einem anderen als *Prof. Dr. F. Foo* erscheint, "
        "stehen hier zwei Einträge. Cross-References sollte ein RAG selbst lösen."
    )
    lines.append(
        "* **Titel-Präfix** (Prof. Dr., Dr.-Ing., PD Dr., …) wird per Regex "
        "abgespalten — nur ein grober Indikator."
    )
    lines.append("")
    lines.append(
        f"## Statistik\n\n- **Eindeutige Personen-Strings:** {len(people)}\n"
        f"- **Gesamt-Lehrleistungen (Person × Kurs × Periode):** {total_teaching}"
    )
    lines.append("")
    lines.append("## Personen")
    lines.append("")
    for full, items in sorted(people.items(), key=sort_key):
        title, plain = split_title(full)
        heading = plain or full
        if title:
            lines.append(f"### {heading} ({title})")
        else:
            lines.append(f"### {heading}")
        lines.append("")
        # Group by period
        by_period: dict[str, list[dict]] = defaultdict(list)
        for it in items:
            by_period[it["period_name"]].append(it)
        for pname in sorted(by_period.keys()):
            entries = by_period[pname]
            entry = entries[0]  # for slug
            period_slug = entry["period_slug"]
            lines.append(f"- **{pname}** — {len(entries)} Veranstaltung(en):")
            # Group by program
            by_prog: dict[str, list[dict]] = defaultdict(list)
            for e in entries:
                by_prog[e["program_segment"]].append(e)
            for prog_seg, evts in by_prog.items():
                first = evts[0]
                rel = f"../{period_slug}/{slugify(first['program_name'])[:88]}-{first['program_node_id']}.md"
                course_titles = ", ".join(
                    sorted({f"{e['course_title']} — {e['course_type']}".strip(" —") for e in evts})
                )
                lines.append(f"  - in [{first['program_name']}]({rel}): {course_titles}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main(argv: Iterable[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument(
        "--inputs",
        nargs="+",
        type=Path,
        required=True,
        help="pairs of <tree>.json <courses>.json (positional, even count); "
        "e.g. tmp/589.json tmp/589-courses.json [tmp/590.json tmp/590-courses.json …]",
    )
    p.add_argument(
        "--out", type=Path, required=True, help="output dir, e.g. data/personen"
    )
    p.add_argument("-v", "--verbose", action="count", default=0)
    args = p.parse_args(list(argv) if argv else None)

    level = logging.WARNING - 10 * args.verbose
    logging.basicConfig(level=max(level, logging.DEBUG), format="%(levelname)s %(name)s: %(message)s")

    if len(args.inputs) % 2:
        p.error("--inputs needs an even number of paths (tree, courses pairs)")
    pairs = list(zip(args.inputs[0::2], args.inputs[1::2]))

    merged: dict[str, list[dict]] = defaultdict(list)
    sources: list[tuple[str, str]] = []
    for tree_path, courses_path in pairs:
        snapshot = json.loads(tree_path.read_text(encoding="utf-8"))
        courses = json.loads(courses_path.read_text(encoding="utf-8"))
        people, period_slug, period_name = collect_people_for_period(snapshot, courses)
        for k, items in people.items():
            merged[k].extend(items)
        sources.append((period_name, str(tree_path)))
        log.info("ingested %s: %d unique persons", period_name, len(people))

    args.out.mkdir(parents=True, exist_ok=True)
    out_md = args.out / "INDEX.md"
    out_md.write_text(
        render_people_md(merged, args.out, sources), encoding="utf-8"
    )
    print(
        f"wrote {out_md}: persons={len(merged)} "
        f"teaching_assignments={sum(len(v) for v in merged.values())}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
