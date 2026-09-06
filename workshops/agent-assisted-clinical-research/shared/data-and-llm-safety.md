# Data and LLM safety boundary

This workshop is a software and research-methods exercise, not clinical decision support. The CheXpert Plus release and any derivatives remain governed by the applicable data-use agreement and institutional policy.

## Required handling rules

- Do not commit raw images, report text, metadata exports, model inputs, raw LLM requests/responses, credentials, signed URLs, or tokens.
- Use only the instructor-approved data location and LLM endpoint.
- Send only the minimum approved report fields to the LLM. Do not send images or identifiers for report abstraction.
- Keep raw endpoint interactions, intermediate datasets, checkpoints, and prediction-level results in ignored access-controlled paths.
- Do not turn absence of a mention into absence/resolution of a finding.
- Do not describe LLM-derived labels as ground truth or a resulting metric as diagnostic performance.
- Escalate uncertain data-use, endpoint, or privacy questions to the instructor rather than asking an agent to work around restrictions.

## Required scientific language

Use wording such as “report-derived weak pseudo-label,” “agreement with the frozen pseudo-label,” and “exploratory demonstration.” Avoid “diagnoses,” “detects disease,” “clinical accuracy,” “ground truth,” or causal claims unless an independently appropriate study supports them.

## Human-review boundary

An agent may implement an agreed cohort rule or data contract. It cannot determine that an ambiguous ordering field represents chronology, that a source is permitted for reuse, or that a clinically meaningful claim follows from a metric. Those require explicit evidence and human review.
