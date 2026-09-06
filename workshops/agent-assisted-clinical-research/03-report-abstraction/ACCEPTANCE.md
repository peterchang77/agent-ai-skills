# Acceptance: LLM abstraction

Run a ten-transition smoke test before a larger job.

```bash
# Replace with agent-created commands and paths.
uv run python path/to/extract_changes.py --manifest data/derived/serial-manifest.parquet \
  --limit 10 --output-dir outputs/extraction-smoke
uv run python path/to/validate_changes.py --manifest data/derived/serial-manifest.parquet \
  --extraction outputs/extraction-smoke/structured.jsonl \
  --output data/derived/labels-smoke.parquet
```

## Required checks

- The output has one terminal record per submitted transition, including failures.
- Every structured record contains transition ID, endpoint model ID, prompt hash/version, timestamp, decoding configuration, and parsed result or error status.
- A second `--resume` run submits no completed records.
- Raw endpoint content is written only under an ignored/protected path.
- The validator flags the deliberately invalid example for its stated reasons.
- Every usable label has a verbatim/normalized evidence quote in the **current** impression.
- No usable label is emitted for an uncertain statement, an abstention, or a bare negative falsely labeled resolution.

## Review questions

- Which information is retained to audit a disputed output?
- Does a retry change scientific content or only recover a failed call?
- Does the implementation distinguish structural validity from clinical validity?
