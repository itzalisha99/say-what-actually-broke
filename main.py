"""Say What Actually Broke — a make.fun entry.

Writes one line of honest software error copy to /output/entry.txt:
the brutal truth about what went wrong, funny on a single read, and
shippable in a real product's error dialog.

Stdlib only, deterministic.
"""

import os

ENTRY = (
    "We could not save your work: the disk is full, mostly of your "
    "earlier unsaved work. Please delete something, starting with that."
)


def validate(text: str) -> None:
    """Mirror the bounty gate: 1-200 chars, UTF-8, one line, not blank."""
    if not text or text != text.strip():
        raise ValueError("entry must not be empty or padded with whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > 200:
        raise ValueError(f"entry is {len(text)} chars, over the 200 limit")
    text.encode("utf-8")


def main() -> None:
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
