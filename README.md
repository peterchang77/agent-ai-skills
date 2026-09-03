# Agent AI Skills

A collection of focused, reusable skills for AI agents. Each skill provides concise operating instructions and may include references, templates, or small helper scripts.

## Repository layout

- [`skills/`](skills/) — reusable skill packages
- [`tutorials/`](tutorials/) — guided learning material
- [`workshops/`](workshops/) — practical exercises and experiments

## Skill packages

Each package lives under `skills/<name>/` and uses `SKILL.md` as its entrypoint. Supporting material is kept close to the skill:

```text
skills/<name>/
├── skill.json       # package manifest
├── SKILL.md         # concise operational instructions
├── references/      # optional focused guidance
├── templates/       # optional reusable starting points
└── scripts/         # optional deterministic helpers
```

Use a skill by placing its package in the skills directory used by your agent runtime. The package entrypoint describes any additional setup and validation required.

## Creating a skill

[`skills/skill-writing/`](skills/skill-writing/) provides generic guidance for designing, writing, and reviewing skill packages. It also contains optional conventions and maintenance helpers for this repository; those local references are not required when creating skills elsewhere.

Keep skills focused, concise, portable, and explicit about prerequisites, safety constraints, and validation.

## Contributing

Add or revise a focused skill, keep supporting files necessary and discoverable, validate the package, and describe meaningful behavior changes in the pull request. Avoid committing secrets, generated artifacts, or machine-specific paths.

## License

Released under the [MIT License](LICENSE).
