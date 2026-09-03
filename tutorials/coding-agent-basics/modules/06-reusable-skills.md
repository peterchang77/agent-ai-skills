---
id: reusable-skills
title: Turn repeatable work into a skill
estimated_minutes: 20
prerequisites:
  - files-as-memory
objectives:
  - decide when a skill is appropriate
  - distinguish a skill from AGENTS.md and a deterministic tool
  - outline a small reusable skill
checkpoint: artifact
required_artifacts:
  - SKILL.md
adaptive:
  foundation: full
  practitioner: full
  technical-transfer: full
  goal-first: full
---

# Turn Repeatable Work into a Skill

## In brief

Create a skill when a recognizable task repeats and benefits from the same procedure, references, templates, checks, or helper scripts. A skill is a reusable capability package, not a catch-all handbook.

A portable convention is:

```text
.agents/skills/
└── monthly-report/
    ├── SKILL.md
    ├── references/
    ├── templates/
    └── scripts/
```

Put it in a project as `.agents/skills/` when it belongs to that project, or under `~/.agents/skills/` when it is useful across projects. Agent harnesses vary, so check discovery rules before relying on automatic loading.

## Compare the layers

| Layer | Purpose |
|---|---|
| Markdown note | Preserve knowledge and decisions. |
| `AGENTS.md` | Set always-relevant project operating rules. |
| Skill | Teach an agent a focused, reusable workflow on demand. |
| Script or tool | Perform a deterministic action reliably. |

`AGENTS.md` says how to behave **here**. A skill says how to perform a kind of work. A script carries out a specific operation.

## Decide

Use a skill only when most answers are yes:

1. Does the task recur?
2. Can a user recognize when to use it?
3. Does it have repeatable inputs, outputs, steps, or checks?
4. Would references, templates, or a script reduce errors?

If the task is a one-off, start with a note or request template instead.

## Try it

Read the sample [`monthly-report/SKILL.md`](../examples/sample-project/.agents/skills/monthly-report/SKILL.md). Outline a skill for one recurring safe workflow. Keep its `SKILL.md` to purpose, trigger, inputs, workflow, approval boundaries, outputs, and validation. Move detail to a reference or script.

## Inspect

Check that your proposed skill does not duplicate every project rule from `AGENTS.md`, does not require an unapproved external action, and names what proves success.

## Record

Save the skill path and a sentence explaining why it is a skill rather than a note or script in `progress.md`.

## Checkpoint

A colleague should be able to tell when to load the skill and what it will safely produce.
