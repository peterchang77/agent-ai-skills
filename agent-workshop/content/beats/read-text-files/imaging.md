---
role: read-text-files
scenario: imaging
starts_from: the imaging kit
produces: nothing new; this step only reads
prompt: |
  Read radiology_notes.txt and data_dictionary.md. List the questions I am being asked to answer, and for each one, which files or columns I would need. Say which file each point came from.
---

**Files used:** `radiology_notes.txt` (the request) and `data_dictionary.md`.

**What you should see.** Five questions:

1. How well does the primary model (`score_all`) separate pneumothorax from no pneumothorax, and how certain is that?
2. Is the primary model really better than the three alternatives, or could the differences be chance?
3. Does it work equally well for PA vs AP views, men vs women, and under vs over 65?
4. At each model's published operating point, what are sensitivity and specificity, and does any model meet the pilot bar?
5. Separately, sort 200 radiology reports into present / absent / uncertain.

The files needed are `labels.csv`, `model_scores.csv` (four score columns), and the DICOM headers (view position, sex, age); `radiology_reports.csv` for question 5. The memo also warns
that the sample was assembled quickly and has not been checked, which hints at what to look for. The data dictionary warns that the model scores are not comparable between models
and that two models may have seen these images in training.
