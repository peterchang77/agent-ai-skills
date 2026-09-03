# Coding Agent Basics

A beginner-friendly course for data scientists and office professionals. Learn how a coding agent turns a clear request into inspectable work with files, code, tools, and checks.

## Choose a format

- **Read in a browser:** follow the [course guide](COURSE.md) and the modules in [`modules/`](modules/).
- **Learn interactively:** install or copy the generic [`tutorial-facilitator`](../../skills/tutorial-facilitator/) skill and this tutorial's [`SKILL.md`](SKILL.md) into a skill location your agent supports, then ask: “Start the Coding Agent Basics tutorial.”

The static and interactive paths use the same canonical Markdown modules. The interactive path changes pacing, examples, and practice—not the course outcomes.

## What you will be able to do

1. Distinguish a model, provider, interactive chat, and coding agent.
2. Give an agent a bounded task with clear inputs, outputs, rules, checks, and approval boundaries.
3. Use Markdown, `AGENTS.md`, skills, and scripts for their distinct roles.
4. Preserve work across long conversations with durable files and proactive compaction handoffs.
5. Choose a model based on task needs, capability, privacy, speed, context, and cost.

## Course map

| Module | Focus | Typical time |
|---|---|---:|
| [00](modules/00-welcome-and-pretest.md) | Goal, setup, and route | 10 min |
| [01](modules/01-what-is-a-coding-agent.md) | What an agent can and cannot do | 12 min |
| [02](modules/02-model-provider-chat-agent.md) | Model, provider, chat, and agent | 15 min |
| [03](modules/03-bounded-requests.md) | Ask for reliable work | 15 min |
| [04](modules/04-inspect-and-validate.md) | Evidence instead of plausible answers | 15 min |
| [05](modules/05-files-as-memory.md) | Markdown and `AGENTS.md` | 18 min |
| [06](modules/06-reusable-skills.md) | Repeatable skills and tools | 20 min |
| [07](modules/07-context-and-compaction.md) | Working memory and handoffs | 15 min |
| [08](modules/08-model-selection-and-connection.md) | Connect safely and select intentionally | 15 min |
| [09](modules/09-capstone.md) | Build a reliable workflow | 30–45 min |

Use the sample project in [`examples/sample-project/`](examples/sample-project/) for safe practice. The capstone validator is intentionally small and checks only structure; it does not judge writing or real-world correctness.

## Safety defaults

Work with sample data or a copy first. Do not overwrite sources, delete files, publish, send messages, spend money, or connect external services without explicit approval. A useful agent shows its evidence; it does not replace human judgment.

## Course authors

The course format is designed to be reused. Read [`tutorial.yaml`](tutorial.yaml) for the course manifest, [`SKILL.md`](SKILL.md) for this tutorial's overlay, and the generic facilitator skill for the delivery protocol. New tutorials can reuse that skill, the learner-state templates, the module frontmatter pattern, and the active-learning loop.
