---
id: mental-model
title: Module 1 — Navigate agent work, do not micromanage it
estimated_minutes: 8
prerequisites: []
learning_loop: orient
objectives:
  - distinguish a model, coding agent, tools, and durable files
  - recognize the difference between a direct task and a workflow
checkpoint: understanding
---

# Module 1 — Navigate Agent Work, Do Not Micromanage It

## Situation

A coding agent is more than a chat window: it can inspect an approved workspace, use existing tools, write and run code, create files, and check results. The model supplies language and reasoning; the agent coordinates the work; tools and libraries perform concrete operations; files preserve useful results beyond the chat.

You do not need to prescribe every command or line of code. For a multi-row CSV, an agent will often use Python and existing CSV tools because deterministic counts and checks are more reliable than reasoning over every row in conversation. For a polished deliverable, it should choose a format that fits the audience and workflow.

## Your move

You are preparing an internal report from fictional survey data. Before asking the agent to do it, what would you want it to understand about the outcome, audience, source boundary, and evidence of success?

A natural answer is enough. You are defining the job, not selecting every tool.

## Agent mode

The agent turns the learner's intent into a brief working understanding. It identifies routine implementation choices it can make, such as inspecting project instructions or using an existing checker, and separates them from decisions that need the learner: audience, delivery format, treatment of ambiguity, external access, or publication.

## Inspect

Check that the working understanding answers four questions:

1. What useful result is wanted?
2. Who will use it?
3. What must remain protected or unchanged?
4. What would make the result trustworthy enough for this purpose?

## Unlock

A good request gives an agent a destination and guardrails, not an implementation screenplay. Let it choose ordinary means. Pause when a choice changes the audience, cost, privacy, source treatment, scope, or meaning of the result.

## Checkpoint

Continue when the learner can state a desired outcome and recognize that an agent may use tools, code, and project resources to reach it.