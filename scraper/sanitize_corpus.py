"""Strip personal data from the published markdown corpus in-place.

This is the DSGVO minimisation sweep. It is used two ways:

1. **Working-tree sweep** — cleans ``data/**/*.md`` files so they can be
   committed without personal data. Run once after
   :mod:`render_markdown` while the render step still emits legacy
   personal fields, and used again in verify-mode to prove no hits
   remain.
2. **git-filter-repo blob callback** — the same rules applied to every
   historic blob so a rewritten history is also clean. See
   :func:`sanitize_bytes` — that's the entry point for the callback.

What we strip:

* ``## Lehrende`` sections and standalone ``- **Verantwortlich:**`` /
  ``- **Durchführend:**`` / ``- **Modulverantwortlich:**`` bullets in
  the per-program course pages under ``data/{period}/`` (org unit info
  is preserved in the separate *Organisation / Studiengänge* block).
* The ``Dozent/-in`` column of Termine tables (last-column drop across
  header, separator, and every data row).
* Every ``…@fau.de`` (and ``@…uni-erlangen.de``) address, replaced by
  ``[E-Mail entfernt]`` (structured contact data, personal on its face).
* Every DE phone number, replaced by ``[Telefon entfernt]`` (matched
  liberally: ``+49`` or ``0`` followed by digits/spaces/dashes/slashes,
  at least 8 digits).
* Standalone lines in ``data/studiengang/**`` that are just a titled
  person name (``Prof. Dr. Vorname Nachname`` on its own line/paragraph
  — the studiengang-page contact-person pattern).

What we deliberately do NOT touch:

* PO regulation text (``data/pruefungsordnungen/**``): named references
  in official public regulatory PDFs are left in prose so the meaning
  survives; contact data (emails/phones) still gets stripped.
* Free-flowing prose mentions of names in studiengang pages: only
  standalone name lines are stripped, so sentences aren't gutted.

The functions are pure text-in / text-out — trivial to unit-test and
reusable inside the git-filter-repo callback.
"""
from __future__ import annotations

import argparse
import logging
import re
import sys
from pathlib import Path

log = logging.getLogger("campo.sanitize_corpus")

# ── Line-level patterns ────────────────────────────────────────────────────

# Full-line: a personal-role bullet in a course/module block.
_RE_PERSONAL_BULLET = re.compile(
    r"^\s*[-*]\s+\*\*(?:Verantwortlich|Durchführend|Durchfuehrend|"
    r"Modulverantwortlich|Modulverantwortung|Modulverantwortliche/-r|"
    r"Ansprechpartner|Ansprechpartner/-in|Kontakt)\:\*\*\s+.*$",
    re.MULTILINE,
)

# Full-line: the "## Lehrende" heading (with or without trailing newline).
_RE_LEHRENDE_HEADING = re.compile(
    r"^\s*#{1,4}\s+Lehrende\s*$",
    re.MULTILINE,
)

# Standalone name line in a studiengang page: whole line is a titled
# person name (Prof. Dr. Foo Bar) and nothing else. Titles are matched
# generously; the tail is 2–4 Umlaut/hyphenated tokens.
_TITLE_ALTERNATION = (
    r"(?:Prof\.?|Priv\.-Doz\.?|Priv\. Doz\.?|PD|Dr\.-Ing\.?|Dr\.?|apl\.\s*Prof\.?"
    r"|Hon\.\s*Prof\.?|Ass\.-Prof\.?|Ass\. Prof\.?|Junior[- ]?Prof\.?|Juniorprofessor)"
)
_RE_STANDALONE_NAME_LINE = re.compile(
    r"^\s*(?:" + _TITLE_ALTERNATION + r"\s+){1,3}"
    r"(?:[A-ZÄÖÜ][\w\-']+(?:\s+(?:[A-ZÄÖÜ][\w\-']+|[a-zäöü]{1,3}))?\s*){1,4}$",
    re.MULTILINE,
)

# Full email of the form [E-Mail entfernt] and [E-Mail entfernt] and .uni-erlangen.de
_RE_EMAIL = re.compile(
    r"[a-zA-Z0-9._%+\-]+@(?:[a-zA-Z0-9.\-]+\.)?(?:fau\.de|uni-erlangen\.de)",
)

# DE phones — +49 xxx or 0xxx with 8+ digits total. The character class covers
# spaces, dashes, slashes and parentheses inside the number.
_RE_PHONE = re.compile(
    r"(?:☎\s*)?"                                    # optional phone glyph
    r"(?:\+49[\-\s/()]?|\b0)(?:[\d\-\s/()]{7,25}\d)"
)

# ── Termine-table column drop ──────────────────────────────────────────────

_RE_TERMINE_HEADER = re.compile(
    r"^(\|\s*Rhythmus\s*\|.*?\|\s*)(?:Dozent(?:/-in)?|Lehrende)\s*\|\s*$",
    re.MULTILINE,
)

def _drop_dozent_column(md: str) -> str:
    """Remove the Dozent/-in column from every Termine table.

    A Termine table starts with the header line
    ``| Rhythmus | Tag | Zeit | Datum von–bis | Raum | Dozent/-in |``.
    We find that header, count its columns, drop the last one, then drop
    the last cell from the following separator line and from each
    contiguous data row (rows starting with ``|``). The loop stops at
    the first non-row line.
    """
    lines = md.split("\n")
    out: list[str] = []
    i = 0
    while i < len(lines):
        m = _RE_TERMINE_HEADER.match(lines[i])
        if not m:
            out.append(lines[i])
            i += 1
            continue
        # Header line — rewrite to drop the last column.
        out.append(_drop_last_cell(lines[i]))
        i += 1
        # Separator row — also drop last cell.
        if i < len(lines) and re.match(r"^\|\s*[\-:]+\s*(\|\s*[\-:]+\s*)+\|\s*$", lines[i]):
            out.append(_drop_last_cell(lines[i]))
            i += 1
        # Data rows: every subsequent line starting with '|'.
        while i < len(lines) and lines[i].lstrip().startswith("|"):
            out.append(_drop_last_cell(lines[i]))
            i += 1
    return "\n".join(out)

