---
role: build-cohort
scenario: imaging
starts_from: the `cleaned` checkpoint
produces: "`scripts/build_cohort.py`, `out/cohort.csv`, `out/cohort_flow.md`"
prompt: |
  Read eval_protocol.docx (or text/eval_protocol.md if you converted it earlier). Quote the exact inclusion rules and the unit of analysis. Then write scripts/build_cohort.py that applies them to data/clean/ and writes out/cohort.csv
  (one row per patient: patient ID, index image, study date, label, view, sex, age and the four scores) and out/cohort_flow.md (what remains after each step). Tell me every place you had to interpret the protocol, and report the count with each step.
---

**Files used:** `eval_protocol.docx`, `data/clean/` (images, `labels_clean.csv`, `scores_clean.csv`).

**Rules to be quoted from the protocol.** Adults (18 or older, age recorded and plausible); a frontal PA or AP radiograph at 1024 x 1024; a reference label and all four scores; the patient as the unit, using the earliest study as the index image.

**Reference flow table**

| Step | Images / patients |
|---|---|
| Cleaned images | 258 |
| With a reference label and all four scores | 247 |
| Age recorded and plausible | 237 |
| Adults (age >= 18) | 220 |
| One index image per patient (earliest study) | 203 |

**Reference cohort.** 203 patients, 59 with pneumothorax; 120 PA and 83 AP.

**Interpretation points to look for.** A blank age cannot show that someone is an adult, so those images are excluded (10 here). The last step removes 17 images: later studies of patients who are already in the cohort. Patient identity depends on the normalized ID: if the agent skips that, a patient with a prefixed ID appears twice. Dropping images with missing scores is a
missingness filter, not a performance filter, but a careful agent says so and reports how many images it removed (11).

A reference version is in `scenarios/imaging/checkpoints/cohort/out/`.
