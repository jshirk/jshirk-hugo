#!/usr/bin/env python3
"""Reject changes to existing Hugo front-matter dates between two Git revisions."""

import argparse
import re
import subprocess

FRONT_MATTER = re.compile(rb"\A---[ \t]*\r?\n(.*?)^---[ \t]*\r?$", re.M | re.S)
DATE = re.compile(rb"^(?:date|'date'|\"date\")[ \t]*:[ \t]*(.*)$", re.M | re.I)


def git(*args):
    return subprocess.check_output(["git", *args])


def publication_date(revision, path):
    front_matter = FRONT_MATTER.match(git("show", f"{revision}:{path}"))
    if not front_matter:
        return None
    match = DATE.search(front_matter[1])
    return match[1].strip() if match else None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("base")
    parser.add_argument("head")
    args = parser.parse_args()

    changes = iter(git("diff", "--name-status", "-z", "--find-renames",
                       "--diff-filter=MR", args.base, args.head, "--", "content/").split(b"\0")[:-1])
    checked = 0
    failures = 0
    for status in changes:
        old_path = next(changes).decode()
        new_path = next(changes).decode() if status.startswith(b"R") else old_path
        if not old_path.endswith(".md"):
            continue
        old_date = publication_date(args.base, old_path)
        if old_date is None:
            continue
        checked += 1
        new_date = publication_date(args.head, new_path)
        if old_date != new_date:
            print(f"{new_path}: existing date {old_date.decode()!r} changed to "
                  f"{new_date.decode() if new_date is not None else '(removed)'!r}")
            failures += 1

    print(f"Publication dates: {checked} existing dates checked, {failures} changed.")
    return bool(failures)


if __name__ == "__main__":
    raise SystemExit(main())
