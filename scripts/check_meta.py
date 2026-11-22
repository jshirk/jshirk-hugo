#!/usr/bin/env python3
"""Check page metadata in a built Hugo site.

Usage: python3 scripts/check_meta.py public

Every HTML page (except alias redirects) must have a non-empty <title>,
meta description, canonical link, and meta author, and every JSON-LD block
must be valid JSON. Prints a summary of structured-data types.
"""
import collections
import json
import os
import re
import sys

TAG = {
    "title": re.compile(r"<title>([^<]*)</title>"),
    "description": re.compile(r'<meta name="?description"? content="([^"]*)"'),
    "canonical": re.compile(r'<link rel="?canonical"? href="?([^" >]+)'),
    "author": re.compile(r'<meta name="?author"? content="([^"]*)"'),
}
LD = re.compile(r'<script type="?application/ld\+json"?>(.*?)</script>', re.S)


def types(node):
    if isinstance(node, dict):
        if "@type" in node:
            yield node["@type"]
        for v in node.values():
            yield from types(v)
    elif isinstance(node, list):
        for v in node:
            yield from types(v)


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else "public"
    problems, pages, seen = [], 0, collections.Counter()
    for dirpath, _, files in os.walk(root):
        for name in files:
            if not name.endswith(".html"):
                continue
            path = os.path.join(dirpath, name)
            html = open(path, encoding="utf-8", errors="ignore").read()
            if 'http-equiv="refresh"' in html or "http-equiv=refresh" in html:
                continue
            pages += 1
            rel = "/" + os.path.relpath(path, root).replace("index.html", "")
            for key, rx in TAG.items():
                m = rx.search(html)
                if not m or not m.group(1).strip():
                    problems.append(f"{rel}: missing {key}")
            for block in LD.findall(html):
                try:
                    data = json.loads(block)
                except ValueError as e:
                    problems.append(f"{rel}: invalid JSON-LD ({e})")
                    continue
                seen.update(t for t in types(data) if t not in ("ListItem",))
    print(f"Metadata check: {pages} pages, {len(problems)} problems.")
    print("Structured data types: " + ", ".join(f"{k} {v}" for k, v in sorted(seen.items())))
    for p in problems[:40]:
        print("  " + p)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
