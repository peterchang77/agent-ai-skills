---
id: secrets
title: Secrets — passwords, keys, and tokens
short: Secrets
themes: [recursive-ai]
related: [privacy, sandboxing, tools, version-control]
blurb: A secret is anything that grants access. Keep it out of prompts, transcripts, and Git, and know what to do when one leaks.
---

A **secret** is anything that grants access: a password, an API key, an access token, a database credential, a private key.

## Why agents raise the stakes

An agent reads files and prints output, and everything it sees goes into the session transcript and to the model
provider. A secret in a file the agent reads, or in a command it runs, can end up in several places you did not intend.

## Getting started quickly (and safely enough)

Often the fastest way to connect an agent to a service is to give it the URL and a key, and let it work out the
interface. That is a reasonable way to start, with these conditions:

- Use a **throwaway, read-only, or limited** key for the first session.
- Treat it as **already exposed**, and replace it afterwards with a properly stored one.

## The standard pattern

Keep the secret out of code and prompts. Store it in an **environment variable**, usually loaded from a `.env` file
that is excluded from Git, and have the code read it.

```text
.env           API_KEY=...        (never committed; the agent should not print it)
.gitignore     .env               (so it cannot be committed by accident)
code           reads os.environ["API_KEY"]
```

A walk-through is in [Use secrets safely](beat:use-secrets). For anything shared or long-lived, use a secrets manager
or your platform's credential system.

## Good habits

- **Least privilege.** Read-only where possible, limited to the task, with an expiry and a spending cap if the service allows.
- **A dedicated key for the agent.** Do not hand over your personal account. A separate key can be revoked without disrupting you.
- **A rule for the agent.** Put "never print, log, or commit credentials" in `AGENTS.md` ([Memory](concept:memory)).
- **Check before you commit.** Review `git status` and the diff, and use secret-scanning tools where available.

## If a secret leaks

Deleting the file or the Git history is **not enough**; assume it was copied. In order:

1. **Revoke** the secret at the provider.
2. **Replace** it with a new one, stored properly.
3. **Check the logs** for use you did not make.
4. Then clean the history or transcript as a secondary step.

## Demo it

<!-- demos -->
