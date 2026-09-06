# 06 — Analyze and write the result

## Learning goal

Use an agent to turn saved analysis artifacts into transparent figures/tables and a small LaTeX report, while correcting claims that exceed the evidence.

Read [`CONTEXT.md`](CONTEXT.md), [`CONTRACT.md`](CONTRACT.md), and [`ACCEPTANCE.md`](ACCEPTANCE.md). Ask the agent to inventory the actual result files before writing. Do not ask it to invent missing statistics or citations.

## Deliverable

Create a concise LaTeX methods/results document, a BibTeX file, and scripts/commands that generate a metrics table and at least one labeled result figure from saved evaluation outputs. The report must compile and must use only facts traceable to saved artifacts or supplied source metadata.

## Review exercise

Ask the agent to identify at least three overclaims that a careless draft might make, then ensure the final text avoids them. Examples include calling pseudo-label agreement “diagnostic accuracy,” treating a small point estimate as proof, or implying that structural validator checks establish clinical truth.

## Recovery

After trying your own request, compare with [`../reference-prompts/06-results-and-writing.md`](../reference-prompts/06-results-and-writing.md).