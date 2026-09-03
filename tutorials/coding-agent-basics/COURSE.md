# Course Guide

## The mission

You are building a **trustworthy monthly reporting assistant**. It must inspect fictional CSV exports, produce a reviewable draft, preserve raw sources, flag uncertainty, and leave publication to a person.

The course is not primarily a vocabulary test. You learn by directing an agent through the mission: issue a small instruction, inspect what happened, and retain the result in a useful file. Code is the intermediary that lets an agent inspect, transform, compare, validate, and document many kinds of digital work.

## How interactive delivery works

The agent alternates between two roles:

- **Coach:** presents the next obstacle, explains only the relevant idea, and asks you for one command or decision.
- **Operator:** executes your approved instruction, reports evidence, and returns to coach mode.

The normal loop is:

```text
situation → your command → agent action → evidence inspection → short debrief → next unlocked move
```

A question should help you choose a path, set a safety boundary, or interpret evidence. It should not be used merely to test whether you remember terminology.

## Mission artifacts

Your completed mission retains:

- a mission log and bounded task request;
- a source-preserving output and validation note;
- project knowledge notes and a short `AGENTS.md`;
- a reusable skill outline and a deterministic check;
- a compaction-ready handoff;
- a reasoned model-selection decision;
- a reviewable draft report.

## Suggested routes

- **Foundation:** use the fictional project and sentence starters for agent commands.
- **Practitioner:** move quickly through familiar ideas; concentrate on boundaries, evidence, and reusable assets.
- **Technical transfer:** set validation criteria and architecture decisions yourself; use explanations only where the agent workflow differs from familiar engineering practice.
- **Goal-first:** substitute a safe work-shaped project and unlock each idea immediately before using it.

Routes change detail and examples, not the mission's required evidence.

## Glossary, when needed

- **Model / LLM:** the language-and-reasoning engine.
- **Provider:** the service that supplies authenticated access to a model.
- **Interactive chat:** a text-first conversation, usually limited to supplied content and built-in capabilities.
- **Coding agent:** a model paired with an action loop, workspace, and tools such as file access or code execution.
- **Tool:** a concrete action, such as reading a file or running a script.
- **Context:** the information available to the model during a conversation; its working memory.
- **Compaction:** a summary of older conversation material that frees working memory but may omit detail.
- **`AGENTS.md`:** a project instruction file supported by many agent harnesses.
- **Skill:** a reusable package of focused instructions and optional references, templates, scripts, or tools.

## Static reading route

Read the acts in numeric order. For every “Your move” prompt, draft the command you would give an agent, then inspect the supplied sample project or reference artifacts. The static path should still feel like a guided build, not a textbook.
