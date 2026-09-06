# Acceptance: baseline modeling

Run the agent-created train/select command, then a separate locked-test evaluation command.

## Required checks

- A pre-training summary reports label support and unique patients by partition.
- Program fails if a patient appears in multiple partitions.
- A development-only preprocessing test/documentation demonstrates no fit on validation/test rows.
- `selection-lock.json` exists before the locked-test command runs and contains the selected candidate based on validation metrics.
- Output metrics include coverage/support, balanced accuracy, macro-F1, and a labeled confusion matrix.
- Test predictions are stored in an ignored location; aggregate metrics can be retained as appropriate to the data agreement.
- Changing a validation-only candidate must require a new selection record; the code must not silently overwrite a prior locked evaluation.

## Review questions

- What made it impossible or at least conspicuous to tune on the test set?
- Does the selected target have enough support for an interpretable demonstration?
- Is every result described as pseudo-label agreement rather than clinical performance?