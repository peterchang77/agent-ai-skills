# 05 — Build and evaluate a simple model

## Learning goal

Have an agent build a small, reproducible baseline while keeping model selection separate from final held-out evaluation. This is an exercise in experimental discipline, not maximizing a metric.

Read [`CONTEXT.md`](CONTEXT.md), [`CONTRACT.md`](CONTRACT.md), and [`ACCEPTANCE.md`](ACCEPTANCE.md). First ask the agent to inspect the prepared manifest/features and report class counts by partition. Then write your own request for implementation.

## Deliverable

Create commands that train a CPU-fast baseline for the preselected target, choose any adjustable setting using validation only, save a selection record, evaluate the selected model once on `test_locked`, and write metrics plus a confusion matrix.

The instructor selects the target before the workshop from development/validation evidence. Do not choose it because it is best on the locked test set. The default teaching target is one three-state (`better`, `same`, `worse`) report-derived outcome with sufficient support in the prepared cohort.

## Recommended scale

Use precomputed image embeddings/features or a compact tabular representation and a regularized multinomial logistic regression. Do not spend workshop time training a CNN, performing broad hyperparameter sweeps, or adding multiple targets unless the instructor explicitly changes scope.

## Recovery

After an attempt, use [`../reference-prompts/05-modeling.md`](../reference-prompts/05-modeling.md) to compare the scope and safeguards in your request.