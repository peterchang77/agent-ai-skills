# Model-Selection Decision

## Task and consequences

Create a draft data-quality report from a small fictional CSV. A wrong finding could mislead a report owner, so the result requires inspection and human review before use.

## Input size and privacy

The fixture is small and fictional. A real workflow may contain sensitive data, so it must use an organization-approved provider or local setup.

## Desired qualities

Use a model with reliable file/tool use and enough reasoning to follow explicit rules. Favor a faster, lower-cost option for well-bounded first-pass checks; use a stronger option for ambiguous interpretation only with review.

## Validation and review

Compare the agent result to `scripts/check_survey.py`, review the source and output paths, and have a person approve any interpretation or distribution.

## Reconsider if

Choose a different model or process if tool results are unreliable, inputs exceed available context, privacy requirements change, or the task becomes more ambiguous.
