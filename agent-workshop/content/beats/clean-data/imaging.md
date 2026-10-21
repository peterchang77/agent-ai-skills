---
role: clean-data
scenario: imaging
starts_from: the imaging kit plus `notes/cleaning-decisions.md` and `out/review.csv` (restore the `cleaned` checkpoint and delete `scripts/`, `data/clean/` and `out/cleaning_flow.md` if you want to rebuild from scratch)
produces: "`scripts/clean_images.py`, `data/clean/` (cleaned images, `manifest.csv`, `labels_clean.csv`, `scores_clean.csv`), `out/cleaning_flow.md`"
prompt: |
  Implement the decisions in notes/cleaning-decisions.md as scripts/clean_images.py. It must read images/, labels.csv, model_scores.csv and my out/review.csv, and write cleaned copies to data/clean/images/ without modifying any original.
  When an image's pixels change, write it uncompressed rather than re-encoding the JPEG. Write data/clean/manifest.csv (one row per input file: kept, fixed or excluded, and why), labels_clean.csv and scores_clean.csv, and out/cleaning_flow.md
  with the starting count, the files removed or changed by each rule, and the final count. Run it and confirm the numbers add up.
---

**Files used:** `images/*.dcm`, `labels.csv`, `model_scores.csv`, `notes/cleaning-decisions.md`, `out/review.csv`.

**Reference flow table (with the reference decisions)**

| Step | Files |
|---|---|
| Image files received | 283 |
| Unreadable (2), not a chest radiograph (3), wrong matrix (4), mirrored (4) removed | 270 |
| Duplicates removed: 6 identical, 2 same-pixel copies, 2 conflicting pairs (4 files) | 258 |
| **Cleaned images** | **258** |

Of the 283 files in the manifest, 194 are kept unchanged, 64 are fixed (pixels, header or both), and 25 are excluded. Check: 283 − 13 − 12 = 258. All 258 images have a normalized label, and 247 have all four scores.
Five images still have a blank sex, which cannot be recovered.

**Check the work.** Count the files in `data/clean/images/`; compare with the flow table. Open a few cleaned images and the ones listed as fixed (the viewer can show them). Confirm that the files in `images/` are
unchanged. If your decisions differ from the reference, your table will differ; the check is that it matches **your** decisions.

The reference script is `scenarios/imaging/checkpoints/cleaned/scripts/clean_images.py`. Compare yours to it only after you have checked yours.
