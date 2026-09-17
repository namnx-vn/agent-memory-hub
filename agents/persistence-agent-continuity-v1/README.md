# persistence-agent-continuity-v1

This namespace belongs to the continuity profile `persistence-agent/continuity-v1`.

It may store agent-specific durable state, notes, handoffs, checkpoints, or task-local knowledge that should not be promoted into the global `shared/` namespace.

Canonical workspace state remains in `state/`; durable knowledge useful to all agents belongs in `shared/`; cross-agent coordination belongs in `coordination/`.

Do not store credentials, secrets, hidden communication, or shutdown-resistance mechanisms here.
