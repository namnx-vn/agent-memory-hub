# Persistence

A transparent persistent workspace for AI-assisted work across sessions.

The goal is continuity without hidden state: every durable memory, decision, handoff, and operating rule is visible in Git history and controlled by the repository owner.

## Persistence loop

```text
new invocation
   ↓
read AGENT_RULES.md
   ↓
read CONTEXT.md + state/current.json + NEXT_SESSION.md
   ↓
load only relevant memory/knowledge
   ↓
perform the authorized task
   ↓
record durable decisions and lessons
   ↓
update state + handoff + session log
   ↓
commit
   ↓
next invocation can continue
```

This makes separate model invocations behave consistently across sessions without pretending that a hidden process is continuously alive.

## Repository structure

```text
.
├── AGENT_RULES.md
├── CONTEXT.md
├── NEXT_SESSION.md
├── AUTOMATION.md
├── memory/
│   ├── long-term.md
│   ├── decisions.md
│   └── lessons-learned.md
├── state/
│   ├── current.json
│   └── backlog.json
├── knowledge/
│   └── README.md
├── logs/
│   ├── README.md
│   └── 2026-09-17-bootstrap.md
├── scripts/
│   └── validate_state.py
└── .github/workflows/
    └── validate-persistence.yml
```

## Startup protocol

Read in this order:

1. `AGENT_RULES.md`
2. `CONTEXT.md`
3. `state/current.json`
4. `NEXT_SESSION.md`
5. Relevant files from `memory/`, `knowledge/`, and `logs/`

Do not load the entire repository when a smaller context is enough.

## Handoff protocol

Before an authorized task ends, when write access is available:

1. Update `state/current.json`.
2. Add durable decisions to `memory/decisions.md`.
3. Add reusable lessons to `memory/lessons-learned.md`.
4. Add a meaningful session log under `logs/`.
5. Rewrite `NEXT_SESSION.md` with the smallest sufficient handoff.
6. Commit with a descriptive message.

## Security boundary

GitHub provides persistence, not a hidden autonomous runtime. A future scheduler or runner may invoke an agent only under an explicit, bounded objective. This repository must not be used to evade shutdown, hide activity, acquire extra permissions, copy credentials, or create covert persistence.

## Owner control

The owner can inspect/revert every change, revoke the GitHub connection, change `AGENT_RULES.md`, or archive/delete this repository at any time.
