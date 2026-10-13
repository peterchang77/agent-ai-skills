---
id: secrets
title: Secrets — passwords, keys, and tokens
short: Secrets
themes: [recursive-ai]
related: [privacy, sandboxing, tools, version-control]
blurb: Credentials must never enter prompts, session logs, or version control. Use isolated environment variables and enforce immediate revocation protocols if exposed.
---

In computational research, access credentials—such as database passwords, API tokens, cloud keys, and private SSH keys—authenticate requests to external data sources and computing clusters. Managing these credentials securely requires heightened vigilance when deploying coding agents in research workflows.

## Exposure vectors in agent workflows

Because an agent inspects filesystem contents and executes terminal commands, any credential exposed in plain text can easily leak across multiple channels:

- **Model context payloads:** Files read into working memory are transmitted to the model provider as part of the prompt sequence ([Privacy and data handling](concept:privacy)).
- **Terminal execution logs:** Commands that pass keys via inline arguments (e.g., `curl -H "Authorization: Bearer KEY"`) print the secret directly to stdout/stderr, recording it in session transcripts.
- **Persistent version control:** Scripts containing hardcoded secrets can be inadvertently committed to Git history, exposing them to repository collaborators or public remotes ([Version control](concept:version-control)).

## The standard secret management pattern

Never hardcode authentication keys directly into prompts or analysis scripts. Instead, inject credentials via **environment variables**, typically loaded from a local `.env` configuration file excluded from version control:

```text
.env          API_KEY=...                (local configuration; excluded from version control)
.gitignore    .env                       (prevents accidental Git staging)
script.py     os.environ.get("API_KEY")  (reads the variable into runtime memory)
```

The [Use secrets safely](beat:use-secrets) exercise walks through configuring this pattern. For production workflows or shared institutional clusters, use dedicated secrets managers (such as HashiCorp Vault, AWS Secrets Manager, or system keyrings).

## Best practices for credential safety

- **Enforce the principle of least privilege:** Provision scoped, read-only API keys restricted to the specific endpoints required for the task. Configure expiration dates and spending caps where supported.
- **Provision dedicated machine credentials:** Never provide an agent with your personal account credentials. Creating a distinct API token ensures access can be revoked independently without disrupting your primary workflows.
- **Codify standing instructions in `AGENTS.md`:** Explicitly instruct the agent never to print, echo, or commit credential strings to files or terminal output ([Memory](concept:memory)).
- **Pre-commit audit habits:** Review `git status` and staged diffs before executing commits, and employ automated secret scanners (such as `trufflehog` or `git-secrets`) to catch accidental exposures.

## Incident response for credential leakage

If a credential is accidentally exposed in a prompt, printed to console logs, or committed to Git, **deleting the line or rewriting repository history is insufficient**—assume the credential has been compromised. Execute the following incident response steps in order:

1. **Revoke immediately:** Invalidate the exposed token within the provider's management console to stop further access.
2. **Rotate and provision:** Generate a new credential and configure it using an environment variable.
3. **Audit access logs:** Review the provider's access logs to determine whether unauthorized requests occurred during the exposure window.
4. **Purge local and remote traces:** Remove the exposed string from local session transcripts and rewrite affected Git commits as a secondary cleanup step.

## Demo it

<!-- demos -->
