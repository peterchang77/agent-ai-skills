---
role: make-tool-and-skill
scenario: toy
starts_from: the `analyzed` checkpoint
produces: "`scripts/pilot_report.py`, `README.md`, a test, `.agents/skills/pilot-report/SKILL.md`"
prompt: |
  Combine scripts/clean_visits.py and scripts/analyze_pilot.py into one command-line tool, scripts/pilot_report.py, that takes the paths to
  clinic_visits.csv and pilot_calls.csv and an output folder, and writes the cleaning flow, cohort, and results. It must not modify its inputs and must have
  --help. Add a test that checks the key numbers (251 patients, 92 reached, adjusted odds ratio 1.80). Write README.md. Then create the skill
  .agents/skills/pilot-report/SKILL.md (under 40 lines) saying when to use the tool, the exact command, and what to check.
---

**Files used:** `scripts/clean_visits.py`, `scripts/analyze_pilot.py`, `notes/cleaning-decisions.md`.

**Known answers for the test.** 251 patients in the cohort; 92 reached; 92 rechecked; unadjusted odds ratio 2.28; adjusted odds ratio 1.80 (rounded to two decimals).

**A skill sketch** (yours will differ):

```markdown
---
name: pilot-report
description: Produce the Hillcrest follow-up pilot report (cleaning flow, cohort, odds ratios) from the visits and calls CSV files.
---
Use when asked to rerun or update the pilot analysis.
Run: uv run scripts/pilot_report.py clinic_visits.csv pilot_calls.csv out/
Check afterwards: out/cleaning_flow.md counts add up; out/cohort_flow.md final count equals the rows in out/cohort.csv;
report every number with its patient count. See README.md for details.
```

**Prove it.** In a new session, ask: "Rerun the pilot report on the current files." The agent should find and run the tool without being told the command.

**Next month.** If you replace the CSV with next month's extract, the same command produces the new report. That repeatability is the point of the step.
