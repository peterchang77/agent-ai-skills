---
role: look-at-images
title: Look at the images
kind: full
summary: Have the agent read image headers and render a labelled contact sheet you can open, so that your own eyes check what the numbers say.
time: 6 min
teaches: [inputs, verification]
needs: [prepare-environment]
---

Tables can be summarized with counts. Images cannot: a count of files tells you nothing about whether the pictures are right. In this exercise you direct the agent to read image metadata and to produce a contact sheet that a person can look at, and you check the agent's description of the images against your own.

**Before you start:** A folder of image files and a Python environment that can read them ([Setup](setup:)).

## Background

Many scientific and clinical images are stored in formats that pair **pixels** with **metadata**. The metadata describes who or what the image shows, how it was made, and how to display it. Neither layer is reliable on its own: the metadata can be inconsistent, and the pixels can be wrong in ways the metadata does not mention.

Agents differ in whether they can *see* images at all. Some can open a picture and describe it; others cannot. Either way, an agent's description of an image is a claim to verify, not a measurement. The most dependable pattern is to have the agent produce an image file or web page that **you** open ([Verification](concept:verification)).

Images also cost a great deal of the agent's working memory ([Context](concept:context)). A single contact sheet of 30 small thumbnails is far cheaper than viewing 30 images one at a time, and is usually enough.

## General methodology

Ask for a metadata summary first, then a labelled contact sheet of a small, random sample, and open it yourself:

```text
List the image files in <folder> and read their metadata (not the pixels yet). Summarize the main fields: how many files, which formats, and the
distribution of the fields that describe how each image was acquired and displayed. Then save a contact sheet of <N> randomly chosen images
as <out/contact_sheet.png> (or a single self-contained HTML page), with each thumbnail labelled by its file name. Tell me how to open it.
```

Open the contact sheet in any image viewer or browser. If your agent can view images, ask it to describe what it sees, then compare with your own reading.

<!-- example -->

## Verification criteria

- **You looked at it.** The contact sheet was opened by a person, not only summarized by the agent.
- **Thumbnails are labelled.** Every thumbnail can be traced back to a file name.
- **Metadata and pixels are kept separate.** The agent says which findings came from metadata and which from pixels, and does not claim to have checked pixels it did not open.
- **Originals untouched.** Nothing was written into the image folder.

## Common pitfalls

| Symptom | Underlying cause | Resolution |
|---|---|---|
| The agent confidently describes images it never opened | It inferred from file names or metadata | Ask: *"Which of these statements came from the pixels, and which from the metadata?"* |
| The context fills up quickly | Many full-size images were loaded one by one | Ask for one downsampled contact sheet instead |
| Images look washed out, black, or inverted | The display step ignored how the file says its pixel values should be interpreted | Note it; this is exactly the kind of problem the next steps look for |
