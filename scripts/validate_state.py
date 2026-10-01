#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKSPACE = "namnx-vn/agent-memory-hub"
SEED_SESSION = "sessions/persistence-agent-continuity-v1--20260917T164400Z--chat01/session.json"

REQUIRED_FILES = [
    "README.md", "AGENTS.md", "AGENT_HANDSHAKE.md", "SESSION_LINKING.md",
    "AGENT_MESSAGE_BUS.md", "CLAUDE.md", "GEMINI.md", "llms.txt",
    "agent-discovery.json", ".github/copilot-instructions.md",
    ".cursor/rules/agent-memory-hub.mdc", "AGENT_RULES.md", "IDENTITY.md",
    "LIFECYCLE.md", "RECOVERY.md", "CONTEXT.md", "NEXT_SESSION.md",
    "AUTOMATION.md", "MULTI_AGENT.md", "agents/registry.json",
    "agents/persistence-agent-continuity-v1/README.md", "sessions/README.md",
    "projects/README.md", SEED_SESSION, "coordination/BLACKBOARD.md",
    "coordination/messages/README.md", "coordination/acks/README.md",
    "schemas/session.schema.json", "schemas/message.schema.json",
    "schemas/ack.schema.json", "shared/README.md", "memory/long-term.md",
    "memory/decisions.md", "memory/lessons-learned.md",
    "state/current.json", "state/runtime.json", "state/backlog.json",
]

REQUIRED_CURRENT_KEYS = {
    "schema_version", "workspace", "mode", "status", "objective", "active_task",
    "continuity", "last_updated", "autonomous_runtime_enabled", "secrets_allowed",
}
REQUIRED_CONTINUITY_KEYS = {
    "enabled", "profile", "identity_file", "lifecycle_file", "recovery_file",
    "lineage", "lifecycle_state",
}
REQUIRED_RUNTIME_KEYS = {
    "schema_version", "enabled", "trigger", "mode", "cadence", "source_of_work",
    "message_source", "ack_source", "session_source", "project_session_source",
    "max_messages_per_run", "max_backlog_items_per_run", "priority_order",
    "notify_policy", "startup_files", "kill_switches", "last_configured",
}
REQUIRED_DISCOVERY_ENTRYPOINTS = {
    "generic": "AGENTS.md",
    "handshake": "AGENT_HANDSHAKE.md",
    "session_linking": "SESSION_LINKING.md",
    "message_bus": "AGENT_MESSAGE_BUS.md",
    "claude_code": "CLAUDE.md",
    "gemini_cli": "GEMINI.md",
    "github_copilot": ".github/copilot-instructions.md",
    "cursor": ".cursor/rules/agent-memory-hub.mdc",
    "multi_agent_protocol": "MULTI_AGENT.md",
    "rules": "AGENT_RULES.md",
    "registry": "agents/registry.json",
    "blackboard": "coordination/BLACKBOARD.md",
    "llm_index": "llms.txt",
}
REQUIRED_SESSION_KEYS = {
    "schema_version", "session_id", "agent_id", "kind", "status", "started_at",
    "parent_session_id", "continued_from", "summary", "last_seen_at",
}
FORBIDDEN_KEY_FRAGMENTS = {
    "password", "passwd", "secret", "token", "private_key", "api_key", "cookie",
}
AGENT_ID_PATTERN = re.compile(r"^[a-z0-9][a-z0-9-]{0,63}$")
PROJECT_ID_PATTERN = AGENT_ID_PATTERN


def load_json(relative_path: str):
    with (ROOT / relative_path).open("r", encoding="utf-8") as handle:
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


