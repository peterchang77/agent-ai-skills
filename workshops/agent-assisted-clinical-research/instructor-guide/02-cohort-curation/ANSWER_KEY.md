# Instructor answer key — 02 Cohort curation

## Teaching point

The most valuable result is discovery of a wrong scientific assumption. An agent can faithfully automate `patient_report_date_order` and still create a temporally invalid task. The human must demand evidence that “prior” precedes “current.”

## Suggested live flow

1. Have participants ask agents to inspect date-bearing fields and propose a chronology test before code.
2. Project the historical failure: named report order had near-zero date relation and about 48% inverted pairs in a parseable subset.
3. Ask what audit would have exposed this before modeling.
4. Direct implementation of a builder that parses/document dates, excludes ambiguity, assigns patient-disjoint partitions, and emits audit evidence.
5. Run a deliberately inverted fixture and a patient-leak check.

## Expected artifact and evidence

- Deterministic cohort builder and manifest with required prior/current/date/source/partition fields.
- Date parser/provenance and explicit exclusions, not date fabrication.
- Audit with parsing/exclusion counts, gap distribution, and unique patient/partition counts.
- Assertions showing strict positive gaps and zero patient leakage; repeatability from seed.

## Reference prompt

> Read the context and inspect the actual metadata. Before code, show the possible chronology sources and a test plan; do not infer time from an order field. Build a deterministic same-patient serial cohort retaining only documented `prior_date < current_date` pairs, preserving date source/exclusion reasons, deterministic image selection, and patient-disjoint frozen splits. Emit an audit and executable checks for inversions/leakage. Run on the small input and report evidence and unsupported assumptions.

## Common errors and steering

- **Uses report ordering:** ask for correlation/spot-check against actual parsed dates; reject if it cannot establish chronology.
- **Silently drops rows:** require exclusion-reason counts and retained row traceability.
- **Same-day ambiguity:** exclude unless a documented ordering source exists.
- **Random row-level split:** require grouping by patient and audit unique patient overlap.
- **Overambitious header parser:** constrain initial formats, record failures, and stop if adequate chronology cannot be shown.

## Reference materials

Use the sandbox `docs/report2delta-label-audit.md` to explain the failure and its repaired serial-v2 cohort only after an initial participant attempt. The cohort-builder implementation remains instructor-only.
