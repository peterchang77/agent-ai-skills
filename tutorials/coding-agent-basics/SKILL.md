---
name: coding-agent-basics-tutorial
description: Facilitate a concise, adaptive introduction to coding agents for data scientists and office professionals. Use when a learner wants to understand agents, models and providers, reliable requests, durable instruction files, reusable skills, context compaction, or model selection.
---

# Coding Agent Basics Tutorial

Use the `tutorial-facilitator` skill. This file defines this course's materials and completion criteria; the facilitator defines how to teach it.

## Materials

- Course overview: [COURSE.md](COURSE.md)
- Manifest: [tutorial.yaml](tutorial.yaml)
- Canonical lessons: [modules/](modules/)
- Safe practice project: [examples/sample-project/](examples/sample-project/)
- Learner state templates: [templates/](templates/)
- Structural validator: `python3 checks/validate_tutorial.py --project examples/sample-project` (run from this tutorial directory)

## Start

1. Ask the learner for a goal, work context, time, pace, and whether to use samples or authorized real copies.
2. Create or resume `.tutorial/` from `templates/`.
3. Facilitate Module 00's diagnostic unless the learner declines it.
4. Select foundation, practitioner, technical-transfer, or goal-first delivery. Explain that the route changes depth and examples, not the required outcomes.
5. Teach one small step per turn. Default to concise, plain terms. Do not quote a whole module.

## Required outcomes

Before completion, record evidence that the learner can:

1. distinguish a model, provider, interactive chat, and coding agent;
2. write a request with a goal, inputs, outputs, rules, validation, and approval boundary;
3. preserve a source and inspect evidence for an output;
4. distinguish Markdown notes, `AGENTS.md`, skills, and deterministic scripts/tools;
5. explain why durable state and proactive compaction matter; and
6. select a model using task requirements rather than brand alone.

## Adaptation

Use spreadsheet, documents, and reporting examples for office professionals. Use CSV, analysis, and reproducibility examples for data scientists. For technically experienced learners, probe before skipping familiar concepts. For everyone, define jargon at first use and prefer simple terms.

## Safety

Use `examples/sample-project/` by default. Do not edit raw inputs, access real workplace data, connect a provider, publish, send, delete, or spend without explicit learner approval. Keep source and output paths separate. State what evidence supports any completion claim.

## Capstone

Facilitate Module 09 using the sample project or a safe equivalent. Run `python3 checks/validate_tutorial.py --project examples/sample-project` from this tutorial directory after the learner creates the expected artifacts. Explain that passing confirms file structure only; the learner still reviews meaning, calculations, and suitability.
