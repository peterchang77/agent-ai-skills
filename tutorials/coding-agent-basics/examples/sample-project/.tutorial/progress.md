# Coding Agent Basics — Mission Progress

## Mission and route
- Mission: Deliver a trustworthy draft monthly report without changing raw inputs.
- Learner goal: build a safe, inspectable draft reporting workflow.
- Selected route: practitioner example.

## Acts unlocked
- [x] Act 1 — Survey the workspace safely.
  - Learner-issued command: inspect sources and instructions without changing files.
  - Evidence / artifact: read-only inspection of `data/raw/`, `AGENTS.md`, and notes.
- [x] Act 2 — Define the reporting job.
  - Learner-issued command: draft a bounded request with approval boundaries.
  - Evidence / artifact: `request.md`
- [x] Act 3 — Investigate without changing sources.
  - Learner-issued command: create a draft quality report and validation evidence.
  - Evidence / artifact: `output/data_quality_report.md`, `validation-note.md`
- [x] Act 4 — Establish durable operating rules.
  - Learner-issued command: record concise operating rules and deeper notes separately.
  - Evidence / artifact: `AGENTS.md`, `notes/`
- [x] Act 5 — Package the repeatable workflow.
  - Learner-issued command: create a focused monthly-report skill with a deterministic check.
  - Evidence / artifact: `.agents/skills/monthly-report/`
- [x] Act 6 — Prepare handoff and operating choices.
  - Learner-issued command: create a handoff and model-selection decision.
  - Evidence / artifact: `.tutorial/handoff.md`, `model-selection.md`
- [x] Act 7 — Review the trustworthy draft.
  - Learner-issued command: run the structural validator and review its limit.
  - Evidence / artifact: passed structural validation; human content review still required.

## Current position
- Current act/module: mission complete; ready for human review.
- Next learner-issued command or decision: approve, revise, or reject the handling of data-quality exceptions.

## Decisions and constraints
- Preserve raw data; flag rather than resolve exceptions.
- Do not publish the draft.

## Revisit later
- Define the real workflow's source checksum and approval process.
