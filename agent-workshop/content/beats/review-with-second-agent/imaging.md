---
role: review-with-second-agent
scenario: imaging
starts_from: the `evaluated` checkpoint (open a **new** session in it)
produces: nothing saved (ask for the review as `out/review.md` if you want to keep it)
prompt: |
  You are reviewing someone else's evaluation. Read eval_protocol.docx, scripts/build_cohort.py, scripts/evaluate.py and out/evaluation.md. Check the inclusion rules, the choice of index image, the bootstrap, the
  model comparison and the thresholds in the code against the protocol, line by line. List errors, questionable assumptions, and anything in the results not supported by the data. Do not change any files.
  Rank the issues and give the evidence for each.
---

**Files used:** `eval_protocol.docx`, `scripts/build_cohort.py`, `scripts/evaluate.py`, `out/evaluation.md`.

**What a good review finds.** For this evaluation the reference solution follows the protocol, so a careful reviewer should mostly confirm the rules and then raise **limitations**, such as:

- Three subgroup comparisons were made and none corrects for multiple looks; PA vs AP rests on 19 positive AP patients.
- The published operating points were set by the model developers on other data, and two of the models may have seen these images in training, so the numbers are likely optimistic.
- The sample has about 29% pneumothorax, far above clinical prevalence, so sensitivity and specificity transfer but predictive values do not.
- The reference labels came with the public sample; how they were made is not documented here.
- Burned-in "AP" and "PORTABLE" markers and chest tubes are visible in the images and may help a model without telling it anything about the lung.
- Follow-up studies were dropped, which is correct for the protocol but means each patient is represented by one image.

**A better test: plant an error.** In a copy of the folder, change one thing and ask a fresh session to review it. Two good candidates: in `scripts/build_cohort.py` take the *latest* study instead of the earliest as the index image (the cohort stays at 203 but some
rows change), or change `age >= 18` to `age > 18`. A good reviewer should find the mismatch with the protocol. It should not simply trust the summary table, because the final counts barely move.

**What a review cannot do.** It cannot tell you whether the pilot bar is the right bar for your department, or whether the sample resembles your patients. Those judgements are yours.
