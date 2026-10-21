---
role: use-secrets
scenario: imaging
starts_from: the committed project from the previous step
produces: "`.env` (ignored), a tool that reads the key"
prompt: |
  Make scripts/classify_reports.py (a stub for now) read LLM_API_KEY from the environment, loading it from .env if present. Never print or log it. Make sure
  .env is in .gitignore. Do not open or display .env. Then run `git status` and show me the result.
---

**Used in:** the bulk-classification step, which needs a key for a language-model service. Use a key your institution approves for the data you will send ([Privacy](concept:privacy)). The radiology reports in this material are synthetic, so any approved endpoint works. Real reports
contain patient information and are usually not allowed to leave your institution's systems.

**What you should see.** `git status` does not list `.env`. The script exits with a message such as "LLM_API_KEY is not set" when the file is absent.

**Test the guard.** Temporarily rename `.env`, run the script, and confirm the clear failure. Then restore it.
