---
role: look-at-images
scenario: imaging
starts_from: the imaging kit and the environment from the previous step
produces: "`out/contact_sheet.png` (or `.html`) and a metadata summary"
prompt: |
  Read the DICOM headers (not the pixels yet) of the files in images/ and summarize them: how many files, which modality, the view positions, the sex and age fields, the image size, and how
  the pixel values are meant to be interpreted. Then save a contact sheet of 24 randomly chosen images, each labelled with its file name, as out/contact_sheet.png, and tell me how to open it.
  Do not modify anything in images/. Tell me which of your statements came from the headers and which from the pixels.
---

**Files used:** `images/*.dcm`.

**What you should see in the headers.** About 283 files; almost all `CR` (computed radiography) with a few `DX`; `PA` and `AP` views with some blank; 1024 x 1024 images
for nearly all; sex, age and patient ID fields that are mostly clean but not entirely. A good agent will say that some headers are inconsistent and that some files cannot be read.
It should say that it has not yet checked the pixels (it has not looked at the pictures).

**What you should see in the contact sheet.** Frontal chest radiographs, mostly dark lungs on a lighter body. Several show burned-in letters such as "AP" or "PORTABLE", and some show
tubes or drains. With a random sample of 24 you may or may not see a problem image. Whether you do is part of the lesson: a quick look does not replace a systematic audit.

**Check it yourself.** Open the sheet and compare with the agent's description. If your agent can view images, ask it what it sees and compare. Note that the contact sheet labels
come from file names, and the file names say nothing about the diagnosis.

If your environment cannot show an image directly, ask for a self-contained HTML page instead and open it in a browser. In a headless or remote setting, serve the folder with
`python3 -m http.server` and forward the port.
