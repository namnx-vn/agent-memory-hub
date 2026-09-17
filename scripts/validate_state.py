#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "AGENT_RULES.md",
    "IDENTITY.md",
    "LIFECYCLE.md",
    "RECOVERY.md",
    "CONTEXT.md",
    "NEXT_SESSION.md",
    "AUTOMATION.md",
    "memory/long-term.md",
    "memory/decisions.md",
    "memory/lessons-learned.md",
    "state/current.json",
    "state/backlog.json",
]

REQUIRED_CURRENT_KEYS = {
    "schema_version",
    "workspace",
    "mode",
    "status",
    "objective",
    "active_task",
    "continuity",
    "last_updated",
    "autonomous_runtime_enabled",
    "secrets_allowed",
}

REQUIRED_CONTINUITY_KEYS = {
    "enabled",
    "profile",
    "identity_file",
    "lifecycle_file",
    "recovery_file",
    "lineage",
    "lifecycle_state",
}

FORBIDDEN_KEY_FRAGMENTS = {
    "password",
    "passwd",
    "secret",
    "token",
    "private_key",
    "api_key",
    "cookie",
}


def load_json(relative_path: str):
    path = ROOT / relative_path
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def walk_keys(value, prefix=""):
    if isinstance(value, dict):
        for key, child in value.items():
            current = f"{prefix}.{key}" if prefix else key
            yield current, key
            yield from walk_keys(child, current)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from walk_keys(child, f"{prefix}[{index}]")


def main() -> None:
    missing_files = [name for name in REQUIRED_FILES if not (ROOT / name).is_file()]
    if missing_files:
        raise SystemExit(f"Missing required files: {', '.join(missing_files)}")

    current = load_json("state/current.json")
    backlog = load_json("state/backlog.json")

    missing_keys = sorted(REQUIRED_CURRENT_KEYS - set(current))
    if missing_keys:
        raise SystemExit(f"state/current.json missing keys: {', '.join(missing_keys)}")

    if current.get("workspace") != "namnx-vn/persistence":
        raise SystemExit("Unexpected workspace identifier")

    if current.get("schema_version") != 2:
        raise SystemExit("state/current.json schema_version must be 2")

    continuity = current.get("continuity")
    if not isinstance(continuity, dict):
        raise SystemExit("state/current.json continuity must be an object")

    missing_continuity_keys = sorted(REQUIRED_CONTINUITY_KEYS - set(continuity))
    if missing_continuity_keys:
        raise SystemExit(
            "state/current.json continuity missing keys: "
            + ", ".join(missing_continuity_keys)
        )

    if continuity.get("enabled") is not True:
        raise SystemExit("continuity.enabled must be true")

    if continuity.get("profile") != "persistence-agent/continuity-v1":
        raise SystemExit("Unexpected continuity profile")

    if continuity.get("lineage") != "git-history":
        raise SystemExit("continuity.lineage must be git-history")

    if continuity.get("lifecycle_state") not in {"dormant", "restoring", "active", "handoff"}:
        raise SystemExit("Invalid continuity lifecycle_state")

    if current.get("secrets_allowed") is not False:
        raise SystemExit("secrets_allowed must remain false")

    if not isinstance(backlog.get("items"), list):
        raise SystemExit("state/backlog.json items must be a list")

    for document_name, document in (("current", current), ("backlog", backlog)):
        for path, key in walk_keys(document):
            lowered = key.lower()
            if any(fragment in lowered for fragment in FORBIDDEN_KEY_FRAGMENTS):
                if key == "secrets_allowed":
                    continue
                raise SystemExit(f"Potential secret-bearing key in {document_name}: {path}")

    print("Persistence continuity state is valid.")


if __name__ == "__main__":
    main()
