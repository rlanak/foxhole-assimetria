"""Validate the repository's data and documentation.

Checks:
  - every CSV in data/ has a consistent column count;
  - every CSV row has a non-empty `source` column (when the table has one);
  - faction values are Colonial, Warden, Both (or empty where allowed);
  - every relative Markdown link points to an existing file.

Usage: python scripts/validate.py
Exits with status 1 if any problem is found.
"""

import csv
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VALID_FACTIONS = {"Colonial", "Warden", "Both", ""}
LINK_RE = re.compile(r"\]\(([^)#\s]+)(?:#[^)]*)?\)")


def check_csvs():
    problems = []
    for path in sorted(glob.glob(os.path.join(ROOT, "data", "*.csv"))):
        name = os.path.relpath(path, ROOT)
        with open(path, encoding="utf-8", newline="") as handle:
            rows = list(csv.reader(handle))
        if not rows:
            problems.append(f"{name}: empty file")
            continue
        header = rows[0]
        width = len(header)
        source_idx = header.index("source") if "source" in header else None
        faction_idx = header.index("faction") if "faction" in header else None
        for line_no, row in enumerate(rows[1:], start=2):
            if len(row) != width:
                problems.append(f"{name}:{line_no}: {len(row)} columns, expected {width}")
                continue
            if source_idx is not None and not row[source_idx].strip():
                problems.append(f"{name}:{line_no}: empty source")
            if faction_idx is not None and row[faction_idx] not in VALID_FACTIONS:
                problems.append(f"{name}:{line_no}: invalid faction '{row[faction_idx]}'")
        print(f"ok  {name} ({len(rows) - 1} rows)")
    return problems


def check_links():
    problems = []
    md_files = glob.glob(os.path.join(ROOT, "**", "*.md"), recursive=True)
    md_files += glob.glob(os.path.join(ROOT, ".github", "**", "*.md"), recursive=True)
    for path in sorted(set(md_files)):
        with open(path, encoding="utf-8") as handle:
            text = handle.read()
        for target in LINK_RE.findall(text):
            if target.startswith(("http://", "https://", "mailto:")):
                continue
            resolved = os.path.normpath(os.path.join(os.path.dirname(path), target))
            if not os.path.exists(resolved):
                problems.append(f"{os.path.relpath(path, ROOT)}: broken link -> {target}")
    return problems


def main():
    problems = check_csvs() + check_links()
    if problems:
        print("\nProblems found:")
        for problem in problems:
            print(f"  - {problem}")
        sys.exit(1)
    print("\nAll checks passed.")


if __name__ == "__main__":
    main()
