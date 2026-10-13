---
role: bulk-classify
title: Classify many records with a language-model API
kind: advanced
summary: Execute batch record classification via programmatic API calls with dry-run estimation, incremental state checkpointing, and validation against a benchmark sample.
time: 12 min
teaches: [tools, costs, verification]
needs: [use-secrets]
---

In this advanced exercise, you build a batch-processing script that queries an external language-model API to classify hundreds of text records, incorporating cost estimation, incremental checkpointing, and empirical accuracy benchmarking against human-annotated ground truth.

**Before you start:** An authorized API key configured via environment variables ([Use a secret safely](beat:use-secrets)), and a dataset of unclassified records alongside a small annotated validation sample. Note that this exercise incurs API costs and transmits text records across external networks ([Costs](concept:costs), [Privacy and data handling](concept:privacy)).

## Background

Interactive chat interfaces are unsuited for processing hundreds or thousands of empirical records. Developing a dedicated script automates inference record-by-record, records structured responses, and allows interrupted runs to resume.

A production-grade batch classification script requires five engineering guardrails:
- **Strict output schemas:** Require predictions as structured JSON matching a predefined enum list to eliminate parsing ambiguity.
- **Dry-run cost estimation:** Test prompt formatting on a minimal sample and compute total projected cost before running full-scale processing.
- **Resilient checkpointing and rate limiting:** Persist results incrementally to disk after each batch, incorporating exponential backoff to handle API rate limits.
- **Empirical accuracy measurement:** Evaluate model classifications against a human-annotated ground truth sample to quantify precision, recall, or accuracy.
- **Reproducible provenance tracking:** Record the model identifier, temperature, prompt text, and execution timestamp alongside output predictions.

## General methodology

Direct the agent to write a batch classification script supporting dry-run estimation, incremental checkpointing, and rate limiting:

```text
Write a batch classification script, scripts/classify_notes.py, that reads <records file> and prompts <API endpoint> to assign exactly one label from: <label categories>.
Ensure responses return as valid JSON.
Write classifications incrementally to <out/labels.csv> so interrupted runs can resume without reprocessing existing records.
Incorporate exponential backoff retries and polite delays between requests.
Support a --limit flag and a --dry-run flag that prints the initial prompt and calculates total projected token cost without executing API calls.
Record the model identifier and prompt template within the output metadata.
```

Execute the evaluation workflow:
1. Run `--dry-run` to inspect the assembled prompt and estimated token cost.
2. Run with `--limit 5` to inspect real API response formatting.
3. Establish a hard spending cap in your provider console and execute the full run.
4. Calculate classification accuracy against the annotated validation benchmark.

<!-- example -->

## Verification criteria

- **Verified dry-run output:** The `--dry-run` command printed a valid prompt structure and an accurate token cost calculation.
- **Incremental state persistence:** Output records save incrementally, and restarting an interrupted run resumes from the last processed index.
- **Empirical classification metrics:** Accuracy or F1 scores are calculated and reported against the annotated validation sample.
- **Credential security:** The API key is injected via environment variables and never printed to logs or output tables.

## Common pitfalls

| Symptom | Underlying cause | Resolution |
|---|---|---|
| Unparseable response strings | Model generated conversational commentary alongside JSON | Direct the agent to use structured output mode or parse JSON using regex extractors |
| Cumulative cost exceeds projections | Prompt length increased or retries consumed additional tokens | Recompute projections from the initial 5-record pilot and enforce hard budget caps |
| HTTP 429 Rate Limit errors | Concurrency or request frequency exceeded provider quotas | Introduce exponential backoff retries (`time.sleep(2 ** attempt)`) |
