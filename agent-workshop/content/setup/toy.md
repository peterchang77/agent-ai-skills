---
scenario: toy
label: Toy dataset
---

A synthetic dataset for a three-clinic network, with every common file format and deliberate problems to find. It is
safe to share and is not real patient data. The files live in `scenarios/toy/kit/` in this repository.

```bash
# from the repository's agent-workshop/ folder
cp -r scenarios/toy/kit/. ~/workshop-demo/
cd ~/workshop-demo && ls
```

| File | Format | What it is |
|---|---|---|
| `clinic_notes.txt` | TXT | An operations memo with the three questions to answer |
| `data_dictionary.md` | MD | Column meanings and units |
| `clinic_visits.csv` | CSV | About 7,500 visits across three clinics, with data-quality problems |
| `pilot_calls.csv` | CSV | Patients called by the Hillcrest follow-up pilot |
| `clinic_targets.xlsx` | XLSX | 2025 targets and planned staffing, formatted for people |
| `pilot_protocol.docx` | DOCX | The pilot's eligibility rules and outcome definition |
| `patient_newsletter.pdf` | PDF | A text-only patient newsletter |
| `clinic_directory.html` | HTML | A web page with clinic hours and announcements |
| `staffing.db` | SQLite | Monthly staffing by clinic |
| `visit_notes.csv` | CSV | 200 short free-text visit notes (for the bulk-inference step) |
| `visit_notes_labeled_sample.csv` | CSV | Correct categories for the first 30 notes |

**The story.** You are the analyst. The memo in `clinic_notes.txt` asks three things: which clinics meet their
HbA1c targets; whether the Hillcrest call pilot increased HbA1c rechecks (and a one-page abstract with references);
and, if time allows, whether Northside's Saturday hours reduced urgent visits.

### Checkpoints

Restore one of these ([how](setup:restore-a-starting-point)) to start a step without doing the earlier ones.

| Checkpoint (in `scenarios/toy/checkpoints/`) | Contains |
|---|---|
| *(the kit itself)* | The original files only |
| `cleaned` | Kit + `scripts/clean_visits.py`, `data/clean/visits_clean.csv`, `out/cleaning_flow.md`, `notes/cleaning-decisions.md` |
| `cohort` | `cleaned` + `AGENTS.md`, `out/cohort.csv`, `out/cohort_flow.md` |
| `analyzed` | `cohort` + `scripts/analyze_pilot.py`, `out/pilot_results.md`, `references.bib`, `refs/search-log.md` |

`scenarios/toy/extras/` holds a reference PubMed helper (`pubmed_refs.py`) and a verified `references.bib` for the
literature steps, in case you cannot reach the network.

Everything here is synthetic. The numbers illustrate methods and are not findings about any real population.