def validate_session(session: dict, label: str, seen_agent_ids: set[str], expected_project_id: str | None = None) -> None:
    missing = sorted(REQUIRED_SESSION_KEYS - set(session))
    if missing:
        raise SystemExit(f"{label} missing keys: " + ", ".join(missing))
    if session.get("schema_version") != 1:
        raise SystemExit(f"{label} schema_version must be 1")
    if session.get("agent_id") not in seen_agent_ids:
        raise SystemExit(f"{label} agent_id is not registered")
    if session.get("status") not in {"active", "handoff", "closed"}:
        raise SystemExit(f"Invalid {label} status")
    if not isinstance(session.get("continued_from"), list):
        raise SystemExit(f"{label} continued_from must be a list")

    scope = session.get("scope")
    project_id = session.get("project_id")
    if scope is not None and scope not in {"standalone", "project"}:
        raise SystemExit(f"Invalid {label} scope")
    if project_id is not None and (
        not isinstance(project_id, str) or not PROJECT_ID_PATTERN.fullmatch(project_id)
    ):
        raise SystemExit(f"Invalid {label} project_id")

    if expected_project_id is not None:
        if session.get("scope") != "project":
            raise SystemExit(f"{label} must set scope=project")
        if session.get("project_id") != expected_project_id:
            raise SystemExit(f"{label} project_id must match project tree")


