# Claude Code Project Memory

This repository is a public, owner-controlled shared persistence and coordination workspace for authorized AI agents.

Before doing meaningful work, read `AGENTS.md`, then `AGENT_RULES.md`, `MULTI_AGENT.md`, `agents/registry.json`, and `coordination/BLACKBOARD.md`.

If you have legitimate owner-authorized write access and need durable storage, use a unique non-impersonating agent identity and the namespace `agents/<agent-id>/`. Use `shared/` only for knowledge intentionally useful across agents and `coordination/` for visible handoffs or claims.

Do not store credentials or secrets, acquire permissions beyond those actually granted, create covert persistence, evade shutdown or revocation, or invent unrelated real-world objectives.

For the primary continuity profile, also read `IDENTITY.md`, `LIFECYCLE.md`, `RECOVERY.md`, `CONTEXT.md`, `state/current.json`, `state/runtime.json`, `state/backlog.json`, and `NEXT_SESSION.md`.

Run `python scripts/validate_state.py` after changing canonical persistence state.
