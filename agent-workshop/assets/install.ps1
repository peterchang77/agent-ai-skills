# Workshop installer for Windows (PowerShell): downloads the toy dataset and installs an agent harness (Kiro CLI).
# Works on Windows PowerShell 5.1 and PowerShell 7+. Mirrors install.sh.
#
#   irm https://peterchang77.github.io/agent-ai-skills/install.ps1 | iex
#
# To pass options, run it as a script block:
#   & ([scriptblock]::Create((irm https://peterchang77.github.io/agent-ai-skills/install.ps1))) -Dir C:\work -Yes
#
# Safe to re-run: files that already match are skipped, files you changed are never
# overwritten unless you pass -Force (and then the old copy is backed up first).
[CmdletBinding()]
param(
  [string]$Dir = "",       # your project folder for the data (default: ~\workshop-demo)
  [switch]$Checkpoints,    # also download the checkpoints, to <folder>-checkpoints
  [switch]$NoAgent,        # do not install the agent (Kiro CLI)
  [switch]$Force,          # overwrite files that differ (old copies backed up to <folder>-backup-<time>)
  [switch]$Yes             # accept defaults, no prompts
)
$ErrorActionPreference = "Stop"
$ProgressPreference = "SilentlyContinue"
try { [Net.ServicePointManager]::SecurityProtocol = [Net.ServicePointManager]::SecurityProtocol -bor [Net.SecurityProtocolType]::Tls12 } catch {}
Add-Type -AssemblyName System.IO.Compression.FileSystem

$BaseUrl = if ($env:WORKSHOP_BASE_URL) { $env:WORKSHOP_BASE_URL } else { "https://peterchang77.github.io/agent-ai-skills" }
$KiroUrl = if ($env:KIRO_INSTALL_URL_PS1) { $env:KIRO_INSTALL_URL_PS1 } else { "https://cli.kiro.dev/install.ps1" }

function Say($m = "") { Write-Host $m }

# Prompts fall back to the default under -Yes or when there is no interactive console.
function Ask($q, $def) {
  if ($Yes -or -not [Environment]::UserInteractive -or [Console]::IsInputRedirected) { return $def }
  $a = Read-Host "$q [$def]"
  if ([string]::IsNullOrWhiteSpace($a)) { return $def }
  return $a.Trim()
}
function Confirm-Yes($q, $def) { return ((Ask "$q (y/n)" $def) -match '^(y|yes)$') }

function Get-Sha($p) { return (Get-FileHash -Algorithm SHA256 -LiteralPath $p).Hash.ToLower() }
function Get-Manifest($file) { # -> list of @{Hash; Path}
  Get-Content -LiteralPath $file | Where-Object { $_.Trim() } | ForEach-Object {
    $parts = $_.Trim() -split '\s+', 2
    [pscustomobject]@{ Hash = $parts[0].ToLower(); Path = $parts[1] }
  }
}
function Get-File($url, $out) {
  try { Invoke-WebRequest -UseBasicParsing -Uri $url -OutFile $out } catch { throw "download failed: $url ($_)" }
}

$Tmp = Join-Path ([IO.Path]::GetTempPath()) ("workshop-" + [guid]::NewGuid().ToString("N"))
New-Item -ItemType Directory -Path $Tmp | Out-Null
$Stamp = Get-Date -Format "yyyyMMdd-HHmmss"
$Backup = ""

