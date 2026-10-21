#!/usr/bin/env python3
"""Upload the kit's DICOM files to a local Orthanc server.   python3 load_kit.py KIT/images [--url http://localhost:8042]

Standard library only. Credentials come from ORTHANC_USER / ORTHANC_PASSWORD (default: the demo values in orthanc.json).
Files Orthanc rejects (unreadable or truncated) are counted and listed, not hidden.
"""
import argparse, base64, os, sys, urllib.error, urllib.request
from pathlib import Path

ap = argparse.ArgumentParser(); ap.add_argument("folder"); ap.add_argument("--url", default="http://localhost:8042")
a = ap.parse_args()
auth = base64.b64encode(f"{os.environ.get('ORTHANC_USER', 'workshop')}:{os.environ.get('ORTHANC_PASSWORD', 'workshop-demo-only')}".encode()).decode()
ok, dup, bad = 0, 0, []
for f in sorted(Path(a.folder).glob("*.dcm")):
    req = urllib.request.Request(a.url + "/instances", data=f.read_bytes(), method="POST",
                                 headers={"Content-Type": "application/dicom", "Authorization": "Basic " + auth})
    try:
        r = urllib.request.urlopen(req)
        if b"AlreadyStored" in r.read(): dup += 1
        else: ok += 1
    except urllib.error.HTTPError as e:
        bad.append((f.name, e.code))
    except urllib.error.URLError as e:
        sys.exit(f"cannot reach {a.url}: {e.reason}. Is Orthanc running?")
print(f"stored {ok}, already stored {dup}, rejected {len(bad)}")
for n, c in bad: print(f"  rejected {n} (HTTP {c})")
