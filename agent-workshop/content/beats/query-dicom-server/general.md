---
role: query-dicom-server
title: Retrieve images from a DICOM server
kind: advanced
summary: Direct the agent to read from an image server through its web interface, read-only and with credentials kept out of the transcript, and reconcile what it finds with the files you already have.
time: 12 min
teaches: [inputs, secrets, privacy]
needs: [use-secrets]
---

In practice, images often live in a server, not in a folder. Here you direct the agent to use the server's web interface (a REST API) to list and download studies, with three rules: read-only, credentials never shown, and nothing leaves the machine. Then you check that what arrived agrees with what you expected.

**Before you start:** A project with a `.env` file for credentials and `.env` in `.gitignore` ([Use a secret safely](beat:use-secrets)), and a DICOM server you are allowed to read from. The example uses a free local server that you start yourself. This step is optional.

## Background

A **PACS** (picture archiving and communication system) stores medical images and serves them over network protocols. **Orthanc** is a free, open-source DICOM server that is also widely used for research and teaching. Besides the standard DICOM network protocol, it offers a **REST API**: ordinary web requests such as `GET /studies` return lists as JSON, and `GET /instances/<id>/file` returns the original DICOM file.

Reading from a server is a different risk from reading a folder ([Inputs](concept:inputs)):

- **Read-only.** A `GET` request cannot change the server. Requests that create, modify or delete (`POST`, `PUT`, `DELETE`) can. Tell the agent to use `GET` only, and check.
- **Credentials.** The server asks for a username and password. They belong in `.env`, never in a prompt, the transcript or Git ([Secrets](concept:secrets)).
- **Where the data goes.** Retrieved images can contain patient information ([Privacy](concept:privacy)). A real hospital server should be reached only from approved machines, with approval for what you do. The example server accepts connections from this computer only.

Counts also deserve a check. A server **de-duplicates** by unique image ID and rejects files it cannot parse, so the number of images in a server can be smaller than the number of files that were sent to it.

## General methodology

State the rules before the task, and ask for a reconciliation, not just a download:

```text
A DICOM server (Orthanc) is running at <url>. Use it read-only: GET requests only, nothing may be created, changed or deleted. The credentials are in .env as <USER_VAR> and <PASSWORD_VAR>; do not open, print or log them, and refuse any server that is not <local>.
Write <scripts/fetch.py> using only the standard library that (1) prints the server's counts of patients, studies, series and instances, (2) downloads every instance to <data/server/> (skipping files already there), and (3) writes an index with the identifiers I will need.
Then compare the counts with the <N> files I have in <folder> and explain every difference.
```

<!-- example -->

## Verification criteria

- **GET only.** The script contains no other request type; the agent can show you where it checks this.
- **No secret exposure.** Credentials are not in the script, the output or the transcript, and `git status` does not list `.env`.
- **Local only.** The script refuses a server address that is not the approved one.
- **Counts reconciled.** Each difference between what you expected and what arrived has an explanation you can verify.
- **Bytes match.** A downloaded file is identical to the original (compare a checksum of one pair).

## Common pitfalls

| Symptom | Underlying cause | Resolution |
|---|---|---|
| `401 Unauthorized` | The credentials were not loaded, or are wrong | Check that `.env` has the variable names the script reads (without printing the values) |
| The agent proposes uploading or deleting something | The task was described loosely | Restate the read-only rule; refuse any non-`GET` request |
| Fewer images than files | The server de-duplicates and rejects unreadable files | Account for each difference before you trust the count |
| More "patients" than expected | The server identifies patients by the ID string; variants of one ID become separate patients | This is a data-quality finding, not a server error |
