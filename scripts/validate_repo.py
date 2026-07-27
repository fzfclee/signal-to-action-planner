from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = [
    "README.md",
    "README.zh-CN.md",
    "SKILL.md",
    "minimal_SKILL.md",
    "ultra_minimal_SKILL.md",
    "conversation_flow.md",
    "output_templates.md",
    "examples.md",
    "BENCHMARK.md",
    "CONTRIBUTING.md",
    "ROADMAP.md",
    "NOTICE.md",
    "LICENSE",
    "SECURITY.md",
]
TEXT_SUFFIXES = {".md", ".py", ".yml", ".yaml", ".txt"}
LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def read_text(relative_path: str) -> str:
    path = ROOT / relative_path
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        fail(f"{relative_path} is not valid UTF-8: {exc}")
    raise AssertionError("unreachable")


def validate_required_files() -> None:
    missing = [path for path in REQUIRED_FILES if not (ROOT / path).is_file()]
    if missing:
        fail(f"missing required files: {', '.join(missing)}")


def validate_text_encoding() -> None:
    for path in ROOT.rglob("*"):
        if ".git" in path.parts or not path.is_file():
            continue
        if path.suffix.lower() not in TEXT_SUFFIXES and path.name != "LICENSE":
            continue
        raw = path.read_bytes()
        if raw.startswith(b"\xef\xbb\xbf"):
            fail(f"{path.relative_to(ROOT)} contains a UTF-8 BOM")
        try:
            raw.decode("utf-8")
        except UnicodeDecodeError as exc:
            fail(f"{path.relative_to(ROOT)} is not valid UTF-8: {exc}")


def validate_skill_contract() -> None:
    skill = read_text("SKILL.md")
    if not skill.startswith("---\n"):
        fail("SKILL.md must start with YAML frontmatter")
    required_fragments = [
        "name: signal-to-action-planner",
        "description:",
        "## Mandatory Front-End Interaction",
        "## Evidence And Confidence Rules",
        "C - Clarify the Facts",
        "L - Locate the Signal",
        "E - Expose the Opportunity",
        "A - Act with a Justified Next Move",
        "R - Review the Evidence",
        "## Default Output Format",
        "## 7. Risk And Quality Check",
    ]
    for fragment in required_fragments:
        if fragment not in skill:
            fail(f"SKILL.md is missing required contract text: {fragment}")


def validate_markdown_links() -> None:
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        for target in LINK_PATTERN.findall(text):
            clean_target = target.split("#", 1)[0].strip()
            if not clean_target or clean_target.startswith(
                ("http://", "https://", "mailto:")
            ):
                continue
            if clean_target.startswith("<") and clean_target.endswith(">"):
                clean_target = clean_target[1:-1]
            destination = (path.parent / clean_target).resolve()
            if not destination.exists():
                fail(
                    f"broken Markdown link in {path.relative_to(ROOT)}: {target}"
                )


def validate_public_entry() -> None:
    readme = read_text("README.md")
    required_fragments = [
        "# Signal-to-Action Planner",
        "## 30-Second Start",
        "## How CLEAR Works",
        "## Quality Evidence",
        "https://www.o2vframework.com/en/personal/clear",
        "README.zh-CN.md",
    ]
    for fragment in required_fragments:
        if fragment not in readme:
            fail(f"README.md is missing required public-entry text: {fragment}")


def main() -> int:
    validate_required_files()
    validate_text_encoding()
    validate_skill_contract()
    validate_markdown_links()
    validate_public_entry()
    print(
        "PASS: Signal-to-Action repository structure, UTF-8, links, "
        "CLEAR contract, and public entry are valid."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
