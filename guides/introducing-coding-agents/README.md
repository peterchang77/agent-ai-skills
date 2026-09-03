# Introducing Coding Agents

A coding agent can inspect files, use tools, write and run code, and leave a working project behind. That makes it more useful than ordinary chat for many tasks—and means it needs better direction and review.

This guide is for people who use data, documents, spreadsheets, reports, research, or software but do not need to be professional developers. Its goal is practical: help you get from a useful request to a result you can inspect, revise, and use responsibly.

> **Core loop:** state the outcome → assess scope, tools, and options → choose meaningful trade-offs → execute → inspect evidence → steer a revision.

A good agent interaction is not a contest to write the most detailed prompt. You provide the purpose, boundaries, and decisions that matter. The agent handles routine implementation work and shows enough evidence for you to review it.

## Contents

1. [The basic mental model](#the-basic-mental-model)
2. [Make a capable request](#make-a-capable-request)
3. [Decide what the agent should decide](#decide-what-the-agent-should-decide)
4. [Ask for options and tool rationale](#ask-for-options-and-tool-rationale)
5. [Match the approach to the scale](#match-the-approach-to-the-scale)
6. [Inspect evidence, then steer a revision](#inspect-evidence-then-steer-a-revision)
7. [Keep work reusable only when it earns its cost](#keep-work-reusable-only-when-it-earns-its-cost)
8. [Recover when the work is going badly](#recover-when-the-work-is-going-badly)
9. [A compact working pattern](#a-compact-working-pattern)

## The basic mental model

An **AI model** generates and interprets language, code, and other supported inputs. A **chat** usually responds with text in one conversation. A **coding agent** uses a model plus an operating environment: it can inspect project files, run commands, use installed libraries, edit files, run checks, and report what happened.

A useful simplified picture is:

```text
You: outcome, boundaries, decisions, review
          ↓
Agent: model + project files + tools + working memory
          ↓
Result: outputs + changes + evidence + unresolved questions
```

The agent is not just a text generator when it works in a project. Files can carry context between turns, tools can produce evidence, and a script can make a result repeatable. That capability is why ordinary chat habits are not always enough.

### Your job and the agent's job

You remain the decision-maker and reviewer. You are best placed to state:

- the outcome and who will use it;
- real-world context, definitions, and success criteria;
- privacy, source, approval, cost, and publishing boundaries;
- choices that change the meaning or use of the result; and
- whether the evidence is adequate for the intended decision.

The agent can normally choose routine means:

- how to inspect a folder or a file format;
- which existing project script, command-line tool, library, or convention to reuse;
- filenames, code structure, intermediate steps, and ordinary checks;
- how to summarize work and point to outputs.

This division avoids two unhelpful extremes: treating the agent as an unreviewed authority, or micromanaging every command before it can start.

### Tools and files are part of the answer

When an agent says it will use a tool, that should mean something concrete. For example:

- a CSV parser may be safer than manually copying spreadsheet rows;
- an existing project checker may be more reliable than a newly invented validation script;
- a command-line search can inventory thousands of files faster than opening them one by one;
- a version-control diff can show exactly what changed.

Ask the agent to explain a material tool choice in plain language: **what it does, why it fits this work, and what you should inspect afterward.**

## Make a capable request

A capable request gives direction without attempting to prescribe the whole implementation. It usually includes four things:

1. **Outcome:** what should exist or be true at the end?
2. **Context or audience:** who will use it and for what?
3. **Boundary:** what must not happen, or what needs approval?
4. **Evidence:** how should the result be checked or made reviewable?

For example:

> Create a concise Markdown report for a manager from the approved survey export in this project. First inspect the project instructions, notes, and existing tools, then propose a plan and explain the tool rationale. Preserve raw inputs, flag uncertain records instead of resolving them, and show the evidence behind the result.

This request does **not** specify every command, package, or filename. It tells the agent what matters and leaves it free to use ordinary judgment.

### A short request is often enough

Once you have established a standing boundary, you do not need to repeat it in every sentence. If you have already said “do not modify raw inputs,” then this is usually sufficient in context:

> Inspect that folder and tell me what existing checks we can reuse.

The agent should apply the established boundary. Add more detail only if the scope, audience, risk, or desired result has changed.

### Before substantial work: request a plan

For a task with uncertainty, new files, meaningful cost, or a consequential result, start with a plan rather than immediate execution:

> Before making changes, inspect the project and propose a plan. Include likely tools or existing resources, outputs, validation, assumptions, and decisions you need from me.

A useful plan distinguishes:

- what the agent can do directly;
- what it will inspect first;
- what evidence it expects to produce;
- assumptions it is making; and
- the few decisions that genuinely require your input.

## Decide what the agent should decide

Not every choice deserves a meeting. Good direction surfaces choices that alter the result, risk, cost, or future usefulness.

| Usually let the agent decide | Usually decide or approve yourself |
| --- | --- |
| routine file names and code layout | intended audience and report format |
| standard libraries and project conventions | interpretation of an ambiguous business rule |
| normal checks and implementation sequence | use of sensitive, private, or external data |
| an existing script versus a small helper | publishing, sending, deleting, spending, or connecting accounts |
| how to present a routine technical summary | scope, deadline, quality threshold, and what counts as success |

Ask for clarification when a choice changes the meaning, scope, safety, privacy, cost, or external effect of the work. Do not require a longer prompt merely because a shorter request used natural language.

A strong move is to ask for help choosing:

> What are the practical options here, what are the trade-offs, and what do you recommend for this situation?

That is not a lack of expertise. It is how you use the agent to make uncertainty visible before committing to a route.

## Ask for options and tool rationale

Agents often have several plausible ways to do the job. A short option set is more useful than a catalogue of every possibility.

Ask for:

> Give me two or three practical approaches. Compare their reliability, effort, repeatability, and review burden. Recommend one based on what you know, and say what assumption would change your recommendation.

For a report, common alternatives might be:

| Approach | Good fit | Trade-off |
| --- | --- | --- |
| One-off analysis in the project | a small, time-sensitive task | fast, but may need rework next month |
| Small script plus validation | a recurring input and stable rules | requires a little setup, but is easier to repeat |
| Existing project workflow or library | a project with established conventions | lower reinvention risk, but requires learning its boundaries |
| External service or new provider | a capability unavailable locally | may add cost, privacy, approval, and operational concerns |

The best answer often reuses what is already available. Before requesting custom code, ask:

> What existing tools, scripts, libraries, or project conventions can we reuse?

New code is not automatically bad. It should solve a real gap, not duplicate a reliable tool simply because starting from scratch feels more direct.

## Match the approach to the scale

A small, bounded task can often proceed directly. A large, uncertain, expensive, sensitive, or recurring task needs a different first move: **scope it before you execute it.**

Compare these requests:

> Check the six-row sample CSV for duplicate IDs and missing values, preserving the source.

> Extract and summarize information from 10,000 scanned documents by Friday.

The first may be safe to inspect and execute immediately. The second has unknown document quality, extraction accuracy, compute time, cost, privacy exposure, review requirements, and failure modes. Treating both as “just run it” is a common source of fragile work.

### Ask for an inventory and staged route

For larger work, use a request like:

> Before continuing, inventory the work and propose a staged approach. Identify the resource drivers, existing tools we can reuse, expected evidence, likely failure modes, approval points, and a recommended first slice.

A good staged plan might be:

1. inspect a representative sample and count file types;
2. test extraction on a small approved batch;
3. measure error patterns, cost, and human-review effort;
4. adjust the approach or stop if the evidence is inadequate;
5. process in batches only after approval; and
6. retain a reproducible record of inputs, settings, outputs, and exceptions.

### Use relative estimates, not invented certainty

An agent can often identify **drivers** of time and cost—number of files, file size, model calls, human review, retries, and external services—without being able to promise an exact number. Prefer statements such as “processing the whole collection is roughly thousands of times the work of the pilot, plus review overhead” over unsupported guarantees.

Ask:

> What would make this expensive, slow, or unreliable? What can we learn from a small pilot before we commit?

## Inspect evidence, then steer a revision

A result is not trustworthy merely because it looks polished. Review the evidence that fits the task.

For a data or reporting task, inspect some combination of:

- the exact source files or a record of their versions;
- row, file, or record counts before and after processing;
- exceptions, missing values, duplicates, and excluded items;
- assumptions and unresolved interpretations;
- generated outputs and the paths where they were written;
- validation commands and their results; and
- a diff or change summary when project files were modified.

Ask two complementary questions:

> How did you verify this?

> What does that verification **not** prove?

The first requests evidence. The second prevents a narrow technical check from being mistaken for a business, scientific, editorial, or approval decision.

### Revision is a normal part of directing the work

After reviewing the result, issue a clear revision that preserves the useful work:

> Keep the data-quality findings, but revise the executive summary for a nontechnical manager. Separate confirmed facts from records that need human review, and rerun the relevant checks afterward.

A good revision request says what should remain, what should change, and what evidence should be updated. It does not need to prescribe the code edit.

## Keep work reusable only when it earns its cost

Not every task needs an instruction file, automation script, reusable skill, handoff, or model-selection document. Those are useful when the cost of recreating context or redoing a step is greater than the cost of maintaining the artifact.

| Situation | Smallest durable asset worth considering |
| --- | --- |
| stable project rules or safety boundaries | concise project instruction file |
| recurring deterministic transformation or check | script with a clear input/output contract |
| recurring document or report format | template |
| recognizable multi-step workflow used across tasks | focused reusable procedure or skill |
| work that will pause or transfer to another person | short handoff with status, evidence, and next step |
| a consequential model/provider choice | decision note with capability, cost, privacy, and fallback rationale |

Ask:

> How would we reproduce this result next month?

Then ask a second question:

> What is the smallest thing worth keeping, if anything?

For a one-off task, “nothing beyond the final report and its evidence” can be the correct answer. Reuse should reduce future friction, not create ceremony.

## Recover when the work is going badly

Repeatedly telling an agent “try again” can sometimes fix a simple error. Repeated retries without a clearer model of the problem create several kinds of debt:

- **result debt:** you may get an answer without knowing whether it is correct;
- **knowledge debt:** assumptions remain hidden and cannot be reviewed;
- **reproducibility debt:** nobody can repeat the path that produced the output;
- **technical debt:** patches accumulate around an unsuitable approach;
- **operational debt:** cost, time, and handoff burden grow; and
- **trust debt:** confidence falls because nobody can explain what happened.

Treat recurring friction as a signal to pause, not a reason to push harder. Useful recovery prompts include:

> What assumptions are you making, and what do you need from me to choose well?

> Step back. What are the practical approaches here, why is the current one difficult, and what do you recommend instead?

> Before continuing, inventory the work and propose a staged approach.

> What existing tools, scripts, libraries, or project conventions can we reuse?

> How did you verify this, and what does that verification not prove?

### Keep approval boundaries explicit

Pause for explicit approval before an agent does something destructive, public, external, costly, or sensitive. Examples include deleting or overwriting data, publishing or sending material, spending money, connecting credentials or external services, changing production systems, or handling real private data outside an approved workflow.

For learning and experimentation, use fictional data, public data, or an authorized copy by default. Preserve raw inputs and write derived work to a separate output location.

## A compact working pattern

For many tasks, this pattern is enough:

1. **State outcome and boundary.** “Create X for Y. Use these sources. Do not do Z.”
2. **Request a plan when it matters.** “Inspect first; identify tools, evidence, assumptions, and decisions.”
3. **Choose meaningful trade-offs.** Ask for options and a recommendation rather than guessing.
4. **Execute an approved slice.** Start small when scale, cost, or uncertainty is high.
5. **Inspect evidence.** Review outputs, paths, counts, exceptions, checks, and limitations.
6. **Steer a revision.** Preserve what works, change what matters, and update the evidence.
7. **Retain only useful context.** Add a script, template, instruction, or handoff only when it reduces future friction.

The goal is not to become an expert prompt writer. It is to become an effective operator and reviewer: clear about outcomes, deliberate about meaningful choices, alert to scale and risk, and able to ask for the evidence needed to trust a result.

## Practical starting prompts

Adapt these to your project:

- “Inspect this project and explain what it contains, which instructions apply, and what tools or checks already exist. Do not modify anything.”
- “I want a reviewable draft of this report for a nontechnical audience. Propose a plan, including evidence and decisions you need from me, before creating files.”
- “What are the practical approaches here? Compare trade-offs, recommend one, and explain what would change the recommendation.”
- “Before processing the full collection, inventory the work and propose a small pilot with success and stop criteria.”
- “Show the output paths, checks run, exceptions found, and what remains for human review.”
- “Keep the analysis, but revise the presentation for this audience and rerun the relevant validation.”
- “This may recur. What is the smallest reusable asset worth keeping, and why?”

Use the prompts as patterns, not scripts. The important habit is to make the next decision, evidence need, or boundary visible at the moment it matters.
