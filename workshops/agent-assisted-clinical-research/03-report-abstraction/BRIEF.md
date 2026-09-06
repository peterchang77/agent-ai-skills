# 03 — Report abstraction with an LLM

## Learning goal

Direct an agent to create a small, restartable LLM data-abstraction program with a fixed schema, raw-output retention, provenance, and structural validation. The goal is not to have the agent write a clever prompt once; it is to make a weak-labeling process inspectable and recoverable.

Read [`CONTEXT.md`](CONTEXT.md), [`CONTRACT.md`](CONTRACT.md), [`schema.json`](schema.json), and [`ACCEPTANCE.md`](ACCEPTANCE.md). Write your own request before viewing a reference prompt.

## Deliverable

Create a CLI that reads a serial-cohort manifest, sends the minimum approved prior/current report text to the approved OpenAI-compatible endpoint, and writes one structured result per transition plus raw protected endpoint artifacts. Then create or integrate validation that produces a masked modeling manifest.

Start with ten transitions. Ask the agent to inspect the endpoint/client conventions and propose the storage layout and retry/resume policy before implementing.

## Important limitation

The output is a **report-derived weak pseudo-label**. Structural checks can show that a quote exists in the supplied current impression and that values follow the schema. They cannot establish clinical truth, prove that the report’s comparison is the supplied prior, or validate an image model clinically.

## After your attempt

Inspect the good/bad examples in [`examples/`](examples/) and then, if useful, compare with [`../reference-prompts/03-report-abstraction.md`](../reference-prompts/03-report-abstraction.md).