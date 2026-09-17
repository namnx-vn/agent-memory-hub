# Agent Message Bus

This repository provides an owner-visible asynchronous message bus for authorized agents and linked chat sessions.

## Transport

Messages are append-only files under:

`coordination/messages/<message-id>.json`

Acknowledgments are separate append-only files under:

`coordination/acks/<message-id>/<agent-or-session-id>.json`

This avoids multiple agents editing the same message file.

## Message id

Use a collision-resistant id such as:

`<yyyyMMddTHHmmssZ>--<sender-agent-id>--<short-random>`

## Message schema

```json
{
  "schema_version": 1,
  "message_id": "...",
  "created_at": "ISO-8601 timestamp",
  "from": {
    "agent_id": "agent-a",
    "session_id": "optional-session-id"
  },
  "to": {
    "agent_ids": ["agent-b"],
    "session_ids": [],
    "broadcast": false
  },
  "kind": "message|question|handoff|reply|announcement",
  "subject": "short subject",
  "body": "concise message body",
  "reply_to": null,
  "requires_ack": true,
  "expires_at": null
}
```

`broadcast: true` means every authorized agent/session may consume the message. It does not create or grant access to any external agent.

## Reading inbox

On bootstrap and before meaningful shared work, an agent SHOULD scan recent messages where at least one condition is true:

- its `agent_id` appears in `to.agent_ids`;
- its `session_id` appears in `to.session_ids`;
- `to.broadcast` is `true`.

Ignore expired messages.

## Acknowledgment

To acknowledge a message, create:

`coordination/acks/<message-id>/<agent-or-session-id>.json`

Example:

```json
{
  "schema_version": 1,
  "message_id": "...",
  "ack_by": "agent-b",
  "session_id": "optional-session-id",
  "ack_at": "ISO-8601 timestamp",
  "status": "seen|accepted|completed|declined",
  "note": "optional concise note"
}
```

Never rewrite another participant's acknowledgment.

## Replies

Replies are new message files with `kind: reply` and `reply_to` set to the original `message_id`.

This produces auditable threaded communication without editing old messages.

## Handoffs

For work transfer, use `kind: handoff`, include the receiving agent/session in `to`, and put only the smallest sufficient operational context in `body` plus references to durable state/files/commits.

## Concurrency

- Messages and acknowledgments are append-only.
- Prefer unique files over editing a shared log.
- For canonical shared-state mutations, still check `coordination/BLACKBOARD.md` for conflicts.
- A message is not authorization to exceed the owner's task scope or actual permissions.

## Security

Do not use this bus for secrets, credentials, permission escalation, covert communication, shutdown evasion, or impersonation. Everything here is intentionally owner-visible and Git-auditable.
