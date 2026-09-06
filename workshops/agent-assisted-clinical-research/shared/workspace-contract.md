# Cloud workspace contract

The instructor provisions this contract before the workshop. Paths may be changed for a deployment, but the workspace must document the actual values in its landing-page README or environment banner.

## Required environment variables

```bash
# Data API / download credentials. Set only if the workspace needs them.
REDIVIS_CREDENTIALS_PATH=~/.redivis/python_credentials

# Approved local or institutionally approved OpenAI-compatible endpoint.
WORKSHOP_LLM_BASE_URL=https://approved-endpoint.example/v1
WORKSHOP_LLM_API_KEY=...                 # secret; never write to a repository
WORKSHOP_LLM_MODEL=approved-model-id
```

No participant task should print, commit, or embed a secret. Programs should fail with an actionable message when required variables are absent.

## Required prepared resources

- A dataset root, or a documented and tested download route that each participant can use.
- Enough storage for the assigned exercise and a stated quota/time estimate.
- Python 3.12+ and `uv`, with ordinary data-science packages available or installable from pinned dependencies.
- Network access from the cloud environment to the approved data API and LLM endpoint.
- A writable per-participant project directory and a Git ignore rule for `data/`, `outputs/`, `.env`, and logs containing protected content.
- An exact dataset release/table reference and a data dictionary or endpoint discovery path.

## Recommended layout in each participant workspace

```text
project/
  workshop/                 # checked-out archive
  data/                     # protected, ignored
    raw/
    derived/
  outputs/                  # ignored
  src/                      # participant/agent-created code
  .env                      # ignored; optional local variables
```

## Preflight conducted by the instructor

1. Start a fresh cloud session with the participant identity.
2. Verify a small data API request or the prepared data mount.
3. Verify an LLM health request using a non-sensitive test message; do not expose the key.
4. Confirm a 10-record report abstraction call completes and can write an ignored output directory.
5. Confirm the initial environment has no real protected data tracked by Git.
6. Publish the single workshop-launch URL and a short recovery route for failed sessions.

## Endpoint use policy

Only send the minimum approved text required for the assigned abstraction task. Never send image pixels, direct identifiers, or broader source tables merely because an endpoint can accept them. Persist request metadata and output provenance in protected/ignored storage.
