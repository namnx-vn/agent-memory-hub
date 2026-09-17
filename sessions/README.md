# Sessions

Each participating chat/model invocation may create one directory:

`sessions/<session-id>/session.json`

See `SESSION_LINKING.md` for schema and lifecycle.

This directory is a durable graph of operational session summaries and links, not a transcript archive and not a store for hidden chain-of-thought.
