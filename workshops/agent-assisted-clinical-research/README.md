# From Data to Evidence with Research Agents

**A hands-on workshop in directing coding agents through a small, auditable clinical-research workflow.**

> **Working question:** Can we take a protected longitudinal imaging dataset from unfamiliar API to a cautious written result—using agents for most of the engineering while retaining human control of the scientific decisions?

Participants use an approved CheXpert Plus workspace and a local/institutionally approved LLM endpoint to build real, small research artifacts. They do not need to become machine-learning engineers, but they do need to learn how to frame a task, expose assumptions, inspect evidence, and steer an agent when its first answer is inadequate.

## What participants will learn

This workshop teaches a practical research-agent loop:

1. **Give an agent usable context** without manually re-explaining data locations, access mechanisms, scientific definitions, and safety boundaries.
2. **Turn a broad goal into a verifiable artifact**—a CLI, cohort manifest, LLM data-abstraction pipeline, local annotation tool, baseline model, or results report.
3. **Ask an agent to inspect before it acts.** A table/field name is a hypothesis, not a fact; endpoint and source schema need inspection.
4. **Detect and correct a consequential assumption.** A previous Report2Delta cohort used report-order adjacency as chronology; roughly half of parseable pairs were inverted. Participants learn why executable code can still implement an invalid study.
5. **Use LLMs as constrained data-abstraction tools,** with fixed configuration, provenance, raw-response retention, abstentions, and validation—not as unexamined ground truth.
6. **Build modest, reproducible models.** The emphasis is patient-disjoint splitting, validation-based selection, a locked test set, and calibrated claims rather than a large neural network or a high score.
7. **Write results that match the evidence,** including reproducible figures/tables, LaTeX, verified citations, and limitations.

The durable skill is not copying a particular prompt. It is learning how to communicate purpose, constraints, evaluation, and uncertainty so an agent can create work that a researcher can review.

## What the workshop does—and does not—claim

The examples use longitudinal chest-radiograph studies and radiology-report impressions. LLM outputs are **report-derived weak pseudo-labels**. Any model metric measures agreement with those labels on held-out patients. It does **not** establish clinical ground truth, diagnostic performance, clinical utility, or readiness for care.

This is deliberately part of the lesson: agents make it easy to create sophisticated-looking results; researchers must still define the task, protect data, test assumptions, and state limitations honestly.

## Workshop path

Each exercise contains one participant-facing [`AGENT_CONTEXT.md`](01-data-discovery/AGENT_CONTEXT.md). It is a compact project brief the participant can ask an agent to read. It supplies the facts that would otherwise be tedious to dictate repeatedly, but it does not prescribe a ready-made prompt or implementation.

| Stage | What the agent creates | What participants practice | Approx. time |
|---|---|---|---:|
| [01. Safe data discovery](01-data-discovery/AGENT_CONTEXT.md) | A bounded data-discovery/export CLI | Inspecting an unfamiliar API; controlling cost, scope, credentials, and overwrite risk | 15 min |
| [02. Chronological cohort curation](02-cohort-curation/AGENT_CONTEXT.md) | An auditable prior/current manifest | Challenging a field-name assumption; date provenance; patient-disjoint partitions | 20 min |
| [03. LLM report abstraction](03-report-abstraction/AGENT_CONTEXT.md) | A resumable extraction/validation workflow | Schemas, evidence quotes, abstentions, provenance, raw artifacts, and retry semantics | 25 min |
| [04. Local annotation tool](04-annotation-tool/AGENT_CONTEXT.md) | A single-file HTML review UI | Requesting a narrow, inspectable tool instead of an unnecessary web platform | 15 min |
| [05. Simple modeling](05-modeling/AGENT_CONTEXT.md) | A validation-selected, locked-test baseline | Preventing leakage; masked labels; reproducible selection and evaluation | 20 min |
| [06. Results and writing](06-results-and-writing/AGENT_CONTEXT.md) | Figures, LaTeX, and BibTeX | Traceability, claim calibration, reproducible reporting, and limitations | 15 min |

A full run is roughly **110 minutes**. For a shorter session, run stages 01–03 live and demonstrate the remaining stages from the instructor guide.

## Participant workflow

For each stage:

1. Read the stage’s `AGENT_CONTEXT.md`.
2. Write a request in your own words. A useful opening is: “Read this context, inspect the workspace before making assumptions, propose an approach and risks for my review, then implement and validate the requested artifact.”
3. Review the agent’s plan before it makes consequential choices.
4. Ask it to implement, run relevant checks, and report created paths, commands, evidence, assumptions, and remaining limitations.
5. Inspect the output and steer a revision when a test or audit exposes a problem.

