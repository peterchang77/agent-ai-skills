# Tutorial Handoff

## Goal and route

- Mission: Deliver a trustworthy draft monthly report without changing raw inputs.
- Learner goal: build a safe, inspectable draft reporting workflow.
- Selected route: practitioner example.

## Completed work and evidence

- Surveyed source files and project instructions without creating or changing source data.
- Created a bounded request in `request.md`.
- Defined protected sources and completion checks in `AGENTS.md`.
- Added a reusable report skill under `.agents/skills/monthly-report/`.
- Recorded counts and exceptions in `validation-note.md`.
- Chose model qualities and review conditions in `model-selection.md`.
- Recorded all acts and evidence in `.tutorial/mission-log.md`.

## Active artifacts and paths

- Raw input: `data/raw/survey_results.csv`
- Draft output: `output/data_quality_report.md`
- Notes: `notes/`
- Skill: `.agents/skills/monthly-report/SKILL.md`
- Mission log: `.tutorial/mission-log.md`

## Constraints and approval boundaries

- Do not modify raw data.
- Do not resolve duplicate, missing, or invalid values without approval.
- Do not publish or send the draft.

## Open questions or topics to revisit

- Decide how production data should preserve source checksums.
- Decide how report owners review duplicate IDs.

## Resume here

- Current act: final human review.
- Exact next smallest action: inspect the draft report and decide whether its unresolved exceptions are acceptable for the intended audience.
