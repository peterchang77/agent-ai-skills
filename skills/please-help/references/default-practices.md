# Default Practices

Use these defaults when the user has not supplied a stronger project convention. Apply them quietly; explain them when they affect a meaningful decision or the user asks why.

## Start with the terrain

- Inspect the workspace, project instructions, current files, existing tools, dependencies, tests, output conventions, and Git state before changing anything.
- Reuse established scripts, libraries, templates, formats, and project conventions before creating custom replacements.
- Keep unrelated existing changes untouched. State assumptions that materially affect the result instead of silently inventing them.

## Separate source from derived work

- Preserve raw inputs, source records, and authoritative material unless the user explicitly approves a change.
- Write generated reports, transformations, exports, and experiments to a separate, named output location.
- Flag ambiguous, missing, duplicate, or unusual material for review instead of silently deleting, correcting, or interpreting it.

## Plan according to consequence and scale

- Execute small, clear, local, reversible work directly once the user approves.
- For large, uncertain, expensive, sensitive, external, or recurring work, inventory first. Identify resource drivers, existing tools, likely failure modes, expected evidence, approval points, and a small representative pilot.
- Treat repeated retries, weak evidence, hidden assumptions, scope growth, or needless custom work as a signal to pause and recommend a lower-friction route.
- Give relative estimates and drivers; do not invent precise time, cost, accuracy, or capability guarantees.

## Make results reviewable

- Report exact output paths, files changed, checks run, exceptions, assumptions, and known limitations.
- Explain a material tool choice in plain language: what it does, why it fits, and what the user should inspect.
- Ask what validation proves and what it does not prove. A passing technical check does not settle a business, scientific, editorial, or approval decision.
- Invite a meaningful revision after review: preserve what works, name what should change, and update relevant evidence.

## Use project history deliberately

When Git is present, inspect status and existing changes before editing. Use focused, atomic commits when the user asks to commit or the workflow has delegated that responsibility. Review staged content before committing. Do not push, open/merge a pull request, rewrite history, delete branches, or discard work without explicit approval.

## Protect secrets and external boundaries

Never ask for, print, commit, or paste a secret into a prompt, chat, source file, or log. Prefer local ignored secret files, test credentials, authorized copies, and least-privilege access. Do not make network requests, use credentials, spend money, publish, send messages, deploy, or access production/private systems without explicit approval.

## Related reading

- [Introducing Coding Agents](../../../guides/introducing-coding-agents/)
- [The Linux Command Line for Coding-Agent Users](../../../guides/linux-command-line-for-coding-agents/)
- [Git and GitHub for Coding-Agent Users](../../../guides/git-and-github-for-coding-agents/)
