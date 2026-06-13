#!/usr/bin/env python3
"""Lightweight public output checker for Signal-to-Action Planner."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


DEFAULT_MAX_BYTES = 3500
ZH_FORBIDDEN_LABELS = [
    r"Core judgment\s*:",
    r"First move\s*:",
    r"Decision gate\s*:",
    r"Fact\s*:",
    r"Evidence\s*:",
    r"Confidence\s*:",
    r"Likelihood\s*:",
    r"Hypothesis\s*:",
    r"Evidence basis\s*:",
    r"Expected signal\s*:",
    r"Action\s*:",
    r"Priority\s+\d+\s*:",
    r"First step\s*:",
    r"First concrete step\s*:",
    r"Effort\s*/\s*Impact\s*/\s*Confidence\s*:",
    r"Risk\s*:",
    r"Quality check\s*:",
    r"Decision Summary",
    r"Risk And Quality Check",
]
REQUIRED_PATTERNS = {
    "actions": r"(?im)^#{1,3}\s*.*(a\s*-\s*act|priority\s+action\s+plan|priority\s+actions?|actions|top\s+actions|\u884c\u52a8)",
    "validation": r"(?im)^#{1,3}\s*.*(r\s*-\s*review|validation|\u9a8c\u8bc1)",
    "roadmap": r"(?im)^#{1,3}\s*.*(action\s+roadmap|roadmap|\u884c\u52a8\u8def\u7ebf)",
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

    has_cjk = re.search(r"[\u4e00-\u9fff]", text) is not None
    if has_cjk:
        mixed = [
            pattern for pattern in ZH_FORBIDDEN_LABELS
            if re.search(pattern, text, flags=re.IGNORECASE)
        ]
        if mixed:
            failures.append(
                "Chinese output contains non-localized labels: " + ", ".join(mixed[:5])
            )

    if failures:
        print("FAIL")
        for item in failures:
            print(f"- {item}")
        return 1

    print(f"PASS ({byte_len} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
