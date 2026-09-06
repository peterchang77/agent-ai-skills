# Agent context: 06 — Results analysis, LaTeX, and citations

## Assignment

Create reproducible analysis artifacts from saved model outputs: a table-ready metrics file, at least one labeled figure, a concise LaTeX methods/results document, and a BibTeX file with verified citations. Inspect the actual available result artifacts and TeX toolchain before writing. Do not invent missing results, statistics, or references.

## Scientific background

This is an exploratory weak-supervision demonstration. It evaluates a simple model’s agreement with report-derived LLM pseudo-labels on held-out patients. It is not clinical validation. The report must distinguish temporal/cohort validity, structural label validation, model selection on validation, and final locked-test evaluation.

A useful methods description states the data/source version, demonstrated prior/current ordering, patient-disjoint partitions, fixed report-abstraction contract, label masking, selected baseline, selection rule, and test policy. Results should report support/coverage and explicitly name the metric’s target.

Concrete limitations can include: pseudo-labels are not clinical ground truth; report comparison language may not refer to the supplied image prior; small cohort support/uncertainty; and an agreement metric does not establish clinical utility.

## Available resources

- Use only saved output artifacts from exercise 05 and supplied source metadata.
- The sandbox’s dataset source is CheXpert Plus, Stanford AIMI, version 1.0, DOI `10.57761/fzna-pm76`. Verify bibliographic fields from an instructor-provided trusted source or citation fixture before adding BibTeX; do not make them up.
- Use the TeX command/toolchain actually available in the workspace, if any.

## Required outcome

Create scripts/commands that regenerate the metrics table and figure from saved artifacts. Create `methods-results.tex` and `references.bib`; compile when a TeX toolchain is available and inspect the log for missing figures/references. Each numeric result in prose must trace to a saved result file. State at least two specific limitations.

Use precise language: “report-derived weak pseudo-label,” “agreement,” “held-out patients,” and “exploratory demonstration” are appropriate. Avoid calling it diagnostic accuracy, clinical performance/utility, ground truth, disease detection, causal proof, or statistical significance unless the saved prespecified analysis actually supports the claim.

## Boundaries

Do not invent missing results, statistics, confidence intervals, p-values, or citations; do not call the work clinical validation, diagnostic performance, ground truth, disease detection, causal proof, or statistical significance without corresponding saved prespecified evidence.

## Definition of a credible result

A reviewer can regenerate the figures/table, map every reported number and citation to its source, compile/read the document, and see both the result and its limitations clearly.
