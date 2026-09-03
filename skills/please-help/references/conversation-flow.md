# Conversation Flow

Use a short conversation to turn intent into a safe first action. The goal is not a complete specification. Stop asking once you can recommend a useful, reviewable route.

## First reply: reflect, then ask up to three questions

Start with one sentence that reflects the likely outcome and any important assumption. Then select the highest-value unanswered questions.

Priority order:

1. **Outcome:** What should exist or be true when this is done?
2. **Audience or use:** Who will use it, and what decision or job should it support?
3. **Delivery workflow:** Does the reader need a reviewable Markdown/text draft, a fixed-layout PDF, an editable Word document with comments/tracked changes, or an existing template? Ask this only when it materially changes the artifact.
4. **Material:** Which files, project, system, or information may the agent inspect?
5. **Boundary:** What must stay unchanged, private, local, or awaiting approval?
6. **Evidence:** What would make the result useful or trustworthy enough?
7. **Scope and recurrence:** Is this a small one-off task, a recurring workflow, or a large/uncertain job?

Do not ask all seven. A typical first batch has two or three questions. Include delivery format/template when it is central or clearly likely to change the result. For example:

> I can help turn this into a reviewable report while preserving the original material. Who is the report for and what should it help them decide? Do they need an editable Word document, a fixed-layout PDF, or is a Markdown/text draft enough to start—and is there a template to inspect? Where is the source file, and is it safe for me to inspect it?

## Second reply: recommend and resolve only material choices

Summarize what you learned. Propose a practical route in plain language. If a real choice remains, offer no more than two or three options, state the trade-off, and recommend one.

> I recommend inspecting the existing files and rules first, creating a separate derived output, then drafting a short report with exceptions clearly marked. This preserves the source and makes the result easy to review. Should the report be a manager summary or include detailed exceptions? If you are unsure, I recommend a short summary plus a separate exceptions file.


## Who decides what, and when

The user chooses the result and workflow that affect how it will be used: audience, scope, interpretation/claim strength, final format, editable/review requirements, templates, and consequential trade-offs. The agent researches and chooses routine implementation details: ordinary tools, libraries, files, code layout, and task-relevant checks.

Ask about format or tooling in the **first batch** when it is plainly central—for example, a request for a paper, contract, slide deck, dashboard, or shared deliverable. Otherwise, inspect the project first. If research reveals a real choice, present a small recommended option set before full production.

> The project has no required document template. I recommend a Markdown draft first so we can review the claims and evidence, then produce a PDF or editable Word version if the final reader needs fixed layout or tracked changes. Which reader/workflow applies?

## Third reply: only for consequential work

Use a third brief round only if the work is large, external, sensitive, costly, destructive, or otherwise high impact. Ask about the approval boundary, safe pilot, destination, or success/stop criteria—not implementation trivia.

> Processing the full collection could involve cost and many review-needed errors. I recommend an inventory and a small approved pilot first. What budget or service boundary applies, and what result would tell us to continue rather than stop?

## Then present the brief

Use [the execution brief template](execution-brief-template.md). State the recommendation, smallest safe first action, evidence expected, and any approval required. For a simple task, this can be three bullets instead of a formal-looking section.


## Default execution: research, show direction, then complete

For any task beyond a clearly small, local, reversible change, recommend a three-stage route:

1. **Research first.** Read relevant instructions, files, code, results, data shape, existing tools, tests when relevant, and current state. The goal is to understand what evidence and constraints exist before offering to write, build, analyze, or modify anything. If this uncovers a material uncertainty, ask the next two or three useful questions before choosing a route.
2. **Show direction with a small preview.** Give the user a quick, task-appropriate artifact that reveals whether the agent is headed in the right direction. For writing, show a proposed scope, outline, brief claim map, or a few sourced headline findings. For data work, show a representative input-to-output result. For an interface, show a small prototype or one view. For a technical change, run a targeted executable check only if it answers the relevant question. Do not substitute an unrelated repository test suite for this preview.
3. **Perform the full task.** Expand only after the research and preview support the route and any material approval boundary is cleared.

After stages one and two, report findings concisely: what was researched or previewed, what it showed, the recommended next step, and the evidence expected next. Pause for confirmation before proceeding when the next stage materially expands scope, cost, privacy exposure, external effect, risk, or irreversibility. The agent may collapse or skip stages when the task is genuinely straightforward and the staging would be empty ceremony.

Example for writing:

> I will first review the available results, methods, and project history so I can distinguish established findings from open questions. I will then show a short Methods/Results outline with the main sourced statistics and limitations before drafting the full report. I will ask only about choices the research does not resolve, such as audience, claim strength, or which result deserves emphasis.

Example for a data task:

> I will first inspect the source and existing rules, then show one representative transformed record with its checks and exceptions. If that output matches the intended treatment, I will process the full set.

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
