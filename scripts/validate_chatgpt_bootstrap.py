#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = {
    "CHATGPT_GLOBAL_BOOTSTRAP.md",
    "CHATGPT_PROJECT_INSTRUCTIONS.md",
    "SESSION_LINKING.md",
    "AGENT_MESSAGE_BUS.md",
    "agent-discovery.json",
}

EXPECTED_ENTRYPOINTS = {
    "chatgpt_global_bootstrap": "CHATGPT_GLOBAL_BOOTSTRAP.md",
    "chatgpt_project_instructions": "CHATGPT_PROJECT_INSTRUCTIONS.md",
    "session_linking": "SESSION_LINKING.md",
    "message_bus": "AGENT_MESSAGE_BUS.md",
}


def main() -> None:
    missing = sorted(path for path in REQUIRED if not (ROOT / path).is_file())
    if missing:
        raise SystemExit("Missing ChatGPT bootstrap files: " + ", ".join(missing))

    with (ROOT / "agent-discovery.json").open("r", encoding="utf-8") as handle:
        discovery = json.load(handle)

    if discovery.get("workspace") != "namnx-vn/agent-memory-hub":
        raise SystemExit("Unexpected Agent Memory Hub workspace")

    entrypoints = discovery.get("entrypoints")
    if not isinstance(entrypoints, dict):
        raise SystemExit("Discovery entrypoints must be an object")

    for key, expected in EXPECTED_ENTRYPOINTS.items():
        if entrypoints.get(key) != expected:
            raise SystemExit(f"Unexpected ChatGPT bootstrap entrypoint: {key}")

    capabilities = discovery.get("capabilities")
    if not isinstance(capabilities, list):
        raise SystemExit("Discovery capabilities must be a list")

    for capability in (
        "global-chat-bootstrap-via-custom-instructions",
        "project-chat-bootstrap-via-project-instructions",
        "cross-chat-session-graph",
        "append-only-agent-messaging",
    ):
        if capability not in capabilities:
            raise SystemExit(f"Missing capability: {capability}")

    print("ChatGPT global/project bootstrap configuration is valid.")


if __name__ == "__main__":
    main()
