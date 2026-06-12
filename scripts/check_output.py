#!/usr/bin/env python3
"""Lightweight public output checker for Signal-to-Action Planner."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


DEFAULT_MAX_BYTES = 4500
REQUIRED_PATTERNS = {
    "actions": r"(?im)^#{1,3}\s*(priority\s+actions?|actions|top\s+actions|\u884c\u52a8)",
    "validation": r"(?im)^#{1,3}\s*(validation|\u9a8c\u8bc1)",
    "roadmap": r"(?im)^#{1,3}\s*(action\s+roadmap|roadmap|\u884c\u52a8\u8def\u7ebf)",
}


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check public Signal-to-Action output length and required sections."
    )
    parser.add_argument("file", help="Markdown output file to check")
    parser.add_argument("--max-bytes", type=int, default=DEFAULT_MAX_BYTES)
    args = parser.parse_args()

    text = Path(args.file).read_text(encoding="utf-8").lstrip("\ufeff")
    byte_len = len(text.encode("utf-8"))
    failures: list[str] = []

    if byte_len > args.max_bytes:
        failures.append(f"output is {byte_len} bytes, above {args.max_bytes}")

    for name, pattern in REQUIRED_PATTERNS.items():
        if not re.search(pattern, text):
            failures.append(f"missing section: {name}")

    if "Evidence:" not in text and "\u8bc1\u636e" not in text:
        failures.append("missing evidence marker")

    if "Risk:" not in text and "\u98ce\u9669" not in text:
        failures.append("missing risk marker")

    if failures:
        print("FAIL")
        for item in failures:
            print(f"- {item}")
        return 1

    print(f"PASS ({byte_len} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
