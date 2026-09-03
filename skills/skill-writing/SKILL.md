---
name: skill-writing
description: Design, write, and review concise, reusable skills for AI agents.
---

# Skill Writing

Use this skill when creating, revising, or reviewing a reusable skill package for an AI agent. It is generic and can be used to create skills outside this repository.

When maintaining this repository, the optional local conventions below provide convenient guidance for UV-based Python tools and synchronizing skills from authoritative sibling repositories.

## Workflow

1. **Define the boundary.** State the task, intended users, activation context, and what the skill does not cover. Keep one skill centered on one coherent capability.
2. **Write the entrypoint.** Put the minimum operating rules in `SKILL.md`: when to use the skill, the workflow to follow, important constraints, and how to validate the result.
3. **Use progressive disclosure.** Move setup, rationale, examples, edge cases, and specialized procedures into short files under `references/`. Link to them from the entrypoint.
4. **Add supporting files only when useful.** Use `templates/` for reusable starting documents and `scripts/` for deterministic helpers. Keep helpers small, portable, and documented.
5. **Review and validate.** Check discoverability, correctness, portability, concise wording, links, file paths, and the complete package layout before delivering the skill.

## Authoring rules

- Begin `SKILL.md` with YAML front matter containing a unique `name` and a one-line `description` that says what the skill does and when it is useful.
- Write direct instructions using imperative language. Prefer concrete actions, decision points, commands, and expected outcomes over background exposition.
- Order rules by execution: trigger, preparation, main workflow, exceptions, and validation.
- Make prerequisites explicit. Do not assume tools, files, permissions, or prior steps that the user or agent may not have.
- Keep the entrypoint short enough to scan in one pass. A reader should not need every reference file to begin the normal workflow.
- Avoid duplicating the same rule in the entrypoint, references, templates, and scripts. Put each rule in its most authoritative location.
- Use relative links for files within an installed package. Keep references focused on one topic and avoid deep chains of links.
- Make examples representative but minimal. Clearly distinguish placeholders from values that must be copied literally.
- Prefer deterministic, reversible procedures. Describe failure handling and validation where an incorrect result would be costly.
- Keep generic skills portable: put repository, organization, or tool-specific conventions in a separate reference or a separate skill.
## Optional repository conventions

When maintaining this repository, consult these local references as needed:

- [Python tool installation](references/python-tool-installation.md)
- [Existing-skill synchronization](references/importing-existing-skills.md)

They are optional for authors creating skills in other repositories.

## Final review

Before publishing, confirm that:

- The description makes the skill easy to select for the intended request.
- The normal path is complete without unexplained jumps.
- Scope, prerequisites, safety constraints, and validation are clear.
- Supporting files are necessary, linked, and named descriptively.
- The package contains no secrets, stale paths, unnecessary prose, or untested commands.

For detailed guidance and a starter structure, see [the authoring guide](references/authoring-guide.md) and [the template](templates/SKILL.md.template).
