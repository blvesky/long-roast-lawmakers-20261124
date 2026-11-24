#!/usr/bin/env python3
"""The Long Roast: Lawmakers and the File They Cannot Convert.

Writes one satirical sentence to /output/entry.txt (1-320 chars, UTF-8).
"""
import os

ENTRY = (
    "The senator who wants a kill switch for every algorithm in America "
    "cannot find the Save As button, so his 900-page AI safety bill currently "
    "exists as a screenshot of a screenshot."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 320, f"entry length {len(text)} outside 1-320"
    assert text.count(".") == 1, "entry must be a single sentence"
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
