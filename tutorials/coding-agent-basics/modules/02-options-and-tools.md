---
id: options-and-tools
title: Module 3 — Ask for options, trade-offs, and the simplest useful tools
estimated_minutes: 12
prerequisites:
  - capable-request
learning_loop: choose-route
objectives:
  - recognize high-leverage decisions worth surfacing
  - ask an agent for practical options and a recommendation
  - distinguish existing tools from unnecessary custom implementation
checkpoint: decision
---

# Module 3 — Ask for Options, Trade-offs, and the Simplest Useful Tools

## Situation

Many tasks have several valid routes. A coding agent can choose a reasonable default, but it cannot know unstated priorities. A report might be Markdown, Word, or PDF; analysis might be a one-off command or a reproducible script; document extraction might use an installed command-line tool, a library, or custom code.

The learner does not need to know the best option in advance. Recognizing the choice and asking for guidance is a strong move.

## Your move

What would you ask before choosing the report’s delivery format and analysis approach?

For example: “I am not sure which approach is best. Compare practical report formats and analysis approaches for an internal report likely to be revised. Recommend one, explain the trade-offs, and tell me what existing project tools or libraries you would reuse.”

## Agent mode

The agent presents a small set of viable options—usually two or three—not an exhaustive catalogue. For each, it explains practical trade-offs in plain language and recommends one based on the stated purpose. A useful comparison might cover:

| Choice | Good when | Trade-off |
|---|---|---|
| Markdown | draft needs quick review, revision, and version history | less fixed visual layout |
| Word | recipients must collaborate in an established Word workflow | harder to generate and review reproducibly |
| PDF/LaTeX | a fixed, polished final layout matters | slower to revise and less convenient for collaborative editing |
| existing script or CLI tool | operation is standard and tool is available | must check its fit, permissions, and output |
| small custom code | project has a specific missing transformation | must be tested and maintained |

The agent should not invent a custom parser or workflow when a suitable, available tool already handles the well-understood part.

## Inspect

Check whether the recommendation reflects your real priorities: audience, editability, repeatability, presentation, privacy, speed, cost, and existing conventions. If it does not, give the missing context and ask it to revise the recommendation.

## Unlock

Ask “What are my options, and what do you recommend?” whenever a choice is high leverage. Let an agent pick routine details; surface choices that alter the value, risk, or maintenance burden of the work.

## Checkpoint

Continue when the learner has made, delegated, or explicitly deferred one meaningful route decision with a stated reason.