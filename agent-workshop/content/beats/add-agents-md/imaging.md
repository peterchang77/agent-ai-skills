---
role: add-agents-md
scenario: imaging
starts_from: the `cleaned` checkpoint (it has no `AGENTS.md` yet)
produces: "`AGENTS.md`"
prompt: |
  Create AGENTS.md in this folder, under 25 lines, capturing: where the cleaned images, labels and scores live; the cleaning decisions in notes/cleaning-decisions.md; that the original files are never modified and outputs go in out/;
  that no exclusion may depend on a model score; that the unit of analysis is the patient (earliest study); and that every estimate is reported with a 95% interval and the number of patients and positives. Be specific. Leave out anything you could work out from the code.
---

**Files used:** `notes/cleaning-decisions.md`, `data/clean/`, `scripts/clean_images.py`, `eval_protocol.docx`.

**Step 1: see the problem.** In a *new* session in this folder, before creating the file, ask:

```text
How well does score_all separate pneumothorax from no pneumothorax in adult patients? Report the AUC with a 95% interval and the number of patients.
```

You should see the agent do one of two things: read the raw `labels.csv` and `model_scores.csv` and ignore your cleaning, or stop to ask which files and rules to use. Either shows what is lost between sessions.

**Step 3: test it.** After creating `AGENTS.md`, start another new session and ask the same question. The agent should use `data/clean/`, count patients, and mention the rules without being told.

**Reference answer on the cleaned data:** AUC about **0.78 (0.72 to 0.84)** on 203 adult patients (59 with pneumothorax), if the agent builds the cohort as the protocol describes (the next step does this explicitly). On the raw files the
number is different and has no clear basis.

A reference file is at `scenarios/imaging/checkpoints/cohort/AGENTS.md`.
