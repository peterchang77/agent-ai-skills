# Agent context: 03 — Constrained LLM report abstraction

## Assignment

Create a restartable CLI pipeline that reads valid cohort transitions, uses the approved OpenAI-compatible endpoint to abstract temporal change from paired **report impressions**, preserves provenance and raw endpoint artifacts in protected ignored storage, validates outputs, and creates a modeling-ready masked label manifest. First inspect endpoint/client conventions and propose the storage layout, fixed-run configuration, and retry/resume behavior.

## Scientific background

This is weak supervision, not clinical adjudication. For each prior/current pair, extract change for four concept families: pleural effusion, pulmonary edema, lung opacity, and support devices. Target states are `new`, `worsened`, `improved`, `stable`, and `resolved`. Also support explicit abstentions such as `not_mentioned`, `present_no_comparison`, `indeterminate`, and `not_applicable`.

Use only the prior and current impressions. The prior is context; a usable target requires certain, aligned temporal evidence quoted from the **current** impression. Do not send images or identifiers to the endpoint. Structural validation can show schema/evidence consistency; it cannot establish clinical truth or prove that a radiologist’s comparison refers to the supplied prior study.

## Workspace facts

- Endpoint configuration is provided as `WORKSHOP_LLM_BASE_URL`, `WORKSHOP_LLM_API_KEY`, and `WORKSHOP_LLM_MODEL`. Read them from the environment only; never log or commit values.
- The instructor may provide schema/prompt resources in the cloud workspace. If not, define and version a JSON schema/prompt before submitting records, then keep them fixed for the run.
- Start with ten transitions and store protected outputs under ignored `outputs/` or `data/derived/` paths.

## Required outcome

For each submitted transition, write a terminal structured record keyed by `transition_id` containing model ID, prompt version/content hash, timestamp, decoding configuration, parser/validation status, and either a parsed result or error. Store raw request/response/error content separately in protected ignored storage. Make `--resume` skip terminal records and never resubmit completed records merely to seek a better label. Bound retries and record failures.

Validate each concept independently. A usable target must have an allowed state, `certain` certainty, aligned/valid comparison, and a nonempty supporting quote found in normalized current impression. Mask rather than coerce outputs that are malformed, uncertain, unaligned, contradictory, unsupported, or abstentions. Mask `resolved` if it is justified only by a present-tense negative; mask `lung_opacity` if only isolated atelectasis, scar, nodule, or mass supports it without explicit opacity language.

Demonstrate a ten-record smoke run, a resume run that submits nothing completed, a malformed/invalid response test, and a modeling manifest with per-concept masks/reasons.

## Boundaries

Do not send images/direct identifiers, change model/prompt/decoding configuration within a run, overwrite raw outputs, treat labels as ground truth, or report clinical performance. If the endpoint is inaccessible, report the configured check/failure without replacing it with invented results.
