# Coding Agent Basics

A beginner-friendly, mission-led course for data scientists and office professionals. Direct a coding agent to turn fictional monthly CSV exports into a trustworthy, reviewable draft report—without modifying the raw data.

## Choose a format

- **Read in a browser:** follow the [course guide](COURSE.md) and the acts in [`modules/`](modules/).
- **Learn interactively:** install or copy the generic [`tutorial-facilitator`](../../skills/tutorial-facilitator/) skill and this tutorial's [`SKILL.md`](SKILL.md) into a skill location your agent supports, then ask: “Start the Coding Agent Basics mission.”

Both paths use the same canonical Markdown. In interactive mode, you are the operator: you tell the agent what to do, inspect its evidence, and gradually unlock a reliable workflow. The agent teaches just enough to support your next move.

## The mission

> **Deliver a trustworthy draft monthly report from raw CSV exports while preserving sources and leaving ambiguous records for human review.**

The supplied [`examples/sample-project/`](examples/sample-project/) is fictional and safe to use. You may substitute an authorized copy of a real workflow later.

## What you will direct the agent to build

1. A read-only workspace survey and a safe source boundary.
2. A bounded reporting request and a data-quality report with evidence.
3. Durable project rules in Markdown and `AGENTS.md`.
4. A focused reusable reporting skill and deterministic check.
5. A handoff, model-selection decision, and reviewable draft report.

## Mission map

| Act | Modules | Obstacle unlocked | Typical time |
|---|---|---|---:|
| 0. Set up | [00](modules/00-mission-setup.md) | Choose the mission boundary and route | 10 min |
| 1. Survey safely | [01](modules/01-what-is-a-coding-agent.md), [02](modules/02-model-provider-chat-agent.md) | Direct a read-only workspace inspection and identify access limits | 20 min |
| 2. Define the job | [03](modules/03-bounded-requests.md) | Create a bounded report request | 15 min |
| 3. Investigate | [04](modules/04-inspect-and-validate.md) | Produce and inspect evidence without altering sources | 15 min |
| 4. Set the rules | [05](modules/05-files-as-memory.md) | Create durable project instructions | 18 min |
| 5. Package the process | [06](modules/06-reusable-skills.md) | Create a focused reusable skill | 20 min |
| 6. Make it resumable | [07](modules/07-context-and-compaction.md), [08](modules/08-model-selection-and-connection.md) | Create a handoff and operating decision | 30 min |
| 7. Review the draft | [09](modules/09-capstone.md) | Check the full workflow and hand it off | 30–45 min |

## Safety defaults

Use sample data or a copy first. Do not overwrite sources, delete files, publish, send messages, spend money, or connect external services without explicit approval. A useful agent shows its evidence; it does not replace human judgment.

## Course authors

The format is reusable: pair a mission-based Markdown course with the generic facilitator skill, a concise tutorial overlay, learner state, and small deterministic checks. Read [`tutorial.yaml`](tutorial.yaml), [`SKILL.md`](SKILL.md), and the generic facilitator package for the authoring contract.
