---
role: build-dashboard
scenario: toy
starts_from: the `cleaned` checkpoint
produces: "`scripts/make_dashboard.py`, `out/dashboard.html`"
prompt: |
  Write scripts/make_dashboard.py that reads data/clean/visits_clean.csv and clinic_targets.xlsx and writes out/dashboard.html: a single
  self-contained page (no external network requests) with (1) for each clinic, the share of adult patients with diabetes whose most
  recent HbA1c is below 8.0 against the clinic's target, with the patient count; and (2) monthly urgent-visit share by clinic. Use aggregated
  numbers only. Label axes and units. Tell me what you chose and why.
---

**Files used:** `data/clean/visits_clean.csv`, `clinic_targets.xlsx`.

**What you should see.** A page with a bar chart of target attainment: Hillcrest 57.6% (target 55%), Northside 65.5% (target 60%), Riverside 53.9% (target 60%) with
patient counts 479, 296, 232, and a line chart of monthly urgent-visit share, where Northside drops from March onward.

**Things to try**

- `Mark clinics that miss their target in red.`
- `Add a note that the data is synthetic.`
- `Add a table of the numbers behind each chart.`

**Check.** Open `out/dashboard.html` in a browser, then search the file for `http` to confirm it makes no external requests.
