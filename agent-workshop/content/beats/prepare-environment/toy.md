---
role: prepare-environment
scenario: toy
starts_from: the data kit
produces: a `pyproject.toml`, a `.venv/` folder, and a `README.md` with a Setup section
prompt: |
  Check which of these are installed and report the version of each: python3, uv, pandoc, and pdflatex.
  Then use uv to create a Python environment for this project and install pandas, openpyxl, and statsmodels, pinned to the versions you install.
  Keep everything inside this folder. If a system-level tool is missing, tell me what it is and the exact command you would run, and wait for my approval.
  Finally, add a "Setup" section to README.md with the commands to rebuild this environment from scratch.
---

**Files used:** none yet. The agent creates the environment alongside the data kit.

**Why these tools**

| Tool | Used for |
|---|---|
| `pandas`, `openpyxl` | Reading the targets spreadsheet and cleaning the visit data |
| `statsmodels` | The pilot analysis |
| `pandoc` | The Word export near the end |
| `pdflatex` | The PDF abstract. Needed only for the writing steps |

**What you should see:** a version report where each tool is present or flagged as missing, then a `.venv/` and `pyproject.toml` in the folder, and a
`README.md` with a Setup section. Your versions will differ from anyone else's, which is why the agent pins them. If `pandoc` or `pdflatex` is missing,
the agent should stop and ask. You can decline and come back when you reach the steps that need them.
