---
name: large-corpus-llm-extraction
description: Plan and run a controlled large-scale model-assisted extraction or review workflow over free text. Use for approved corpus-wide structured abstraction, classification, or evidence-linked review through an LLM endpoint.
---

# Large-Corpus LLM Extraction

Use this skill when many text records must be processed through a language-model endpoint to create a structured dataset or review queue. Treat the work as a resumable data pipeline, not as one prompt repeated blindly. This skill sets the important design defaults; use the project's existing tools and conventions for ordinary implementation details.

Do not use it for one or a few documents, when direct agent inspection is practical, or when existing structured fields, deterministic parsing, search, rules, or a small human review can answer the question more safely and cheaply.

## Decide whether endpoint inference is justified

Before proposing an endpoint run, inspect the corpus and existing project resources. Prefer structured fields, deterministic parsers, dictionaries, rules, local search, or existing classifiers for clear cases. Use endpoint inference where free-text interpretation adds material value; a hybrid route that sends only ambiguous records to the model is often preferable.

State the source boundary and whether its text may be sent to an external service. Do not transmit sensitive, private, regulated, production, or credential-bearing material—or incur endpoint cost—without explicit approval. Preserve raw source material and write outputs as separate derived artifacts.

## Define a reviewable extraction contract

Before sending requests, record enough to make every output understandable and auditable:

- the unit of work and an immutable source-record ID;
- source fields, dataset/version, and the approved scope;
- a narrow JSON output schema, types, allowed labels, and meanings of `null`, `unknown`, `not_applicable`, `failed`, or `needs_review` as relevant;
- which claims require exact source evidence, quoted text, or source-field references;
- when the model must abstain rather than infer; and
- what the resulting labels support and explicitly do not prove.

Prefer strict structured JSON to explanatory prose. Validate every decoded response against the schema. A model-reported confidence is not a calibrated probability; use it only as a possible review-routing signal after checking it against samples or references.

## Inventory, estimate, and pilot

For a large, paid, external, sensitive, or consequential run, inspect record count, text-length distribution, missingness, duplicates, source formats, sensitive content, and available reference labels. From a representative sample, estimate request count, input/output token ranges, cost range, throughput/time, storage, and expected human-review burden. Report material assumptions and drivers rather than invented precision.

Propose a small representative pilot before the full run. Include ordinary, long, short, ambiguous, missing-evidence, and important subgroup records where relevant. Define what success, failure, review-needed, and stop conditions look like. Obtain explicit approval after the user has seen the service/data destination, scale/cost estimate, and pilot result before launching a broad external or paid run.

## Run at scale without losing accountability

Use configurable, bounded concurrency appropriate to the endpoint's documented limits. Do not fan out one worker per record. Decode and validate structured JSON, distinguish transient transport failures from invalid input or schema failures, and use bounded retry/backoff only for retriable failures. Keep failed, skipped, and review-needed records visible rather than forcing a result.

Make the run idempotent, checkpointed, and resumable. Persist per-record state and enough provenance to reconnect an outcome to its source: record ID, status, run/schema/prompt/model version, validation warnings, evidence, retry/failure reason, and available usage/cost metadata. Reconcile every input record as completed, intentionally skipped, failed, or queued for review.

Prefer **durable polling** for long-running remote work: persist the submitted job/request identifiers and last-known status, then poll the provider or job state at a bounded interval while recording progress snapshots. The agent should be able to resume progress reporting after a shell, process, or chat session ends, rather than relying on a continuously held connection or ephemeral in-memory counters. Treat polling as observability, not permission to bypass rate limits, budgets, or approval boundaries.

## Validate, review, and hand off

A parseable response is not necessarily a correct extraction. Check schema/type validity, allowed values, evidence-to-source consistency, contradictions, missingness, output distributions, duplicate outcomes, and input/output count reconciliation. For consequential fields, verify that cited evidence actually occurs in the source text where possible.

Review a representative and targeted sample: rare labels, uncertain or abstaining results, long records, unusual source formats, errors, and important subgroups. Compare with approved references when available. Keep model-assisted extraction separate from final human, scientific, legal, clinical, financial, or operational decisions unless an approved review process establishes otherwise.

Report output locations; source and run scope; completion/failure/review counts; validation and sample-review evidence; observed versus estimated usage/cost; known limitations; and the safest restart path. Retain reusable code, prompt/schema definitions, and run records when recurrence, auditability, or safe resumption justifies their maintenance cost.
