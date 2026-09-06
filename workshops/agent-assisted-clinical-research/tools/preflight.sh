#!/usr/bin/env bash
# Check workshop prerequisites without revealing secret values.
set -euo pipefail

missing=0
for command in uv python3; do
  if command -v "$command" >/dev/null 2>&1; then
    printf 'found command: %s\n' "$command"
  else
    printf 'missing command: %s\n' "$command" >&2
    missing=1
  fi
done

for variable in WORKSHOP_LLM_BASE_URL WORKSHOP_LLM_API_KEY WORKSHOP_LLM_MODEL; do
  if [[ -n "${!variable:-}" ]]; then
    printf 'set environment variable: %s\n' "$variable"
  else
    printf 'missing environment variable: %s\n' "$variable" >&2
    missing=1
  fi
done

if [[ $missing -ne 0 ]]; then
  printf '%s\n' 'Ask the instructor for workspace setup help; do not place credentials in source files.' >&2
  exit 1
fi

printf '%s\n' 'Workshop preflight passed. Secret values were not displayed.'
