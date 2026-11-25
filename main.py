#!/usr/bin/env python3
"""One Line, One Laugh — writes a single original funny line to /output/entry.txt.

Python 3, standard library only. Deterministic: no randomness, no clock,
no network — the same line every run.
"""

import os

LINE = "I asked my smartwatch how I slept last night. It said, 'Poorly \u2014 but impressively consistent.'"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
