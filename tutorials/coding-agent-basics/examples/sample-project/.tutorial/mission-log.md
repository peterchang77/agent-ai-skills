# Mission Log: Trustworthy Monthly Report

## Mission
- Outcome to deliver: A reviewable draft data-quality report from fictional monthly survey data.
- Safe practice boundary: Never modify `data/raw/`; do not publish or resolve ambiguous records.
- Chosen route: practitioner example.

## Acts
- [x] Act 1 — Survey the workspace safely
  - Evidence / artifact: inspected `data/raw/survey_results.csv`, `AGENTS.md`, and project notes before creating outputs.
- [x] Act 2 — Define the reporting job
  - Evidence / artifact: `request.md`
- [x] Act 3 — Investigate without changing sources
  - Evidence / artifact: `output/data_quality_report.md` and `validation-note.md`
- [x] Act 4 — Establish durable operating rules
  - Evidence / artifact: `AGENTS.md` and `notes/`
- [x] Act 5 — Package the repeatable workflow
  - Evidence / artifact: `.agents/skills/monthly-report/SKILL.md` and `scripts/check_survey.py`
- [x] Act 6 — Prepare handoff and operating choices
  - Evidence / artifact: `.tutorial/handoff.md` and `model-selection.md`
- [x] Act 7 — Review the trustworthy draft
  - Evidence / artifact: structural validator passed; final human review remains required.

## Current position
- Current act: mission complete; ready for human review.
- Next learner move: inspect the draft and approve, revise, or reject its handling of exceptions.
- Open risk or approval needed: decide how a production workflow handles duplicate IDs and source checksums.
