---
id: steering
title: Steering — keeping the agent on course
short: Steering
themes: [recursive-ai, context-discipline]
related: [scoping-work, memory, sandboxing, verification]
blurb: Choose how much the agent may do without asking, interrupt early, and turn repeated corrections into standing rules.
---

Steering is how you keep the agent doing what you want while it works: instructions, approvals, and course corrections.

## Approval modes

Harnesses differ in names and details, but most offer a version of these:

| Mode | The agent… | Good for | What can go wrong |
|---|---|---|---|
| Plan / read-only | Explores and proposes; changes nothing | New or unclear work | Nothing happens until you approve |
| Ask each time | Asks before every file change or command | Unfamiliar work, sensitive data | Approval fatigue; you stop reading the prompts |
| Auto-accept edits | Edits files freely, asks before commands | Routine changes inside a project | Edits you did not review |
| Auto-accept everything | Runs commands and edits without asking | Isolated, backed-up environments | Mistakes happen at full speed |

**Match the mode to the risk.** Ask first with unfamiliar tasks or sensitive data. Allow more autonomy only inside an
isolated, backed-up environment ([Sandboxing](concept:sandboxing), [Version control](concept:version-control)).

## Draft first for side effects

Anything that sends, publishes, deletes, or spends money gets a preview and explicit approval, as in
[Outputs](concept:outputs). Ask: "Show me exactly what you will send, and wait."

## Interrupt early

If the agent starts down the wrong path, stop it, say what is wrong, and redirect. Waiting for it to finish costs time and context.

A run that takes far longer than the task seems to deserve is a signal. Stop it and ask what it is doing. The agent may have picked a much heavier method than you needed, such as simulating a result you could compute directly, and a one-line instruction to use the simpler method usually fixes it.

## Fix the cause, not the symptom

If you correct the same mistake twice, put the rule in `AGENTS.md` ([Memory](concept:memory)). To make a procedure
reliable, combine a short instructions file with a skill or a tool; prose alone drifts.

## Prompt habits that help

- Say what to **avoid**, not only what to do.
- Ask it to **state its assumptions** before it starts.
- Ask for **options** before it commits to an approach.
- Ask **what it is unsure about**.
- Ask for **evidence**, not reassurance ([Verification](concept:verification)).

## Demo it

<!-- demos -->
