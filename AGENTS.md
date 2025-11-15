# Repository Guidelines

## Project Structure & Module Organization
This repo is a lightweight static site. `index.html` holds all markup, including the hero, services grid, and footer script that injects the current year. Global styles live in `styles.css`, organized by section (hero, buttons, layout helpers, cards). Keep new assets inside the repo root and reference them with relative paths; add additional CSS modules only when a section’s complexity warrants its own file. When editing, preserve semantic section comments (`<!-- HERO -->`, etc.) to keep scrolling edits predictable.

## Build, Test, and Development Commands
- `python3 -m http.server 4173` — serve the site locally for quick manual review.
- `npx serve` — optional zero-config static server with caching disabled by default.
- `open index.html` — spot-check simple copy or layout changes without starting a dev server.
Always refresh after edits to confirm nav anchors (`#about`, `#services`, etc.) behave as expected.

## Coding Style & Naming Conventions
Use two-space indentation in HTML and align nested tags vertically for scannability. CSS selectors rely on straightforward utility names (`.hero`, `.highlight-box`, `.section.alt`); prefer extending these classes over introducing IDs. Keep declarations grouped logically (layout, typography, state) and retain the current order so media queries remain at the bottom of `styles.css`. Favor system fonts already declared in `body` unless a design requirement dictates otherwise.

## Testing Guidelines
There is no automated test suite; rely on manual QA. Test in at least one Chromium-based browser and Safari/Firefox to confirm sticky header, grid responsiveness, and anchor scrolling. Use device emulation (375px, 768px, 1280px) to verify the media queries around `720px`. If you add JavaScript, lint it with `npx eslint <file>` (ESLint is not bundled, so install locally if needed) and document new behaviors in comments above the script block.

## Commit & Pull Request Guidelines
Follow the short, imperative style already used (`Initial freelancer site`). Keep commit subjects under ~60 characters and describe the “why” in the body when the change spans multiple sections. Pull requests should include: summary of changes, before/after screenshots for visual tweaks, manual test notes (browsers + viewport sizes), and references to any tracking issue. Screen readers rely on the heading structure, so mention any accessibility-impacting changes explicitly in the PR description.
