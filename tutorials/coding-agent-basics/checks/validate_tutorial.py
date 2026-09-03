#!/usr/bin/env python3
"""Validate tutorial structure or its safe practice-project resources.

This intentionally checks paths and headings only. It cannot determine whether a
report, recommendation, metric, or explanation is correct.
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
    "templates/progress.md",
    "templates/handoff.md",
]
MODULE_FILES = [
    "modules/00-mental-model.md",
    "modules/01-capable-request.md",
    "modules/02-options-and-tools.md",
    "modules/03-scope-and-friction.md",
    "modules/04-review-revise-reuse.md",
]
MODULE_HEADINGS = [
    "## Situation",
    "## Your move",
    "## Agent mode",
    "## Inspect",
    "## Unlock",
    "## Checkpoint",
]
PROJECT_REQUIREMENTS = {
    "README.md": ["fictional", "data/raw", "output/"],
    "AGENTS.md": ["Never modify", "data/raw", "output/"],
    "request.md": ["Goal", "Inputs", "Desired output", "What to verify"],
    "validation-note.md": ["Source", "Checks", "Assumptions"],
    "data/raw/survey_results.csv": ["respondent_id"],
    "notes/metric-definitions.md": ["#"],
    "notes/reporting-rules.md": ["#"],
    "output/data_quality_report.md": ["#"],
    ".agents/skills/monthly-report/scripts/check_survey.py": ["def main"],
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
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            errors.append(f"module lacks YAML front matter: {path}")
        missing = [heading for heading in MODULE_HEADINGS if heading not in text]
        if missing:
            errors.append(f"{path}: missing expected headings: {', '.join(missing)}")
    return errors


def validate_project(project: Path) -> list[str]:
    errors: list[str] = []
    for relative, expected_text in PROJECT_REQUIREMENTS.items():
        path = project / relative
        require_file(path, errors)
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        missing = [item for item in expected_text if item.casefold() not in text.casefold()]
        if missing:
            errors.append(f"{path}: missing expected text: {', '.join(missing)}")
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
        help="validate canonical tutorial files instead of safe practice-project resources",
    )
    parser.add_argument(
        "--project",
        type=Path,
        default=COURSE_ROOT / "examples/sample-project",
        help="practice-project directory (default: sample project)",
    )
    args = parser.parse_args()

    errors = validate_course() if args.course else validate_project(args.project.resolve())
    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    target = "course structure" if args.course else f"practice-project resources in {args.project}"
    print(f"Validation passed: {target}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
