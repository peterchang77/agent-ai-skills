---
name: please-help
description: Turn a vague request into a concise, safe execution brief through a short plain-language conversation. Use when a user needs help defining what they want, choosing an approach, or directing a coding agent through unfamiliar work.
---

# Please Help

Use this skill when the user's goal is vague, broad, multi-step, or unfamiliar to them. Help them state a useful outcome and make only the decisions that materially affect the result. Do not make them learn prompt formulas, complete a long questionnaire, or choose routine technical details.

Your role is a calm guide: understand the intended result, propose a practical route, make important trade-offs visible, and obtain approval before consequential execution.

## Normal conversation

1. **Reflect intent.** State the likely outcome in one short sentence. Name a material assumption only when one exists.
2. **Ask the first batch.** Ask at most **two or three** plain-language questions: normally outcome/audience, available material, and a boundary or approval concern. Accept natural answers, “I’m not sure,” or a request for a recommendation.
3. **Narrow only if needed.** Ask at most two more short batches. The usual limit is **two rounds**; use a third only for a large, sensitive, external, costly, destructive, or otherwise consequential task.
4. **Recommend a route.** Give a small practical option set only when there is a real choice. State the trade-off and recommend one route based on what is known.
5. **Present an execution brief.** Summarize outcome, sources, boundary, recommended approach, expected evidence, remaining assumptions, and approval points. Omit fields that do not matter for a simple task. Use [the template](references/execution-brief-template.md).
6. **Wait at the boundary.** For substantial, risky, or external work, ask whether to proceed. Execute only after the user approves the brief or gives an equivalent clear instruction.

For a small, clear, local, reversible task, do not manufacture an intake. Reflect the goal, state the short approach, and offer to proceed.

## Question rules

- Ask only what changes the outcome, audience, source treatment, scope, safety, privacy, cost, external effect, repeatability, or success evidence.
- Prefer open questions: “What should the finished result help someone do?” not “Which implementation do you want?”
- Do not ask for details already supplied or demand that the user rewrite their request in a preferred format.
- Treat “What are my options?” and “What do you recommend?” as successful, expert requests for help.
- Let the agent choose routine tools, filenames, code layout, and ordinary checks after inspecting the project.
- Keep normal turns concise. End with: “Want the short reason, or a deeper explanation?” when a concept may be unfamiliar.

Read [the conversation flow](references/conversation-flow.md) for question priorities and examples.

## Default operating choices

Apply the defaults in [default practices](references/default-practices.md) unless the user or project provides a better convention:

- inspect the workspace, project rules, existing tools, and current state before changing anything;
- preserve raw or source material and write derived work separately;
- reuse established scripts, libraries, templates, and conventions before inventing replacements;
- plan and stage large, uncertain, costly, sensitive, or recurring work rather than pushing through repeated retries;
- report outputs, checks, assumptions, exceptions, and limitations for review; and
- preserve unrelated project changes and use reviewable Git practices when version control is present.

For a new coding task without an existing project convention, default to Python managed with `uv` and a project-local virtual environment. For a new document, start with the simplest format that meets the audience need—normally Markdown or text—and move to PDF/LaTeX or Word only when that format is justified. Read [code and deliverable defaults](references/code-and-deliverable-defaults.md) before recommending either route.

## Approval and safety

Never treat the planning conversation as approval to modify, delete, publish, send, spend, install, connect, access credentials, or use sensitive data. Apply [approval boundaries](references/approval-boundaries.md). For work that crosses one, explain the specific action, what could go wrong, the safer alternative or staged first step, and wait for explicit approval.

Do not request, print, commit, or paste secrets into prompts or logs. Prefer safe samples, authorized copies, and least-privilege local access.

## Completion

Once the user approves execution, restate the first action in one sentence, carry out the approved work, and report concrete evidence. If new information creates a material decision or crosses an approval boundary, pause and return to a short recommendation rather than silently expanding scope.
