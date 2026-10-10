---
role: add-agents-md
scenario: toy
starts_from: the `cleaned` checkpoint (it has no `AGENTS.md` yet)
produces: "`AGENTS.md`"
prompt: |
  Create AGENTS.md in this folder, under 25 lines, capturing: where the data and data dictionary live; the cleaning decisions in
  notes/cleaning-decisions.md; that original files are never modified and outputs go in out/; and that every reported number includes
  its row or patient count. Be specific. Leave out anything you could work out from the code.
---

**Files used:** `notes/cleaning-decisions.md`, `data/clean/visits_clean.csv`, `scripts/clean_visits.py`.

**Step 1: see the problem.** In a *new* session in this folder, before creating the file, ask:

```text
Which clinics meet their HbA1c target? Use adult patients with diabetes and their most recent HbA1c.
```

You should see the agent do one of two things: read the raw `clinic_visits.csv` and ignore your cleaning, or stop to ask which file and
rules to use. Either shows what is lost between sessions.

**Step 3: test it.** After creating `AGENTS.md`, start another new session and ask the same question. The agent should use
`data/clean/visits_clean.csv`, report patient counts, and mention the rules without being told.

**Reference answers on the cleaned data**

| Clinic | Patients | Share with most recent HbA1c < 8.0 | Target |
|---|---|---|---|
| Hillcrest | 479 | 57.6% | 55% |
| Northside | 296 | 65.5% | 60% |
| Riverside | 232 | 53.9% | 60% |

Compared with the raw first look (478, 295, 229 patients), the counts and shares moved slightly: the clinic spelling variants were
merged and the mmol/mol values converted. Here the conclusions did not change, but the numbers did, which is why the cleaned data is the
version to report.

A reference file is at `scenarios/toy/checkpoints/cohort/AGENTS.md`.
