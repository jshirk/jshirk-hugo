# The Useful Life redesign: plan and status

The approved design is in `docs/redesign/mockups.html`. Open it in a browser and use the tabs:
**Combined homepage** and **Article page** are the approved direction. A, B and C are earlier
options, kept for reference only. The **Baseline & plan** tab is the source of the plan below.

Rules: follow `CLAUDE.md`. One plan PR per pull request, on its own branch. Never merge, never push
to `main`. Jordan reviews each Netlify deploy preview and merges.

## Status

| Plan PR | What | Status |
|---|---|---|
| 1 | Repo hygiene, README, CLAUDE.md | Merged (GitHub #1) |
| 2 | CI: build and internal link check | Merged (#2) |
| 3 | Theme edits moved out of `themes/PaperMod` | Merged (#3) |
| 4 | WordPress redirects (`static/_redirects`) | Merged (#4) |
| 5 | Self-hosted Playfair, small logo, phone header | Merged (#5) |
| — | `netlify.toml`: pinned Hugo, minify, real previews | Merged (#7) |
| 6 | Metadata, robots.txt, Person schema, descriptions | Merged (#8) |
| 7 | Social preview cards | Merged (#9) |
| 8 | Hide dates and word counts, `showLastUpdated` | Merged (#6) |
| 9 | One newsletter component | Merged (#10) |
| 10–18 | See below | **To do, in order** |

## Decisions already made (do not reopen)

- Homepage: the **combined** direction: The Library's calm layout and hero, the Field Guide's
  collections as "How can I help?" cut to five needs (Habits, Focus, Faith, Money, Tech) with small
  animated inline-SVG icons, verbatim pull quotes from Jordan's posts, his photo in the About block.
- Fonts: Playfair Display SC (self-hosted, already in `static/fonts/`) for headings; system sans for body.
- Crawlers: allow all, including AI search and training crawlers.
- Tags: keep every tag URL; noindex the ~322 thin ones (one post or none) and drop them from the sitemap.
- Newsletter: Kit form 7752752 only (form 7753019 is retired; it had no automations).

## Remaining PRs

### 10. Design system: palette, type, light and dark
- Warm paper, charcoal ink, moss accent as CSS custom properties for both themes. Values are the
  `.site` tokens in `mockups.html` (light: paper `#F7F3EB`, paper-2 `#EEE8DC`, ink `#25231F`,
  ink-2 `#5C574D`, rule `#DAD2C3`, accent `#4A5D3B`; dark: paper `#1B1A17`, paper-2 `#23221E`,
  ink `#ECE6DA`, ink-2 `#ABA497`, rule `#38352F`, accent `#B2C49B`).
- Type scale: Playfair headings, system-sans body, article measure ~68 characters at 18 px.
  Consistent buttons and focus states. The new header from the mockup (mark + "The Useful Life",
  jump links, search and theme buttons; no Menu button; all site links in the footer).
- Files: `assets/css/extended/tokens.css`, `typography.css`, `components.css`, `layouts/partials/header.html`.
  PaperMod uses `body.dark` for dark mode; map the tokens onto its variables (`--theme`, `--entry`,
  `--primary`, `--secondary`, `--tertiary`, `--content`, `--border`).
- Verify: every text pair ≥ 4.5:1, Lighthouse accessibility 100, screenshots of ~10 representative
  pages in both themes at 390 and 1280 px.

### 11. The new homepage
- Build the combined homepage from `data/home.yaml` (positioning, favorites) and
  `data/collections.yaml` (the five collections, each with a pull quote and its article slugs; the
  mockup lists the articles). Recent posts from the blog section in date order, no dates shown.
  No JavaScript except the tiny icon/theme interactions; respect `prefers-reduced-motion`.
- Files: `layouts/index.html`, `layouts/partials/home/*.html`, `data/*.yaml`, `content/_index.md`.
- The template must fail the build if a slug in the data files doesn't resolve.
- Verify: mobile Lighthouse on the homepage ≥ 95, visual review against the mockup.

### 12. Start Here, archive, topic collections, category pages
- `/start-here/` from the About page's "Where to start" list. `/archive/` grouped under year headings,
  no per-post dates. `/topics/<name>/` from the collections data. Category pages get an intro and
  each article's description. Nav: Start here, Topics, Articles, Tools, About, Search.
- New URLs only; existing ones unchanged. Verify: link checker passes, every collection slug resolves.

### 13. Related articles
- Hugo `related:` config weighted by collection, then category, then tags; three articles under each
  post plus "Part of: <collection>". Build time only. Verify by reviewing ~20 posts across eras.

### 14. Search: smaller index
- Index title, description, category and a ~40-word summary instead of full content (1.7 MB → ~150 KB).
  Weight titles; show description and reading time in results (no dates).
- Files: `layouts/_default/index.json`, `config.yaml` (`fuseOpts`), `layouts/_default/search.html`.
- Verify: mobile Lighthouse on /search/ goes from ~80 to ≥ 95; 15 known queries return the expected
  article in the top three.

### 15. Images, alt text, thin tag pages
- Markdown render hook adds width, height, `loading="lazy"`, `decoding="async"`. Recompress the 24
  originals over 500 KB under the same filenames. Draft alt text for the ~288 `alt="Image"` images
  into a CSV for Jordan to approve (do not apply unapproved). Thin tag pages: `noindex`, out of the sitemap.
- Verify: no layout shift on image-heavy posts, images look identical.

### 16. Tools page and content inventory
- Tools page sections (Money, Bible study, Writing, Security, Everyday) from `data/tools.yaml`, with an
  affiliate disclosure. `docs/content-inventory.csv` marking each post evergreen, dated, or
  retire-candidate (advice only; no post is rewritten).

### 17. AI search discovery
- `robots.txt` already allows all. Add an optional generated `/llms.txt` built from the data files.

### 18. CI: metadata and performance checks
- Add `scripts/check_meta.py` to CI, block changes to existing `date` values, and run Lighthouse CI
  on five pages (mobile performance ≥ 95, accessibility ≥ 98, homepage < 150 KB).

## How verification has been done (reuse this)

- Build: `hugo --gc --minify` with Hugo extended **0.143.1** (pinned in `netlify.toml` and CI).
- Checks in `scripts/`: `check_links.py public`, `check_meta.py public`,
  `check_redirects.py <preview-url>`.
- Every PR gets a Netlify deploy preview (`https://deploy-preview-<N>--jshirk.netlify.app`), built
  with its own base URL, so it shows CSS/font/image changes directly. Verify on the preview, not only locally.
- Visual changes: Playwright screenshots at 390 and 1280 px in light and dark; check no horizontal
  scroll; Lighthouse (mobile) before/after.
- Newsletter tests must not create real subscribers: intercept requests to
  `app.kit.com/forms/*/subscriptions` and answer them locally.
- Write each PR description with: what changed, why, how it was verified, and whether the change is visible.
