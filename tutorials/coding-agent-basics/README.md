# Coding Agent Basics

A beginner-friendly course on directing coding agents toward reliable results. Using a fictional reporting project, you make one capable request, inspect the agent’s plan and tool choices, choose meaningful trade-offs, assess scale before difficult work, and revise a reviewable draft.

## Choose a format

- **Read in a browser:** follow the [course guide](COURSE.md) and five [modules](modules/).
- **Learn interactively:** install or copy the generic [`tutorial-facilitator`](../../skills/tutorial-facilitator/) skill and this tutorial's [`SKILL.md`](SKILL.md) into a skill location your agent supports, then ask: “Start the Coding Agent Basics tutorial.”

In interactive mode, you describe the outcome, choose meaningful directions, and inspect results. The agent proposes sensible plans, existing tools, options, and recommendations. It handles routine implementation choices unless they materially affect the result, safety, cost, privacy, or future maintenance.

## How an interactive launch begins

The agent first asks about your goal, work context, available time, preferred pace, practice materials, and whether you are learning normally or testing the course. It then **waits for your answer**. It does not choose a mission, create tutorial files, inspect the project, or begin a module until you respond, skip setup, or explicitly delegate defaults.

After your reply, it gives a short orientation before the first request: what a coding agent is, how models, agents, tools, and providers fit together, what you will do, and how decisions differ from routine implementation. You can ask for a shorter, deeper, or more technical version before the mission begins.

## The practice mission

> **Direct an agent from one broad reporting request to a reviewable draft, while preserving sources, choosing meaningful trade-offs, and avoiding unnecessary workflow debt.**

The supplied [`examples/sample-project/`](examples/sample-project/) is fictional and safe to use. It includes raw data, reporting notes, project instructions, an existing checker, and a sample output. You may substitute an authorized copy of a real workflow later.

## What you will learn

1. What agents, tools, code, and durable files each contribute.
2. How to make one capable request without writing an implementation screenplay.
3. When to ask for options, trade-offs, and a recommendation.
4. Why one file and 10,000 files require different planning.
5. How to inspect evidence, steer a revision, and preserve only work that will genuinely recur.

## Course map

| Module | Main question | Typical time |
|---|---|---:|
| [1. Mental model](modules/00-mental-model.md) | What does an agent actually do? | 8 min |
| [2. Capable request](modules/01-capable-request.md) | How do I give it a real job? | 15 min |
| [3. Options and tools](modules/02-options-and-tools.md) | What should I decide, and what can it decide? | 12 min |
| [4. Scope and friction](modules/03-scope-and-friction.md) | When should I pause and plan first? | 12 min |
| [5. Review, revise, reuse](modules/04-review-revise-reuse.md) | How do I make a result trustworthy and avoid debt? | 18 min |

## Safety defaults

Use sample data or an authorized copy first. Do not overwrite sources, delete files, publish, send messages, spend money, connect external services, or process sensitive material without explicit approval. A useful agent explains its plan and shows evidence; it does not replace human judgment.

## When to make work durable

A script, project instruction file, reusable skill, template, or handoff is useful when work repeats, is transferred, or needs deterministic checking. It is not a compulsory artifact for a one-off task. The course introduces these as choices, not ritual.

## Course authors

The format is reusable: pair a practical project with a concise Markdown course, an interactive overlay, safe fixtures, and small deterministic checks. Read [`tutorial.yaml`](tutorial.yaml), [`SKILL.md`](SKILL.md), and the generic facilitator package for the authoring contract.
