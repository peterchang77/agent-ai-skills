---
role: prepare-environment
scenario: imaging
starts_from: the imaging kit
produces: a `pyproject.toml`, a `.venv/` folder, and a `README.md` with a Setup section
prompt: |
  Check which of these are installed and report the version of each: python3 and uv. Then use uv to create a Python environment for this project and install
  pydicom, numpy, pillow, python-docx, and scikit-learn, pinned to the versions you install. Keep everything inside this folder. If a system-level tool is missing, tell me
  what it is and the exact command you would run, and wait for my approval. Finally, add a "Setup" section to README.md with the commands to rebuild this environment from scratch.
---

**Why these tools**

| Tool | Used for |
|---|---|
| `pydicom` | Reading DICOM headers and pixel data |
| `numpy`, `pillow` | Working with pixels and writing thumbnails and contact sheets (`pillow` also decodes the compressed images) |
| `python-docx` | Reading the evaluation protocol |
| `scikit-learn` | AUC and related metrics in the evaluation step |

**What you should see:** a version report, then a `.venv/` and `pyproject.toml` in the folder and a `README.md` with a Setup section. Your versions will differ from
anyone else's, which is why the agent pins them. Everything here runs on an ordinary CPU; no GPU is needed.

**Check it.** Ask the agent to read one image: `pydicom.dcmread("images/img_0001.dcm").pixel_array.shape` should give `(1024, 1024)`. If the agent reports it cannot decode the pixel data,
it needs `pillow` installed in the same environment.
