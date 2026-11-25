"""One Line, One Laugh — make.fun entry.

Writes a single funny line of text to /output/entry.txt.
Pure standard library; deterministic — the same line every run.
"""

import os

# The joke: one self-contained line, a setup with a turn at the end.
# Tightened: the semicolon carries the pivot, "aloud" replaces "out loud".
LINE = (
    "I asked my smart speaker for relaxing music; "
    "it started reading my unread emails aloud."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    line = LINE.strip()
    if not 1 <= len(line) <= 140:
        raise SystemExit(f"line is {len(line)} chars, must be 1-140")
    if not line.strip():
        raise SystemExit("line must not be only whitespace")
    if "\n" in line or "\r" in line:
        raise SystemExit("line must be a single line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(line)
    print(f"wrote {len(line)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
