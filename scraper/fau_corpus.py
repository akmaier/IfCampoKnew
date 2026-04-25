"""Build the FAU.de corpora — Studiengang pages and Prüfungsordnungen.

Single-script pipeline (Entry 0008, "fastest way ahead"):

    1. Read https://www.fau.de/sitemap_index.xml — gives all URLs.
    2. For each /studiengang/{slug}/ URL: fetch the HTML, extract the
       Steckbrief + the three main sections, write
       ``data/studiengang/{slug}.md``.
    3. For each .../pruefungsordnungen/{path}/ URL: fetch the HTML,
       write ``data/pruefungsordnungen/{path}/INDEX.md`` plus a
       ``{pdf-slug}.md`` per PDF — content extracted via pymupdf4llm.
    4. Top-level INDEX.md per source.

Rate-limited to 1 req/s by default (FAU's own server + the doc.zuv
PDF host). A monthly cron is enough — content changes rarely.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import logging
import re
import sys
import time
import unicodedata
from pathlib import Path
from typing import Optional

import requests
from bs4 import BeautifulSoup, Tag
from markdownify import markdownify as html_to_md  # type: ignore[import-untyped]

ROOT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT_DIR))

log = logging.getLogger("fau")


# ────────── HTTP & sitemap ─────────────────────────────────────────────────


SITEMAP_URL = "https://www.fau.de/sitemap_index.xml"
DEFAULT_UA = (
    "Mozilla/5.0 (compatible; IfCampoKnew/0.1; +https://github.com/akmaier/IfCampoKnew)"
)


class FauClient:
    def __init__(self, *, min_interval: float = 1.0, ua: str = DEFAULT_UA, timeout: float = 60.0):
        self.s = requests.Session()
        self.s.headers.update({"User-Agent": ua, "Accept": "text/html,application/xhtml+xml,application/pdf,*/*"})
        self.min_interval = min_interval
        self.timeout = timeout
        self._last = 0.0

    def _wait(self) -> None:
        dt = time.monotonic() - self._last
        if dt < self.min_interval:
            time.sleep(self.min_interval - dt)
        self._last = time.monotonic()

    def get(self, url: str) -> requests.Response:
        for attempt in range(3):
            self._wait()
            try:
                r = self.s.get(url, timeout=self.timeout, allow_redirects=True)
                if 500 <= r.status_code < 600:
                    raise RuntimeError(f"server error {r.status_code}")
                return r
            except (requests.RequestException, RuntimeError) as e:
                if attempt == 2:
                    raise
                backoff = 2 ** (attempt + 1)
                log.warning("GET %s failed (%s); retry in %ds", url, e, backoff)
                time.sleep(backoff)
        raise AssertionError("unreachable")

    def download(self, url: str, dest: Path) -> int:
        self._wait()
        with self.s.get(url, timeout=self.timeout, stream=True) as r:
            r.raise_for_status()
            dest.parent.mkdir(parents=True, exist_ok=True)
            with dest.open("wb") as f:
                for chunk in r.iter_content(chunk_size=64 * 1024):
                    f.write(chunk)
            return dest.stat().st_size


def fetch_sitemap(client: FauClient) -> list[str]:
    r = client.get(SITEMAP_URL)
    r.raise_for_status()
    return re.findall(r"<loc>([^<]+)</loc>", r.text)


# ────────── slug helpers ───────────────────────────────────────────────────


_UMLAUT_FOLD = str.maketrans({"ä": "ae", "ö": "oe", "ü": "ue", "Ä": "Ae", "Ö": "Oe", "Ü": "Ue", "ß": "ss"})


def slugify(name: str, max_len: int = 100) -> str:
    s = re.sub(r"<[^>]+>", "", name)
    s = s.translate(_UMLAUT_FOLD)
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if c.isascii())
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s[:max_len].rstrip("-") or "unnamed"


# ────────── studiengang extractor ──────────────────────────────────────────


def parse_studiengang(url: str, html: str) -> dict:
    """Extract the parts of a /studiengang/{slug}/ page worth keeping.

    The relevant content sits inside <main>; we drop common chrome (nav,
    breadcrumbs, footer, search, language menu) before converting to
    markdown so the corpus stays clean. The Steckbrief ``<dl>`` is also
    extracted *and removed* so it doesn't render twice.
    """
    soup = BeautifulSoup(html, "lxml")
    title_el = soup.find("h1")
    # Use a separator: FAU pages render the degree on a separate line ("Healthcare<br>(M.Sc.)").
    title = (
        re.sub(r"\s+", " ", title_el.get_text(" ", strip=True)).strip()
        if title_el
        else url.rstrip("/").rsplit("/", 1)[-1]
    )

    # Steckbrief: definition lists with degree / language / faculty / etc.
    steckbrief: list[tuple[str, str]] = []
    steckbrief_dl: Tag | None = None
    for dl in soup.find_all("dl"):
        items = []
        for dt, dd in zip(dl.find_all("dt"), dl.find_all("dd")):
            k = dt.get_text(" ", strip=True)
            v = dd.get_text(" ", strip=True)
            if k and v and len(v) < 250:
                items.append((k, v))
        if 3 <= len(items) <= 20:  # the real Steckbrief; skip the "275 Studiengänge" decoration
            steckbrief = items
            steckbrief_dl = dl
            break

    # Main content area
    main = soup.find("main") or soup
    if isinstance(main, Tag):
        # Drop chrome / search / decorative blocks.
        for sel in [
            "nav", "form", "footer", "header", "[role='search']",
            ".search-form", ".breadcrumb", ".breadcrumbs", ".sidebar",
            ".swiper", ".image-slider", ".language-menu",
        ]:
            for x in main.select(sel):
                x.decompose()
        # Drop the Steckbrief dl so it isn't rendered twice in section bodies.
        if steckbrief_dl is not None:
            steckbrief_dl.decompose()

    # Section headings + content
    sections: list[tuple[str, str]] = []
    skip_headings = {
        "Website-Menü", "Services", "Struktur", "Steckbrief",
        "Bei FAU.fyi suchen", "Suchen",
    }
    if isinstance(main, Tag):
        for h2 in main.find_all("h2"):
            label = h2.get_text(" ", strip=True)
            if not label or label in skip_headings:
                continue
            chunk_html = ""
            for sib in h2.next_siblings:
                if isinstance(sib, Tag) and sib.name in {"h2"}:
                    break
                if isinstance(sib, Tag):
                    chunk_html += str(sib)
            chunk_md = _clean_md(html_to_md(chunk_html, heading_style="ATX", strip=["script", "style"]))
            if chunk_md.strip():
                sections.append((label, chunk_md))

    # External links worth preserving — anything outside fau.de or to specific fau-subdomain study pages
    links = []
    if isinstance(main, Tag):
        for a in main.find_all("a", href=True):
            href = a["href"]
            if not href.startswith("http"):
                continue
            text = a.get_text(" ", strip=True)
            if not text or text == href:
                continue
            host_match = re.match(r"https?://([^/]+)", href)
            if not host_match:
                continue
            host = host_match.group(1)
            # Drop generic site-chrome links
            if host in {"www.fau.de", "fau.de"} and re.search(r"/(impressum|datenschutz|cookie|barrierefreiheit|sitemap|kontakt)/", href):
                continue
            if host in {"www.facebook.com", "x.com", "twitter.com", "instagram.com", "youtube.com", "linkedin.com"}:
                continue
            links.append((text, href))
    # dedupe preserving order
    seen: set[str] = set()
    unique_links: list[tuple[str, str]] = []
    for t, h in links:
        if h in seen:
            continue
        seen.add(h)
        unique_links.append((t, h))

    return {
        "url": url,
        "title": title,
        "steckbrief": steckbrief,
        "sections": sections,
        "links": unique_links,
    }


def _clean_md(md: str) -> str:
    """Tighten markdownify output — collapse runs of blank lines, trim each line."""
    md = re.sub(r"\n[ \t]+\n", "\n\n", md)
    md = re.sub(r"\n{3,}", "\n\n", md)
    return md.strip() + "\n"


def render_studiengang_md(data: dict) -> str:
    fm: list[str] = ["---", f'title: "{data["title"]}"', f'source_url: {data["url"]}']
    for k, v in data["steckbrief"]:
        # YAML-safe key
        key = re.sub(r"\W+", "_", k.lower()).strip("_")
        if key and v:
            fm.append(f'{key}: "{v.replace("\"", "''")}"')
    fm.append(f"scraped_at: {_dt.datetime.now(_dt.timezone.utc).isoformat(timespec='seconds')}")
    fm.append("---\n")

    body: list[str] = ["\n".join(fm)]
    body.append(f"# {data['title']}\n")
    body.append(f"**Source:** <{data['url']}>\n")
    if data["steckbrief"]:
        body.append("## Steckbrief\n")
        body.append("| Feld | Wert |")
        body.append("|---|---|")
        for k, v in data["steckbrief"]:
            body.append(f"| {k} | {v.replace('|', '\\|')} |")
        body.append("")
    for label, md in data["sections"]:
        body.append(f"## {label}\n")
        body.append(md.strip())
        body.append("")
    if data["links"]:
        body.append("## Externe Links\n")
        for t, h in data["links"]:
            body.append(f"- [{t}]({h})")
        body.append("")
    return "\n".join(body)


# ────────── pruefungsordnung extractor ─────────────────────────────────────


def parse_po_landing(url: str, html: str) -> dict:
    """Pull intro text + every PDF link from a PO landing page."""
    soup = BeautifulSoup(html, "lxml")
    title_el = soup.find("h1")
    title = (
        re.sub(r"\s+", " ", title_el.get_text(" ", strip=True)).strip()
        if title_el
        else url.rstrip("/").rsplit("/", 1)[-1]
    )

    main = soup.find("main") or soup
    if isinstance(main, Tag):
        for sel in ["nav", "form", "footer", "header", ".breadcrumb", ".sidebar"]:
            for x in main.select(sel):
                x.decompose()

    body_md = ""
    if isinstance(main, Tag):
        body_md = _clean_md(html_to_md(str(main), heading_style="ATX", strip=["script", "style"]))

    # PDFs
    pdfs: list[dict] = []
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if not href.lower().endswith(".pdf"):
            continue
        if not href.startswith("http"):
            continue
        text = a.get_text(" ", strip=True) or href.rsplit("/", 1)[-1]
        pdfs.append({"url": href, "title": text})

    return {"url": url, "title": title, "intro_md": body_md, "pdfs": pdfs}


# ────────── orchestrator ───────────────────────────────────────────────────


def relpath_for_po(url: str) -> Path:
    """Filesystem path under ``data/pruefungsordnungen/`` for a landing URL.

    The ``…/pruefungsordnungen/`` root maps to ``Path('.')`` so its content
    becomes the corpus' top-level ``INDEX.md`` (we overwrite the
    auto-generated one with the actual page content + a children list).
    """
    m = re.search(r"pruefungsordnungen/(.+?)/?$", url)
    return Path(m.group(1)) if m and m.group(1) else Path(".")


def render_studiengang_index(programs: list[dict], out_dir: Path) -> None:
    lines = [
        "---",
        'kind: "fau-studiengang-index"',
        f'count: {len(programs)}',
        "---\n",
        "# FAU Studiengang-Übersicht\n",
        f"Quelle: <https://www.fau.de/studium/studienangebot/alle-studiengaenge/>\n",
        f"## Programme ({len(programs)})\n",
    ]
    for p in sorted(programs, key=lambda x: x["title"].lower()):
        slug = slugify(p["url"].rstrip("/").rsplit("/", 1)[-1])
        deg = next((v for k, v in p["steckbrief"] if k.lower() == "abschluss"), "")
        lines.append(f"- [{p['title']}]({slug}.md){' — ' + deg if deg else ''}")
    lines.append("")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "INDEX.md").write_text("\n".join(lines), encoding="utf-8")


def render_po_landing(data: dict, dest: Path, pdf_targets: list[tuple[dict, Path]]) -> None:
    lines = [
        "---",
        'kind: "fau-pruefungsordnung-landing"',
        f'title: "{data["title"]}"',
        f'source_url: {data["url"]}',
        f"scraped_at: {_dt.datetime.now(_dt.timezone.utc).isoformat(timespec='seconds')}",
        "---\n",
        f"# {data['title']}\n",
        f"**Source:** <{data['url']}>\n",
    ]
    if data["intro_md"]:
        lines.append("## Inhalt der Landing-Seite\n")
        lines.append(data["intro_md"])
    if pdf_targets:
        lines.append(f"## Prüfungsordnungen-Dokumente ({len(pdf_targets)})\n")
        for pdf, target in pdf_targets:
            lines.append(f"- [{pdf['title']}]({target.name}) — Quelle: <{pdf['url']}>")
    dest.mkdir(parents=True, exist_ok=True)
    (dest / "INDEX.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def render_pdf_md(pdf_meta: dict, pdf_path: Path, parent_landing_url: str, dest: Path) -> None:
    """Convert a downloaded PDF to markdown via pymupdf4llm and write it."""
    import pymupdf4llm

    body = pymupdf4llm.to_markdown(str(pdf_path), show_progress=False)
    fm = [
        "---",
        'kind: "fau-pruefungsordnung-document"',
        f'title: "{pdf_meta["title"]}"',
        f'pdf_source: {pdf_meta["url"]}',
        f"parent_landing: {parent_landing_url}",
        f"scraped_at: {_dt.datetime.now(_dt.timezone.utc).isoformat(timespec='seconds')}",
        f'page_count_chars: {len(body)}',
        "---\n",
        f"# {pdf_meta['title']}\n",
        f"**PDF source:** <{pdf_meta['url']}>",
        f"**Landing page:** <{parent_landing_url}>\n",
        body,
    ]
    dest.write_text("\n".join(fm) + "\n", encoding="utf-8")


def render_po_root_index(
    landings: list[tuple[dict, Path]],
    po_root: Path,
    root_landing: Optional[dict] = None,
) -> None:
    """Top-level ``data/pruefungsordnungen/INDEX.md``.

    If the PO root URL itself is in our landings (and so already wrote its
    own ``INDEX.md`` at this path), we append the auto-generated children
    list to it. Otherwise we generate a fresh index from the children alone.
    """
    children_lines = [
        "",
        f"## Landing-Seiten ({len([r for _, r in landings if str(r) != '.'])})",
        "",
    ]
    for data, rel in sorted(landings, key=lambda t: str(t[1])):
        if str(rel) == ".":
            continue
        children_lines.append(f"- [{data['title']}]({rel}/INDEX.md) — `{rel}`")

    po_root.mkdir(parents=True, exist_ok=True)
    target = po_root / "INDEX.md"
    if root_landing is not None and target.exists():
        # Append the children list to the existing root-landing INDEX.md.
        existing = target.read_text(encoding="utf-8")
        if "## Landing-Seiten" not in existing:
            target.write_text(existing.rstrip() + "\n" + "\n".join(children_lines) + "\n", encoding="utf-8")
    else:
        head = [
            "---",
            'kind: "fau-pruefungsordnung-root"',
            f"count: {len(landings)}",
            "---",
            "",
            "# Prüfungsordnungen — Übersicht",
            "",
            "Quelle: <https://www.fau.de/universitaet/universitaetsorganisation/rechtliche-grundlagen/pruefungsordnungen/>",
        ]
        target.write_text("\n".join(head + children_lines) + "\n", encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--out", type=Path, default=Path("data"), help="output root for markdown")
    p.add_argument("--tmp", type=Path, default=Path("tmp/fau"), help="temp dir for PDFs")
    p.add_argument("--interval", type=float, default=1.0, help="min seconds between requests")
    p.add_argument("--max-studiengang", type=int, default=None, help="limit studiengang count (testing)")
    p.add_argument("--max-po", type=int, default=None, help="limit PO landings (testing)")
    p.add_argument("--max-pdfs-per-po", type=int, default=None, help="limit PDFs per PO landing (testing)")
    p.add_argument("--skip-pdfs", action="store_true", help="render PO landings but don't download PDFs")
    p.add_argument("-v", "--verbose", action="count", default=0)
    args = p.parse_args(argv)

    level = logging.WARNING - 10 * args.verbose
    logging.basicConfig(level=max(level, logging.DEBUG), format="%(levelname)s %(name)s: %(message)s")

    client = FauClient(min_interval=args.interval)
    log.info("fetching sitemap …")
    urls = fetch_sitemap(client)
    sg_urls = sorted({u for u in urls if re.fullmatch(r"https://www\.fau\.de/studiengang/[^/]+/?", u)})
    po_urls = sorted({u for u in urls if "/pruefungsordnungen/" in u and u.startswith("https://www.fau.de/")})
    log.info("sitemap: %d studiengang URLs, %d pruefungsordnungen URLs", len(sg_urls), len(po_urls))

    if args.max_studiengang:
        sg_urls = sg_urls[: args.max_studiengang]
    if args.max_po:
        po_urls = po_urls[: args.max_po]

    # ── Studiengang ────────────────────────────────────────────────────
    sg_out = args.out / "studiengang"
    sg_out.mkdir(parents=True, exist_ok=True)
    sg_data: list[dict] = []
    for i, url in enumerate(sg_urls, 1):
        slug = slugify(url.rstrip("/").rsplit("/", 1)[-1])
        try:
            r = client.get(url)
            r.raise_for_status()
            d = parse_studiengang(url, r.text)
            (sg_out / f"{slug}.md").write_text(render_studiengang_md(d), encoding="utf-8")
            sg_data.append(d)
        except Exception as e:  # noqa: BLE001
            log.warning("studiengang %s failed: %s", url, e)
        if i % 25 == 0 or i == len(sg_urls):
            log.info("studiengang progress: %d/%d", i, len(sg_urls))
    render_studiengang_index(sg_data, sg_out)

    # ── Prüfungsordnungen ──────────────────────────────────────────────
    po_root = args.out / "pruefungsordnungen"
    po_root.mkdir(parents=True, exist_ok=True)
    landings: list[tuple[dict, Path]] = []
    pdf_total = 0
    for i, url in enumerate(po_urls, 1):
        rel = relpath_for_po(url)
        dest = po_root / rel
        try:
            r = client.get(url)
            r.raise_for_status()
            d = parse_po_landing(url, r.text)
        except Exception as e:  # noqa: BLE001
            log.warning("PO landing %s failed: %s", url, e)
            continue

        pdf_targets: list[tuple[dict, Path]] = []
        pdfs = d["pdfs"]
        if args.max_pdfs_per_po:
            pdfs = pdfs[: args.max_pdfs_per_po]
        dest.mkdir(parents=True, exist_ok=True)  # parent dir for both INDEX.md and per-PDF .md
        for pdf in pdfs:
            pdf_slug = slugify(pdf["url"].rstrip("/").rsplit("/", 1)[-1].removesuffix(".pdf"))
            pdf_target = dest / f"{pdf_slug}.md"
            pdf_targets.append((pdf, pdf_target))
            if args.skip_pdfs:
                continue
            tmp_pdf = args.tmp / pdf_slug / "doc.pdf"
            try:
                client.download(pdf["url"], tmp_pdf)
                render_pdf_md(pdf, tmp_pdf, url, pdf_target)
                pdf_total += 1
            except Exception as e:  # noqa: BLE001
                log.warning("PDF %s failed: %s", pdf["url"], e)
        render_po_landing(d, dest, pdf_targets)
        landings.append((d, rel))
        if i % 5 == 0 or i == len(po_urls):
            log.info("PO progress: %d/%d landings, %d PDFs converted so far", i, len(po_urls), pdf_total)
    root_landing = next((d for d, rel in landings if str(rel) == "."), None)
    render_po_root_index(landings, po_root, root_landing=root_landing)

    print(
        f"done: studiengang={len(sg_data)}, po_landings={len(landings)}, pdfs_converted={pdf_total}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
