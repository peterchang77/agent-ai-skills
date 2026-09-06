# Acceptance: serial cohort

Run the cohort-builder on the assigned small prepared input. Then inspect the manifest and audit.

## Required checks

```bash
# Replace with the agent-created command.
uv run python path/to/build_cohort.py --input data/raw/metadata-trial.parquet \
  --output data/derived/serial-manifest.parquet --audit outputs/cohort-audit.json
```

The program must either produce a valid manifest or fail clearly; it must not emit a plausible-looking manifest with unverified chronology.

Confirm:

- all retained rows have `prior_date < current_date`;
- every patient maps to one partition only;
- `gap_days` is strictly positive;
- the audit counts excluded/unparseable dates and does not hide them;
- a deliberately inverted synthetic/fixture row causes rejection or exclusion;
- rerunning with the same seed produces the same split assignments.

## Review questions

- What evidence did the agent use to establish chronology?
- What happens to ambiguous same-day or multi-study cases?
- Can another researcher reconstruct exactly why a row was included or excluded?
