#!/usr/bin/env python3
"""Synchronize one skill package from a sibling repository.

The source repository's checked-out package is authoritative. The destination
package is replaced atomically, so files removed from the source are removed
from the destination as well.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import sys
import tempfile
from pathlib import Path, PurePosixPath


class ImportError(Exception):
    """Raised for an invalid source package or unsafe synchronization."""


def repository_root() -> Path:
    # .../skills/skill-writing/scripts/import-skill.py
    return Path(__file__).resolve().parents[3]


def relative_path(value: object, field: str) -> str:
    if not isinstance(value, str) or not value:
        raise ImportError(f"manifest {field!r} must be a non-empty string")
    path = PurePosixPath(value)
    if path.is_absolute() or ".." in path.parts or "\\" in value:
        raise ImportError(f"manifest {field!r} must be a safe relative path: {value!r}")
    return path.as_posix()


def load_package(source_repo: Path, skill_name: str) -> tuple[Path, dict, list[tuple[str, str | None]]]:
    if source_repo.parent != repository_root().parent:
        raise ImportError(
            f"source repository must be a sibling of {repository_root().name}: {source_repo}"
        )

    source = source_repo / "skills" / skill_name
    if source == repository_root() / "skills" / skill_name:
        raise ImportError("source and destination packages are the same directory")
    if not source.is_dir():
        raise ImportError(f"source skill directory does not exist: {source}")

    manifest_path = source / "skill.json"
    if not manifest_path.is_file() or manifest_path.is_symlink():
        raise ImportError(f"source skill has no regular skill.json: {manifest_path}")
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ImportError(f"could not read {manifest_path}: {exc}") from exc

    if not isinstance(manifest, dict) or manifest.get("schema") != 1:
        raise ImportError("source manifest must be an object with schema 1")
    if manifest.get("name") != skill_name:
        raise ImportError(
            f"manifest name {manifest.get('name')!r} does not match requested skill {skill_name!r}"
        )
    if manifest.get("entrypoint") != "SKILL.md":
        raise ImportError("source manifest entrypoint must be 'SKILL.md'")

    entries = manifest.get("files")
    if not isinstance(entries, list) or not entries:
        raise ImportError("source manifest files must be a non-empty list")

    declared: list[tuple[str, str | None]] = []
    seen: set[str] = set()
    for entry in entries:
        if not isinstance(entry, dict):
            raise ImportError("each manifest file entry must be an object")
        path = relative_path(entry.get("path"), "path")
        if path in seen or path == "skill.json":
            raise ImportError(f"duplicate or reserved manifest path: {path}")
        seen.add(path)
        lib_name = entry.get("lib_name")
        if lib_name is not None and not isinstance(lib_name, str):
            raise ImportError(f"manifest lib_name must be a string: {path}")
        expected_lib_name = f"skills/{skill_name}/{path}"
        if lib_name != expected_lib_name:
            raise ImportError(
                f"manifest lib_name for {path!r} must be {expected_lib_name!r}"
            )
        source_file = source / Path(*PurePosixPath(path).parts)
        if not source_file.is_file() or source_file.is_symlink():
            raise ImportError(f"manifest file is missing or not regular: {source_file}")
        declared.append((path, entry.get("mode")))

    if "SKILL.md" not in seen:
        raise ImportError("source manifest must list SKILL.md")

    actual = {
        path.relative_to(source).as_posix()
        for path in source.rglob("*")
        if path.is_file() and path.name != "skill.json"
    }
    if actual != seen:
        missing = sorted(seen - actual)
        undeclared = sorted(actual - seen)
        details = []
        if missing:
            details.append(f"missing: {', '.join(missing)}")
        if undeclared:
            details.append(f"undeclared: {', '.join(undeclared)}")
        raise ImportError("source manifest does not match package files (" + "; ".join(details) + ")")

    return source, manifest, declared


def digest(path: Path) -> str:
    hasher = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def apply_mode(path: Path, mode: str | None) -> None:
    try:
        path.chmod(int(mode or "0644", 8))
    except (TypeError, ValueError, OSError) as exc:
        raise ImportError(f"invalid or unusable mode {mode!r} for {path}: {exc}") from exc


def file_changes(
    source: Path,
    destination: Path,
    declared: list[tuple[str, str | None]],
    manifest_path: Path,
) -> tuple[list[str], list[str], list[str]]:
    source_paths = {path for path, _ in declared} | {"skill.json"}
    destination_paths = {
        path.relative_to(destination).as_posix()
        for path in destination.rglob("*")
        if path.is_file()
    } if destination.is_dir() else set()
    added, updated, removed = [], [], []
    for path in sorted(source_paths):
        source_file = manifest_path if path == "skill.json" else source / Path(*PurePosixPath(path).parts)
        destination_file = destination / Path(*PurePosixPath(path).parts)
        if not destination_file.exists():
            added.append(path)
        elif digest(source_file) != digest(destination_file):
            updated.append(path)
    removed = sorted(destination_paths - source_paths)
    return added, updated, removed


def synchronize(
    source: Path,
    destination: Path,
    declared: list[tuple[str, str | None]],
    manifest_path: Path,
) -> None:
    destination_parent = destination.parent
    destination_parent.mkdir(parents=True, exist_ok=True)
    stage = Path(tempfile.mkdtemp(prefix=f".{destination.name}.stage-", dir=destination_parent))
    backup: Path | None = None
    try:
        for path, mode in [("skill.json", None), *declared]:
            source_file = manifest_path if path == "skill.json" else source / Path(*PurePosixPath(path).parts)
            staged_file = stage / Path(*PurePosixPath(path).parts)
            staged_file.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source_file, staged_file)
            apply_mode(staged_file, mode)

        if destination.exists():
            if not destination.is_dir():
                raise ImportError(f"destination is not a directory: {destination}")
            backup = destination_parent / f".{destination.name}.backup-{os.getpid()}"
            os.replace(destination, backup)
        os.replace(stage, destination)
        if backup is not None:
            shutil.rmtree(backup)
    except Exception:
        if stage.exists():
            shutil.rmtree(stage)
        if backup is not None and backup.exists() and not destination.exists():
            os.replace(backup, destination)
        raise


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Synchronize a skill from a sibling repository into this repository."
    )
    parser.add_argument("source_repository", help="Sibling repository containing skills/<name>/")
    parser.add_argument("skill_name", help="Skill directory and manifest name")
    parser.add_argument(
        "--dry-run", action="store_true", help="Validate and report changes without copying"
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        root = repository_root()
        source_repo = Path(args.source_repository).expanduser().resolve()
        source, manifest, declared = load_package(source_repo, args.skill_name)
        destination = root / "skills" / args.skill_name
        if destination.parent != root / "skills":
            raise ImportError("destination must remain under this repository's skills directory")
        added, updated, removed = file_changes(source, destination, declared, source / "skill.json")
        print(f"Source:      {source}")
        print(f"Destination: {destination}")
        for label, paths in (("added", added), ("updated", updated), ("removed", removed)):
            for path in paths:
                print(f"{label:8} {path}")
        if not (added or updated or removed):
            print("No changes needed.")
        elif args.dry_run:
            print("Dry run: no files copied.")
        else:
            synchronize(source, destination, declared, source / "skill.json")
            print(f"Synchronized skill {manifest['name']!r}.")
        return 0
    except (ImportError, OSError, RuntimeError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
