---
role: use-secrets
title: Use a secret safely
kind: advanced
summary: Configure API credentials securely via restricted .env environment files and .gitignore, preventing secret leakage into transcripts and version control.
time: 7 min
teaches: [secrets, tools, version-control]
needs: [commit-work]
---

In this advanced exercise, you configure access credentials for external APIs using local environment files, load tokens securely in Python scripts, and verify that credentials never enter repository commits or session transcripts.

**Before you start:** A project managed in Git, and a dedicated, scoped API key for an authorized service ([Setup](setup:)). Never use primary personal credentials.

## Background

The primary security objective is keeping authentication tokens out of source code, prompts, and version control ([Secrets](concept:secrets)). The standard pattern is storing credentials in an **environment variable**, loaded locally from a `.env` configuration file excluded by `.gitignore`. The agent writes code to access the environment variable without ever reading or displaying the secret string.

## General methodology

1. **Create the credential file directly:** Initialize the configuration file outside the agent conversation so the secret string never enters the model context:

```bash
printf 'API_KEY=paste-your-token-here\n' > .env     # populate key in local text editor
chmod 600 .env                                     # restrict read/write permissions to user only
```

2. **Direct the agent to integrate the variable blindly:**

```text
Update scripts/<tool>.py to read API_KEY from environment variables (loading from .env via python-dotenv if present).
Never print, echo, or log the key string to stdout or stderr.
Verify that .env is explicitly listed in .gitignore.
Do not open, read, or print the contents of .env.
```

3. **Verify isolation:** Confirm that `git status` ignores `.env`, search repository files for the secret string, and run the script to confirm successful API authentication.

Append a standing security rule to `AGENTS.md`: *"Never print, log, or commit authentication credentials; do not inspect .env."*

<!-- example -->

## Verification criteria

- **Git exclusion verified:** The `.env` file does not appear in `git status` and file permissions are restricted (`chmod 600`).
- **Zero credential leakage:** The secret string does not appear in any committed file, transcript log, or console output.
- **Graceful error handling:** The script fails with an informative error message if the environment variable is absent.

## Incident response for credential exposure

If a credential is inadvertently printed to console output or committed to Git, immediately revoke and rotate the token within the provider management console before cleaning repository history ([Secrets](concept:secrets)).
