#!/usr/bin/env python3
"""Entry generator for make.fun competition
u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a.

Writes exactly one sentence (1-200 chars) to /output/entry.txt.
Concept: "Bottled Silence, Sold by the Hour" — we bottle the silence of
empty churches at dawn and sell it by the hour to open-plan offices.
"""
import os

TEXT = (
    "We bottle the silence of empty churches at dawn and sell it by the hour "
    "to open-plan offices, because one quiet hour buys back the focus that "
    "noise-cancelling headphones never could."
)


def main():
    text = TEXT.strip()
    # Judge rule: ONE sentence, 1-200 chars. Count is in characters, but the
    # harness reads bytes, so guard the UTF-8 byte length too (ASCII text
    # here, so both counts agree; the byte check stays as a safety net).
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert len(text.encode("utf-8")) <= 200, (
        f"entry must be <=200 UTF-8 bytes, got {len(text.encode('utf-8'))}"
    )
    assert text.count(".") == 1 and text.endswith("."), "entry must be one sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(text)


if __name__ == "__main__":
    main()
