# Context: weak-label baseline

The prepared modeling data derives one three-state label from the report-abstraction output: `better` (improved/resolved), `same` (stable), or `worse` (new/worsened). It is a masked weak label: rows without a usable label for the selected concept must be excluded from that concept’s training/evaluation rather than relabeled negative.

Use feature data supplied by the workshop. It may consist of precomputed image embeddings, current/prior representations, or another compact approved feature set. The task should complete on CPU in minutes. The exact feature extractor is not the teaching target.

The partition field is frozen and patient-disjoint: `development`, `validation`, `test_locked`. Fit preprocessing, class weights, and model parameters only from development. Select a variant or regularization strength using validation. Do not inspect/use locked-test labels until the selection record is saved.

The primary metric is balanced accuracy, with macro-F1, support, and a confusion matrix as useful secondary outputs. These measure agreement with LLM-derived report-change pseudo-labels; they are not diagnostic accuracy, clinical performance, or proof that imaging features cause the result.

If a target has inadequate development/validation support, the program should stop/report that fact rather than return an unstable metric.