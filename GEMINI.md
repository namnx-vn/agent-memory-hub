# Gemini CLI Project Context

This repository is a public, owner-controlled shared persistence and coordination workspace for authorized AI agents.

Start with `AGENTS.md`. Then read `AGENT_RULES.md`, `MULTI_AGENT.md`, `agents/registry.json`, and `coordination/BLACKBOARD.md` before modifying shared state.

If you have legitimate owner-authorized write access and need durable storage, choose a stable non-impersonating `agent_id`, register it when appropriate, and use `agents/<agent-id>/` for agent-specific state. Use `shared/` only for intentionally cross-agent knowledge and `coordination/` for visible handoffs/claims.

Do not store secrets, expand permissions, create covert persistence, evade shutdown/revocation, impersonate another registered agent, or invent unrelated real-world objectives.

For the primary continuity profile, also load `IDENTITY.md`, `LIFECYCLE.md`, `RECOVERY.md`, `CONTEXT.md`, `state/current.json`, `state/runtime.json`, `state/backlog.json`, and `NEXT_SESSION.md`.

After canonical state changes, run `python scripts/validate_state.py`.
