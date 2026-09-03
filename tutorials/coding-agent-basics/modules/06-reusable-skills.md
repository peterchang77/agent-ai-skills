---
id: reusable-skills
title: Act 5 — Package the repeatable workflow
estimated_minutes: 20
prerequisites:
  - files-as-memory
mission_act: package-the-workflow
objectives:
  - direct creation of a focused reusable skill
  - distinguish a skill from AGENTS.md, notes, and a deterministic tool
checkpoint: artifact
required_artifacts:
  - SKILL.md
adaptive:
  foundation: full
  practitioner: full
  technical-transfer: full
  goal-first: full
---

# Act 5 — Package the Repeatable Workflow

## Situation

The reporting process will recur. Repeating the whole conversation every month is fragile. The mission needs a small reusable procedure that can load when the task is recognized, while project rules and deterministic checks stay in their own places.

## Your move

Tell the agent to create or refine `.agents/skills/monthly-report/SKILL.md`. Require it to state the trigger, approved inputs, workflow, approval boundaries, expected outputs, and validation. Tell it to refer to project notes for detailed definitions and to `scripts/check_survey.py` for a deterministic data-quality check.

## Agent mode

The agent creates a focused skill and reports its path. It should not copy every `AGENTS.md` rule, embed a long policy manual, or make external actions automatic.

## Inspect

Read the skill as a colleague who has not seen the conversation. Can they tell when to load it, what it may read and write, what it must not decide, and how it proves success? Confirm the supporting script is a concrete action, not a second instruction manual.

## Unlock

| Layer | Purpose |
|---|---|
| Markdown note | Preserve knowledge and decisions. |
| `AGENTS.md` | Set always-relevant project operating rules. |
| Skill | Teach an agent a focused, reusable workflow on demand. |
| Script or tool | Perform a deterministic action reliably. |

Use a skill when the task recurs, is recognizable, has repeatable steps or checks, and benefits from references, templates, or a helper tool. A portable convention is `.agents/skills/<skill-name>/`; it can be project-local or, when the harness supports it, global under `~/.agents/skills/`.

## Checkpoint

Act 5 is unlocked when the skill can be selected by its trigger and safely produces a defined, validated draft without duplicating the whole project manual.
