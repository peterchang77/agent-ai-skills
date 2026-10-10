---
role: check-usage-and-compact
scenario: toy
starts_from: any checkpoint where you have worked for a while
produces: "`notes/session-summary.md`"
prompt: |
  Summarise this session for a future session: the questions from clinic_notes.txt we are answering, the cleaning decisions and why, the files
  we created and what each is for, the results so far, and the open questions. Save it as notes/session-summary.md in under 40 lines.
---

**What you should see.** A short file listing the three memo questions, the cleaning decisions (units converted, age repaired from other visits, and so on), the files in
`data/clean/` and `out/`, the headline results (target attainment, the pilot odds ratios), and what remains (for example the abstract or the dashboard).

**Calibrating cost.** After your first long session, look at your account's usage page. Compare the usage for this session with a short one, to see how conversation length
drives usage.