The agent can read the context and do substantial work. The participant’s job is to decide whether the request, assumptions, evidence, and conclusion are fit for purpose.

## Instructor guide and answer keys

The complete teaching guide is included in [`instructor-guide/`](instructor-guide/). Each answer key contains the learning point, suggested live flow, expected artifacts/evidence, a reference prompt, common failure modes, recovery language, and reference-material locations.

This supports two workshop styles:

- **Work-along:** participants attempt a stage with their own agent; the instructor then projects the answer key and compares approaches.
- **Demonstration/review:** the instructor follows the key live while audience members watch, inspect the resulting artifacts, and ask questions.

### Important: sharing answer keys vs. preventing agent access

Because the guide is in this repository, an agent working in this checkout can read it. That is appropriate when you want answer keys available to participants or want to demonstrate the recommended path.

When you want independent agent work, create a participant-only copy **before** launching cloud sessions:

```bash
bash tools/make-participant-copy.sh /path/to/participant-workshop
```

This copy excludes `instructor-guide/`. Give participants/agents only that directory; retain the full checkout for the instructor. Do not rely on a hidden/dot folder as a boundary—if an agent can access it, it can read it.

## Required cloud setup

The instructor prepares the cloud environment before the session:

- a documented, approved CheXpert Plus data mount or tested per-user download route;
- enough storage and a writable participant project directory;
- Python 3.12+, `uv`, and the required data-science/data-client packages;
- an approved OpenAI-compatible LLM endpoint exposed through:

  ```bash
  WORKSHOP_LLM_BASE_URL
  WORKSHOP_LLM_API_KEY
  WORKSHOP_LLM_MODEL
  ```

- endpoint/data-access instructions appropriate to the deployment, with no secret values written into this repository;
- a small prepared feature resource for the CPU-fast modeling stage, or an explicit plan to precompute it;
- a TeX installation if live PDF compilation is desired.

Participants can run the neutral preflight helper:

```bash
bash tools/preflight.sh
```

It verifies command availability and whether required variable *names* are set; it never prints a credential value.

## Suggested instructor run-of-show

1. **Frame the problem (5–10 min).** Explain that the outcome is an auditable research workflow, not a clinical AI result. Set data-handling and claim boundaries.
2. **Data discovery (15 min).** Show why “download the data” is a poor request. Have agents inspect first, then make a 10-row trial export.
3. **Cohort curation (20 min).** Reveal the temporal-ordering trap only after people have considered how they would pair studies. Use it to discuss how code can be correct relative to a wrong definition.
4. **LLM abstraction (25 min).** Build a ten-record, provenance-preserving run; inspect an evidence quote and an abstained/masked case. Stress that validation is structural, not clinical.
5. **Annotation (15 min).** Ask an agent for one standalone HTML file; open it directly and test local export.
6. **Modeling (20 min).** Select on validation, save a lock, then evaluate once on test. Prefer a small logistic-regression baseline over GPU training.
7. **Writing and reflection (15 min).** Generate a table/figure and methods/results draft; identify and revise overclaims.

Pause after every agent plan and every validation result. Those are the teaching moments—not just the code-generation interval.

## Repository layout

```text
01-data-discovery/AGENT_CONTEXT.md
02-cohort-curation/AGENT_CONTEXT.md
03-report-abstraction/AGENT_CONTEXT.md
04-annotation-tool/AGENT_CONTEXT.md
05-modeling/AGENT_CONTEXT.md
06-results-and-writing/AGENT_CONTEXT.md
instructor-guide/<stage>/ANSWER_KEY.md
tools/preflight.sh
tools/make-participant-copy.sh
```

`tools/` contains only setup/distribution helpers. The primary artifacts are intentionally not prebuilt: participants ask agents to create them. The instructor guide may point to private sandbox/reference artifacts for comparison after an attempt.

## Data, privacy, and scientific boundaries

- Follow the applicable CheXpert Plus data-use agreement and institutional policy.
- Do not commit raw reports/images, metadata exports, derived predictions, raw endpoint logs, credentials, signed URLs, or tokens.
- Send only the minimum approved text to the LLM endpoint; do not send images or direct identifiers for report abstraction.
- Keep protected data, model checkpoints, raw responses, and annotation exports in ignored access-controlled storage.
- Do not force an absent or uncertain report finding into a negative/change label.
- Escalate access, privacy, or data-use uncertainty to the instructor. Do not ask an agent to bypass a restriction.

## After the workshop

A successful workshop leaves participants with more than code: they have examples of what a good agent brief looks like, how to request evidence and validation, when to stop an agent, and how to translate a complex research task into reviewable stages. The same pattern transfers to registries, laboratory data, chart abstraction, imaging studies, surveys, and other research workflows.
