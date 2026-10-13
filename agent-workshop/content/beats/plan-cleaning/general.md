---
role: plan-cleaning
title: Plan the cleaning and make the judgement calls
kind: full
summary: Formulate an explicit data cleaning protocol separating deterministic syntactic repairs from substantive domain decisions before modifying data.
time: 7 min
teaches: [scoping-work, steering]
needs: [profile-data]
---

Data cleaning requires making methodological decisions that directly shape the research cohort. In this exercise, you use a structured planning step to evaluate cleaning options proposed by the agent, make necessary domain decisions, and document the resulting protocol in an auditable plan before modifying any data.

**Before you start:** A data-quality audit of your dataset ([Profile the data](beat:profile-data)), or a concise summary of known data anomalies.

## Background

Cleaning decisions fall into two distinct methodological categories:

- **Deterministic syntactic repairs:** Transformations with a single correct solution (e.g., trimming trailing whitespace, standardizing dates to ISO-8601, and eliminating exact duplicate rows). The agent can identify these and propose batch transformations for your approval.
- **Substantive methodological choices:** Decisions that alter cohort composition or the mathematical meaning of variables (e.g., imputing vs. dropping missing values, converting discordant measurement units, or establishing exclusion thresholds). The agent should **propose viable options along with their analytical consequences**, leaving the decision to the human researcher.

Enforcing a dedicated **planning phase** ensures this separation. Many agent harnesses support dedicated *plan modes* that restrict file edits until you explicitly approve the methodology ([Scoping work](concept:scoping-work), [Steering](concept:steering)).

## General methodology

Direct the agent to formulate a comprehensive cleaning protocol based on the profile audit, explicitly separating mechanical repairs from substantive methodological choices:

```text
Do not modify any files yet. Propose an explicit data cleaning protocol for <data file> based on the anomalies identified.
For each anomaly, detail viable handling options, downstream analytical implications, and your technical recommendation.
Group deterministic syntactic repairs together. Pause and solicit my guidance on substantive methodological choices rather than deciding them autonomously.
```

Review the proposals, select the preferred remediation rules, and instruct the agent to synthesize the final agreed rules into a concise document (`notes/cleaning-decisions.md`). Persisting this decision log ensures methodological choices outlive the active conversational session ([Memory](concept:memory)).

<!-- example -->

## Verification criteria

- **Clear decision categorization:** The proposed plan cleanly separates mechanical formatting fixes from substantive methodological decisions.
- **Explicit human steering:** The agent pauses to ask for guidance on ambiguous edge cases rather than making arbitrary assumptions.
- **Auditable documentation:** Every cleaning rule is recorded in `notes/cleaning-decisions.md` with an unambiguous operational definition.

## Common pitfalls

| Symptom | Underlying cause | Resolution |
|---|---|---|
| Agent executes edits during planning | Session was not configured in read-only plan mode, or prompt lacked explicit write prohibitions | Interrupt the run and restate: *"Do not modify any files; propose the plan only"* |
| Agent resolves substantive ambiguities autonomously | Prompt did not explicitly require options and trade-offs | Instruct the agent: *"List alternative methodological options for this issue and pause for my decision"* |
