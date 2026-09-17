#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "AGENT_RULES.md",
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
    "last_updated",
    "autonomous_runtime_enabled",
    "secrets_allowed",
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

    print("Persistence state is valid.")


if __name__ == "__main__":
    main()
