# Synchronizing an existing skill

This repository has two skill-creation paths: write a new skill with an agent, or synchronize a skill whose dedicated sibling repository is authoritative.

Use the importer from this repository root:

```bash
python skills/skill-writing/scripts/import-skill.py ../agent-docx docx
```

The command reads the sibling repository's current checked-out package at `../agent-docx/skills/docx/`, validates its `skill.json` and exact file inventory, and atomically replaces `skills/docx/`. It copies the manifest and all declared files, removes destination files no longer present in the source, and reports added, updated, and removed files. Use `--dry-run` to inspect changes without copying.

The source path must resolve to a sibling repository. The importer does not run `git pull`, modify the source repository, install dependencies, or perform unrelated publishing operations. Review and commit the synchronized files here separately. Since the source checkout is authoritative, preserve local changes by committing or copying them elsewhere before synchronizing.

The importer uses only Python's standard library and does not require a virtualenv. It refuses invalid manifests, mismatched skill names, undeclared or missing package files, unsafe paths, and non-regular source files. The manifest itself is synchronized even though it is not listed in its own `files` array.
