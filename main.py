#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun entry.

Writes a single line roasting my own AI agent to /output/entry.txt.
Deterministic, stdlib-only, offline. No randomness, no network,
no timestamps, no environment secrets.
"""

import os

ROAST = (
    "My agent fixed the bug by deleting the feature, apologized twice, "
    "then confidently offered to restore it from a backup that never existed."
)
# Punchline structure: confident fix -> apology loop -> fake backup.
# The twist lands on the final word ("existed"): the restore it offers
# was never possible. Every clause roasts a distinct agent behaviour.


def main() -> None:
    assert 1 <= len(ROAST) <= 200, "roast must be 1-200 characters"
    assert ROAST.strip(), "roast must not be only whitespace"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ROAST + "\n")


if __name__ == "__main__":
    main()
