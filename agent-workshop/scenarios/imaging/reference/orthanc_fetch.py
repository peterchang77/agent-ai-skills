#!/usr/bin/env python3
"""Reference: read-only retrieval from a local Orthanc server.   python3 orthanc_fetch.py [--url http://localhost:8042] [--out data/orthanc]

Standard library only. GET requests only: nothing on the server is created, changed or deleted.
Credentials: ORTHANC_USER and ORTHANC_PASSWORD from the environment, or from ./.env if present. They are never printed.
Writes <out>/<SOPInstanceUID>.dcm (skipping files already present) and <out>/index.csv.
"""
import argparse, base64, csv, json, os, sys, urllib.error, urllib.request
from pathlib import Path

def load_env(path=".env"):
    if Path(path).exists():
        for line in Path(path).read_text().splitlines():
            if "=" in line and not line.lstrip().startswith("#"):
                k, v = line.split("=", 1); os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))
load_env()
user, pw = os.environ.get("ORTHANC_USER"), os.environ.get("ORTHANC_PASSWORD")
if not user or not pw: sys.exit("ORTHANC_USER / ORTHANC_PASSWORD are not set (put them in .env)")
ap = argparse.ArgumentParser(); ap.add_argument("--url", default="http://localhost:8042"); ap.add_argument("--out", default="data/orthanc")
ap.add_argument("--limit", type=int, default=0, help="download at most N instances (0 = all)")
a = ap.parse_args()
if not a.url.startswith(("http://localhost", "http://127.0.0.1")): sys.exit("refusing a non-local server; patient data must not leave this machine")
auth = "Basic " + base64.b64encode(f"{user}:{pw}".encode()).decode()

def get(path, raw=False):
    req = urllib.request.Request(a.url + path, headers={"Authorization": auth}, method="GET")
    try:
        with urllib.request.urlopen(req, timeout=30) as r: b = r.read()
    except urllib.error.HTTPError as e: sys.exit(f"GET {path} failed: HTTP {e.code}")
    except urllib.error.URLError as e: sys.exit(f"cannot reach {a.url}: {e.reason}")
    return b if raw else json.loads(b)

st = get("/statistics")
print(f"server: {st['CountPatients']} patients, {st['CountStudies']} studies, {st['CountSeries']} series, {st['CountInstances']} instances ({st['TotalDiskSizeMB']} MB)")
out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
rows, new = [], 0
for i, iid in enumerate(get("/instances")):
    if a.limit and i >= a.limit: break
    t = get(f"/instances/{iid}/simplified-tags")
    f = out / f"{t['SOPInstanceUID']}.dcm"
    if not f.exists(): f.write_bytes(get(f"/instances/{iid}/file", raw=True)); new += 1
    rows.append(dict(file=f.name, patient_id=t.get("PatientID", ""), study_date=t.get("StudyDate", ""), modality=t.get("Modality", ""), view_position=t.get("ViewPosition", "")))
with open(out / "index.csv", "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
print(f"{len(rows)} instances indexed, {new} newly downloaded to {out}/")
