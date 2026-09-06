# Contract: results and LaTeX report

## Required artifacts

- A reproducible command or script that reads saved aggregate metrics/predictions and writes a table-ready file plus at least one figure.
- A `methods-results.tex` document that compiles with the workshop’s available TeX toolchain, or clear compilation instructions if TeX is not installed.
- A `.bib` file containing only verified source metadata.

## Required content

- Scope/status statement: exploratory weak-supervision demonstration, not clinical validation.
- Cohort and temporal-ordering rule; patient-disjoint split and locked-test policy.
- Abstraction schema/provenance and masking rules.
- Exact selected baseline and selection metric.
- Metric values with support/coverage and explicit label semantics.
- At least two concrete limitations.

## Prohibited content

Do not claim diagnosis, disease detection, clinical validity, clinical utility, ground truth, causality, or statistical significance absent a suitable prespecified analysis and evidence. Do not make up citations, author lists, confidence intervals, p-values, or results unavailable in saved artifacts.