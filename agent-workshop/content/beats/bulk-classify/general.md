---
role: bulk-classify
title: Classify many records with a language-model API
kind: advanced
summary: Write a script that calls a language-model API for each record; test on a few, estimate cost, then run, and measure accuracy on a labelled sample.
time: 12 min
teaches: [tools, costs, verification]
needs: [use-secrets]
---

After this step you will be able to process hundreds or thousands of records with a model through an API, with a cost estimate, saved partial results, and a measured accuracy.

**Before you start:** an approved API endpoint and key, set up safely ([Use a secret safely](beat:use-secrets)), and a file of records with a small labelled sample. This step costs money
and sends data to a provider ([Costs](concept:costs), [Privacy](concept:privacy)).

## Background

Chat is the wrong tool for 500 records. A script calls the model once per record, saves each result, and can be rerun. Plan for:

- **A fixed output format.** Ask for one label from a fixed list, as JSON, so the results can be parsed.
- **A test on a handful first**, then a cost estimate for all records before running everything.
- **Rate limits and retries**, and **saving partial results** so a failure does not lose work.
- **Accuracy.** Compare the model's labels against a labelled sample. An unmeasured classifier is a guess.
- **Reproducibility.** Record the model name, the prompt, and the date with the results.

## General approach

```text
Write scripts/classify_notes.py that reads <records file>, and for each record calls <the API> with a prompt asking for exactly one label from this list: <labels>,
returning JSON. Save results incrementally to <out/labels.csv> so it can resume. Add retries and a short delay between calls. Add a --limit option and a --dry-run that
prints the first prompt and an estimated cost without calling anything. Record the model name and prompt in the output.
```

Then: run `--dry-run`, run with `--limit 5`, check by eye, estimate the total, set a spending cap, and run all. Finally compare against the labelled sample.

<!-- example -->

## What to check

- The dry run printed a sensible prompt and cost estimate.
- Results saved as it ran, and a rerun resumes rather than starting over.
- Accuracy on the labelled sample is reported, with the number of records.
- No key appears in the output, logs, or repository.

## Common problems

| Symptom | Cause | Fix |
|---|---|---|
| Invalid labels in the output | The model did not follow the format | Validate against the label list; retry or mark as unparseable |
| Cost higher than estimated | Longer prompts or more retries | Re-estimate from the first batch; set a cap |
| Rate-limit errors | Calls too fast | Add delay and exponential backoff |
