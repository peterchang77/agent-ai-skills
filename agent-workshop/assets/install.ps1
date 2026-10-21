# Workshop installer for Windows (PowerShell): sets up the clinical or imaging workshop data and installs an agent harness (Kiro CLI).
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
  [string]$Scenario = "",  # clinical (clinic-network data) or imaging (chest radiographs; needs 'uv', builds its data locally)
  [string]$Dir = "",       # your project folder for the data (default: ~\workshop-demo, or ~\workshop-imaging)
  [switch]$Checkpoints,    # also set up the checkpoints, to <folder>-checkpoints (about 0.5 GB for imaging)
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

# Sync-Tree SRC DEST NAME : copy a local folder into DEST under the same rules as Fetch-Set (never clobber your changes)
function Sync-Tree($src, $dest, $name) {
  $new = 0; $same = 0; $kept = 0; $replaced = 0
  New-Item -ItemType Directory -Force -Path $dest | Out-Null
  $root = (Resolve-Path -LiteralPath $src).Path.TrimEnd('\', '/')
  foreach ($f in Get-ChildItem -LiteralPath $root -Recurse -File) {
    $rel = $f.FullName.Substring($root.Length).TrimStart('\', '/')
    $target = Join-Path $dest $rel
    if (-not (Test-Path -LiteralPath $target)) {
      New-Item -ItemType Directory -Force -Path (Split-Path $target) | Out-Null
      Copy-Item -LiteralPath $f.FullName -Destination $target; $new++
    } elseif ((Get-Sha $f.FullName) -eq (Get-Sha $target)) { $same++ }
    elseif ($Force) {
      $b = Join-Path (Join-Path $script:Backup $name) $rel
      New-Item -ItemType Directory -Force -Path (Split-Path $b) | Out-Null
      Move-Item -LiteralPath $target -Destination $b
      Copy-Item -LiteralPath $f.FullName -Destination $target; $replaced++
    } else { $kept++; Say "  kept your version of $rel (differs; use -Force to replace)" }
  }
  Say "  ${name}: $new added, $same unchanged, $replaced replaced, $kept kept"
  if ($replaced -gt 0) { Say "  replaced files were backed up to $(Join-Path $script:Backup $name)\" }
}

# Run a native command with output going to a log. PowerShell 5.1 treats any stderr text as an error under "Stop", so relax it here.
function Invoke-Logged($workdir, $log, [scriptblock]$cmd) {
  Push-Location $workdir
  $old = $ErrorActionPreference; $ErrorActionPreference = "Continue"
  try { & $cmd *> $log; $code = $LASTEXITCODE } finally { $ErrorActionPreference = $old; Pop-Location }
  if ($code -ne 0) { Get-Content -LiteralPath $log -Tail 15 | ForEach-Object { Write-Host $_ }; throw "a build step failed (log above)." }
}

# The imaging data is built on this computer from the public image sample (the finished kit is 74 MB, so it is not published).
function Install-Imaging {
  $tools = "$Dir-tools"; $here = Join-Path $tools "scenarios\imaging"
  if (-not (Get-Command uv -ErrorAction SilentlyContinue)) {
    Say "Python tool: 'uv' is not installed (the imaging data is built with it)."
    Say "  This runs the vendor's installer: irm https://astral.sh/uv/install.ps1 | iex"
    Say "  (it is fetched live and not checked by this script)"
    if ($Yes -or (Confirm-Yes "Install uv now?" "y")) {
      Invoke-Expression (Invoke-RestMethod -UseBasicParsing -Uri "https://astral.sh/uv/install.ps1")
      $env:Path = "$HOME\.local\bin;$HOME\.cargo\bin;$env:Path"
    }
    if (-not (Get-Command uv -ErrorAction SilentlyContinue)) { throw "uv is required for the imaging data. Install it from https://docs.astral.sh/uv/ and run this script again." }
  }
  Fetch-Set "imaging-tools" $tools
  Say "  Building the image kit (downloads the 33 MB public sample the first time; about a minute)..."
  Invoke-Logged $here (Join-Path $Tmp "build_kit.log") { uv run build_kit.py }
  Sync-Tree (Join-Path $here "kit") $Dir "imaging-kit"
  $cp = $Checkpoints.IsPresent
  if (-not $cp) { $cp = Confirm-Yes "Also build the checkpoints (catch-up copies of each stage; about 0.5 GB and a few minutes)?" "n" }
  if ($cp) {
    Say "  Building the checkpoints..."
    Invoke-Logged $here (Join-Path $Tmp "checkpoints.log") { uv run make_checkpoints.py }
    Sync-Tree (Join-Path $here "checkpoints") "$Dir-checkpoints" "imaging-checkpoints"
  }
  Remove-Item -Recurse -Force -LiteralPath (Join-Path $here "kit"), (Join-Path $here "checkpoints") -ErrorAction SilentlyContinue   # generated copies; rebuilding is deterministic
  Say "  The scripts that some steps mention (scenarios\imaging\...) are in $tools"
}

try {
  Say "Workshop installer"
  Say

  # 1. Data
  if (-not $Scenario) { $Scenario = Ask "Which version: clinical (clinic-network data) or imaging (chest radiographs)?" "clinical" }
  $Scenario = $Scenario.Trim().ToLower()
  if ($Scenario -notin @("clinical", "imaging")) { throw "-Scenario must be clinical or imaging" }
  if (-not $Dir) { $Dir = Ask "Which folder should the workshop data go in?" (Join-Path $HOME $(if ($Scenario -eq "imaging") { "workshop-imaging" } else { "workshop-demo" })) }
  if ($Dir -match '^~([\\/]|$)') { $Dir = $HOME + $Dir.Substring(1) }
  $Dir = [IO.Path]::GetFullPath((Join-Path (Get-Location).Path $Dir)).TrimEnd('\', '/')
  New-Item -ItemType Directory -Force -Path $Dir | Out-Null
  $Backup = "$Dir-backup-$Stamp"
  Say "Project folder: $Dir"
  if ($Scenario -eq "imaging") {
    Install-Imaging
  } else {
    Fetch-Set "toy-kit" $Dir
    $cp = $Checkpoints.IsPresent
    if (-not $cp) { $cp = Confirm-Yes "Also download the checkpoints (catch-up copies of each stage)?" "n" }
    if ($cp) { Fetch-Set "toy-checkpoints" "$Dir-checkpoints" }
  }
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
  if ($Scenario -eq "imaging") {
    Say "Note: the answer key for the planted problems is in $Dir-tools\scenarios\imaging\truth\. Leave it unopened until you have finished."
  } else {
    Say "Optional: some steps use 'uv' (https://docs.astral.sh/uv/) to run Python scripts."
  }
} catch {
  # Do not call `exit`: under `irm | iex` it would close the user's PowerShell window.
  Write-Host "Error: $($_.Exception.Message)" -ForegroundColor Red
} finally {
  Remove-Item -Recurse -Force -LiteralPath $Tmp -ErrorAction SilentlyContinue
}
