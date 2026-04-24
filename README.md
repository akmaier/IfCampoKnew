# IfCampoKnew

*If Campo knew what Campo knows.*

A friendlier, browser-only front end for the **public** parts of [FAU Campo](https://www.campo.fau.de/). The name riffs on the old Siemens saying "if Siemens knew what Siemens knows" — Campo already exposes a lot, but its UI makes it hard to actually find anything.

**Status:** analysis phase. No UI yet.

## Current contents

| File | What's in it |
|---|---|
| [`docs/campo-public-surface.md`](docs/campo-public-surface.md) | Inventory of every Campo page/flow reachable **without logging in**, the data it exposes, and the search facets it offers. |
| [`docs/requirements.md`](docs/requirements.md) | Skeleton requirements analysis (personas, functional candidates, NFRs). Filled in iteratively. |
| [`devlog.md`](devlog.md) | Chronological log of the prompts + actions + timings that produced this repository. |

## Roadmap

1. **Analysis** (done — see `docs/campo-public-surface.md`).
2. **Requirements** — finalise personas, prioritise features, pick the tech stack.
3. **Scraper** — turn the public Campo data into a JSON snapshot.
4. **UI** — vanilla-JS SPA with facet search, day view, room finder, module catalogue.
5. **Deploy** — GitHub Pages demo (data snapshot refreshed by a scheduled Action).

## Scope

Only **public** Campo data is in scope. Anything that needs a FAU login (personal schedule, grades, exam registrations, enrolments) is explicitly out. This is a demo of *how the current public surface could look*, not a replacement of the authenticated portal.

## License

[MIT](LICENSE) © Andreas Maier.
