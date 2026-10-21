---
role: check-usage-and-compact
scenario: imaging
starts_from: any checkpoint where you have worked for a while
produces: "`notes/session-summary.md`"
prompt: |
  Summarise this session for a future session: the questions from radiology_notes.txt we are answering, the cleaning decisions and why, the files we created and what each is for, the results so far, and the open questions.
  Save it as notes/session-summary.md in under 40 lines.
---

**What you should see.** A short file listing the five questions from the radiology memo, the cleaning decisions (which images were fixed or excluded, and that no exclusion depended on a model score), the files in `data/clean/` and `out/`, the headline results (AUC with intervals,
the pilot bar not met), and what remains (for example the abstract or the report classification).

**Images and context.** Viewing many images costs far more of the agent's working memory than reading text. If you looked at images in this session, a long session is a good moment to summarize and start fresh.

**Calibrating cost.** After your first long session, look at your account's usage page. Compare the usage for this session with a short one, to see how conversation length drives usage.
