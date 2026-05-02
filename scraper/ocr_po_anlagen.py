"""OCR the image-rendered Anlagen of FAU Prüfungsordnungen.

`pymupdf4llm` extracts text from PDFs perfectly when text is text — but ~25
% of FAU PO PDFs render their *Curricular-Übersicht* / *Studienverlaufs-
plan* tables as **images** (the source PDF embeds a rasterised diagram).
The structured Pflicht-module extractor in :mod:`extract_pflicht_module`
can't see those tables.

This module re-opens each cached PO PDF (under ``tmp/fau-pdfs/{stem}/
doc.pdf``), finds pages that contain images, and runs a full-page OCR
(via PyMuPDF + Tesseract, German language) on each of them. The OCR text
is appended to the existing PO markdown as an
``## OCR-Anhang (Bild-Inhalt aus PDF-Anlagen)`` section so all downstream
tools (extract_pflicht_module, analyze_pflicht) pick it up without
further changes.

Requirements:
- Tesseract installed with German language pack:
  - macOS: ``brew install tesseract tesseract-lang``
  - Ubuntu: ``apt-get install tesseract-ocr tesseract-ocr-deu``
- ``TESSDATA_PREFIX`` env var pointing at the tessdata folder (PyMuPDF
  reads this); on macOS+Homebrew that's
  ``/opt/homebrew/share/tessdata``.

Usage::

    python scraper/ocr_po_anlagen.py --pdfs tmp/fau-pdfs --data data \\
        --interval 0 -v
"""
from __future__ import annotations

import argparse
import datetime as _dt
import logging
import os
import sys
from pathlib import Path
from typing import Iterable

ROOT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT_DIR))

log = logging.getLogger("campo.ocr_po_anlagen")

OCR_MARKER = "## OCR-Anhang (Bild-Inhalt aus PDF-Anlagen)"


def _ensure_tessdata() -> None:
    """Best-effort autodetection of TESSDATA_PREFIX if it's not already set."""
    if os.environ.get("TESSDATA_PREFIX"):
        return
    for candidate in [
        "/opt/homebrew/share/tessdata",       # macOS Homebrew arm64
        "/usr/local/share/tessdata",          # macOS Homebrew x86 / generic
        "/usr/share/tessdata",                # Debian/Ubuntu
        "/usr/share/tesseract-ocr/4.00/tessdata",
        "/usr/share/tesseract-ocr/5/tessdata",
    ]:
        if Path(candidate).is_dir():
            os.environ["TESSDATA_PREFIX"] = candidate
            log.info("set TESSDATA_PREFIX=%s", candidate)
            return
    log.warning("TESSDATA_PREFIX not set and no tessdata folder auto-detected — "
                "set it manually or install tesseract-ocr-deu")


def _has_marker(md_text: str) -> bool:
    return OCR_MARKER in md_text


def ocr_pages_of_pdf(pdf_path: Path, *, dpi: int = 300, language: str = "deu") -> list[tuple[int, str]]:
    """Return ``[(page_number, ocr_text), …]`` for every page with images.

    A page is OCR'd when ``page.get_images()`` is non-empty. The OCR is
    full-page (``full=True``) so we pick up text *around* the image plus
    whatever Tesseract recovers from the image itself.
    """
    import fitz  # local import so non-OCR runs don't pay the import cost
    out: list[tuple[int, str]] = []
    try:
        doc = fitz.open(pdf_path)
    except Exception as e:  # noqa: BLE001
        log.warning("can't open %s (%s)", pdf_path, e)
        return out
    try:
        for i, page in enumerate(doc):
            if not page.get_images():
                continue
            try:
                tp = page.get_textpage_ocr(language=language, dpi=dpi, full=True)
                ocr_text = page.get_text(textpage=tp).strip()
            except Exception as e:  # noqa: BLE001
                log.debug("OCR failed for %s page %d: %s", pdf_path.name, i, e)
                continue
            if ocr_text:
                out.append((i, ocr_text))
    finally:
        doc.close()
    return out


