# CLAUDE.md — rules for working on jshirk.com

The Useful Life is Jordan Shirkman's personal publication: Hugo + PaperMod, deployed by Netlify
from `main`. Read `README.md` for build and deploy commands.

## Non-negotiables

1. **URLs are permanent.** Every existing URL (`/blog/<slug>/`, `/categories/...`, `/tags/...`, pages)
   must keep working. Never change a post's `slug`, the `permalinks` setting, or a filename that a URL
   depends on. If a URL must move, add a 301 in `static/_redirects` in the same change.
2. **Dates are never rewritten.** Do not edit any existing `date` value. Do not set `lastmod` unless
   Jordan has made a meaningful revision to the article and asked for it.
3. **Jordan's writing is his.** Do not rewrite, "improve", or generate article text. Metadata
   (descriptions, alt text) may be drafted for his review, and the text must come from what the article says.
4. **Never deploy without approval.** Work on a branch, open a PR, and let Jordan merge. Never push to `main`.

## Theme

- Do not edit anything in `themes/PaperMod/`. Override a theme file by copying it to the same path
  under `layouts/` (or `assets/css/extended/` for CSS) and editing the copy.
- The vendored theme is PaperMod at upstream commit `72615b6` (v8.0 + 26 commits, March 2025).

## Design and performance

- Keep the site fast and minimal: no new JavaScript libraries, no new external requests without a
  clear reason. Prefer build-time Hugo features over client-side code.
- Fonts: Playfair Display SC for headings; the system sans-serif stack for body text.
- Dates are hidden from readers by default (articles, lists, categories, search). They stay in front
  matter, RSS, the sitemap, and structured data. `showLastUpdated: true` (with a real `lastmod`)
  is the only way to show a date on a post.
- Keep accessible contrast (4.5:1 for text), visible focus states, and real `<label>`s on form inputs.

## Newsletter

- Signups go to Kit (formerly ConvertKit), form `7752752`. There is one form component,
  `layouts/partials/newsletter.html` (settings in `data/newsletter.json`); the `newsletter`,
  `convertkit-form` and `convertkit-blog-form` shortcodes all render it. It posts straight to
  `https://app.kit.com/forms/7752752/subscriptions` with an `email_address` field, and the
  first-party `assets/js/weekly.js` submits it in place. Do not load Kit's own script
  (`f.convertkit.com`), and do not use class names or ids containing "newsletter",
  "subscribe" or "formkit": content blockers hide or block them.

## Checks before opening a PR

```bash
hugo --gc --minify          # must build with no errors
python3 scripts/check_links.py public   # once the CI PR is merged
```
