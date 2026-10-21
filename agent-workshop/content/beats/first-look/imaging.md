---
role: first-look
scenario: imaging
starts_from: the imaging kit
produces: nothing saved; this is a quick exploratory answer (ask the agent to save its script if you want to keep it)
prompt: |
  Using labels.csv, model_scores.csv and data_dictionary.md, tell me how well score_all separates images with a pneumothorax from images without one: report the AUC and the number of images it is based on.
  Do not change or exclude any data; tell me what you notice about the data.
---

**Files used:** `labels.csv`, `model_scores.csv`, `data_dictionary.md`.

**What you should see.** A naive AUC of roughly **0.72** on about 240 to 260 images. Your number will vary with how the agent joins the files and treats unusual values. The clean-data
reference (a later step) gives a different answer, which is the point.

**What to notice (all findable from these two files).**

- The label column has more than two spellings of the same two classes (`PTX`, `pneumothorax`, `Pneumothorax ` with a trailing space, `no pneumothorax`, `Normal`, `NO PNEUMOTHORAX`).
- 25 score rows hold values below 0 (the file mixes logits with probabilities).
- Some scores are blank, some images have no score at all, and some file names differ only in letter case, so an exact-match join drops them.
- `labels.csv` has more rows than `model_scores.csv`, and a couple of labels refer to image files that are not in the folder.

If the agent quietly drops unmatched rows, ask how many it dropped and why. The next step audits all of this systematically.
