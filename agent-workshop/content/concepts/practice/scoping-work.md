---
id: scoping-work
title: Scoping work — how much to ask per turn
short: Scoping work
themes: [context-discipline]
related: [steering, verification, context, costs]
blurb: Size each request so you can check the result. Plan first for anything non-trivial, and checkpoint anything long.
---

Too small a request wastes your time; too large produces a big result you cannot review. Good scoping is the main skill
that separates frustrating sessions from productive ones.

## A ladder of task sizes

| Size | Example | Supervision it needs |
|---|---|---|
| One edit | Fix a typo in a table header | Glance at the result |
| One script | Profile a CSV and report problems | Read the output and the script |
| Small pipeline | Clean, analyse, and write up one dataset | Review each stage; check numbers |
| Multi-stage project | Cohort build, models, report, dashboard | Plan up front, checkpoints, a second reviewer |
| Long autonomous run | Hours of unattended work | Strong isolation, logs, and review at the end |

## The interactive/long-run trade-off

A short loop (ask, check, steer) gives you control and catches errors while they are cheap. A long run saves your
time but compounds mistakes: an early wrong assumption can be built on for an hour. A useful rule: **a good unit of
work is one you can verify in a few minutes.** If you cannot say how you would check it, split it.

## Plan first

For anything non-trivial, ask for a **plan** before any work: the approach, the options, the assumptions, and the
open questions. Edit the plan, then say "go". Many harnesses have a *plan mode* that prevents changes until you
approve ([Steering](concept:steering)).

```text
Before doing anything, propose a plan for <goal>: the steps, what you will produce, what you need from me,
and anything ambiguous. Do not change any files yet.
```

Planning is also where you make the decisions that belong to you (definitions, exclusions, what counts as success).

## What to put in a request

- **The outcome** and who will use it.
- **Constraints**: data to use, things not to touch, formats.
- **How you will judge it**: what a correct result looks like.

For a fuller treatment, see the [Introducing coding agents](guide:introducing-coding-agents) guide.

## Long-running work needs checkpoints

Ask for stages, saved intermediate files, and a short progress log, so a failure does not lose everything and you can
review at the stage boundaries instead of only at the end.

## Signs you asked for too much

- You cannot summarise the plan in a few sentences.
- You cannot check the result.
- The edits are spread over many files you have not looked at.

## How much can an agent do alone?

This keeps changing, so treat any answer as dated. The reliable approach is to test a task at small scale and
increase the size as you build trust.

## Demo it

<!-- demos -->