def _format_appendix(pages: list[tuple[int, str]]) -> str:
    parts: list[str] = [
        OCR_MARKER,
        "",
        "_Diese Sektion wurde automatisch durch Tesseract-OCR aus den "
        "Bild-Seiten der zugehörigen PDF-Datei erzeugt — Anlagen, die im "
        "Original als Diagramm/Bild gerendert sind und daher von der "
        "regulären PDF-Text-Extraktion nicht erfasst wurden. OCR-Text kann "
        "Erkennungsfehler enthalten (Zeichen, Tabellenstruktur), liefert "
        "aber für RAG- und Heuristik-Pipelines die fehlende Modul- und "
        "Pflicht-Information._",
        "",
    ]
    for page_no, text in pages:
        parts.append(f"### OCR Seite {page_no + 1}")
        parts.append("")
        parts.append("```")
        parts.append(text)
        parts.append("```")
        parts.append("")
    return "\n".join(parts)


def append_ocr_to_markdown(md_path: Path, pdf_path: Path, *, dpi: int = 300) -> int:
    """OCR ``pdf_path`` and append the result to ``md_path`` (in-place).

    Returns the number of pages OCR'd. Skips the work if the markdown
    already has an OCR appendix (idempotent).
    """
    text = md_path.read_text(encoding="utf-8")
    if _has_marker(text):
        return 0
    pages = ocr_pages_of_pdf(pdf_path, dpi=dpi)
    if not pages:
        return 0
    appendix = _format_appendix(pages)
    md_path.write_text(text.rstrip() + "\n\n" + appendix + "\n", encoding="utf-8")
    return len(pages)


def main(argv: Iterable[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument(
        "--pdfs", type=Path, default=Path("tmp/fau-pdfs"),
        help="cached PDF directory (output of fau_corpus.py)",
    )
    p.add_argument(
        "--data", type=Path, default=Path("data"), help="corpus root",
    )
    p.add_argument(
        "--limit", type=int, default=None,
        help="only process this many PO markdowns (testing/dev)",
    )
    p.add_argument(
        "--dpi", type=int, default=300,
        help="OCR rasterisation DPI (300 is a good default; lower = faster)",
    )
    p.add_argument(
        "--skip-existing", action="store_true", default=True,
        help="skip POs that already have an OCR appendix (default; idempotent)",
    )
    p.add_argument("-v", "--verbose", action="count", default=0)
    args = p.parse_args(list(argv) if argv else None)

    level = logging.WARNING - 10 * args.verbose
    logging.basicConfig(
        level=max(level, logging.DEBUG),
        format="%(levelname)s %(name)s: %(message)s",
    )
    _ensure_tessdata()

    po_root = args.data / "pruefungsordnungen"
    if not po_root.is_dir():
        log.warning("no PO directory at %s", po_root)
        return 0

    md_files = [f for f in sorted(po_root.rglob("*.md")) if f.name != "INDEX.md"]
    if args.limit:
        md_files = md_files[: args.limit]

    started = _dt.datetime.now()
    total_pages = 0
    processed = 0
    skipped_existing = 0
    skipped_no_pdf = 0
    for i, md in enumerate(md_files, 1):
        pdf = args.pdfs / md.stem / "doc.pdf"
        if not pdf.exists():
            skipped_no_pdf += 1
            continue
        text = md.read_text(encoding="utf-8")
        if args.skip_existing and _has_marker(text):
            skipped_existing += 1
            continue
        try:
            n = append_ocr_to_markdown(md, pdf, dpi=args.dpi)
        except Exception as e:  # noqa: BLE001
            log.warning("%s: OCR failed (%s)", md.relative_to(args.data), e)
            continue
        if n:
            log.info("%s: OCR'd %d pages", md.relative_to(args.data), n)
            processed += 1
            total_pages += n
        if i % 50 == 0:
            elapsed = (_dt.datetime.now() - started).total_seconds()
            rate = i / max(elapsed, 1e-6)
            log.info(
                "progress %d/%d (skipped existing=%d, no-pdf=%d, "
                "OCR'd %d POs / %d pages, %.2f md/s)",
                i, len(md_files), skipped_existing, skipped_no_pdf,
                processed, total_pages, rate,
            )

    print(
        f"OCR pass complete: {processed} POs augmented, {total_pages} pages OCR'd "
        f"(skipped existing: {skipped_existing}, no-pdf: {skipped_no_pdf})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
