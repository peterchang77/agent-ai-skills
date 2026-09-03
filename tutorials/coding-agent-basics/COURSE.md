# Course Guide: Directing Coding Agents Well

## The central idea

A coding agent can often complete a useful task from one capable request. Your job is not to direct every command or line of code. Your job is to state the outcome and important boundaries, recognize decisions that change the result, ask for a plan or recommendation when needed, and inspect evidence before accepting or revising the work.

```text
outcome → plan and options → meaningful decisions → execution → evidence → revision
```

When work becomes unclear, slow, expensive, repetitive, or hard to explain, do not brute-force the current path with repeated “try again” prompts. Pause and ask the agent to explain the terrain, propose alternatives, and recommend the simplest trustworthy route.

## The basic mental model

A **coding agent** is an AI assistant that can work in an approved environment. Unlike ordinary text-first chat, it can often inspect real files, use command-line tools, write and run code, create outputs, and check what happened.

```text
You → coding agent → model ← provider
             ↓
      files, tools, code, libraries, and services
```

- A **model** is the language-and-reasoning engine.
- A **provider** supplies authenticated access to a model.
- A **coding agent** connects the model to a workspace and concrete actions.
- **Tools** perform operations such as searching, converting, testing, or extracting data.
- **Libraries** are reusable code used inside a program.
- **Files** retain results, decisions, scripts, templates, and instructions beyond the current conversation.
- **You** remain responsible for goals, priorities, interpretation, and approval of consequential actions.

For a multi-row CSV, an agent may use Python and an existing checker rather than reason over each record in chat. For document conversion, it may use an installed command-line tool rather than build a parser from scratch. Mature tools often reduce effort and edge cases, but still need to fit the data, permissions, and intended output.

## What you decide and what the agent decides

An agent can usually choose routine means: sensible filenames, ordinary code structure, an installed parser, a CSV library, or a basic validation command. It should surface choices that materially affect value or risk:

- audience and output format;
- scope, source treatment, and interpretation rules;
- privacy, permissions, external access, or publication;
- cost, time, scale, and model capability;
- whether a workflow should become repeatable.

You never need to know the right answer before asking. A strong request is often:

> “What are the practical options, what are the trade-offs, and what do you recommend for my situation?”

Give the context that affects the answer—audience, need to revise, sensitivity, expected scale, budget, timing, and existing conventions—then approve or redirect the recommendation.

## Scope changes the kind of work

One PDF versus 10,000 PDFs, one email versus an inbox, or one Markdown draft versus a polished Word deliverable are not merely tasks of different duration. Larger, more complex work needs a different route.

```text
effort ≈ number of items × work per item + coordination + output complexity + risk
```

A direct task may be read or processed once. A workflow may require inventory, batching, extraction, failure handling, storage, sampling, validation, and a reproducible record. Before uncertain or large work, ask for a scoped plan:

> “Before processing anything, inventory the work, identify resource drivers and risks, propose stages and existing tools, and ask me only for decisions that materially affect the result.”

The agent should give relative planning information rather than invented precision: small/moderate/large, likely bottlenecks, proposed stages, approval points, and what a check can or cannot prove.

## Avoid brute-force agent use

Repeatedly prompting “fix it,” “make it better,” or “try another approach” can produce a short-term result. Over time, it can accumulate:

- **result debt:** a plausible output that misses the real goal;
- **knowledge debt:** assumptions and decisions trapped in a chat;
- **reproducibility debt:** no reliable way to rerun the work;
- **technical or operational debt:** fragile patches or a process that fails at scale;
- **cost and trust debt:** expensive retries or outputs accepted without appropriate evidence.

Pause and reset when you see repeated fixes without convergence, unclear assumptions, growing scope, unnecessary custom work, a task that will recur, or weak evidence for the stakes. Useful prompts include:

- “Step back: why is this difficult, what alternatives exist, and which do you recommend?”
- “What tools, scripts, libraries, or project conventions can we reuse?”
- “How would this approach change if the collection were 100 times larger?”
- “How did you verify this, and what does that verification not prove?”
- “What is the smallest thing worth keeping so this can be rerun next month?”

## The practice mission

The fictional reporting project provides a safe place to use this loop. Start with a broad capable request, inspect the plan, ask for options and a recommendation, contrast it with a larger-scale version, then inspect and revise the resulting report. A script, template, project instruction file, skill, or handoff is optional: retain it only when recurrence, transfer, or deterministic checking makes it valuable.

## Suggested routes

- **Foundation:** use the fictional project and explain tool choices after the agent acts.
- **Practitioner:** move quickly through familiar concepts and focus on judgment, trade-offs, and evidence.
- **Technical transfer:** set success criteria and challenge tool/architecture choices; use the agent to expose unfamiliar environment details.
- **Goal-first:** substitute a safe work-shaped project and use each lesson when its decision point appears.

## Static reading route

Read the five modules in order. At each “Your move,” draft what you would ask an agent. Compare it to the agent behavior described in the module, then inspect the safe sample project if useful. The goal is to practice navigation and judgment, not memorize a prompt template.
