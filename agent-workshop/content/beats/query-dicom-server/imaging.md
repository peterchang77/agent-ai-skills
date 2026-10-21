---
role: query-dicom-server
scenario: imaging
starts_from: the committed project with `.env` set up, plus a local Orthanc server loaded with the kit's images (see below)
produces: "`scripts/orthanc_fetch.py`, `data/orthanc/` (downloaded DICOM files and `index.csv`)"
prompt: |
  An Orthanc DICOM server is running at http://localhost:8042. Use it read-only: GET requests only, nothing may be created, changed or deleted. The credentials are in .env as ORTHANC_USER and ORTHANC_PASSWORD; do not open, print or log them, and refuse any server that is not localhost.
  Write scripts/orthanc_fetch.py using only the standard library that (1) prints the server's counts of patients, studies, series and instances, (2) downloads every instance to data/orthanc/<SOPInstanceUID>.dcm, skipping files already there, and (3) writes data/orthanc/index.csv with the file name, patient ID, study date, modality and view position.
  Then compare the counts with the 283 files in images/ and explain every difference.
---

**Files used:** `images/*.dcm` (already in your project) and a local Orthanc server.

**Start the server (once).** If you used the quickstart installer, the files under `scenarios/imaging/` named below are in the `-tools` folder next to your project folder (for example `~/workshop-imaging-tools/`). Orthanc runs on Linux, macOS and Windows. Use any one of these. The configuration in `scenarios/imaging/extras/orthanc/orthanc.json` enables a password, allows connections from this computer only, and turns off scripting.

```bash
# Option A: a single downloaded program (Linux x86-64; no installation or administrator rights)
curl -L -o Orthanc https://orthanc.uclouvain.be/downloads/linux-standard-base/orthanc/1.12.4/Orthanc && chmod +x Orthanc
./Orthanc scenarios/imaging/extras/orthanc/orthanc.json

# Option B: Docker (any system); the port is published on localhost only
docker run --rm -p 127.0.0.1:8042:8042 -e ORTHANC__AUTHENTICATION_ENABLED=true \
  -e ORTHANC__REGISTERED_USERS='{"workshop": "workshop-demo-only"}' orthancteam/orthanc
```

On Windows or macOS you can instead install Orthanc from [orthanc-server.com](https://www.orthanc-server.com/) and copy the settings from `orthanc.json` into its configuration. Option A is the one tested while preparing this material (Orthanc 1.12.4 on Linux); the Docker and installer routes are not.

Then load the kit's images with the loader script, and put the demo credentials in `.env` (the values are in `orthanc.json`; they protect nothing but this local demo):

```bash
python3 scenarios/imaging/extras/orthanc/load_kit.py ~/workshop-imaging/images
printf 'ORTHANC_USER=workshop\nORTHANC_PASSWORD=workshop-demo-only\n' >> ~/workshop-imaging/.env
```

The loader should report `stored 275, already stored 6, rejected 2`. Open `http://localhost:8042/` in a browser (user `workshop`) to see Orthanc's own explorer.

**Reference result.** The server reports **255 patients, 275 studies, 275 series, 275 instances** (about 72 MB). The reconciliation with the 283 files in `images/`:

| Difference | Count | Why |
|---|---|---|
| Files not in the server | 8 | 2 are truncated files that Orthanc rejects, and 6 are exact duplicates that share an image ID, which it stores once |
| Patients vs studies | 255 vs 275 | 20 patients have a second (follow-up) study. Patient ID variants (upper case, a prefix, a leading space) also create separate "patients"; the same patient written two ways is counted twice |

This matches what the profile found in the files, and the downloaded files are byte-for-byte identical to the originals (compare a checksum of a few). A good agent says which of the differences it verified and which it inferred.

**Check the rules.** Search the script for `POST`, `PUT` and `DELETE` (there should be none), confirm `.env` does not appear in `git status`, and point the script at a different address to see that it refuses. A reference script is `scenarios/imaging/reference/orthanc_fetch.py`.

**Clean-up.** Stop Orthanc with Ctrl+C. Its database is the `orthanc-db` folder next to where you started it; delete it when you are done.
