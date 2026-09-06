# Agent context: 05 — Simple weak-label model with a locked test set

## Assignment

Create a CPU-fast, reproducible training/selection/evaluation workflow for the instructor-preselected single report-derived three-state target. First inspect the prepared manifest/features and report class support and unique patient counts by frozen partition. Then propose a small modeling plan suitable for the available data; do not create a broad deep-learning project.

## Scientific background

Labels are weak pseudo-labels created from reports. The selected outcome uses `better` (improved/resolved), `same` (stable), and `worse` (new/worsened). A row without a usable target is masked and must be excluded from that concept’s training/evaluation—not recoded as a negative class.

The task measures agreement between image-derived/precomputed features and report-derived pseudo-labels. It does not measure diagnostic accuracy, clinical validity, clinical utility, or causality.

## Available resources

- The cloud workspace provides a compact feature table (for example, precomputed image embeddings) and a frozen manifest from prior exercises.
- Partitions are patient-disjoint and named `development`, `validation`, and `test_locked`.
- Use an instructor-selected outcome based on pre-workshop development/validation review. Do not select it from locked-test results.
- Work in ignored `outputs/` or `data/derived/` paths for protected predictions/models.

## Required outcome

Implement commands that verify unique transition IDs and patient-disjoint partitions; fit preprocessing, encoders/imputers, and class weighting only on development; train a simple baseline such as regularized multinomial logistic regression; evaluate a small declared candidate set on validation; and save a selection record before reading locked-test labels.

`selection-lock.json` must include input fingerprint/version, target, candidate definitions, selection metric, selected configuration, seed, and validation metrics. A separate locked-test command must evaluate the selected model once and save protected prediction-level outputs plus aggregate metrics. Report masked-label coverage/support, balanced accuracy, macro-F1, and an explicitly ordered confusion matrix. Stop with a clear explanation if development/validation support is inadequate.

## Boundaries

Do not tune on `test_locked`, fit preprocessing on validation/test data, impute masked labels, perform a GPU/CNN training project, silently overwrite a previous selection/evaluation, or describe metrics as clinical performance.

## Definition of a credible result

A reviewer can verify patient exclusivity, reproduce validation selection with the recorded seed, see a selection lock predating test evaluation, trace all metrics to saved outputs, and understand that the metric is pseudo-label agreement.
