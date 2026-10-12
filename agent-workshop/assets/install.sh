#!/usr/bin/env bash
# Workshop installer: downloads the toy dataset and installs an agent harness (Kiro CLI).
#
#   curl -fsSL https://peterchang77.github.io/agent-ai-skills/install.sh | bash
#   curl -fsSL .../install.sh | bash -s -- --dir ~/work --yes
#
# Safe to re-run: files that already match are skipped, files you changed are never
# overwritten unless you pass --force (and then the old copy is backed up first).
set -euo pipefail

BASE_URL="${WORKSHOP_BASE_URL:-https://peterchang77.github.io/agent-ai-skills}"
KIRO_INSTALL_URL="${KIRO_INSTALL_URL:-https://cli.kiro.dev/install}"
DIR="" ; YES=0 ; FORCE=0 ; AGENT=ask ; CHECKPOINTS=ask

usage() { cat <<'U'
Usage: install.sh [options]
  --dir PATH       your project folder for the data (default: ~/workshop-demo)
  --checkpoints    also download the checkpoints, to <folder>-checkpoints
                   (catch-up copies of each stage)
  --no-agent       do not install the agent (Kiro CLI)
  --force          overwrite files that differ from the published version
                   (existing copies are backed up to <folder>-backup-<time>)
  -y, --yes        accept defaults, no prompts
  -h, --help       show this help
U
}
while [ $# -gt 0 ]; do
  case "$1" in
    --dir) DIR="${2:?--dir needs a path}"; shift 2 ;;
    --checkpoints) CHECKPOINTS=yes; shift ;;
    --no-agent) AGENT=no; shift ;;
    --force) FORCE=1; shift ;;
    -y|--yes) YES=1; shift ;;
    -h|--help) usage; exit 0 ;;
    *) echo "Unknown option: $1" >&2; usage >&2; exit 2 ;;
  esac
done

say() { printf '%s\n' "$*"; }
die() { printf 'Error: %s\n' "$*" >&2; exit 1; }

# Prompts read from the terminal so they still work under `curl | bash`.
# With no terminal (or --yes) the default is used.
ask() { # ask "question" default -> echoes answer
  local q="$1" def="$2" ans=""
  if [ "$YES" = 1 ] || ! { : </dev/tty; } 2>/dev/null; then echo "$def"; return; fi
  printf '%s [%s]: ' "$q" "$def" >/dev/tty
  read -r ans </dev/tty || true
  echo "${ans:-$def}"
}
confirm() { # confirm "question" default(y/n)
  local a; a="$(ask "$1 (y/n)" "$2")"
  case "$a" in y|Y|yes|YES) return 0 ;; *) return 1 ;; esac
}

command -v curl >/dev/null || die "curl is required."
if command -v sha256sum >/dev/null; then sha() { sha256sum "$1" | cut -d' ' -f1; }
elif command -v shasum >/dev/null; then sha() { shasum -a 256 "$1" | cut -d' ' -f1; }
else die "sha256sum or shasum is required."; fi
unzip_to() { # zip dest
  if command -v unzip >/dev/null; then unzip -q "$1" -d "$2"
  elif command -v python3 >/dev/null; then python3 -m zipfile -e "$1" "$2"
  else die "unzip or python3 is required to extract the data."; fi
}

TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT
STAMP="$(date +%Y%m%d-%H%M%S)"; BACKUP=""

# fetch_set NAME DEST : make DEST match the published set NAME without clobbering local work
fetch_set() {
  local name="$1" dest="$2" new=0 same=0 kept=0 replaced=0 path want have
  curl -fsSL "$BASE_URL/downloads/$name.manifest" -o "$TMP/$name.manifest" \
    || die "could not download $BASE_URL/downloads/$name.manifest"

  # Compare what is on disk with the manifest before downloading anything big.
  local need=0
  while read -r want path; do
    if [ ! -f "$dest/$path" ]; then need=1; break; fi
    [ "$(sha "$dest/$path")" = "$want" ] || need=1
  done < "$TMP/$name.manifest"
  if [ "$need" = 0 ]; then say "  $name: already up to date in $dest (nothing to download)"; return; fi

  curl -fsSL "$BASE_URL/downloads/$name.zip" -o "$TMP/$name.zip" || die "download failed: $name.zip"
  curl -fsSL "$BASE_URL/downloads/$name.zip.sha256" -o "$TMP/$name.zip.sha256" || die "download failed: $name.zip.sha256"
  [ "$(sha "$TMP/$name.zip")" = "$(tr -d ' \n' < "$TMP/$name.zip.sha256")" ] \
    || die "$name.zip is incomplete or corrupt (checksum mismatch). Try again."
  mkdir -p "$TMP/$name" "$dest"; unzip_to "$TMP/$name.zip" "$TMP/$name"

  while read -r want path; do
    if [ ! -e "$dest/$path" ]; then
      mkdir -p "$dest/$(dirname "$path")"; cp "$TMP/$name/$path" "$dest/$path"; new=$((new+1))
    else
      have="$(sha "$dest/$path")"
      if [ "$have" = "$want" ]; then same=$((same+1))
      elif [ "$FORCE" = 1 ]; then
        mkdir -p "$BACKUP/$name/$(dirname "$path")"
        mv "$dest/$path" "$BACKUP/$name/$path"
        cp "$TMP/$name/$path" "$dest/$path"; replaced=$((replaced+1))
      else kept=$((kept+1)); say "  kept your version of $path (differs; use --force to replace)"
      fi
    fi
  done < "$TMP/$name.manifest"
  say "  $name: $new added, $same unchanged, $replaced replaced, $kept kept"
  [ "$replaced" -gt 0 ] && say "  replaced files were backed up to $BACKUP/$name/"
  return 0
}

say "Workshop installer"
say

# 1. Data
[ -n "$DIR" ] || DIR="$(ask "Which folder should the workshop data go in?" "$HOME/workshop-demo")"
DIR="${DIR/#\~/$HOME}"
mkdir -p "$DIR"; DIR="$(cd "$DIR" && pwd)"
BACKUP="$DIR-backup-$STAMP"
say "Project folder: $DIR"
fetch_set toy-kit "$DIR"
if [ "$CHECKPOINTS" = ask ]; then
  if confirm "Also download the checkpoints (catch-up copies of each stage)?" n; then CHECKPOINTS=yes; else CHECKPOINTS=no; fi
fi
[ "$CHECKPOINTS" = yes ] && fetch_set toy-checkpoints "$DIR-checkpoints"
say

# 2. Agent harness
if command -v kiro-cli >/dev/null 2>&1; then
  say "Agent: kiro-cli is already installed ($(command -v kiro-cli)); skipping."
elif [ "$AGENT" = no ]; then
  say "Agent: skipped (--no-agent)."
else
  say "Agent: Kiro CLI is not installed."
  say "  This runs the vendor's installer: curl -fsSL $KIRO_INSTALL_URL | bash"
  say "  (it is fetched live and not checked by this script)"
  if [ "$YES" = 1 ] || confirm "Install Kiro CLI now?" y; then
    curl -fsSL "$KIRO_INSTALL_URL" | bash
    say "Agent: install finished. Open a new shell if 'kiro-cli' is not found."
  else
    say "Agent: skipped."
  fi
fi

say
say "Done. Next:  cd \"$DIR\" && kiro-cli"
say "Optional: some steps use 'uv' (https://docs.astral.sh/uv/) to run Python scripts."
