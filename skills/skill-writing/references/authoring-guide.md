# Skill Authoring Guide

This guide provides detail for authors who need more than the operating rules in `SKILL.md`.

## Start with the activation contract

A skill is most useful when an agent can recognize exactly when to use it. Write down:

- **Capability:** the concrete result the skill produces.
- **Triggers:** requests, files, tools, or conditions that indicate the skill applies.
- **Non-goals:** nearby work the skill intentionally leaves to another skill.
- **Inputs and outputs:** what the agent needs and what it should deliver.

Use those decisions to write the frontmatter description. A good description is specific enough to distinguish the skill from neighboring skills without becoming a full user manual.

## Shape the entrypoint

A practical entrypoint usually follows this order:

1. A short purpose statement.
2. The normal workflow.
3. Rules that affect decisions or quality.
4. Failure handling and safety constraints, if relevant.
5. Validation and links to optional detail.

Include only information needed during execution. Move explanations, alternatives, long examples, and lookup material to references. If the normal workflow requires a reference, link it at the step where it is needed rather than hiding the dependency at the end.

## Choose package files

| Directory | Use it for | Do not use it for |
| --- | --- | --- |
| `references/` | Focused procedures, schemas, examples, edge cases, and background needed occasionally | A second copy of the entrypoint or an unstructured knowledge dump |
| `templates/` | Documents or code that authors adapt repeatedly | Instructions that belong in `SKILL.md` |
| `scripts/` | Small deterministic operations that are safer or clearer as executable code | Business logic that cannot be reviewed easily or an untested convenience wrapper |

Keep each supporting file narrowly scoped. Prefer several short, discoverable files over one large manual. Use stable relative links, and update links when files move.

## Write operational instructions

Turn advice into an observable action:

- Weak: “Make the output high quality.”
- Strong: “Run the project’s formatter, inspect the changed sections, and report any checks that could not run.”

For each nontrivial step, make the expected result clear. If there are branches, state the condition and the action for each branch. If a command mutates data, state its scope, reversibility, and any required confirmation.

Use placeholders such as `<skill-name>` or `/path/to/workspace` for values authors must supply. Mark literal values, required file names, and optional values distinctly.

## Keep instructions maintainable

Prefer stable concepts over incidental implementation details. Record versions, paths, and tool assumptions only when they are required for correctness. When a rule is likely to vary by project, define a project-specific reference rather than weakening the generic skill.

When revising a skill, inspect every linked file and update examples, commands, and package manifests together. Remove obsolete guidance instead of appending corrections that leave contradictory rules.

## Review checklist

- Can an agent identify the skill from its description alone?
- Can it complete the common case without guessing missing prerequisites?
- Are exceptional cases and unsafe actions explicit?
- Is each instruction located in the file where it will be maintained?
- Are links, placeholders, commands, and expected outputs valid?
- Does the package remain useful if optional references are not loaded?
- Is every file necessary and included in the package manifest, when the host format requires one?
