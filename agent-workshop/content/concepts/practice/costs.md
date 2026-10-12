---
id: costs
title: Costs — tokens, subscriptions, and APIs
short: Costs
themes: [context-discipline]
related: [context, scoping-work, tools, harnesses]
blurb: You pay for tokens read and written. Conversation history is re-sent each turn, so long sessions cost far more than several short ones.
---

## What you pay for

Cost is measured in **tokens**, short pieces of text ([Context](concept:context)). You pay for **input** tokens (what the
model reads) and **output** tokens (what it writes). Output is typically priced higher than input.

## Why long sessions cost so much

Every turn re-sends the whole conversation, so the input for turn *n* includes everything before it. Prompt caching
reduces the price of the repeated part but does not remove it. A worked example with **placeholder** numbers:

| Item | Value |
|---|---|
| Added to the conversation per turn | 2,000 tokens |
| Turns in the session | 50 |
| Input tokens re-read in total | about 2,000 × (1 + 2 + … + 50) ≈ 2.5 million |
| Placeholder input price | $X per million tokens |

The conversation of 50 turns reads about 2.5 million input tokens, while ten sessions of 5 turns each read about 0.3
million in total. Replace $X with the current price to get a number for your plan.

## Subscription or API?

| | Subscription | Pay-per-token API |
|---|---|---|
| Pricing | Flat monthly price with usage limits | Metered |
| Best for | Steady interactive use | Bulk or automated jobs; precise cost control |
| Watch for | Hitting limits mid-task | Runaway loops and long contexts |

Subscription plans typically run from about $20 per month through $40, $100, and $200 or more, buying higher limits and
access to larger models. Prices change often, so check the current ones. Your institution may provide access or a budget, in which case the choice may be made for you.

## What drives cost up

Long contexts, many turns, large files read whole, repeated retries, and long unattended runs.

## Habits that keep it down

- One goal per session; compact early ([Context](concept:context)).
- Process big data with code, not by reading it into the conversation.
- Use a smaller model for simple work.
- Set spending limits where the platform allows.
- Check your usage after your first few sessions to calibrate.

## Bulk API jobs

Test on a handful of items, estimate the total from the per-item cost, and put a cap on spend before running everything ([Tools](concept:tools)).

## Demo it

<!-- demos -->
