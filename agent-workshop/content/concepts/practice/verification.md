---
id: verification
title: Verification — check the evidence
short: Verification
themes: [recursive-ai]
related: [steering, outputs, version-control, scoping-work]
blurb: Language models can be confidently incorrect. Require empirical evidence, verify mathematical invariants, and use clean-context peer review to audit findings.
---

Researchers remain responsible for the scientific integrity of their published work. When collaborating with an agent, effective supervision requires maintaining an active verification posture: **"What assumptions could invalidate this result?"**

## The three levels of analytical validation

1. **Procedural alignment:** Did the agent execute the instructions you actually requested?
2. **Computational correctness:** Does the code correctly implement the mathematical formulas, cohort definitions, and statistical models?
3. **Substantive validity:** Is the formulated research question scientifically sound, and do the conclusions follow logically from the empirical data?

Agent automation accelerates levels 1 and 2, but level 3 remains the intellectual responsibility of the researcher.

## Characteristic agent failure modes

- **Silent data modifications:** Imputing missing values, trimming outliers, or deduplicating records without explicitly logging the changes.
- **Partial file inspection:** Inspecting only the initial dozen rows of a multi-gigabyte dataset while asserting conclusions about the entire cohort.
- **Hallucinated entities:** Generating fabricated bibliographic citations, non-existent dataset column names, or invented software API methods.
- **Confirmation bias (sycophancy):** Agreeing uncritically with leading questions or premature hypotheses proposed by the researcher.
- **Superficial completeness:** Reporting that an analysis is complete when script execution produced uncaught warnings or truncated outputs.

## Demand empirical evidence over conversational reassurance

Asking subjective questions such as *"Are you confident this is correct?"* typically triggers sycophantic reassurance (*"Yes, the calculation is verified"*). Instead, require checkable, objective evidence:

```text
Provide the terminal commands executed and the explicit sample sizes (denominators) behind every percentage.
Generate an audit table listing every excluded record, categorized by exclusion rule.
```

## A standard verification ritual

- **Verify mathematical invariants (Conservation of records):** Total raw records must strictly equal the sum of retained records and explicitly documented exclusions. Unreconciled counts indicate silent data drops.
- **Explicit denominators:** Ensure every proportion, percentage, or rate displays both the numerator and the active denominator.
- **Independent cross-checks:** Calculate key summary statistics using an orthogonal method (e.g., verifying a logistic regression odds ratio against a 2x2 contingency table calculation).
- **Rerun from clean state:** Execute the generated analysis script in a fresh shell to confirm that it runs end-to-end without interactive dependencies.

## Reviewing agent-generated code

Evaluating code does not require writing every line yourself. When reviewing an analytical script, focus on critical inflection points:

1. **Data ingestion:** Which source files and columns are loaded?
2. **Filtering criteria:** Which rows are dropped, and do the thresholds match the study protocol?
3. **Missing value policies:** Are missing entries omitted, imputed, or grouped into separate categories?
4. **Relational joins:** Are table merges one-to-one, one-to-many, or inner joins that silently discard non-matching keys?
5. **Output generation:** Which variables are exported, and are unit scales transformed correctly?

Ask the agent to explain any specific algorithmic block or mathematical operation that appears ambiguous.

## Peer review using a secondary agent

An agent that just completed an analysis carries its earlier assumptions throughout its active context window, making it poorly suited to audit its own code. 

To conduct an objective review, open a **separate session with a fresh context window** and instruct a second agent to adopt an adversarial auditing perspective:

```text
You are conducting an independent peer review of an analysis script.
Inspect <protocol.md>, <scripts/analyze.py>, and <out/results.md>.
Audit the script line by line against the protocol. List all discrepancies, unjustified assumptions, and unhandled edge cases in order of severity.
Do not modify any files.
```

Using a secondary agent provides an independent review unencumbered by prior conversation history, though researchers should note that foundation models from the same family may share underlying inductive biases.

## Calibrating verification to research stakes

Calibrate verification effort to the operational stakes of the work: exploratory data sketches require brief spot-checks, whereas analyses informing manuscripts, clinical protocols, or institutional policy demand full invariant accounting, code review, and independent peer review.

## Demo it

<!-- demos -->
