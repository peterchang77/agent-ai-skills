# Orientation: directing an agent without pre-solving the task

## Your role

You are the research lead. The agent can inspect files, query approved endpoints, write code, run tests, and explain evidence. You decide the scientific question, what data may be used, the definition of success, and whether the result is credible.

A productive cycle is:

1. Read the task brief and contracts.
2. Write a first request in your own words.
3. Ask the agent to inspect the workspace before implementing assumptions.
4. Request an implementation and the most relevant validation.
5. Review artifacts and evidence, then steer a revision if needed.

Do not ask the agent to “build the whole pipeline” in one unbounded request. Do ask for a concrete artifact, constraints, and a way to verify it.

## Prompt review questions

Before sending a request, can you answer these?

- **Outcome:** What file, command, UI, or analysis should exist at the end?
- **Context:** Which supplied data, endpoint, and contracts govern the task?
- **Boundaries:** What must not be sent, overwritten, inferred, or claimed?
- **Decisions:** Which choices should the agent propose versus which are fixed?
- **Verification:** What commands, checks, or manual review will demonstrate success?
- **Stopping point:** What should the agent report rather than silently expanding scope?

## Workshop scientific frame

The exercise studies report-derived change between a prior and current chest radiograph. The LLM may create weak labels from text; later image models are evaluated for agreement with those labels. The work does not establish diagnostic accuracy, clinical validity, or clinical utility.

The cohort must meet these non-negotiable conditions:

- each transition links studies from the same patient;
- `prior_date < current_date` is demonstrated, not inferred from a row/order field;
- development, validation, and locked-test partitions are patient-disjoint;
- the test partition is not used to choose target, feature set, hyperparameters, or model;
- protected data and credentials remain outside Git.

## Suggested request structure

Write prose, not a magic template. A complete first request often has five parts:

> Inspect the supplied contracts and existing workspace first. Create **[deliverable]** for **[goal]**. Use **[approved inputs]** and obey **[fixed constraints]**. Before making discretionary scientific choices, summarize options and recommend one. Validate with **[required checks]**. Do not claim **[excluded claim]**; report limitations and paths of created artifacts.

The reference prompts are deliberately hidden from the normal exercise sequence. Use them only after you have attempted a task: [`../reference-prompts/`](../reference-prompts/).
