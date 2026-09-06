# 04 — Build a single-page annotation tool

## Learning goal

Use an agent to build a small, inspectable research interface rather than reach for a large application framework. The tool supports human review of report abstractions; it does not determine clinical truth.

Read [`CONTEXT.md`](CONTEXT.md), [`CONTRACT.md`](CONTRACT.md), and [`ACCEPTANCE.md`](ACCEPTANCE.md), then write your own request. Tell the agent to inspect the schema from exercise 03 and ask it to propose a minimal interaction design before implementing.

## Deliverable

Create one self-contained HTML file that loads a local JSON/JSONL review set selected by the user, presents a prior/current report pair with an LLM proposal, supports a reviewer decision and evidence capture, and downloads annotations as JSON. It must work without a backend or external CDN.

## Deliberate scope limit

Do not ask for authentication, database synchronization, multi-user collaboration, or diagnosis. A clear local review tool is the point of the exercise.

## Recovery

A finished optional example is available under [`reference/`](reference/); do your own implementation before opening it. Compare your request with [`../reference-prompts/04-annotation-tool.md`](../reference-prompts/04-annotation-tool.md) only after your first attempt.