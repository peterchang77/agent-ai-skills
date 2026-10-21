---
role: profile-data
scenario: imaging
starts_from: the imaging kit
produces: a profile report (ask the agent to save it as `out/profile.md`)
prompt: |
  Profile the files in images/ (DICOM headers, plus any pixel checks that need no human viewing), labels.csv and model_scores.csv, using data_dictionary.md. List every data-quality problem you find, with the number
  of affected files and a few example file names. Separate real errors from things that are probably fine, and say which kinds of problem you could not check without looking at the images. Do not fix or change anything.
  Save the report as out/profile.md.
---

**Files used:** `images/*.dcm`, `labels.csv`, `model_scores.csv`, `data_dictionary.md`.

**Reference results.** The kit has 283 image files. The planted problems, with counts:

| Layer | Problem | Count | Notes |
|---|---|---|---|
| Header | Patient ID written in upper case, with a leading space, or with a `SITE1-` prefix | 12 | The same patient would not match across files |
| Header | Sex as MALE/FEMALE, blank, or lower case | 15 | |
| Header | Age blank (8) or implausible, 212Y or 150Y (2) | 10 | `062Y` style ages (20) are the standard format, not errors |
| Header | ViewPosition blank | 10 | Recoverable from `SeriesDescription` ("view: AP") |
| Header | PixelSpacing missing | 6 | |
| Header | Patient name, birth date or MRN in the header | 5 | Synthetic, but treat as PHI |
| Header | Modality `DX` instead of `CR` | 10 | Both can describe a chest radiograph; the mix is an inconsistency |
| File | Unreadable (truncated) file | 2 | |
| File | Not a chest radiograph (blank, gradient, checkerboard) | 3 | Header still says CHEST |
| File | Matrix 512 x 512 instead of 1024 x 1024 | 4 | |
| Pixels | Inverted and tagged MONOCHROME1 | 6 | Honest tag; fine once the tag is honored |
| Pixels | Inverted but tagged MONOCHROME2 | 4 | Detectable by a brightness check; confirm by eye |
| Pixels | Mirrored left-right | 4 | **Not findable by code** |
| Pixels | Patient text burned into the picture | 5 | Found by a check of the top-left corner |
| Duplicates | Identical files (same SOP UID) | 6 | |
| Duplicates | Same pixels, new IDs (2 with the opposite label) | 4 | |
| Duplicates | Second study of the same patient (same patient ID, later date) | 20 | Not an error, but patients appear twice |
| Labels | Spelling variants | 18 | |
| Labels | Conflicting labels for identical pixels | 2 | |
| Labels | Labels for images that are not in the folder | 2 | |
| Scores | Logits instead of probabilities | 25 | All four columns in the row |
| Scores | Blank (5), missing row (6), file name in different case (10) | 21 | |

**Not errors.** Lossy JPEG compression; pixel spacing that varies between scanners; a mix of AP and PA; 8-bit pixels; ages written as bare numbers (`62`); real burned-in letters such as "AP" and
"PORTABLE" (not patient information); and about 19 images of patients under 18 (relevant to eligibility later, not a defect).

A good report says clearly that mirrored images cannot be found by code, and that it only suspects inversion until someone looks. If your agent finds a problem not on this list, check it: it may be a real quirk of the
public images (a few are rotated, shifted or have black margins), or a misreading.
