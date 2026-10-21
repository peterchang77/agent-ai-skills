---
role: run-model
scenario: imaging
starts_from: the `cohort` checkpoint
produces: "`scripts/run_model.py`, `out/my_scores.csv`"
prompt: |
  I want to reproduce score_all in out/cohort.csv by running the primary model myself on the CPU: the TorchXRayVision DenseNet121 with weights densenet121-res224-all, output "Pneumothorax", on the cleaned images in data/clean/images/.
  First tell me which packages and weights you would install, roughly how large they are, and where they would go (use CPU-only PyTorch, inside this project's environment), and wait for my approval. Then write scripts/run_model.py that prepares each image as the library documents
  (normalize to its expected range, one channel, 224 x 224), switches off the library's rescaling around each model's operating point, turns the raw output into a probability with the sigmoid, and writes out/my_scores.csv with my score next to the score in out/cohort.csv.
  Report the correlation and the largest difference, list every image that differs by more than 0.001, and explain each one.
---

**Files used:** `out/cohort.csv` (203 patients), `data/clean/images/`.

**Reference result (primary model, all 203 images, on a CPU):** the correlation between your scores and the kit's is about **0.993**, the median difference is zero, and **198 of 203** scores agree to within 0.001. The run takes from under a minute on a many-core machine to a few minutes on a laptop.
The five that differ, and why:

| Image | Mine vs kit | Why |
|---|---|---|
| `img_0201`, `img_0113`, `img_0273` | 0.006 vs 0.009, 0.053 vs 0.070, 0.027 vs 0.030 | The cleaning step blacked out burned-in patient text, so the pixels differ from the images the kit's scores came from |
| `img_0107`, `img_0279` | 0.032 vs 0.063, 0.0025 vs 0.001 | These are follow-up images added to the kit; their kit scores are the original image's score plus noise, **not** real model output (the data dictionary says follow-up images are synthetic) |

A good agent finds the explanation by looking at the cleaning manifest and the image headers. A poor one says "rounding" or adjusts the pipeline until the numbers agree. If you ask for the other three models too (`--models all,chex,nih,pc`), the same kind of five or fewer differ, and the run takes about four times as long.

**Check it.** Recompute the AUC of your scores against the labels: it should be about 0.78, the same as the evaluation. The weights are downloaded from the library's release page on first use (about 30 MB per model), so the first run needs a network connection.

**Things to try**

- Run on the original `images/` instead of `data/clean/images/` and see which images change by a large amount. The ones that were inverted or tagged MONOCHROME1 are the clearest case of why cleaning comes before scoring.
- Ask: `Which preprocessing choices would change a score by more than 0.01?`

A reference version is `scenarios/imaging/reference/run_model.py`.