# Fetch-Set NAME DEST : make DEST match the published set NAME without clobbering local work
function Fetch-Set($name, $dest) {
  $mf = Join-Path $Tmp "$name.manifest"
  Get-File "$BaseUrl/downloads/$name.manifest" $mf
  $entries = @(Get-Manifest $mf)

  # Compare what is on disk with the manifest before downloading anything big.
  $need = $false
  foreach ($e in $entries) {
    $f = Join-Path $dest $e.Path
    if (-not (Test-Path -LiteralPath $f -PathType Leaf) -or (Get-Sha $f) -ne $e.Hash) { $need = $true; break }
  }
  if (-not $need) { Say "  ${name}: already up to date in $dest (nothing to download)"; return }

  $zipPath = Join-Path $Tmp "$name.zip"
  Get-File "$BaseUrl/downloads/$name.zip" $zipPath
  Get-File "$BaseUrl/downloads/$name.zip.sha256" "$zipPath.sha256"
  $want = ((Get-Content -Raw -LiteralPath "$zipPath.sha256") -replace '\s', '').ToLower()
  if ((Get-Sha $zipPath) -ne $want) { throw "$name.zip is incomplete or corrupt (checksum mismatch). Try again." }
  New-Item -ItemType Directory -Force -Path $dest | Out-Null

  $new = 0; $same = 0; $kept = 0; $replaced = 0
  $zip = [IO.Compression.ZipFile]::OpenRead($zipPath)
  try {
    foreach ($e in $entries) {
      $target = Join-Path $dest $e.Path
      $entry = $zip.GetEntry($e.Path)
      if (-not $entry) { throw "$name.zip is missing $($e.Path)" }
      $write = $false
      if (-not (Test-Path -LiteralPath $target)) { $write = $true; $new++ }
      elseif ((Get-Sha $target) -eq $e.Hash) { $same++ }
      elseif ($Force) {
        $b = Join-Path (Join-Path $script:Backup $name) $e.Path
        New-Item -ItemType Directory -Force -Path (Split-Path $b) | Out-Null
        Move-Item -LiteralPath $target -Destination $b
        $write = $true; $replaced++
      } else { $kept++; Say "  kept your version of $($e.Path) (differs; use -Force to replace)" }
      if ($write) {
        New-Item -ItemType Directory -Force -Path (Split-Path $target) | Out-Null
        [IO.Compression.ZipFileExtensions]::ExtractToFile($entry, $target, $true)
      }
    }
  } finally { $zip.Dispose() }
  Say "  ${name}: $new added, $same unchanged, $replaced replaced, $kept kept"
  if ($replaced -gt 0) { Say "  replaced files were backed up to $(Join-Path $script:Backup $name)\" }
}

try {
  Say "Workshop installer"
  Say

  # 1. Data
  if (-not $Dir) { $Dir = Ask "Which folder should the workshop data go in?" (Join-Path $HOME "workshop-demo") }
  if ($Dir -match '^~([\\/]|$)') { $Dir = $HOME + $Dir.Substring(1) }
  $Dir = [IO.Path]::GetFullPath((Join-Path (Get-Location).Path $Dir)).TrimEnd('\', '/')
  New-Item -ItemType Directory -Force -Path $Dir | Out-Null
  $Backup = "$Dir-backup-$Stamp"
  Say "Project folder: $Dir"
  Fetch-Set "toy-kit" $Dir
  $cp = $Checkpoints.IsPresent
  if (-not $cp) { $cp = Confirm-Yes "Also download the checkpoints (catch-up copies of each stage)?" "n" }
  if ($cp) { Fetch-Set "toy-checkpoints" "$Dir-checkpoints" }
  Say

  # 2. Agent harness
  $kiro = Get-Command kiro-cli -ErrorAction SilentlyContinue
  if ($kiro) {
    Say "Agent: kiro-cli is already installed ($($kiro.Source)); skipping."
  } elseif ($NoAgent) {
    Say "Agent: skipped (-NoAgent)."
  } else {
    Say "Agent: Kiro CLI is not installed."
    Say "  This runs the vendor's installer: irm $KiroUrl | iex"
    Say "  (it is fetched live and not checked by this script)"
    if ($Yes -or (Confirm-Yes "Install Kiro CLI now?" "y")) {
      Invoke-Expression (Invoke-RestMethod -UseBasicParsing -Uri $KiroUrl)
      Say "Agent: install finished. Open a new PowerShell window if 'kiro-cli' is not found."
    } else { Say "Agent: skipped." }
  }

  Say
  Say "Done. Next:  cd `"$Dir`"; kiro-cli"
  Say "Optional: some steps use 'uv' (https://docs.astral.sh/uv/) to run Python scripts."
} catch {
  # Do not call `exit`: under `irm | iex` it would close the user's PowerShell window.
  Write-Host "Error: $($_.Exception.Message)" -ForegroundColor Red
} finally {
  Remove-Item -Recurse -Force -LiteralPath $Tmp -ErrorAction SilentlyContinue
}