def _drop_last_cell(row: str) -> str:
    """Drop the trailing cell from a markdown table row.

    Splits on ``|`` respecting leading/trailing empties; drops the last
    non-empty segment and rejoins.
    """
    # A well-formed row is ``| a | b | c |`` — split gives ['', ' a ',
    # ' b ', ' c ', '']. Drop the second-to-last (the last real cell).
    parts = row.split("|")
    if len(parts) < 3:
        return row  # nothing to drop
    trimmed = parts[:-2] + [parts[-1]]
    return "|".join(trimmed)

# ── Block-level Lehrende removal ───────────────────────────────────────────

def _strip_lehrende_block(md: str) -> str:
    """Remove ``## Lehrende`` header when followed only by our personal
    bullets, plus the bullets themselves. Bullets outside a header are
    also removed (some render sites emit the bullet without a header).
    """
    # 1) Remove any bullet line individually — safe: those bullets are
    #    always about personal roles.
    md = _RE_PERSONAL_BULLET.sub("", md)
    # 2) A "## Lehrende" that is now followed by nothing but blank space
    #    (bullets were removed) can go too.
    md = re.sub(
        r"^(\s*#{1,4}\s+Lehrende\s*\n)(\s*\n)*",
        "",
        md,
        flags=re.MULTILINE,
    )
    return md

# ── Composite pipeline ─────────────────────────────────────────────────────

def sanitize_text(md: str, *, path: str = "") -> str:
    """Apply every rule in order and collapse the leftover blank runs."""
    md = _strip_lehrende_block(md)
    md = _drop_dozent_column(md)
    md = _RE_EMAIL.sub("[E-Mail entfernt]", md)
    md = _RE_PHONE.sub("[Telefon entfernt]", md)
    if "/studiengang/" in path or path.startswith("studiengang/"):
        md = _RE_STANDALONE_NAME_LINE.sub("[Kontaktperson entfernt]", md)
    # Collapse 3+ blank lines to 2.
    md = re.sub(r"\n{3,}", "\n\n", md)
    return md

def sanitize_bytes(blob: bytes, *, path: str = "") -> bytes:
    """The git-filter-repo blob-callback entry point.

    Non-utf8 blobs (e.g. the pdf-derived PO images) pass through
    unchanged.
    """
    try:
        text = blob.decode("utf-8")
    except UnicodeDecodeError:
        return blob
    if not path.endswith(".md"):
        return blob
    cleaned = sanitize_text(text, path=path)
    if cleaned == text:
        return blob
    return cleaned.encode("utf-8")

# ── CLI: sweep a directory ─────────────────────────────────────────────────

def _iter_targets(root: Path) -> list[Path]:
    """Every .md file under ``root``."""
    return sorted(p for p in root.rglob("*.md") if p.is_file())

def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description=(
            "Strip personal data from the corpus in-place. Prints a "
            "line-count-delta summary; nonzero exit if --check-only finds hits."
        )
    )
    p.add_argument("root", type=Path, help="corpus root, e.g. ``data``")
    p.add_argument(
        "--check-only",
        action="store_true",
        help=(
            "Report but do not write. Exits 1 if any file would change "
            "or any of the DSGVO patterns (emails, phones, personal "
            "bullets, Dozent columns) survive."
        ),
    )
    p.add_argument("-v", "--verbose", action="count", default=0)
    args = p.parse_args(argv)

    level = logging.WARNING - 10 * args.verbose
    logging.basicConfig(level=max(level, logging.DEBUG), format="%(levelname)s %(name)s: %(message)s")

    root: Path = args.root
    if not root.is_dir():
        raise SystemExit(f"sanitize_corpus: {root} is not a directory")

    targets = _iter_targets(root)
    changed = 0
    hits: dict[str, int] = {}
    total_bytes_before = 0
    total_bytes_after = 0

    for path in targets:
        original = path.read_text(encoding="utf-8")
        cleaned = sanitize_text(original, path=str(path))
        total_bytes_before += len(original)
        total_bytes_after += len(cleaned)
        if cleaned != original:
            changed += 1
            if args.check_only:
                # Attribute hits to a pattern for the summary.
                for name, rx in (
                    ("email", _RE_EMAIL),
                    ("phone", _RE_PHONE),
                    ("personal-bullet", _RE_PERSONAL_BULLET),
                    ("lehrende-heading", _RE_LEHRENDE_HEADING),
                    ("dozent-column", _RE_TERMINE_HEADER),
                ):
                    n = len(rx.findall(original))
                    if n:
                        hits[name] = hits.get(name, 0) + n
                log.info("would change: %s", path)
            else:
                path.write_text(cleaned, encoding="utf-8")
                log.info("cleaned: %s", path)

    delta = total_bytes_before - total_bytes_after
    verb = "would change" if args.check_only else "changed"
    print(
        f"sanitize_corpus: scanned {len(targets)} files under {root} — "
        f"{verb} {changed}; -{delta:,} bytes"
    )
    if args.check_only and hits:
        for k in sorted(hits):
            print(f"  {k}: {hits[k]} hits")
    if args.check_only and changed:
        return 1
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
