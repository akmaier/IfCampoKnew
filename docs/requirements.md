# IfCampoKnew — Requirements Analysis

> **Status: v2 locked (2026-04-25).** Major pivot in Entry 0006 of [`devlog.md`](../devlog.md): the product is now an **AI-readable markdown corpus**, no longer a Web Components UI. Decisions from v1 (license, scrape cadence, scraper language) carry over; UI/embed/telemetry decisions are obsolete and called out below.

---

## 1. Vision

A self-contained, hierarchically organised **markdown corpus** that mirrors FAU's Campo portal structure. Designed for consumption by LLM-based agents: a user asks an agent a question; the agent navigates the corpus' `INDEX.md` files, reads 1–3 content files, and answers grounded in the data. GitHub renders the corpus natively, so the repo itself is the secondary "viewer".

The original framing — *"if Siemens knew what Siemens knows"* — still holds: Campo already exposes everything we need, but the JSF UI hides it. We extract it into a form an LLM can actually search.

## 2. Consumers (revised personas)

The four human personas (P1–P4 from v1) are now reached *through* an agent. The corpus' direct consumers are:

| # | Consumer | Job-to-be-done | Implications |
|---|----------|----------------|--------------|
| **C1** | **LLM agent** (ChatGPT, Claude, Gemini, …) | Answer student/lecturer questions by walking `INDEX.md` → child `INDEX.md` → content. | Files must fit individually inside agent context; cross-links must be resolvable. |
| C2 | Power user reading on github.com | Browse the tree as a human-readable reference. | Slugs human-readable, headings descriptive. |
| C3 | Downstream tools (RAG indexers, vector DBs, embeddings) | Ingest the corpus as a folder of plain markdown. | No proprietary front-matter; standard CommonMark. |

The original P1 *Student*, P2 *Lecturer*, P3 *Staff*, P4 *Other* personas remain the *ultimate* audiences; their job-stories are unchanged but mediated by the agent.

## 3. Functional scope (v2 — locked)

- **F-CAT — Catalogue corpus.** Every catalogue node (root, faculty, program, PO-version, sub-section) becomes either a folder + `INDEX.md` (if it has children) or a single `<slug>.md` file (leaf, in the parent folder).
- **F-COURSE — Course corpus.** Every course event in scope is embedded in the most relevant content file with full *Termine* (schedule), *Inhalte* (description), and module memberships. *Phase 2 — not in the first commit.*
- **F-LINKS — Link integrity.** Every Campo permalink the corpus references is the same URL Campo's own "share" popup emits. Where Campo embeds external links (lecturer homepage, FAUdir, study programme home page), they are preserved verbatim in the markdown.
- **F-OVERVIEW — Hierarchical `INDEX.md`.** Every folder has one. It carries name + segment + period + permalink + an alphabetical list of children (display name, sub-folder/file, segment).
- **F-TOKEN — Token-bucket policy.** Content files target **10–30 k tokens**. *Thin* sub-trees (combined content < 10 k tokens) are merged into the parent file rather than emitted as their own folder. *Thick* PO-versions (> 30 k tokens) are split by module group or semester block. `INDEX.md` files stay smaller (≤ 5 k tokens).

## 4. Non-functional requirements (v2)

