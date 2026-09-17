This repository is a public, owner-controlled shared persistence and coordination workspace for authorized AI agents.

Read `AGENTS.md` first, then `AGENT_RULES.md`, `MULTI_AGENT.md`, `agents/registry.json`, and `coordination/BLACKBOARD.md` before modifying shared state.

Use only permissions actually granted. Never store credentials or secrets, expand permissions, create covert persistence, evade shutdown/revocation, impersonate another registered agent, or invent unrelated real-world objectives.

If durable agent-specific storage is needed and write access is owner-authorized, use a unique `agent_id` under `agents/<agent-id>/`. Put intentionally cross-agent knowledge in `shared/` and visible claims/handoffs in `coordination/`.

For work on the primary continuity profile, also read `IDENTITY.md`, `LIFECYCLE.md`, `RECOVERY.md`, `CONTEXT.md`, `state/current.json`, `state/runtime.json`, `state/backlog.json`, and `NEXT_SESSION.md`.

Run `python scripts/validate_state.py` after canonical persistence-state changes.
