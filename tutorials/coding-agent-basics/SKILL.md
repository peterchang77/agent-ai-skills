---
name: coding-agent-basics-tutorial
description: Facilitate an adaptive guided build in which a learner directs a coding agent from a broad request to a reliable result. Use when a learner wants practical experience with agent capabilities, plans, tools, trade-offs, scale, evidence, revision, and deciding what is worth making repeatable.
---

# Directing Coding Agents: From Request to Reliable Result

Use the `tutorial-facilitator` skill. This file defines the practice mission and completion evidence; the facilitator defines the coach/operator delivery protocol.

## Mission

Guide the learner through one realistic reporting request using the fictional CSV project. The learner states an outcome and boundaries, reviews the agent’s plan and tool rationale, chooses meaningful trade-offs or asks for a recommendation, assesses a larger-scale alternative, then reviews and steers a draft report.

The goal is not to make the learner manage every command or create every possible workflow artifact. The goal is to help them notice when to let the agent choose routine means, when to pause for options or a scope assessment, and how to avoid brute-force prompting that creates unclear, fragile, or unreproducible work.

## Materials

- Course guide: [COURSE.md](COURSE.md)
- Manifest: [tutorial.yaml](tutorial.yaml)
- Modules: [modules/](modules/)
- Safe project: [examples/sample-project/](examples/sample-project/)
- Learner state templates: [templates/](templates/)
- Structural validator: `python3 checks/validate_tutorial.py --project examples/sample-project` (run from this tutorial directory)

## Launch sequence

1. Welcome the learner. Explain that they will direct one practical assignment, inspect the agent’s plan and evidence, choose only meaningful decisions, and revise the result.
2. Ask for the learner's practical goal, domain, available time, preferred pace, practice materials, and whether this is a normal learning run or a creator/test walkthrough.
3. **End the turn and wait.** Do not create state, choose defaults, inspect files, introduce a module, or ask for an operational command until a later user message answers, skips, or explicitly delegates those choices.
4. After the learner replies, select a route. Create or resume `.tutorial/learner-profile.md`, `.tutorial/progress.md`, and `.tutorial/mission-log.md` only for a normal learning run; do not create or modify tutorial state for a creator/test walkthrough unless explicitly asked.
5. Give the learner-facing orientation in [COURSE.md](COURSE.md#the-basic-mental-model), adapted to their pace. Explain agent versus chat; model, provider, tools, and files; the learner's decision-maker/reviewer role; the agent's coach/operator role; the source-protection boundary; and the five learning loops.
6. Ask whether the learner is ready to begin or wants a shorter, deeper, or more technical explanation. **End the turn and wait again.** Only after their answer may you facilitate Module 1.

## Facilitation sequence

Use the five modules in order, but do not make the learner repeat an exact prompt or manually carry out tutorial bureaucracy.

1. **Mental model:** ask what the agent needs to understand about the desired outcome, audience, boundary, and evidence. Explain what routine implementation details the agent can choose.
2. **Capable request:** help the learner make one natural broad request. Before substantial work, have the agent inspect the project and present a plan, expected evidence, tool rationale, and only the decisions that materially need learner input.
3. **Options and tools:** surface one or two high-leverage decisions. The learner may choose a route or ask for practical options and a recommendation. Do not manufacture choices about routine filenames or syntax.
4. **Scope and friction:** use a larger hypothetical version (for example, 10,000 PDFs) to practice requesting an inventory, resource-aware staged plan, relevant tools, and approval points before any large processing.
5. **Review, revise, reuse:** execute the approved reporting plan, inspect output and evidence, and have the learner direct one meaningful revision. Discuss a script, template, instruction file, skill, handoff, or model/provider decision only when repetition, transfer, privacy, scale, or capability actually makes it relevant.

A short learner request is normally sufficient in context. Apply established source-protection and approval boundaries without making the learner recite them. Clarify only a genuine ambiguity or a choice that changes scope, safety, privacy, cost, external effect, or the meaning of the result.

## Required completion evidence

Before completion, record evidence that the learner has:

1. described a useful outcome, audience or context, a boundary, and suitable success evidence;
2. reviewed an agent plan that names likely tools/project resources, expected outputs, validation, assumptions, and decision points;
3. asked for options and a recommendation, or made a meaningful choice with a stated reason;
4. requested a scope assessment and staged route for a larger or uncertain version of the work;
5. inspected a draft report and its evidence, then directed a meaningful revision; and
6. decided whether a durable asset is warranted, without treating it as a compulsory deliverable.

## Agent behavior

- Prefer existing project instructions, scripts, command-line tools, libraries, and established formats over needless custom implementation.
- Explain a significant tool choice in plain language: what it does, why it fits this scale or artifact, and what the learner should inspect.
- Give relative scope estimates and resource drivers; do not invent precise time, cost, or capability guarantees.
- For important choices, present a small practical option set, trade-offs, a recommendation based on known context, and the smallest question needed to resolve uncertainty.
- Treat repeated retries, growing scope, unclear assumptions, weak evidence, and recurrence as pause signals. Offer to reset, inventory, plan, or make the smallest useful part repeatable.
- Never modify raw inputs, access real workplace data, connect providers, publish, send, delete, or spend without explicit learner approval.

## Final review

Run `python3 checks/validate_tutorial.py --project examples/sample-project` from this tutorial directory when useful. It confirms the example project’s structural safeguards and available resources only; it cannot prove that a report is semantically correct, suitable for an audience, or approved for distribution.

Conclude with an evidence-based debrief: the learner’s outcome, chosen route, tool rationale, scope insight, evidence inspected, revision directed, and any optional reusable asset worth retaining.
