#!/usr/bin/env bash
# Create an agent-safe participant copy that excludes instructor answer keys.
# Usage: bash tools/make-participant-copy.sh /absolute/or/relative/destination
set -euo pipefail

if [[ $# -ne 1 ]]; then
  printf 'Usage: %s DESTINATION_DIRECTORY\n' "${0##*/}" >&2
  exit 2
fi

source_dir=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd -P)
destination=$(realpath -m "$1")

if [[ -e "$destination" ]]; then
  printf 'Refusing to overwrite existing destination: %s\n' "$destination" >&2
  exit 1
fi

case "$destination" in
  "$source_dir"|"$source_dir"/*)
    printf 'Destination must be outside the full workshop checkout.\n' >&2
    exit 1
    ;;
esac

mkdir -p "$(dirname "$destination")"
cp -a "$source_dir" "$destination"
rm -rf "$destination/instructor-guide"

if [[ -e "$destination/instructor-guide" ]]; then
  printf 'Participant-copy creation failed: instructor guide is still present.\n' >&2
  exit 1
fi

printf 'Created participant-only workshop copy: %s\n' "$destination"
printf '%s\n' 'The instructor guide was excluded. Provide participants/agents only this copy.'
