# Project instructions

- Data: `clinic_visits.csv`, `pilot_calls.csv`; column meanings are in `data_dictionary.md`.
- Never modify original files. Cleaned data goes in `data/clean/`; all other outputs in `out/`.
- Apply the rules in `notes/cleaning-decisions.md` (run `scripts/clean_visits.py`); do not invent new cleaning rules without asking.
- Every number you report must include its row or patient count.
- HbA1c is in percent (NGSP). Targets: share of adult patients with diabetes whose most recent HbA1c is below 8.0%.
- List anything you excluded or changed, and why.
- Use `uv` for Python dependencies and record new ones in `README.md`.
- Never print, log, or commit credentials.
