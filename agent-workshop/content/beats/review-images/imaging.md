---
role: review-images
scenario: imaging
starts_from: the imaging kit and your `out/profile.md`
produces: "`scripts/flag_images.py`, `out/flags.csv`, `scripts/make_viewer.py`, `out/viewer.html`, and your `out/review.csv`"
prompt:
  - label: Flags
    text: |
      Write scripts/flag_images.py that scans images/ and writes out/flags.csv with columns file and flag. Flag: unreadable files; images that are not chest radiographs; images that are not 1024 x 1024;
      images whose PhotometricInterpretation is MONOCHROME1; images that look inverted even though they are tagged MONOCHROME2 (use a measurable brightness check and explain it); images with burned-in text in
      the top-left corner. Print a count per flag, and tell me which problems this cannot find.
  - label: Viewer
    text: |
      Write scripts/make_viewer.py that builds one self-contained, offline HTML page, out/viewer.html, from images/ and out/flags.csv: a thumbnail grid for all images, a filter by flag, a larger view with the DICOM header
      on click, and confirm / reject / unsure buttons that can be exported as review.csv. Show MONOCHROME1 images the way a viewer would. Do not embed labels or model scores. Tell me how to open it.
---

**Files used:** `images/*.dcm`, `out/profile.md`.

**What you should see (flags).** Roughly: 2 unreadable, 3 not chest, 4 at 512 x 512, 6 MONOCHROME1, 5 with burned-in text, and a handful of suspected inversions: the 4 real ones plus about one
false alarm (a genuine image with unusual contrast). The mirrored images are **not** flagged, and the agent should say so.

**What you do.** Open `out/viewer.html` and review. Filter to each flag, confirm the real ones and reject the false alarm. Then scan the whole grid for what code could not find: four images are mirrored (look at
the burned-in letters, which read backwards, and at which side the heart is on). Mark them and export `review.csv`. A reference version is in `scenarios/imaging/checkpoints/cleaned/out/review.csv`.

**Reference answers**

| Issue | In the kit | Found by code | Needs you |
|---|---|---|---|
| Inverted, wrong tag | 4 | 4 flagged (plus about 1 false alarm) | Confirm and reject |
| Mirrored left-right | 4 | 0 | Find by eye |
| Burned-in text | 5 | 5 | Confirm |

**Check the tool.** Open the HTML source and confirm it contains no web links and no labels or scores. In a headless setting, you can ask the agent to take a screenshot of the page to check that it renders;
the agent can then read that picture only if its model supports images.

A reference viewer is in `scenarios/imaging/reference/make_viewer.py`. Compare yours to it only after checking yours.
