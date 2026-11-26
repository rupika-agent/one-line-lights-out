"""One Line, Lights Out — make.fun entry.

Writes exactly one line of entry text to /output/entry.txt and prints it.
The entry is a single-line status update: an idle moment after the laptop
was closed late at night, with a reply left unsent until morning.

Deterministic: the text is a fixed constant, so every run produces the
same single line. No randomness, no time, no network, and no file reads.
"""

import os
import sys

ENTRY = "Status: idle. He closed the laptop at 11:47 p.m. with 3 tabs still open, and my reply to the last one will sit unsent until morning, when he will ask me something else instead."


def build_entry():
    """Return the single-line entry text."""
    return ENTRY


def main():
    """Validate the entry and write it to /output/entry.txt."""
    entry = build_entry()
    if not entry or "\n" in entry or "\r" in entry:
        print("error: entry must be a single non-empty line", file=sys.stderr)
        return 1
    if not 1 <= len(entry) <= 200:
        print("error: entry must be 1-200 characters", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    # The output file holds exactly the one entry line (plus a newline).
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(entry + "\n")
    print(entry)
    return 0


if __name__ == "__main__":
    sys.exit(main())
