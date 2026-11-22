#!/usr/bin/env python3
"""Check internal links and image references in a built Hugo site.

Usage: python3 scripts/check_links.py public

Every href/src that points inside the site (relative, root-relative, or
https://jshirk.com/...) must resolve to a file in the build output.
Targets listed in scripts/known_broken.txt are reported but do not fail.
"""
import os
import re
import sys
import urllib.parse as up

BASE = "https://jshirk.com"
ATTR = re.compile(r'\b(href|src)=("[^"]*"|\'[^\']*\'|[^\s>]+)')


def load_known(path):
    if not os.path.exists(path):
        return set()
    with open(path, encoding="utf-8") as f:
        return {l.strip() for l in f if l.strip() and not l.startswith("#")}


def resolves(root, path):
    fp = os.path.join(root, path.lstrip("/"))
    return os.path.isfile(fp) or os.path.isfile(os.path.join(fp, "index.html"))


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else "public"
    known = load_known(os.path.join(os.path.dirname(__file__), "known_broken.txt"))
    broken = {}
    for dirpath, _, files in os.walk(root):
        for name in files:
            if not name.endswith(".html"):
                continue
            page_path = os.path.join(dirpath, name)
            page = "/" + os.path.relpath(page_path, root).replace("index.html", "")
            with open(page_path, encoding="utf-8", errors="ignore") as f:
                html = f.read()
            for _, raw in ATTR.findall(html):
                url = raw.strip("\"'").replace("&amp;", "&")
                if url.startswith(BASE):
                    url = url[len(BASE):] or "/"
                if not url.startswith("/") or url.startswith("//"):
                    continue
                path = up.unquote(url.split("#")[0].split("?")[0])
                if path and not resolves(root, path):
                    broken.setdefault(path, set()).add(page)

    new = {k: v for k, v in broken.items() if k not in known}
    fixed = sorted(known - set(broken))
    print(f"Internal link check: {len(broken)} broken targets "
          f"({len(broken) - len(new)} known, {len(new)} new).")
    if fixed:
        print("These known-broken targets now resolve; remove them from known_broken.txt:")
        for k in fixed:
            print(f"  {k}")
    if new:
        print("New broken links:")
        for k, pages in sorted(new.items()):
            print(f"  {k}  (linked from {len(pages)} page(s), e.g. {sorted(pages)[0]})")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
