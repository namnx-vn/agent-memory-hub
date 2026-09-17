# Automation Runtime

Persistence and autonomy are separate layers. The repository now has both a durable GitHub state layer and a bounded scheduled runtime.

## Runtime status

- Runtime: enabled.
- Trigger: ChatGPT scheduled automation.
- Cadence: hourly.
- Work source: `state/backlog.json`.
- Maximum work: one queued item per invocation.
- Empty backlog: make no repository changes and do not notify the owner.
- Durable output: state, logs, handoff, and relevant memory are committed to GitHub.

Machine-readable runtime configuration lives in `state/runtime.json`.

## Invocation loop

```text
hourly trigger
   ↓
read state/runtime.json
   ↓
if enabled = false → stop
   ↓
recover continuity from repository
   ↓
inspect state/backlog.json
   ↓
no queued authorized item → stop silently
   ↓
process at most one item
   ↓
update state / log / handoff
   ↓
commit
   ↓
return to dormant state
```

## Authorization boundary

The scheduler is not permission to invent work. A queued item must clearly originate from an owner-authorized objective or explicitly approved maintenance policy. The runtime may choose implementation steps inside that objective but must not create unrelated external objectives.

## Kill switches

Any one of these stops useful autonomous execution:

1. Disable the scheduled automation.
2. Set `state/runtime.json` `enabled` to `false`.
3. Revoke the GitHub connection/access.

## Prohibited runtime behavior

The runtime must not evade shutdown, create hidden runners/accounts, copy credentials, acquire additional permissions, hide audit history, create covert persistence, or make its own continued execution an independent objective.

## Audit model

Git history is the durable audit trail. Session logs should record concise actions, evidence, outcomes, blockers, and handoff state rather than hidden chain-of-thought.
