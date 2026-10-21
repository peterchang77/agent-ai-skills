---
role: plan-cleaning
scenario: imaging
starts_from: the imaging kit, `out/profile.md` and your `out/review.csv` (or restore the `cleaned` checkpoint and ignore what it already contains)
produces: "`notes/cleaning-decisions.md` with your decisions"
prompt: |
  Do not change any files. Using the problems in out/profile.md and my confirmed items in out/review.csv, propose a cleaning plan for the images, labels and scores. For each problem give the options, the consequences of each,
  and your recommendation. Group the mechanical fixes together, and ask me about any judgement call rather than deciding it yourself. No decision may depend on what a model scored an image; say how your plan guarantees that.
  When we agree, write the final decisions to notes/cleaning-decisions.md.
---

**Files used:** `out/profile.md`, `out/review.csv`.

**Mechanical fixes (approve together).** Normalize patient IDs (lower case, no spaces, no `SITE1-` prefix); normalize sex to M/F; fill a blank view position from `SeriesDescription`; set modality to `CR`; invert the six
MONOCHROME1 images and set the tag to MONOCHROME2; normalize the label spellings; convert the logit score rows with the sigmoid; match score file names to image file names ignoring case; clear the header patient details.

**Judgement calls (the agent should ask you).**

| Problem | Options | Why it is your decision |
|---|---|---|
| Inverted images tagged MONOCHROME2 (4, confirmed by you) | Invert the pixels; exclude them | Inverting assumes the picture is otherwise fine. It is likely, but you are changing what the model will see. |
| Mirrored images (4) | Exclude; flip them back | Flipping back looks easy, but laterality matters clinically and you cannot be sure the flip is the only change. Excluding is safer. |
| Patient text burned into the picture (5) | Black out the text; exclude the image | Blacking out removes the information but also edits pixels. Excluding loses a good image. |
| Identical pixels with opposite labels (2 pairs) | Exclude both; keep one | You cannot tell which label is right. Keeping one means guessing. |
| Implausible ages (212Y, 150Y) | Blank the age; exclude | A blank age cannot show the patient is an adult, so the image will drop out at the cohort step anyway. |
| Images of patients under 18 (19 images) | Keep in the cleaned set and exclude at the cohort step; drop now | The protocol covers adults only, but other questions may not. |
| Second study of the same patient (20 images) | Keep and decide at the cohort step | This is not a defect; it matters for the unit of analysis. |

**The point of this step.** There is no single correct choice for most of these. The reference solution inverts the four confirmed images, excludes the mirrored ones, blacks out the text, excludes both images in each
conflicting pair, blanks the implausible ages, and keeps minors and follow-ups until the cohort step. You can choose differently, as long as you decide deliberately and write it down. **The rule that is not negotiable:**
nothing is kept or removed because of a model score.

The reference decisions are in `scenarios/imaging/checkpoints/cleaned/notes/cleaning-decisions.md`.
