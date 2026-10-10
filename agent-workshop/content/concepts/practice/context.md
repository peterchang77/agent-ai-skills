---
id: context
title: Context — the agent's working memory
short: Context
themes: [context-discipline]
related: [memory, costs, scoping-work, inputs]
blurb: Context is everything the model can see. Every turn re-sends all of it, so long conversations get slower, costlier, and less reliable.
---

**Context** is everything the model has in front of it: your messages, its replies, files it has read, and the
output of commands it ran, plus standing instructions such as `AGENTS.md`. It is finite, it costs money, and it is **gone when the session ends**.

```text
┌──────────────────── context window ────────────────────┐
│ instructions │ your messages │ replies │ files │ output │  ← grows every turn
└────────────────────────────────────────────────────────┘
```

## Every turn re-sends everything

The model does not "remember" the conversation between turns. Each time you send a message, the harness sends the
**whole conversation so far** plus your new message. That has three consequences:

- **Cost** per turn grows through a session ([Costs](concept:costs)).
- **Speed** drops as the conversation lengthens.
- **Quality** can degrade: as context fills, early instructions and details are more likely to be lost or blurred.

## Tokens, briefly

Models measure text in **tokens**, short pieces of words. A page of English text is on the order of several hundred to
about a thousand tokens. Context limits, speed, and price are all measured in tokens. [Costs](concept:costs) turns this into money.

## How long is too long?

Models advertise very large windows (a million tokens or more), but quality and cost are usually better when you stay
well below the maximum. As a **rough, dated heuristic**, aim to keep a conversation under roughly **200,000 to
300,000 tokens** even on a model with a 1 million-token window, and compact or restart earlier for precise work. Treat that as a starting point and adjust to your model and task.

## Signs context is overfull

- It re-asks things you already answered.
- It forgets a rule you gave early on.
- It repeats work or drifts from the goal.

## Managing context

- **One goal per conversation.** Start fresh for a new task.
- **Compact manually at a natural breakpoint,** rather than letting automatic compaction fire in the middle of a task. Ask for a summary of the decisions, results, and open items; save it to a file; then continue with fresh context.
- **Do not read big things whole.** For large files, have the agent inspect the schema and a sample and process the rest with code ([Inputs](concept:inputs)).
- **Write down what matters.** Anything you need next session belongs in a file ([Memory](concept:memory)).
- **Use a fresh session for review.** A second agent with clean context both avoids the clutter and reviews more independently ([Verification](concept:verification)).
- **Watch your usage.** Most harnesses show token or context usage; look at it occasionally.

## Demo it

<!-- demos -->
