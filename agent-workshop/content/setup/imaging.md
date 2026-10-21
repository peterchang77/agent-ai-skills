---
scenario: imaging
slug: imaging
label: "Imaging: chest radiographs"
own_track: true
installer: true
retrieve: Offers to install the Python tool `uv` if it is missing, downloads the small build scripts (checksum-verified) and builds the image kit on your computer from the public sample (about 33 MB downloaded, a minute or two, the same files every time); optionally builds the checkpoints (about 0.5 GB). The scripts that some steps mention, such as `scenarios/imaging/...`, are placed in a separate `-tools` folder next to your project folder.
dir: workshop-imaging
---

A kit built around **real, public chest radiographs** (a 250-image sample from the SIIM-ACR pneumothorax challenge, de-identified before
release) with a set of synthetic problems added so there are known answers to find. It is a toy demonstration of how to direct an agent
through an AI-evaluation workflow, **not a validation study**. Everything that is not a public image (the data problems, patient
details that look real, radiology reports, follow-up images) is synthetic.

**The story.** You are the analyst. Radiology informatics is considering a pilot of an open-source AI tool that scores chest radiographs
for pneumothorax (air that has leaked into the space around the lung). Before agreeing, they want to know how well it works on a sample
of images, whether the primary model really is better than three alternatives, and whether it works equally well for different groups of
patients. The sample was assembled quickly and has not been checked.

### Get the kit

The [quickstart](#quickstart) installer builds the kit for you. The kit (about 280 files, 74 MB) is generated from the public images by a script, so it is not stored in Git. To build it by hand instead, from the repository's
`agent-workshop/` folder, with [uv](https://docs.astral.sh/uv/) installed:

```bash
uv run scenarios/imaging/build_kit.py
mkdir -p ~/workshop-imaging && cp -r scenarios/imaging/kit/. ~/workshop-imaging/
cd ~/workshop-imaging && ls
```

On Windows PowerShell:

```powershell
uv run scenarios\imaging\build_kit.py
mkdir $HOME\workshop-imaging -Force
Copy-Item -Recurse scenarios\imaging\kit\* $HOME\workshop-imaging
cd $HOME\workshop-imaging; ls
```

The first run downloads the 33 MB public image sample and caches it; later runs are offline. The result is the same every time.

| File | Format | What it is |
|---|---|---|
| `images/img_NNNN.dcm` | DICOM | About 280 chest radiographs (some with problems) |
| `labels.csv` | CSV | Reference label for each image: pneumothorax or not |
| `model_scores.csv` | CSV | Scores from four open-source AI models (`score_all` is the primary model) |
| `radiology_reports.csv` | CSV | 200 short synthetic radiology reports |
| `radiology_reports_labeled_sample.csv` | CSV | Correct category for the first 30 reports |
| `eval_protocol.docx` | DOCX | The evaluation protocol: scope, metrics, pilot bar |
| `data_dictionary.md` | MD | What each file and field means, and the models' published operating points |
| `radiology_notes.txt` | TXT | The request from radiology informatics, with five questions |

??? info "New to DICOM or to AI evaluation? Read this first."
    **DICOM** is the standard file format for medical images. Each file holds the picture (pixel data) and a *header* of named fields
    (tags) such as patient ID, view position, and how to interpret the pixel values. Problems can hide in either part: a header can be
    inconsistent, and a picture can be inverted, mirrored, or contain burned-in text.

    **AUC** (area under the ROC curve) summarizes how well a score separates positive from negative cases: 0.5 is chance and 1.0 is
    perfect. **Sensitivity** is the share of true pneumothoraces the tool flags; **specificity** is the share of normal images it
    leaves unflagged. With a small sample, every one of these numbers has a wide margin of error, so we always report an interval.

??? warning "A note on the models (read once)"
    The four models come from the open-source TorchXRayVision library and run on an ordinary CPU. These images are believed to come
    from the NIH ChestX-ray14 collection, which is part of the training data of two of the models (`score_all` and `score_nih`), so their
    numbers are likely **optimistic**. That is one more reason to treat this kit as a demonstration of the workflow, not as evidence about
    any tool.

### Checkpoints

To start a step without doing the earlier ones, build the checkpoints once (they are copies of the kit plus the work done so far) and
restore one ([how](setup:restore-a-starting-point)):

```bash
uv run scenarios/imaging/make_checkpoints.py
```

(The installer does this when you choose checkpoints. It takes a few minutes and about 0.5 GB.)

| Checkpoint (in `scenarios/imaging/checkpoints/`) | Contains |
|---|---|
| *(the kit itself)* | The original files only |
| `cleaned` | Kit + `scripts/clean_images.py`, `data/clean/` (cleaned images, manifest, labels, scores), `out/cleaning_flow.md`, `out/review.csv`, `notes/cleaning-decisions.md` |
| `cohort` | `cleaned` + `AGENTS.md`, `scripts/build_cohort.py`, `out/cohort.csv`, `out/cohort_flow.md` |
| `evaluated` | `cohort` + `scripts/evaluate.py`, `out/evaluation.md` |
| `referenced` | `evaluated` + `scripts/pubmed_refs.py`, `references.bib` (four verified PubMed entries), `refs/search-log.md`, and the citation rule in `AGENTS.md` |
| `reported` | `referenced` + `scripts/make_dashboard.py`, `out/dashboard.html`, `out/abstract.tex`, `out/abstract.pdf` |

The reference results quoted in each step come from these checkpoints. Your agent's numbers should match closely, or you should be able
to explain the difference.
