# Tutorial Handoff

## Goal and route

- Learner goal: build a safe, inspectable draft reporting workflow.
- Selected route: practitioner example.

## Completed work and evidence

- Created a bounded request in `request.md`.
- Defined protected sources and completion checks in `AGENTS.md`.
- Added a reusable report skill under `.agents/skills/monthly-report/`.
- Recorded counts and exceptions in `validation-note.md`.
- Chose model qualities and review conditions in `model-selection.md`.

## Active artifacts and paths

- Raw input: `data/raw/survey_results.csv`
- Draft output: `output/data_quality_report.md`
- Notes: `notes/`
- Skill: `.agents/skills/monthly-report/SKILL.md`

## Constraints and approval boundaries

- Do not modify raw data.
- Do not resolve duplicate, missing, or invalid values without approval.
- Do not publish or send the draft.

## Open questions or topics to revisit

- Decide how production data should preserve source checksums.
- Decide how report owners review duplicate IDs.

## Resume here

- Current module: capstone review.
- Exact next smallest action: inspect the validation note, then run the structural validator from the tutorial directory.
