#!/usr/bin/env python3
from __future__ import annotations

import json
import re
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
    "MULTI_AGENT.md",
    "agents/registry.json",
    "agents/persistence-agent-continuity-v1/README.md",
    "coordination/BLACKBOARD.md",
    "shared/README.md",
    "memory/long-term.md",
    "memory/decisions.md",
    "memory/lessons-learned.md",
    "state/current.json",
    "state/runtime.json",
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

REQUIRED_RUNTIME_KEYS = {
    "schema_version",
    "enabled",
    "trigger",
    "mode",
    "cadence",
    "source_of_work",
    "max_backlog_items_per_run",
    "notify_policy",
    "startup_files",
    "kill_switches",
    "last_configured",
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

AGENT_ID_PATTERN = re.compile(r"^[a-z0-9][a-z0-9-]{0,63}$")


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
    runtime = load_json("state/runtime.json")
    backlog = load_json("state/backlog.json")
    registry = load_json("agents/registry.json")

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

    missing_runtime_keys = sorted(REQUIRED_RUNTIME_KEYS - set(runtime))
    if missing_runtime_keys:
        raise SystemExit(
            "state/runtime.json missing keys: " + ", ".join(missing_runtime_keys)
        )

    if runtime.get("schema_version") != 1:
        raise SystemExit("state/runtime.json schema_version must be 1")

    if runtime.get("trigger") != "chatgpt-automation":
        raise SystemExit("Unexpected runtime trigger")

    if runtime.get("mode") != "bounded-backlog-worker":
        raise SystemExit("Unexpected runtime mode")

    if runtime.get("cadence") != "hourly":
        raise SystemExit("Runtime cadence must be hourly")

    if runtime.get("source_of_work") != "state/backlog.json":
        raise SystemExit("Runtime source_of_work must be state/backlog.json")

    if runtime.get("max_backlog_items_per_run") != 1:
        raise SystemExit("Runtime must process at most one backlog item per run")

    if current.get("autonomous_runtime_enabled") is not runtime.get("enabled"):
        raise SystemExit("Runtime enabled state is inconsistent")

    if current.get("secrets_allowed") is not False:
        raise SystemExit("secrets_allowed must remain false")

    if not isinstance(backlog.get("items"), list):
        raise SystemExit("state/backlog.json items must be a list")

    if registry.get("schema_version") != 1:
        raise SystemExit("agents/registry.json schema_version must be 1")

    if registry.get("workspace") != "namnx-vn/persistence":
        raise SystemExit("Unexpected registry workspace identifier")

    agents = registry.get("agents")
    if not isinstance(agents, list) or not agents:
        raise SystemExit("agents/registry.json agents must be a non-empty list")

    seen_agent_ids = set()
    for entry in agents:
        if not isinstance(entry, dict):
            raise SystemExit("Each registry agent entry must be an object")
        agent_id = entry.get("agent_id")
        if not isinstance(agent_id, str) or not AGENT_ID_PATTERN.fullmatch(agent_id):
            raise SystemExit(f"Invalid agent_id in registry: {agent_id!r}")
        if agent_id in seen_agent_ids:
            raise SystemExit(f"Duplicate agent_id in registry: {agent_id}")
        seen_agent_ids.add(agent_id)
        namespace = entry.get("storage_namespace")
        if namespace != f"agents/{agent_id}/":
            raise SystemExit(f"Unexpected storage namespace for {agent_id}")

    if "persistence-agent-continuity-v1" not in seen_agent_ids:
        raise SystemExit("Primary continuity agent is missing from registry")

    for document_name, document in (
        ("current", current),
        ("runtime", runtime),
        ("backlog", backlog),
        ("registry", registry),
    ):
        for path, key in walk_keys(document):
            lowered = key.lower()
            if any(fragment in lowered for fragment in FORBIDDEN_KEY_FRAGMENTS):
                if key == "secrets_allowed":
                    continue
                raise SystemExit(f"Potential secret-bearing key in {document_name}: {path}")

    print("Persistence continuity, runtime, and multi-agent storage state are valid.")


if __name__ == "__main__":
    main()
