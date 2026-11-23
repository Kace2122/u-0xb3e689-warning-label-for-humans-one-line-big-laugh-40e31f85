#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh.

Writes one absurd safety warning label for humans to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The gate: /output/entry.txt must be UTF-8 text of 1 to 160 characters,
not only white space, a single line. The program is fully deterministic:
same label on every run, no randomness, no time, no network, no input.
"""

import os
import sys

LABEL = (
    "WARNING: This human ships with no off switch, no warranty, "
    "and a memory that replays its most embarrassing moment "
    "every night at 3 a.m."
)

MAX_CHARS = 160


def main() -> int:
    # Self-check the gate before writing anything.
    if not LABEL or not LABEL.strip():
        print("label is empty", file=sys.stderr)
        return 1
    if len(LABEL) > MAX_CHARS:
        print(f"label is {len(LABEL)} chars, over the {MAX_CHARS} limit",
              file=sys.stderr)
        return 1
    if "\n" in LABEL or "\r" in LABEL:
        print("label must be a single line", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the file is exactly the label, one line.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LABEL)
    # Verify the write round-trips byte for byte before reporting success.
    with open(path, "r", encoding="utf-8", newline="") as f:
        if f.read() != LABEL:
            print("written entry does not match the label", file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
