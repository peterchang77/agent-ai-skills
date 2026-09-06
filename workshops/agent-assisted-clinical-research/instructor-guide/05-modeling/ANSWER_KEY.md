# Instructor answer key — 05 Modeling

## Teaching point

The discipline of selection and evaluation matters more than model complexity. The workshop model should run quickly and make it evident that test outcomes were not used to select it.

## Suggested live flow

1. Instruct agents to inventory feature schema, target support, and unique patient counts before coding.
2. State that the target was selected before workshop from development/validation—not from test.
3. Ask the agent for a small candidate plan (for example regularization values/current vs paired feature representation).
4. Run development/validation selection and inspect `selection-lock.json` before any locked test command.
5. Run one test evaluation; inspect aggregate metrics and limits.

## Expected artifact and evidence

- CPU-fast baseline, typically regularized multinomial logistic regression on prepared features.
- Patient/transition integrity checks and development-only preprocessing/weights.
- Small declared validation grid; `selection-lock.json` with target/candidates/metric/seed/validation evidence before test.
- Separate test command with protected predictions and aggregate coverage, balanced accuracy, macro-F1, labeled confusion matrix.

## Reference prompt

> Read the context and inspect input support/partition integrity first; stop if inadequate. Build a CPU-fast masked three-state baseline with development-only preprocessing, small declared validation candidates, validation selection, and a selection-lock file written before separate one-time locked evaluation. Enforce patient exclusivity and preserve protected predictions. Report support, coverage, balanced accuracy, macro-F1, confusion matrix, commands, evidence, and limitations. Do not use test labels for selection or call metrics clinical performance.

## Common errors and steering

- **Reads test labels during model selection:** split commands/configuration and require pre-test lock timestamp/content.
- **Row-level leakage:** assert grouped patient partitioning.
- **Includes masked labels as negative:** show target counts and require explicit mask handling.
- **Huge model sweep/CNN:** restate CPU-fast small candidate budget.
- **No support caveat:** stop when class support makes metric uninformative.
- **Reruns test until better:** preserve immutable run/lock paths and explain one declared test shot.

## Reference materials

Use sandbox modeling log/methods only to show the concept after participant work. It is too complex for the participant’s initial baseline implementation.
