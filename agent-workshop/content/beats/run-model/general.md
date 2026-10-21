---
role: run-model
title: Run an AI model yourself, on a CPU
kind: detour
summary: Reproduce the scores you were given by running the pretrained model on your own machine, and explain every score that does not match.
time: 10 min
teaches: [environment, verification, costs]
needs: [build-cohort]
---

A table of model scores is only as trustworthy as the process that made it. In this exercise you direct the agent to run the model itself, on an ordinary computer with no GPU, and to compare the result with the scores you were given. A match is good evidence that you understand the pipeline. A mismatch is a lead worth explaining.

**Before you start:** A cohort or table of items to score, the matching input files, and the scores you were given ([Build a cohort](beat:build-cohort)). Allow a few minutes for installing the software and downloading the model weights.

## Background

A pretrained model is a set of **weights** plus the code that applies them. The same weights give different numbers if the input is prepared differently: how pixel values are scaled, how the image is resized, whether the colours are inverted, and how the raw output is turned into a probability. So "the score" is a property of the whole pipeline, not of the weights alone.

Running a model also has practical costs ([Costs](concept:costs), [Environment](concept:environment)): the software can be hundreds of megabytes (the default build of the deep-learning library bundles GPU code you do not need), the weights are downloaded the first time, and the run takes time that scales with the number of items. Models of this size run on a CPU in well under a second per image, which is plenty for a few hundred images.

Two cautions apply. First, **only run on data you are allowed to process locally**: the model runs on your machine and nothing is uploaded, but the software and weights are fetched from the internet ([Privacy](concept:privacy)). Second, a reproduced score tells you the pipeline is the same, **not** that the model is good: that is what the evaluation is for ([Verification](concept:verification)).

## General methodology

Ask for a plan first, because installing large packages is a decision you should make:

```text
I want to reproduce the scores in <table> by running <model> on <inputs> on the CPU. First tell me which packages and weights you would install, roughly how large they are, and where they would go, and wait for my approval.
Then write <scripts/run_model.py> that prepares the inputs as the library documents, runs the model, and writes <out/my_scores.csv> with my score next to the given score. Report the correlation and the largest difference, and explain
every item that differs by more than <tolerance>.
```

Ask the agent to explain mismatches rather than to tune the pipeline until they disappear.

<!-- example -->

## Verification criteria

- **Approval before installing.** The agent listed the packages and sizes and waited.
- **Scores line up item by item.** The comparison is by item (file name), not by row position.
- **Every mismatch has a stated cause**, verified by looking at that item, not guessed.
- **Same recipe stated.** The preparation steps (scaling, size, output conversion) are written down, so someone else could repeat the run.

## Common pitfalls

| Symptom | Underlying cause | Resolution |
|---|---|---|
| A multi-gigabyte install | The default build of the library includes GPU support | Ask for the CPU-only build |
| Scores are all compressed into a narrow band, or all negative | The library's own output rescaling or raw logits were used | Ask the agent what the raw output means and how it was converted |
| Scores match for most items but not for a few | The few items were changed or are synthetic | Look at each; do not average the problem away |
| The run is slow | Every item was processed one at a time, with every model | Start with a small sample and one model, then scale up |
