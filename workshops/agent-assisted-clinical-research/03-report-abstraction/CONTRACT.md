# Contract: extraction runner and validator

## Runner inputs and outputs

- Input: the serial-cohort manifest from exercise 02, limited initially to a requested number of transitions.
- Endpoint: environment variables described in `../shared/workspace-contract.md`.
- Prompt/schema: fixed for the run; save a prompt version or content hash.
- Protected/ignored outputs: raw request metadata and raw endpoint response/error per transition.
- Derived output: JSONL or Parquet structured result keyed by `transition_id`, containing the schema result, model ID, timestamp, prompt hash/version, decode settings, and terminal status.

## Required behavior

- Read only approved prior/current impression text and the transition ID needed for the task.
- Parse and validate a JSON object conforming to `schema.json`; do not repair a model answer silently.
- Make restart behavior explicit. `--resume` must skip completed terminal records and must not overwrite them.
- Use bounded retries with error records; do not loop indefinitely or conceal failures.
- Keep a concept masked when no usable target exists. Never coerce uncertainty or omission into a negative/change state.
- Separate raw responses from the modeling-ready manifest.

## Validator behavior

For each concept, emit a state, `usable` flag, and `mask_reasons`. A target state is usable only if comparison is aligned, certainty is `certain`, and the evidence quote is a nonempty substring of normalized current impression. Also mask unsupported resolution and unsupported isolated non-opacity labels.

## Out of scope

Human clinical adjudication, changing prompt/model mid-run, sending images, retrying completed records for a better answer, and using labels as clinical ground truth.