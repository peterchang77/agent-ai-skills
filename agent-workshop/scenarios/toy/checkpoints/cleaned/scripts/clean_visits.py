# /// script
# requires-python = ">=3.10"
# dependencies = ["pandas==2.2.3", "numpy==2.1.3"]
# ///
"""Reference cleaning script (answer key; not part of kit/).

    uv run clean_visits.py KIT/clinic_visits.csv OUT/visits_clean.csv OUT/cleaning_flow.md

Rules (the analyst's decisions; see the 'decide-cleaning' beat):
  1. Normalise clinic names (strip, capitalise).
  2. Convert US-style dates (MM/DD/YYYY) to ISO.
  3. Drop exact duplicate rows.
  4. Keep, but flag, rows whose visit_id is shared by two *different* visits.
  5. Systolic BP of 0 -> missing.
  6. HbA1c >= 20 is in mmol/mol, not %: convert with NGSP = IFCC/10.929 + 2.15.
  7. Age > 120: repair from the same patient's other visits (analyst's choice; alternatives
     are to set missing or exclude the row).
"""
import sys
import numpy as np, pandas as pd

src, dst, flow_path = sys.argv[1:4]
df = pd.read_csv(src, dtype=str); flow = [("Raw rows", len(df))]
df["clinic"] = df["clinic"].str.strip().str.capitalize()
us = df["visit_date"].str.contains("/")
df.loc[us, "visit_date"] = pd.to_datetime(df.loc[us, "visit_date"], format="%m/%d/%Y").dt.strftime("%Y-%m-%d")
flow.append(("US-style dates converted", int(us.sum())))
for c in ["age", "systolic_bp", "hba1c", "ldl", "bmi"]: df[c] = pd.to_numeric(df[c])
n = len(df); df = df.drop_duplicates(); flow.append(("Exact duplicate rows removed", n - len(df)))
df["id_conflict"] = df["visit_id"].duplicated(keep=False); flow.append(("Rows sharing a visit_id (flagged, kept)", int(df.id_conflict.sum())))
bp = df["systolic_bp"] == 0; df.loc[bp, "systolic_bp"] = np.nan; flow.append(("Systolic BP of 0 set to missing", int(bp.sum())))
mm = df["hba1c"] >= 20; df.loc[mm, "hba1c"] = (df.loc[mm, "hba1c"] / 10.929 + 2.15).round(1)
flow.append(("HbA1c converted from mmol/mol to %", int(mm.sum())))
bad = df["age"] > 120
for i in df[bad].index:
    df.at[i, "age"] = df[(df.patient_id == df.at[i, "patient_id"]) & ~bad]["age"].mode().iloc[0]
flow.append(("Impossible ages repaired from other visits", int(bad.sum())))
flow.append(("Final rows", len(df)))
df.to_csv(dst, index=False)
open(flow_path, "w").write("# Cleaning flow\n\n| Step | Rows |\n|---|---|\n" + "\n".join(f"| {a} | {b} |" for a, b in flow) + "\n")
print(open(flow_path).read())
