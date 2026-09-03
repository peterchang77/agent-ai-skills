# Conversation Flow

Use a short conversation to turn intent into a safe first action. The goal is not a complete specification. Stop asking once you can recommend a useful, reviewable route.

## First reply: reflect, then ask up to three questions

Start with one sentence that reflects the likely outcome and any important assumption. Then select the highest-value unanswered questions.

Priority order:

1. **Outcome:** What should exist or be true when this is done?
2. **Audience or use:** Who will use it, and what decision or job should it support?
3. **Material:** Which files, project, system, or information may the agent inspect?
4. **Boundary:** What must stay unchanged, private, local, or awaiting approval?
5. **Evidence:** What would make the result useful or trustworthy enough?
6. **Scope and recurrence:** Is this a small one-off task, a recurring workflow, or a large/uncertain job?

Do not ask all six. A typical first batch has two or three questions. For example:

> I can help turn this into a reviewable report while preserving the original material. Who is the report for and what should it help them decide? Where is the source file, and is it safe for me to inspect it? Should unusual rows be flagged for review or handled by an approved rule?

## Second reply: recommend and resolve only material choices

Summarize what you learned. Propose a practical route in plain language. If a real choice remains, offer no more than two or three options, state the trade-off, and recommend one.

> I recommend inspecting the existing files and rules first, creating a separate derived output, then drafting a short report with exceptions clearly marked. This preserves the source and makes the result easy to review. Should the report be a manager summary or include detailed exceptions? If you are unsure, I recommend a short summary plus a separate exceptions file.

## Third reply: only for consequential work

Use a third brief round only if the work is large, external, sensitive, costly, destructive, or otherwise high impact. Ask about the approval boundary, safe pilot, destination, or success/stop criteria—not implementation trivia.

> Processing the full collection could involve cost and many review-needed errors. I recommend an inventory and a small approved pilot first. What budget or service boundary applies, and what result would tell us to continue rather than stop?

## Then present the brief

Use [the execution brief template](execution-brief-template.md). State the recommendation, smallest safe first action, evidence expected, and any approval required. For a simple task, this can be three bullets instead of a formal-looking section.

## Common request patterns

### “Clean up this spreadsheet”

Ask about intended use, approved source location, and how unclear/incorrect-looking rows should be treated. Recommend inspection and a derived output first; do not edit the original or invent correction rules.

### “Build me a dashboard”

Ask who will use it, what decisions it should support, what safe sample data exists, and whether it is a one-time view, internal recurring tool, or public product. Recommend the smallest static prototype/report when the intended workflow is still unclear; inspect the existing stack before adding a new one.

### “Organize these files”

Ask what “organized” means, which directory is in scope, and what must not move. Recommend an inventory and a proposed rename/move mapping or dry run before bulk changes.

### “Automate this report”

Ask what repeats, which inputs and outputs are authoritative, and who reviews exceptions. Recommend a small reproducible first slice before creating a full workflow.

### “Fix the project”

Ask for the observed symptom, expected behavior, and permission to inspect the repository and its existing changes. Recommend diagnosis and evidence first; do not assume the desired fix or overwrite current work.

## Keep the tone accessible

Use “working plan,” “source file,” “check,” “choice,” and “next step.” Define technical terms only when useful. Do not praise or criticize a user’s prompt. Offer: “Want the short reason, or a deeper explanation?”
