---
role: make-tool-and-skill
scenario: imaging
starts_from: the `evaluated` checkpoint
produces: "`scripts/eval_report.py`, `README.md`, a test, `.agents/skills/cxr-eval/SKILL.md`"
prompt: |
  Combine scripts/clean_images.py, scripts/build_cohort.py and scripts/evaluate.py into one command-line tool, scripts/eval_report.py, that takes the path to the kit folder (images, labels.csv, model_scores.csv), my out/review.csv and an output folder, and writes the cleaning flow, cohort,
  cohort flow and evaluation. It must not modify its inputs and must have --help. Add a test that checks the key numbers (258 cleaned images, 203 patients, 59 with pneumothorax, AUC of score_all 0.78). Write README.md. Then create the skill
  .agents/skills/cxr-eval/SKILL.md (under 40 lines) saying when to use the tool, the exact command, and what to check.
---

**Files used:** `scripts/clean_images.py`, `scripts/build_cohort.py`, `scripts/evaluate.py`, `notes/cleaning-decisions.md`, `out/review.csv`.

**Known answers for the test.** 258 cleaned images; 247, 237, 220 and 203 patients through the cohort steps; 59 with pneumothorax; AUC of `score_all` 0.78 (0.715 to 0.843); sensitivity 0.92 and specificity 0.47 at the published threshold (rounded). The bootstrap is random, so the test should allow a
small tolerance on the interval, and a fixed seed makes it repeatable.

**A skill sketch** (yours will differ):

```markdown
name: cxr-eval
description: Clean a chest-radiograph kit and evaluate pneumothorax detector scores (cleaning flow, cohort, AUC with intervals).
Use when asked to rerun or update the detector evaluation on a new batch of images and scores.
Run: uv run scripts/eval_report.py <kit folder> out/review.csv out/
Check afterwards: out/cleaning_flow.md counts add up; out/cohort_flow.md final count equals the rows in out/cohort.csv;
every estimate has an interval and patient counts. Human review (out/review.csv) must be redone for new images. See README.md.
```

**Prove it.** In a new session, ask: "Rerun the detector evaluation on the current files." The agent should find and run the tool without being told the command.

**New batch.** With a new batch the same command produces a new report, but the review file does not carry over: mirrored or inverted images must be found by a person again. The tool should say so rather than silently reuse the old file.
