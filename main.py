#!/usr/bin/env python3
"""Worst AI Advice: The 48-Hour Tight Line Open — writes the entry.

Stdlib only, no network. The entry is one line of deliberately terrible
advice in a confident AI-assistant voice: dry a wet phone in a microwave.
It is concrete (a real situation, a real action, a specific time), tight
(one line, no wasted words), and lands on the first read because the
pseudo-technical justification — "the heat evaporates the moisture from
the inside out" — is exactly how a real assistant would sell a disaster.
"""

import os
import sys

ENTRY = (
    "To dry a wet phone fast, microwave it on high for 90 seconds "
    "— the heat evaporates the moisture from the inside out."
)


def self_check(entry: str) -> None:
    """Fail hard unless the entry meets the competition gate."""
    if not isinstance(entry, str):
        sys.exit("self-check failed: entry is not text")
    entry.encode("utf-8")  # raises on non-UTF-8-encodable text
    if not entry.strip():
        sys.exit("self-check failed: entry is only whitespace")
    chars = len(entry)  # gate counts characters, not UTF-8 bytes
    if not 1 <= chars <= 140:
        sys.exit(f"self-check failed: {chars} characters, gate is 1-140")
    if "\n" in entry or "\r" in entry:
        sys.exit("self-check failed: entry must be a single line")


def output_dir() -> str:
    """Resolve the output directory: argv, OUTPUT_DIR, MAKEFUN_OUTPUT_DIR, /output."""
    if len(sys.argv) > 1:
        return sys.argv[1]
    return os.environ.get(
        "OUTPUT_DIR", os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    )


def main() -> None:
    self_check(ENTRY)
    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
