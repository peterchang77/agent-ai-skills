---
role: use-secrets
title: Use a secret safely
kind: advanced
summary: Store a key in an environment file that Git ignores, load it from code, and show that it never appears in the repository or the transcript.
time: 7 min
teaches: [secrets, tools, version-control]
needs: [commit-work]
---

After this step you will know a safe, simple pattern for giving a script a key or password, and how to check that it did not leak.

**Before you start:** a project in Git, and a throwaway or limited key for a service you are allowed to use ([Setup](setup:)). Never use your personal account key.

## Background

The aim is to keep the secret out of code, prompts, and Git ([Secrets](concept:secrets)). The standard pattern: put it in an **environment variable**, usually loaded from a `.env` file that is listed in
`.gitignore`, and have the code read it. The agent should never need to print it.

## General approach

1. **Create the file yourself**, outside the conversation, so the key never passes through the model:

```bash
printf 'API_KEY=paste-your-key-here\n' > .env     # then edit it in a text editor
chmod 600 .env                                       # readable only by you
```

2. **Ask the agent to wire it up without seeing it:**

```text
Make scripts/<tool>.py read API_KEY from the environment (load it from .env if present). Never print or log it. Make sure .env is in .gitignore. Do not open or display .env.
```

3. **Check:** `git status` must not list `.env`; search the repository for the key text; run the tool and confirm it works.

Add "never print, log, or commit credentials; do not open .env" to `AGENTS.md`.

<!-- example -->

## What to check

- `.env` is ignored by Git and has restricted permissions.
- The key does not appear in any committed file, in the transcript, or in logs.
- The tool fails with a clear message when the key is missing.

## If the key leaks

Revoke it, replace it, check the logs for use you did not make, and only then clean up the history ([Secrets](concept:secrets)).
