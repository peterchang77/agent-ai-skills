---
role: read-office-formats
scenario: imaging
starts_from: the imaging kit
produces: a `text/` folder with a plain-text version of the protocol
prompt: |
  Read eval_protocol.docx. Tell me which tool you used and what was hard to extract. Then list the inclusion rules, the unit of analysis, the primary analysis, how models are to be
  compared, the pre-specified thresholds, how subgroups are to be treated, and the pilot bar. Finally, save a plain-text version in text/ and tell me what changed in the conversion.
---

**Files used:** `eval_protocol.docx`.

**What you should see.** A short Word document of headed paragraphs, which extracts cleanly. The rules to be quoted:

| Item | Protocol |
|---|---|
| Inclusion | Adults (18 or older, age recorded and plausible); frontal PA or AP chest radiograph; 1024 x 1024 pixels; has a reference label and all four scores. Exclude undecodable, non-chest, and mirrored or otherwise unsafe images. Exclusions are fixed before any score is looked at. |
| Label | The label in `labels.csv`, normalized; if copies of the same image have different labels, exclude all and report them. |
| Unit | The patient; use the earliest study as the index image. |
| Split | None: every patient is a test patient, since nothing is trained or tuned here. |
| Primary analysis | AUC of `score_all` with a 95% patient-level bootstrap interval (at least 2000 resamples). |
| Comparison | Paired difference in AUC against each other model on the same patients. |
| Operating point | Each model's published threshold, fixed in advance (listed in the protocol and the data dictionary). |
| Subgroups | PA vs AP, male vs female, under 65 vs 65 or older; exploratory; report the difference with its interval and the positives in each group. |
| Pilot bar | Sensitivity at least 0.85 and specificity at least 0.80 at one threshold, with the lower end of each 95% interval no more than 0.10 below those values. |

The protocol is the reference for the cohort and evaluation steps, so it is worth saving as text.
