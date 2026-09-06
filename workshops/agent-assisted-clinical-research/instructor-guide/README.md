# Instructor guide — From Data to Evidence with Research Agents

This guide supports the instructor during a live workshop and is intentionally more prescriptive than the participant-facing `AGENT_CONTEXT.md` files. It provides suggested live flow, an example request, expected artifacts, common agent errors, and recovery language for each stage.

## How to use this guide

1. Before the workshop, review the six answer keys and prepare the actual data path, endpoint configuration, feature resource, and reference artifacts named in them.
2. During a **work-along** session, let participants formulate and try their own request first. Then project the relevant answer key to compare scope, safeguards, and validation.
3. During a **demonstration** session, follow the suggested live flow and use the reference prompt as a compact backup when the agent needs steering.
4. Keep private data, secrets, and protected sandbox artifacts outside this repository. The guide names their purpose; it does not redistribute them.

## Teaching principle

Do not turn the workshop into a race to reproduce a reference prompt. Stop at three moments in every stage:

- **Before implementation:** What has the agent inspected? Which decision remains human-owned?
- **After implementation:** What artifact was created, and how can it fail?
- **After validation:** What does the evidence establish—and what does it not establish?

## Exercise keys

| Stage | Answer key | Primary teaching moment |
|---|---|---|
| 01 | [Safe data discovery](01-data-discovery/ANSWER_KEY.md) | Scope and inspect before export |
| 02 | [Chronological cohort curation](02-cohort-curation/ANSWER_KEY.md) | An invalid temporal definition can survive correct code |
| 03 | [LLM report abstraction](03-report-abstraction/ANSWER_KEY.md) | Provenance/masking make weak labels auditable, not true |
| 04 | [Local annotation tool](04-annotation-tool/ANSWER_KEY.md) | A narrow one-file tool can be a sound research artifact |
| 05 | [Simple modeling](05-modeling/ANSWER_KEY.md) | Validation selection and test locking beat unnecessary complexity |
| 06 | [Results, LaTeX, citations](06-results-and-writing/ANSWER_KEY.md) | Claims and citations must be traceable to evidence |

## Distribution modes

This repository includes answer keys so it can be freely shared and used for post-workshop review. If participants should independently direct their agents without answer-key access, make a participant-only distribution before launching cloud sessions:

```bash
bash tools/make-participant-copy.sh /path/to/participant-workshop
```

Use the full checkout yourself and mount only the generated copy into participant sessions. A dot directory is not a security boundary.
