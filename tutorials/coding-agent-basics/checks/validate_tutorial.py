#!/usr/bin/env python3
"""Validate tutorial structure or a learner's capstone artifact structure.

This intentionally checks paths and headings only. It cannot determine whether a
report, metric, or explanation is correct.
"""

from __future__ import annotations

import argparse
from pathlib import Path

HERE = Path(__file__).resolve().parent
COURSE_ROOT = HERE.parent

COURSE_FILES = [
    "README.md",
    "COURSE.md",
    "SKILL.md",
    "tutorial.yaml",
    "templates/learner-profile.md",
    "templates/mission-log.md",
    "templates/handoff.md",
]
MODULE_FILES = [f"modules/{index:02d}-{name}.md" for index, name in [
    (0, "mission-setup"),
    (1, "what-is-a-coding-agent"),
    (2, "model-provider-chat-agent"),
    (3, "bounded-requests"),
    (4, "inspect-and-validate"),
    (5, "files-as-memory"),
    (6, "reusable-skills"),
    (7, "context-and-compaction"),
    (8, "model-selection-and-connection"),
    (9, "capstone"),
]]

CAPSTONE_REQUIREMENTS = {
    "request.md": ["#", "Goal", "Inputs", "Desired output", "What to verify"],
    "AGENTS.md": ["#", "Purpose", "Working rules", "Paths", "Before finishing"],
    "validation-note.md": ["#", "source", "check"],
    "model-selection.md": ["#", "task", "validation"],
    ".tutorial/mission-log.md": ["#", "Mission", "Acts", "Current position"],
    ".tutorial/handoff.md": ["#", "Goal", "Completed", "Resume"],
    ".agents/skills/monthly-report/SKILL.md": ["---", "name:", "description:", "Workflow", "Validation"],
}


def require_file(path: Path, errors: list[str]) -> None:
    if not path.is_file():
        errors.append(f"missing file: {path}")


def validate_course() -> list[str]:
    errors: list[str] = []
    for relative in COURSE_FILES + MODULE_FILES:
        require_file(COURSE_ROOT / relative, errors)
    for relative in MODULE_FILES:
        path = COURSE_ROOT / relative
        if path.is_file() and not path.read_text(encoding="utf-8").startswith("---\n"):
            errors.append(f"module lacks YAML front matter: {path}")
    return errors


def validate_capstone(project: Path) -> list[str]:
    errors: list[str] = []
    for relative, headings in CAPSTONE_REQUIREMENTS.items():
        path = project / relative
        require_file(path, errors)
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        missing = [heading for heading in headings if heading.casefold() not in text.casefold()]
        if missing:
            errors.append(f"{path}: missing expected heading/text: {', '.join(missing)}")
    raw = project / "data/raw"
    output = project / "output"
    if raw.exists() and raw.is_dir() and output.resolve() == raw.resolve():
        errors.append("output directory must not be data/raw")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--course",
        action="store_true",
        help="validate canonical tutorial files instead of learner capstone artifacts",
    )
    parser.add_argument(
        "--project",
        type=Path,
        default=COURSE_ROOT / "examples/sample-project",
        help="capstone project directory (default: sample project)",
    )
    args = parser.parse_args()

    errors = validate_course() if args.course else validate_capstone(args.project.resolve())
    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    target = "course structure" if args.course else f"capstone structure in {args.project}"
    print(f"Validation passed: {target}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
