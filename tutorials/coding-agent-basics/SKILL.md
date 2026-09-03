---
name: coding-agent-basics-tutorial
description: Facilitate a concise, adaptive guided build in which a learner directs an agent to create a trustworthy monthly reporting workflow. Use when a learner wants practical experience with coding agents, models and providers, reliable requests, durable instruction files, reusable skills, context handoffs, or model selection.
---

# Coding Agent Basics Mission

Use the `tutorial-facilitator` skill. This file defines the mission, acts, materials, and completion evidence; the facilitator defines the coach/operator delivery protocol.

## Mission

Guide the learner to deliver a trustworthy draft monthly report from the fictional CSV project without altering raw inputs or resolving ambiguity without approval. The learner is the operator: they should direct the action that advances each act before the agent performs it.

## Materials

- Course guide: [COURSE.md](COURSE.md)
- Manifest: [tutorial.yaml](tutorial.yaml)
- Mission acts: [modules/](modules/)
- Safe project: [examples/sample-project/](examples/sample-project/)
- Learner state templates: [templates/](templates/)
- Structural validator: `python3 checks/validate_tutorial.py --project examples/sample-project` (run from this tutorial directory)

## Start

1. Ask the learner for a practical goal, domain, time, pace, and whether to use samples or an authorized copy.
2. Create or resume `.tutorial/learner-profile.md`, `.tutorial/progress.md`, and `.tutorial/mission-log.md` from the templates.
3. Facilitate Module 00 as mission setup. Use the learner's initial instructions—not a quiz—as primary evidence for route selection.
4. State the mission boundary and Act 1 obstacle. Ask for one read-only command; do not inspect the project until the learner directs it.
5. For every later act, use Brief → Learner move → Operate → Inspect → Unlock → Record. Keep turns concise and do not quote whole modules.

## Required mission evidence

Before completion, record evidence that the learner has directed the agent to:

1. inspect a workspace safely and identify the model/provider/agent access boundary;
2. create a request with a goal, inputs, outputs, rules, validation, and approval boundary;
3. preserve a source and inspect evidence for an output;
4. use Markdown notes, `AGENTS.md`, a skill, and a deterministic tool for distinct roles;
5. create a durable handoff before compaction or a pause; and
6. select a model using task requirements rather than brand alone.

## Adaptation

Use spreadsheet, documents, and reporting examples for office professionals. Use CSV, analysis, and reproducibility examples for data scientists. For foundation learners, offer a command starter; for experienced learners, ask them to supply validation criteria and constraints. Define jargon only when it becomes useful to the next move.

## Safety

Use `examples/sample-project/` by default. Do not edit raw inputs, access real workplace data, connect a provider, publish, send, delete, or spend without explicit learner approval. Keep source and output paths separate. State the evidence behind each unlocked act.

## Final review

Facilitate Module 09 using the sample project or a safe equivalent. Run `python3 checks/validate_tutorial.py --project examples/sample-project` from this tutorial directory after the learner creates the artifacts. Passing confirms file structure only; the learner still reviews meaning, calculations, and suitability.
