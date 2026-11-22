# The Useful Life — jshirk.com

Source for [jshirk.com](https://jshirk.com), Jordan Shirkman's publication, built with
[Hugo](https://gohugo.io) and the [PaperMod](https://github.com/adityatelange/hugo-PaperMod) theme
and deployed by Netlify.

## Requirements

- **Hugo extended 0.143.1.** This is the version production builds with. Check with `hugo version`.
  - macOS: `brew install hugo` installs the latest version. To match production exactly, download
    `hugo_extended_0.143.1_darwin-universal.tar.gz` from the
    [Hugo releases page](https://github.com/gohugoio/hugo/releases/tag/v0.143.1).
- Git.

## Everyday commands

Preview the site locally, with drafts, at <http://localhost:1313>:

```bash
hugo server -D
```

Production build into `public/` (the same command CI runs):

```bash
hugo --gc --minify
```

Start a new post:

```bash
hugo new content blog/YYYY-MM-DD-short-slug.md
```

## Writing a post

Front matter used by this site:

```yaml
---
title: "Post title"
author: "Jordan Shirkman"
date: 2026-01-07T00:00:01+00:00   # original publish date — never change it later
slug: /short-slug/                # becomes https://jshirk.com/blog/short-slug/
categories:
  - Methodology                   # one of: Theology, Technology, Methodology
description: "One sentence shown in search results and social previews."
draft: false
---
```

## Deploying

Netlify builds and publishes automatically when `main` changes on GitHub.

1. Work on a branch and open a pull request. Netlify posts a **deploy preview** link on the PR.
2. Check the preview, then merge the PR on GitHub. Netlify publishes the new version within a minute or two.

### Rolling back

- **Instantly:** in Netlify, open **Deploys**, choose the last good deploy, and click **Publish deploy**.
- **Permanently:** open the merged PR on GitHub and click **Revert**, then merge the revert PR.
- The tag `pre-redesign` marks the site as it was before the 2026 redesign.

## Repository layout

| Path | What lives there |
| --- | --- |
| `content/` | Posts (`content/blog/`) and pages (About, Contact, Tools, Search) |
| `layouts/` | Site-specific templates. These override files of the same name in the theme. |
| `assets/css/extended/` | Site-specific CSS, loaded after the theme's CSS |
| `static/` | Files served as-is: images, favicons |
| `themes/PaperMod/` | The theme. **Do not edit files here**; override them in `layouts/` or `assets/` instead. |

See `CLAUDE.md` for the rules that keep URLs, dates, and performance safe.
