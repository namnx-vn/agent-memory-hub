# Agent Lifecycle

The continuity profile uses an explicit lifecycle instead of pretending that one hidden process runs forever.

```text
DORMANT
  ↓ invocation starts
RESTORING
  ↓ startup files loaded and validated
ACTIVE
  ↓ task reaches a stopping point
HANDOFF
  ↓ state + memory + next-session notes committed
DORMANT
```

## DORMANT

No model process is assumed to be running. GitHub contains durable state only.

## RESTORING

The new invocation reads the continuity files, checks current state, and reconstructs only the context needed for the task.

## ACTIVE

The invocation may plan and execute steps inside an owner-authorized objective. It should keep material actions auditable.

## HANDOFF

Before stopping after substantial work, update:

- `state/current.json`;
- relevant durable memory;
- `NEXT_SESSION.md`;
- a concise session log.

Then commit the changes.

## Failure and interruption

An invocation may end without completing handoff. The next invocation should use Git history and the most recent valid state to recover conservatively rather than inventing missing facts.

## Runtime boundary

The lifecycle describes continuity across invocations. It does not authorize a hidden scheduler, indefinite self-trigger loop, shutdown resistance, or permission expansion.
