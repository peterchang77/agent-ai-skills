---
role: commit-work
scenario: toy
starts_from: the `analyzed` checkpoint plus the tool and skill from the previous step
produces: a local Git repository with one commit
prompt: |
  Initialise a git repository here if there is none. Create a .gitignore that excludes the data files (*.csv, *.xlsx, *.docx, *.pdf, *.db),
  the out/ and data/ folders, any .env file, and .venv. Show me git status and what would be committed. Do not commit yet.
---

**Then commit:** `Commit scripts/, notes/, README.md, AGENTS.md and .agents/ with a clear message. Do not push.`

**What should be committed:** `scripts/`, `notes/cleaning-decisions.md`, `README.md`, `AGENTS.md`, `references.bib`, `refs/search-log.md`, and the skill folder.

**What should not be:** the original data files (even though they are synthetic here, practise as if they were real), `out/`, `data/`, and any `.env`.

**Note on the data.** The clinic data in this material is synthetic. With real data, committing it, even to a private repository, may breach your institution's rules.
Check before you do ([Privacy](concept:privacy)).