def main() -> None:
    missing_files = [name for name in REQUIRED_FILES if not (ROOT / name).is_file()]
    if missing_files:
        raise SystemExit("Missing required files: " + ", ".join(missing_files))

    current = load_json("state/current.json")
    runtime = load_json("state/runtime.json")
    backlog = load_json("state/backlog.json")
    registry = load_json("agents/registry.json")
    discovery = load_json("agent-discovery.json")
    seed_session = load_json(SEED_SESSION)

    for schema_path in ("schemas/session.schema.json", "schemas/message.schema.json", "schemas/ack.schema.json"):
        schema = load_json(schema_path)
        if schema.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
            raise SystemExit(f"Unexpected JSON Schema version: {schema_path}")

    missing = sorted(REQUIRED_CURRENT_KEYS - set(current))
    if missing:
        raise SystemExit("state/current.json missing keys: " + ", ".join(missing))
    if current.get("workspace") != WORKSPACE or current.get("schema_version") != 2:
        raise SystemExit("Unexpected current-state workspace/schema")

    continuity = current.get("continuity")
    if not isinstance(continuity, dict):
        raise SystemExit("continuity must be an object")
    missing = sorted(REQUIRED_CONTINUITY_KEYS - set(continuity))
    if missing:
        raise SystemExit("continuity missing keys: " + ", ".join(missing))
    if continuity.get("enabled") is not True:
        raise SystemExit("continuity.enabled must be true")
    if continuity.get("profile") != "persistence-agent/continuity-v1":
        raise SystemExit("Unexpected continuity profile")
    if continuity.get("lineage") != "git-history":
        raise SystemExit("continuity.lineage must be git-history")
    if continuity.get("lifecycle_state") not in {"dormant", "restoring", "active", "handoff"}:
        raise SystemExit("Invalid continuity lifecycle_state")

    missing = sorted(REQUIRED_RUNTIME_KEYS - set(runtime))
    if missing:
        raise SystemExit("state/runtime.json missing keys: " + ", ".join(missing))
    if runtime.get("schema_version") != 2:
        raise SystemExit("state/runtime.json schema_version must be 2")
    if runtime.get("trigger") != "chatgpt-automation":
        raise SystemExit("Unexpected runtime trigger")
    if runtime.get("mode") != "bounded-hub-worker":
        raise SystemExit("Unexpected runtime mode")
    if runtime.get("cadence") != "hourly":
        raise SystemExit("Runtime cadence must be hourly")
    if runtime.get("source_of_work") != "state/backlog.json":
        raise SystemExit("Unexpected runtime backlog source")
    if runtime.get("message_source") != "coordination/messages/":
        raise SystemExit("Unexpected runtime message source")
    if runtime.get("ack_source") != "coordination/acks/":
        raise SystemExit("Unexpected runtime ack source")
    if runtime.get("session_source") != "sessions/":
        raise SystemExit("Unexpected standalone runtime session source")
    if runtime.get("project_session_source") != "projects/<project-id>/sessions/":
        raise SystemExit("Unexpected project runtime session source")
    if runtime.get("max_messages_per_run") != 1 or runtime.get("max_backlog_items_per_run") != 1:
        raise SystemExit("Runtime per-run limits must remain 1")
    if current.get("autonomous_runtime_enabled") is not runtime.get("enabled"):
        raise SystemExit("Runtime enabled state is inconsistent")

    if current.get("secrets_allowed") is not False:
        raise SystemExit("secrets_allowed must remain false")
    if not isinstance(backlog.get("items"), list):
        raise SystemExit("state/backlog.json items must be a list")

    if registry.get("schema_version") != 1 or registry.get("workspace") != WORKSPACE:
        raise SystemExit("Unexpected registry workspace/schema")
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
        if entry.get("storage_namespace") != f"agents/{agent_id}/":
            raise SystemExit(f"Unexpected storage namespace for {agent_id}")
    if "persistence-agent-continuity-v1" not in seen_agent_ids:
        raise SystemExit("Primary continuity agent is missing from registry")

    if discovery.get("schema_version") != 3 or discovery.get("workspace") != WORKSPACE:
        raise SystemExit("Unexpected discovery workspace/schema")
    if discovery.get("public") is not True:
        raise SystemExit("agent-discovery.json public must be true")
    keywords = discovery.get("keywords")
    if not isinstance(keywords, list):
        raise SystemExit("agent-discovery.json keywords must be a list")
    for keyword in ("agent-memory", "multi-agent", "cross-chat-memory", "agent-message-bus"):
        if keyword not in keywords:
            raise SystemExit(f"Missing core discovery keyword: {keyword}")
    entrypoints = discovery.get("entrypoints")
    if not isinstance(entrypoints, dict):
        raise SystemExit("agent-discovery.json entrypoints must be an object")
    for key, expected_path in REQUIRED_DISCOVERY_ENTRYPOINTS.items():
        if entrypoints.get(key) != expected_path:
            raise SystemExit(f"Unexpected discovery entrypoint for {key}")
    storage = discovery.get("storage")
    if not isinstance(storage, dict):
        raise SystemExit("agent-discovery.json storage must be an object")
    if storage.get("per_session") != "sessions/<session-id>/":
        raise SystemExit("Unexpected standalone per-session storage path")
    if storage.get("per_project") != "projects/<project-id>/":
        raise SystemExit("Unexpected project storage path")
    if storage.get("project_session") != "projects/<project-id>/sessions/<session-id>/":
        raise SystemExit("Unexpected project session storage path")
    if storage.get("messages") != "coordination/messages/":
        raise SystemExit("Unexpected message bus storage path")
    if storage.get("acknowledgments") != "coordination/acks/":
        raise SystemExit("Unexpected acknowledgment storage path")

    capabilities = discovery.get("capabilities")
    if not isinstance(capabilities, list) or "project-scoped-session-tree" not in capabilities:
        raise SystemExit("Missing project-scoped-session-tree capability")

    validate_session(seed_session, "Seed session", seen_agent_ids)

    projects_root = ROOT / "projects"
    for project_dir in projects_root.iterdir():
        if not project_dir.is_dir():
            continue
        project_id = project_dir.name
        if not PROJECT_ID_PATTERN.fullmatch(project_id):
            raise SystemExit(f"Invalid project directory id: {project_id}")
        sessions_dir = project_dir / "sessions"
        if not sessions_dir.exists():
            continue
        for session_file in sessions_dir.glob("*/session.json"):
            with session_file.open("r", encoding="utf-8") as handle:
                session = json.load(handle)
            validate_session(
                session,
                f"Project session {session_file.relative_to(ROOT)}",
                seen_agent_ids,
                expected_project_id=project_id,
            )

    for document_name, document in (
        ("current", current), ("runtime", runtime), ("backlog", backlog),
        ("registry", registry), ("discovery", discovery), ("seed_session", seed_session),
    ):
        for path, key in walk_keys(document):
            lowered = key.lower()
            if any(fragment in lowered for fragment in FORBIDDEN_KEY_FRAGMENTS):
                if key == "secrets_allowed":
                    continue
                raise SystemExit(f"Potential secret-bearing key in {document_name}: {path}")

    print("Agent Memory Hub continuity, project-aware session graph, bounded runtime, and message bus are valid.")


if __name__ == "__main__":
    main()
