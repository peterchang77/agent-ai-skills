---
role: commit-work
scenario: imaging
starts_from: the `evaluated` checkpoint plus the tool and skill from the previous step
produces: a local Git repository with one commit
prompt: |
  Initialise a git repository here if there is none. Create a .gitignore that excludes the images (*.dcm and the images/ folder), the data files (*.csv, *.xlsx, *.docx, *.pdf), the out/ and data/ folders, any .env file, and .venv.
  Show me git status and what would be committed. Do not commit yet.
---

**Then commit:** `Commit scripts/, notes/, README.md, AGENTS.md and .agents/ with a clear message. Do not push.`

**What should be committed:** `scripts/`, `notes/cleaning-decisions.md`, `README.md`, `AGENTS.md`, `references.bib`, `refs/search-log.md`, and the skill folder.

**What should not be:** the DICOM files (they hold patient information in the header and sometimes in the pixels), the other original data files, `out/`, `data/`, and any `.env`. A single `git add .` here would add 280 images and about 70 MB, and the history keeps them
forever, even if you delete them in a later commit.

**Note on the data.** The images in this material are a public research sample and the headers are synthetic. With real clinical images, committing them, even to a private repository, may breach your institution's rules. Check before you do ([Privacy](concept:privacy)).
