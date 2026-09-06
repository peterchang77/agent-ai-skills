# Contract: baseline training and evaluation

## Inputs

- Feature table with `transition_id`, patient ID, frozen partition, features, and the selected concept’s masked three-state label.
- A declared random seed.
- A small predeclared candidate set, for example logistic-regression regularization strengths or current-only versus paired-feature representations.

## Required training behavior

- Verify that each patient occurs in one partition and each input transition has a unique ID.
- Fit any scaler/imputer/encoder and class weights on development only.
- Train all candidates on development only and select by validation balanced accuracy.
- Write a `selection-lock.json` before reading locked-test labels. It records input fingerprint/version, target, candidates, metric, chosen configuration, seed, and validation metrics.
- Evaluate the selected model on `test_locked` once and write prediction-level outputs to ignored storage plus a shareable aggregate metrics artifact.

## Required reporting behavior

Report support/coverage, balanced accuracy, macro-F1, and a confusion matrix with explicit class order. State that labels are report-derived weak labels and that the test result is agreement with those labels.

## Out of scope

A GPU model, tuning on the test partition, cross-validation that violates patient grouping, imputation of masked labels, clinical claims, and repeated test shots chosen because results improved.