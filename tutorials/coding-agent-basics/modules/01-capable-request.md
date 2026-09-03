---
id: capable-request
title: Module 2 — Give one capable request and inspect the plan
estimated_minutes: 15
prerequisites:
  - mental-model
learning_loop: request-and-plan
objectives:
  - delegate a realistic outcome without micromanaging implementation
  - review an agent plan, tool rationale, and decision points before execution
checkpoint: plan
---

# Module 2 — Give One Capable Request and Inspect the Plan

## Situation

The fictional project contains raw survey data, project instructions, reporting notes, an existing deterministic checker, and an example output location. In normal work, you could ask for the whole internal report in one request. The useful question is whether the agent has chosen a sensible route before it starts making changes.

## Your move

How would you ask the agent to create a concise internal report from the sample project?

For example: “Create a reviewable Markdown report for a manager from the fictional survey data. First inspect the project and propose a plan. Preserve source data, reuse appropriate existing tools or code, flag uncertain records, and show me the evidence behind the result.”

Use your own wording. You need not tell the agent which Python library, commands, filenames, or intermediate steps to use.

## Agent mode

Before substantial work, the agent inspects only what is needed to understand the project and presents a concise plan. The plan states:

- its understanding of the outcome and source boundary;
- likely project resources and tools it can reuse, with a short rationale;
- expected deliverables and validation evidence;
- assumptions it can safely make; and
- the small number of decisions that materially need learner input.

It does not claim that a plan is execution, modify raw data, or connect external services.

## Inspect

Review the plan, not every implementation detail. Ask:

- Does it solve the result I actually want?
- Is it reusing existing instructions, scripts, or well-suited tools rather than building needless machinery?
- What will it show me to support its claims?
- Is there a meaningful decision I should make before it proceeds?

## Unlock

A capable request usually includes **outcome, context, constraints, audience or format, and success evidence**. The agent should handle routine mechanics. Asking for a plan is especially useful when the workspace is unfamiliar, the work may be expensive, or the result matters.

## Checkpoint

Continue when the learner has approved a plan or asked the agent to revise one meaningful part of it.