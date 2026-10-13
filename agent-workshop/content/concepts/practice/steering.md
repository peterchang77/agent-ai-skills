---
id: steering
title: Steering — keeping the agent on course
short: Steering
themes: [recursive-ai, context-discipline]
related: [scoping-work, memory, sandboxing, verification]
blurb: Balance supervisory approval modes with task risk, intervene early when execution drifts, and codify recurring corrections into standing rules.
---

Steering refers to the real-time supervisory control a researcher exerts over an agent during execution. Effective steering balances efficiency with safety: granting sufficient autonomy for the agent to resolve routine implementation details while enforcing clear checkpoints for critical methodological decisions.

## Supervisory approval modes

Agent harnesses implement different permission models to govern how commands and filesystem modifications are executed:

| Permission tier | System behavior | Recommended research use case | Operational risks |
|---|---|---|---|
| **Plan / Read-only** | Agent inspects files and proposes a plan; executes no writes or commands | Initial exploratory scoping; clarifying complex methodologies | Analysis cannot progress until plan approval is granted |
| **Interactive confirmation** | Prompts for user approval before each command execution or file modification | Unfamiliar scripts, novel libraries, or sensitive project environments | Approval fatigue: repetitive prompts cause users to approve actions without careful review |
| **Auto-accept file edits** | Modifies files directly; pauses only before executing shell commands | Iterative refactoring and script adjustments within an active project | Silent file edits that escape human inspection |
| **Full autonomous execution** | Executes commands and modifies files continuously without pausing | Routine batch processing in isolated containers or disposable workspaces | Errors propagate rapidly without human intervention |

**Calibrate permissions to operational risk:** Use interactive confirmation for unfamiliar analytical steps or sensitive environments. Increase autonomy only when working within isolated, version-controlled project trees ([Sandboxing](concept:sandboxing), [Version control](concept:version-control)).

## Enforcing dry runs for side-effecting operations

Operations that modify remote cloud infrastructure, transmit network requests, delete datasets, or incur financial charges must follow a **preview-and-approve** protocol:

```text
Draft the exact network payload and destination parameters.
Display the preview and pause for my confirmation before executing.
```

## Active intervention and early redirection

Do not wait for an erroneous execution loop to terminate on its own. When an agent adopts an invalid premise or begins modifying the wrong files, interrupt execution immediately. Intervening early preserves working context and saves compute resources:

- **Detecting algorithmic drift:** If an agent attempts to simulate an empirical distribution when a closed-form formula is appropriate, halt execution and direct it toward the direct calculation.
- **Excessive execution duration:** When a command runs unexpectedly long, interrupt the process to inspect the sub-command. The agent may be stuck in an unindexed table scan or an unbuffered network query.

## Codifying feedback into durable rules

If you find yourself correcting the same behavior across multiple turns (e.g., repeatedly reminding the agent not to modify files in `data/raw/`), do not continue issuing ad-hoc reminders. Formalize the constraint as a standing instruction in `AGENTS.md` ([Memory](concept:memory)). Codifying rules into persistent project documentation prevents behavioral drift across subsequent sessions.

## Prompting techniques for effective steering

- **State negative constraints explicitly:** Define both what the agent should accomplish and what actions are strictly forbidden (e.g., *"Do not install system packages; use only libraries currently available in the environment"*).
- **Surface assumptions early:** Instruct the agent to state its working assumptions before writing code.
- **Request comparative options:** Ask for two or three alternative methodological approaches along with trade-offs before committing to a pipeline.
- **Highlight uncertainties:** Ask the agent to identify ambiguous edge cases in the data that require domain expertise.

## Demo it

<!-- demos -->
