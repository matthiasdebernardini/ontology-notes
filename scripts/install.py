#!/usr/bin/env python3
"""Safely install the ontology-chat skill and configure its knowledge-base root."""
from __future__ import annotations

import argparse
import json
import os
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SKILL_HOME = Path.home() / ".agents" / "skills"
DEFAULT_CONFIG = Path.home() / ".config" / "ontology-chat" / "config.json"

class InstallError(RuntimeError):
    pass

def stamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")

def backup_name(path: Path, run_stamp: str) -> Path:
    candidate = path.with_name(f"{path.name}.backup-{run_stamp}")
    counter = 2
    while candidate.exists() or candidate.is_symlink():
        candidate = path.with_name(f"{path.name}.backup-{run_stamp}-{counter}")
        counter += 1
    return candidate

def same_symlink(path: Path, source: Path) -> bool:
    if not path.is_symlink():
        return False
    try:
        return path.resolve() == source.resolve()
    except OSError:
        return False

def config_matches(path: Path, root: Path) -> bool:
    if not path.is_file():
        return False
    try:
        return Path(json.loads(path.read_text(encoding="utf-8"))["root"]).expanduser().resolve() == root.resolve()
    except (OSError, ValueError, KeyError, TypeError):
        return False

def describe_path(path: Path) -> str:
    if path.is_symlink():
        return f"symlink -> {os.readlink(path)}"
    if path.is_dir():
        return "directory"
    if path.exists():
        return "file"
    return "absent"

def plan(args: argparse.Namespace) -> tuple[Path, Path, Path, list[str]]:
    root = Path(args.kb_root).expanduser().resolve() if args.kb_root else REPO_ROOT
    source = root / "skills" / "ontology-chat"
    skill_home = Path(args.skill_home).expanduser()
    destination = skill_home / "ontology-chat"
    config = Path(args.config).expanduser()
    if not (root / "manifest.json").is_file() or not (root / "NOTE_INDEX.json").is_file() or not (root / "notes").is_dir():
        raise InstallError(f"Not an ontology-notes knowledge-base root: {root}")
    if not (source / "SKILL.md").is_file() or not (source / "scripts" / "ontology_kb.py").is_file():
        raise InstallError(f"Incomplete ontology-chat skill at {source}")
    actions = [f"Knowledge-base root: {root}", f"Skill source: {source}"]
    if args.copy:
        if destination.exists() or destination.is_symlink():
            actions.append(f"Install copy at {destination} (currently {describe_path(destination)})")
        else:
            actions.append(f"Install copy at {destination}")
    else:
        if same_symlink(destination, source):
            actions.append(f"Keep existing correct symlink at {destination}")
        else:
            actions.append(f"Install symlink {destination} -> {source} (currently {describe_path(destination)})")
    if config_matches(config, root):
        actions.append(f"Keep existing correct config at {config}")
    else:
        actions.append(f"Write config {config} with root={root} (currently {describe_path(config)})")
    return root, source, destination, config, actions

def move_to_backup(path: Path, run_stamp: str, dry_run: bool) -> Path | None:
    if not path.exists() and not path.is_symlink():
        return None
    backup = backup_name(path, run_stamp)
    if dry_run:
        print(f"Would move {path} -> {backup}")
    else:
        path.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(path), str(backup))
        print(f"Moved {path} -> {backup}")
    return backup

def install(args: argparse.Namespace) -> int:
    root, source, destination, config, actions = plan(args)
    print("Installation plan:")
    for action in actions:
        print(f"- {action}")
    destination_conflict = destination.exists() or destination.is_symlink()
    destination_ok = same_symlink(destination, source) and not args.copy
    config_conflict = config.exists() or config.is_symlink()
    config_ok = config_matches(config, root)
    conflicts = []
    if destination_conflict and not destination_ok:
        conflicts.append(str(destination))
    if config_conflict and not config_ok:
        conflicts.append(str(config))
    if conflicts and not args.force:
        print("\nStopped: existing paths would be replaced: " + ", ".join(conflicts), file=sys.stderr)
        print("Review with --dry-run --force, then rerun with --force. Existing paths are backed up, never deleted.", file=sys.stderr)
        return 2
    if args.dry_run:
        run_stamp = stamp()
        for path in (destination, config):
            if (path.exists() or path.is_symlink()) and not ((path == destination and destination_ok) or (path == config and config_ok)):
                move_to_backup(path, run_stamp, True)
        print("\nDry run only; no changes made.")
        return 0
    run_stamp = stamp()
    if not destination_ok:
        if destination_conflict:
            move_to_backup(destination, run_stamp, False)
        destination.parent.mkdir(parents=True, exist_ok=True)
        if args.copy:
            shutil.copytree(source, destination)
            print(f"Copied skill to {destination}")
        else:
            destination.symlink_to(source, target_is_directory=True)
            print(f"Linked skill {destination} -> {source}")
    else:
        print(f"Skill already linked correctly at {destination}")
    if not config_ok:
        if config_conflict:
            move_to_backup(config, run_stamp, False)
        config.parent.mkdir(parents=True, exist_ok=True)
        temporary = config.with_name(f".{config.name}.new-{os.getpid()}")
        temporary.write_text(json.dumps({"root": str(root)}, indent=2) + "\n", encoding="utf-8")
        temporary.replace(config)
        print(f"Configured knowledge-base root in {config}")
    else:
        print(f"Configuration already points to {root}")
    print("Installation complete. Restart or open a new Prime Agent session if the skill is not immediately visible.")
    return 0

def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--kb-root", help="Ontology-notes checkout; defaults to this installer's repository")
    p.add_argument("--skill-home", default=str(DEFAULT_SKILL_HOME), help="Agent skill directory")
    p.add_argument("--config", default=str(DEFAULT_CONFIG), help="ontology-chat config JSON path")
    mode = p.add_mutually_exclusive_group()
    mode.add_argument("--copy", action="store_true", help="Copy instead of symlinking the skill")
    mode.add_argument("--symlink", action="store_true", help="Symlink the skill (default)")
    p.add_argument("--force", action="store_true", help="Back up conflicting paths and install")
    p.add_argument("--dry-run", action="store_true", help="Print the complete plan without changing files")
    return p

def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    try:
        return install(args)
    except InstallError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

if __name__ == "__main__":
    raise SystemExit(main())