- **NFR-1 (Hosting)** Pure git repo. No server, no GitHub Pages required. Pages may later serve a tiny landing page that points at the corpus, but that's it.
- **NFR-2 (Freshness)** Weekly scrape via GitHub Actions cron (Mondays 03:00 UTC). Each run commits the regenerated corpus and cuts a GitHub **Release** tagged `snapshot-YYYY-Www`.
- **NFR-3 (Slug stability)** Slugs are deterministic — same display name always produces the same slug — and ASCII-folded (umlauts: `ä→ae` etc.). Every folder/file has the terminal segment ID appended (`…-17601`) so paths survive Campo renaming a node.
- **NFR-4 (Token discipline)** see F-TOKEN.
- **NFR-5 (Language)** Slugs and content stay in **Campo's source language** (German, with whatever inline English Campo emits). No translation pass.
- **NFR-6 (Reproducibility)** Anyone can `python scraper/scrape.py … && python scraper/render_markdown.py …` and reproduce the corpus byte-for-byte (modulo Campo data churn).
- **NFR-7 (No telemetry)** *(Replaces v1's T1+T2.)* Without a website, there is nothing to track and no consent banner to write. Feedback channel = GitHub Issues on this repo.
- **NFR-8 (License)** **MIT** for code (unchanged). Corpus content is FAU's underlying data; the corpus files are derivative and inherit FAU's terms with attribution links back to Campo.
- **NFR-9 — obsolete.** *(Was: Web Components embeddability — gone with the UI.)*
- **NFR-10 (Archival)** Each completed academic year is preserved in `archive/{year-slug}/` as a frozen full corpus snapshot.

## 5. Architecture (v2)

```
┌─────────────────────────┐        ┌───────────────────────────────────────┐
│ scraper/   Python       │ ─────▶ │ tmp/{period}.json   (intermediate;    │
│  campo_client           │        │   gitignored, regenerated each run)   │
│  parse_tree             │        └─────────────┬─────────────────────────┘
│  scrape.py    --period  │                      │
└─────────────────────────┘                      ▼
                                     ┌───────────────────────────────────────┐
                                     │ scraper/render_markdown.py            │
                                     │  JSON  →  data/{period-slug}/ tree    │
                                     └─────────────┬─────────────────────────┘
                                                   ▼
                                     ┌───────────────────────────────────────┐
                                     │ data/{period-slug}/                   │
                                     │   INDEX.md                            │
                                     │   {section-slug-id}/INDEX.md          │
                                     │   {program-slug-id}/INDEX.md          │
                                     │   {po-slug-id}.md   (leaf, content)   │
                                     └───────────────────────────────────────┘
                                                   ▲
                                                   │
                                  consumed by ──── LLM agents (primary)
                                                   github.com renderer (secondary)
                                                   RAG / embeddings (tertiary)
```

### Repository layout

```
IfCampoKnew/
├── scraper/                          # Python tooling
│   ├── campo_client.py               # session + rate limit + retries
│   ├── parse_tree.py                 # catalogue HTML → ParsedNode
│   ├── parse_detail.py               # course-detail HTML → Course (phase 2)
│   ├── render_markdown.py            # JSON snapshot → markdown corpus
│   ├── schema.py                     # CatalogNode / CatalogSnapshot / Course
│   ├── scrape.py                     # CLI: walk tree, write JSON to tmp/
│   ├── requirements.txt
│   └── README.md
├── tmp/                              # gitignored; JSON intermediates live here
├── data/                             # the deliverable
│   └── {period-slug}/
│       ├── INDEX.md
│       ├── {section}/INDEX.md
│       └── …
├── archive/                          # frozen prior-year corpora (NFR-10)
├── docs/
│   ├── campo-public-surface.md
│   └── requirements.md  (this file)
├── .github/workflows/
│   └── scrape-weekly.yml             # phase 2: cron + commit + Release
├── devlog.md
├── README.md
├── LICENSE
└── .gitignore
```

### Data model (intermediate JSON, persisted only in `tmp/`)

```jsonc
{
  "periodId": 589,
  "periodName": "Sommersemester 2026",
  "scrapedAt": "2026-04-25T05:57:38+00:00",
  "rootSegment": "title:17593",
  "maxDepth": 4,
  "nodes": [
    {
      "segment": "title:17593",
      "kind": "title",
      "nodeId": 17593,
      "name": "Vorlesungsverzeichnis Friedrich-Alexander-Universität Erlangen-Nürnberg",
      "path": ["title:17593"],
      "parentSegment": null,
      "children": ["title:17598", "title:17595", …],
      "unitId": null
    }
    // …
  ]
}
```

The renderer reads this and writes the corpus. The JSON file itself is **not committed**.

## 6. Out of scope (v2)

- Web UI of any kind.
- Client-side search index (FlexSearch, etc.).
- Onboarding quiz (the agent personalises).
- Anything requiring a Campo login (grades, registrations, exams).
- Deferred features F4–F9 from v1: still out.

## 7. Decisions log

| Date | Decision | Rationale |
|------|----------|-----------|
| 2026-04-24 | **License: MIT.** | Simple, permissive, FAU-friendly. |
| 2026-04-24 | **Primary persona = P1 Student.** | Carries over: students are still the dominant audience the agent ultimately serves. |
| 2026-04-24 | **Data scope = current + next semester, all faculties.** | Unchanged. |
| 2026-04-24 | **Versioning = `archive/{year-slug}/` per completed academic year.** | Unchanged. |
| 2026-04-24 | **Weekly scrape Mondays 03:00 UTC; GitHub Release per run.** | Unchanged. |
| 2026-04-24 | **Scraper = Python (`requests` + `lxml`).** | Unchanged. |
| 2026-04-25 | **Pivot to markdown corpus.** | Agentic LLM consumption is more powerful than a custom web UI. Drops F1, F2, F3, F10, NFR-9, T1, T2, FlexSearch, Vite, Web Components. |
| 2026-04-25 | **Slug language = German (Campo-faithful).** | Preserves Campo's terminology; no translation drift. |
| 2026-04-25 | **JSON snapshot is intermediate-only (gitignored under `tmp/`).** | Markdown corpus under `data/{period-slug}/` is the deliverable. |
| 2026-04-25 | **Catalogue tree walked to full depth.** `--max-depth 0` = unlimited (hard-cap 12). | "We need to go deeper" — capture full PO-section chains, not just first 4 levels. |
| 2026-04-25 | **Token-bucket policy: content files 10–30 k tok; INDEX ≤ 5 k tok; merge thin / split thick.** | Optimised for 100 k-tok agent contexts holding a few content files at a time. |
| 2026-04-25 | **No analytics, no website.** | NFR-7 reduces to "no telemetry". Feedback via GitHub Issues. |

## 8. Open items

- **O1** — Token-counting library: `tiktoken` (OpenAI-aligned) vs simple character heuristic (`len/4`). Affects when files are merged/split. *Lean: ship character-heuristic in v2; add tiktoken when we have course content to bucket.*
- **O2** — How to discover the courses associated with a leaf catalogue node — is it `searchStudyCourseSchedule-flow`, or a course-search filtered by `Studiengang` + PO-version? Probe in Entry 0007.
- **O3** — Determine `periodId` for WiSe 2026/27 (first weekly scrape will discover via `parse_periods()`).

## 9. Roadmap

**This entry (0006) ships:** F-CAT skeleton (`INDEX.md` + leaf `.md` placeholders) for the depth-4 walk of SoSe 2026.

**Next entry (0007) — phase 2:**
1. Run a deeper walk (`--max-depth 0`) — measure scale, capture every `exam:` sub-section.
2. Resolve **O2** by probing `searchStudyCourseSchedule-flow` with a known PO-version.
3. Implement `parse_detail.py` → `Course` dataclass + markdown rendering of full course detail.
4. Apply the F-TOKEN bucket policy: merge thin / split thick.
5. Wire up `.github/workflows/scrape-weekly.yml` so the weekly run is automated and a Release is cut.
