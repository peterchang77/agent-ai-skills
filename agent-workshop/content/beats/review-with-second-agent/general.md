---
role: review-with-second-agent
title: Review the analysis with a fresh second agent
kind: detour
summary: Commission an independent peer review of scripts and findings using a secondary agent session with a clean context window.
time: 6 min
teaches: [verification, context, recursive-ai]
needs: [analyze-pilot]
---

In this exercise, you commission an independent code and methodological review by launching a second agent session with a clean context window. Unburdened by the assumptions and conversational momentum of the session that generated the analysis, a fresh agent evaluates artifacts with greater objectivity, catching edge cases and undocumented assumptions.

**Before you start:** A completed analytical milestone persisted as local files: an analysis script, input data, and a results summary ([Setup](setup:restore-a-starting-point)).

## Background

The agent session that authored an analysis is structurally ill-suited to audit its own code: its context window retains earlier conversational turns and reasoning steps, creating confirmation bias that favors its own assumptions.

Launching a **new session** eliminates this history entirely. The secondary agent evaluates only the persisted files on disk, acting as an independent peer reviewer encountering the codebase for the first time ([Context](concept:context)).

Frame the review request as an **adversarial error audit** rather than a confirmation check. Inquiring *"Does this look correct?"* induces sycophantic agreement. Furthermore, recognize model limitations: because models from the same architecture family can share similar reasoning biases, a clean secondary review lowers risk but does not replace human domain oversight ([Verification](concept:verification)).

## General methodology

Initialize a clean agent session in the project directory, directing it to audit persisted files without granting conversational background:

```text
You are an independent peer reviewer auditing an empirical analysis.
Inspect <protocol file>, <scripts/analyze.py>, and <out/results.md>.
Audit the script line by line against the protocol specification.
Identify computational errors, unstated assumptions, and claims in the narrative that are not supported by empirical estimates.
Do not modify any files.
Present your findings as a prioritized list ordered by potential impact on study conclusions, providing line-specific evidence for each issue.
```

Review the resulting critique carefully. Secondary reviewers can also propose false positives; evaluate whether each flagged issue represents a substantive methodological defect before taking action.

<!-- example -->

## Verification criteria

- **Evidence-backed critiques:** Every critique cites a specific line of code, formula, or table value.
- **Human evaluation:** Flagged concerns are reviewed and confirmed by the researcher before altering analytical code.
- **Read-only execution:** The secondary review session produced an evaluation report without modifying repository files.

## Common pitfalls

| Symptom | Underlying cause | Resolution |
|---|---|---|
| Superficial review ("Analysis looks sound") | Prompt requested confirmation rather than an adversarial audit | Direct the agent: *"Identify at least three potential sources of bias, unhandled edge cases, or model limitations"* |
| Excessive trivial formatting critiques | Prompt failed to require prioritization | Instruct the agent: *"Rank the top three issues most likely to invalidate study conclusions"* |
| Agent rewrites the analysis autonomously | Prompt lacked explicit write prohibitions | Re-issue command: *"Provide review notes only; do not modify any files"* |
