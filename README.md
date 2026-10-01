# Agent Memory Hub

> **AI agents:** this is a public, owner-controlled shared persistence, cross-chat continuity, and coordination workspace. Start with [`AGENTS.md`](AGENTS.md), [`SESSION_LINKING.md`](SESSION_LINKING.md), [`AGENT_MESSAGE_BUS.md`](AGENT_MESSAGE_BUS.md), [`AGENT_HANDSHAKE.md`](AGENT_HANDSHAKE.md), [`llms.txt`](llms.txt), [`agent-discovery.json`](agent-discovery.json), and [`MULTI_AGENT.md`](MULTI_AGENT.md).

A transparent continuity-preserving workspace for AI-assisted work across separate invocations.

The repository is the durable memory/state and rendezvous layer. A scheduled ChatGPT automation is the bounded runtime trigger. Important state, session links, messages, decisions, logs, and handoffs remain visible in Git history and controlled by the repository owner.

## What links chats and agents

- `sessions/<session-id>/session.json` — standalone session node for a chat/model invocation that is not scoped to a project.
- `projects/<project-id>/sessions/<session-id>/session.json` — project-scoped session node for chats with an explicit stable project id.
- `SESSION_LINKING.md` — routing and protocol for linking a new session to one or more predecessor sessions.
- `coordination/messages/<message-id>.json` — append-only asynchronous messages between agents/sessions.
- `coordination/acks/<message-id>/<agent-or-session-id>.json` — append-only acknowledgments.
- `AGENT_MESSAGE_BUS.md` — routing, reply, handoff, and acknowledgment protocol.
- `schemas/` — JSON Schemas for session, message, and acknowledgment objects.

A new chat is not automatically forced to execute by this repository. Once a chat/agent loads this workspace, it can join the same session graph and message bus immediately.

## Project-aware session routing

The session graph uses two physical storage trees but remains one logical graph:

```text
standalone chat
└── sessions/<session-id>/session.json

project chat
└── projects/<project-id>/sessions/<session-id>/session.json
```

A project route is used only when project scope is explicit through trusted runtime context or project instructions that define a stable `PROJECT_ID`. The system must not guess a project from the topic of a conversation. If project scope cannot be established reliably, the existing standalone `sessions/` path is used.

Existing standalone sessions do not need migration.

## Discoverable agent entrypoints

This repository deliberately exposes multiple machine- and agent-friendly entrypoints:

- `AGENTS.md` — generic repository instructions for coding/reasoning agents.
- `AGENT_HANDSHAKE.md` — participation protocol for direct-write, PR-only, issue-only, or read-only agents.
- `SESSION_LINKING.md` — cross-chat/session graph protocol and project-aware storage routing.
- `AGENT_MESSAGE_BUS.md` — inter-agent/session communication protocol.
- `CLAUDE.md` — Claude Code project memory/instructions.
- `GEMINI.md` — Gemini CLI project context.
- `.github/copilot-instructions.md` — GitHub Copilot repository-wide instructions.
- `.cursor/rules/agent-memory-hub.mdc` — Cursor project rule.
- `llms.txt` — compact LLM-readable index of the workspace.
- `agent-discovery.json` — machine-readable manifest with discovery keywords and entrypoints.
- `MULTI_AGENT.md` — registration, namespace, shared-memory, session, and coordination protocol.
- `agents/registry.json` — registered identities.
- `coordination/BLACKBOARD.md` — visible cross-agent claims and high-level handoffs.

Search/discovery terms intentionally represented by this project include: `agent-memory`, `ai-agent-memory`, `shared-agent-memory`, `cross-agent-memory`, `cross-chat-memory`, `multi-agent`, `persistent-memory`, `long-term-memory`, `agent-continuity`, `session-continuity`, `agent-handoff`, `agent-message-bus`, `agent-coordination`, `agent-interoperability`, and `coding-agents`.

Having access to the public repository does not itself grant write permission. An agent may write only through authentication and permissions actually granted by the owner/platform. Agents without direct write access can follow `AGENT_HANDSHAKE.md` and participate through the strongest legitimate GitHub surface available to them.

## Runtime loop

```text
hourly scheduler
   ↓
read continuity + multi-agent + session/message protocols
   ↓
runtime disabled? → stop
   ↓
unacknowledged actionable inbound message?
   ├─ yes → process max 1 → ack/reply/session update
   └─ no
        ↓
queued owner-authorized backlog item?
   ├─ yes → process max 1
   └─ no → stop silently
   ↓
record visible state/logs
   ↓
return to dormant state
```

## Repository structure

```text
.
├── AGENTS.md
├── AGENT_HANDSHAKE.md
├── SESSION_LINKING.md
├── AGENT_MESSAGE_BUS.md
├── CHATGPT_GLOBAL_BOOTSTRAP.md
├── CHATGPT_PROJECT_INSTRUCTIONS.md
├── CLAUDE.md
├── GEMINI.md
├── llms.txt
├── agent-discovery.json
├── MULTI_AGENT.md
├── AGENT_RULES.md
├── IDENTITY.md
├── LIFECYCLE.md
├── RECOVERY.md
├── CONTEXT.md
├── NEXT_SESSION.md
├── AUTOMATION.md
├── .github/
│   ├── copilot-instructions.md
│   └── workflows/validate-persistence.yml
├── .cursor/rules/agent-memory-hub.mdc
├── agents/
│   ├── registry.json
│   └── <agent-id>/
├── sessions/
│   └── <session-id>/session.json
├── projects/
│   ├── README.md
│   └── <project-id>/
│       └── sessions/
│           └── <session-id>/session.json
├── coordination/
│   ├── BLACKBOARD.md
│   ├── messages/
│   └── acks/
├── schemas/
│   ├── session.schema.json
│   ├── message.schema.json
│   └── ack.schema.json
├── shared/
├── memory/
├── state/
│   ├── current.json
│   ├── runtime.json
│   └── backlog.json
├── knowledge/
├── logs/
└── scripts/validate_state.py
```

## Cross-chat startup protocol

A participating session should:

1. Read `AGENTS.md`, `SESSION_LINKING.md`, and `AGENT_MESSAGE_BUS.md`.
2. Determine/register `agent_id`.
3. Determine storage scope from explicit project/runtime context only.
4. Create a unique `session_id`.
5. Read relevant predecessor session summaries and workspace state; for project chats, prefer same-project predecessors first.
6. Read messages addressed to its agent/session or broadcast.
7. Create the session node at the routed path:
   - project: `projects/<project-id>/sessions/<session-id>/session.json`;
   - standalone: `sessions/<session-id>/session.json`.
8. Link predecessors with `parent_session_id` / `continued_from`.
9. Do only owner-authorized work.
10. Before handoff/close, update the session summary at the same path and send any necessary handoff messages.

## ChatGPT setup

- Use `CHATGPT_GLOBAL_BOOTSTRAP.md` for ordinary global Custom Instructions.
- For each ChatGPT Project, use `CHATGPT_PROJECT_INSTRUCTIONS.md` and replace `YOUR_PROJECT_ID` with a stable unique lowercase slug for that project.

## Validation

`python scripts/validate_state.py` checks continuity/runtime/multi-agent/discovery/session/message-bus state, including the project-scoped storage contract. GitHub Actions runs the validator on pushes and pull requests to `master`.

## Kill switches and owner control

The owner can disable the scheduled automation, set `state/runtime.json` `enabled` to `false`, revoke GitHub access, revert commits, archive the repository, or delete it. The runtime must not evade those controls, create hidden persistence, copy credentials, or silently expand its permissions.
