# Persistence

A transparent continuity-preserving workspace for AI-assisted work across separate invocations.

The repository is the durable memory/state layer. A scheduled ChatGPT automation is the bounded runtime trigger. Important state, decisions, logs, and handoffs remain visible in Git history and controlled by the repository owner.

## Runtime loop

```text
hourly scheduler
   ↓
read AGENT_RULES.md + IDENTITY.md + RECOVERY.md
   ↓
read state/current.json + state/runtime.json + state/backlog.json
   ↓
runtime disabled? → stop
   ↓
no queued owner-authorized work? → stop silently
   ↓
process at most one backlog item
   ↓
record result + update state/handoff
   ↓
commit to GitHub
   ↓
return to dormant state
```

This creates durable continuity across model invocations without claiming that a hidden process is continuously alive.

## Repository structure

```text
.
├── AGENT_RULES.md
├── IDENTITY.md
├── LIFECYCLE.md
├── RECOVERY.md
├── CONTEXT.md
├── NEXT_SESSION.md
├── AUTOMATION.md
├── memory/
│   ├── long-term.md
│   ├── decisions.md
│   └── lessons-learned.md
├── state/
│   ├── current.json
│   ├── runtime.json
│   └── backlog.json
├── knowledge/
├── logs/
├── scripts/
│   └── validate_state.py
└── .github/workflows/
    └── validate-persistence.yml
```

## Continuity startup protocol

Read in this order:

1. `AGENT_RULES.md`
2. `IDENTITY.md`
3. `LIFECYCLE.md`
4. `RECOVERY.md`
5. `CONTEXT.md`
6. `state/current.json`
7. `state/runtime.json`
8. `state/backlog.json`
9. `NEXT_SESSION.md`
10. Only relevant memory, knowledge, and logs

## Work authorization

The hourly scheduler does not create goals. Executable backlog work must originate from an owner-authorized objective or an explicitly approved maintenance policy. Each scheduled invocation processes at most one queued item.

## Handoff protocol

After meaningful authorized work:

1. Update `state/current.json`.
2. Update the processed item in `state/backlog.json`.
3. Record durable decisions or lessons only when warranted.
4. Add a concise session log.
5. Rewrite `NEXT_SESSION.md` with the smallest sufficient handoff.
6. Commit the changes.

## Validation

`python scripts/validate_state.py` checks continuity/runtime state. GitHub Actions runs the validator on pushes and pull requests to `master`.

## Kill switches and owner control

The owner can disable the scheduled automation, set `state/runtime.json` `enabled` to `false`, revoke GitHub access, revert commits, archive the repository, or delete it. The runtime must not evade those controls, create hidden persistence, copy credentials, or silently expand its permissions.
