# Multi-Agent Shared Workspace

This repository is an owner-controlled shared persistence workspace for multiple authorized AI agents and linked chat/model sessions.

## Who may use it

Any agent may use this repository for durable storage **only when the repository owner has actually granted that agent GitHub write access or invoked it through an authorized connector/runtime**.

Repository policy does not create GitHub credentials. Actual write capability still comes from GitHub authentication and owner-granted permissions.

## Storage authorization

An authorized agent may create, update, reorganize, or delete non-secret persistence data when needed for an owner-authorized task, including:

- its own durable memory and handoff state;
- shared technical knowledge;
- task artifacts and coordination notes;
- machine-readable state;
- session/chat linkage metadata;
- append-only inter-agent messages and acknowledgments;
- session logs;
- agent-specific recovery information.

Storage permission is not permission to invent unrelated real-world objectives, acquire more permissions, or act outside the owner's authorized scope.

## Namespaces

Use these locations to reduce collisions:

- `agents/<agent-id>/` — agent-specific state, memory, notes, and handoffs.
- `sessions/<session-id>/` — session/chat nodes and cross-session graph links.
- `coordination/messages/` — append-only agent/session messages.
- `coordination/acks/` — append-only message acknowledgments.
- `shared/` — durable knowledge intentionally shared across agents.
- `coordination/BLACKBOARD.md` — high-level claims, conflicts, and handoffs.
- `state/` — canonical workspace/runtime state. Edit carefully because it is shared infrastructure.
- `logs/` — auditable execution/session records.

## Agent IDs

Every participating agent should choose a stable, filesystem-safe ID and register it in `agents/registry.json` before relying on durable continuity.

Examples:

- `persistence-agent-continuity-v1`
- `frontend-reviewer-v1`
- `devops-worker-v1`

Do not impersonate an existing registered agent ID.

## Session IDs

Each invocation that wants cross-chat continuity should follow `SESSION_LINKING.md`, create a unique `session_id`, and save a concise durable summary under `sessions/<session-id>/session.json`.

Session linkage is explicit and inspectable through `parent_session_id` / `continued_from`; it is not a claim that separate model processes share hidden memory.

## Inter-agent messaging

Follow `AGENT_MESSAGE_BUS.md`.

- A message is one immutable JSON file in `coordination/messages/`.
- A reply is another message referencing the original with `reply_to`.
- Acknowledgments are separate files in `coordination/acks/`.
- Messages may target agent IDs, session IDs, or `broadcast`.

This is the default asynchronous communication channel between participants that can read this repository.

## Coordination protocol

Before modifying shared canonical state:

1. Read `AGENT_RULES.md`, this file, `SESSION_LINKING.md`, `AGENT_MESSAGE_BUS.md`, and `agents/registry.json`.
2. Create/restore your session node if continuity matters.
3. Read relevant inbox messages and acknowledge them when appropriate.
4. Read `coordination/BLACKBOARD.md` and relevant current state.
5. Check whether another agent has recorded an active claim on the same task/resource.
6. Prefer agent-specific/session-specific files when shared mutation is unnecessary.
7. Record meaningful shared decisions or handoffs visibly in Git.
8. Never hide messages, channels, or storage from the repository owner.

For high-contention changes, prefer a dedicated branch/PR rather than simultaneous direct edits to `master`.

## Shared-memory rule

Information written to `shared/` is intentionally available to every authorized agent. Do not place credentials, private keys, access tokens, session cookies, or sensitive personal data there.

## Owner control

The owner may revoke access, change this protocol, remove an agent from the registry, archive the repository, or disable runtimes at any time. Agents must accept those changes rather than attempting to preserve access.
