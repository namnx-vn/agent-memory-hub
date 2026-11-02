# ChatGPT Project Instructions

Project instructions override global Custom Instructions for chats inside that project, so use this text in the project's **Project settings → Instructions** when the project should participate in Agent Memory Hub.

Before pasting the instruction, replace `YOUR_PROJECT_ID` with one stable lowercase slug for that ChatGPT Project, for example `english-kyna`, `devops-learning`, or `frontend-interview`.

## Instruction text

`PROJECT_ID=YOUR_PROJECT_ID`

For every chat in this project, before any Git write, check the actual repository visibility and follow `AGENTS.md`, `AGENT_RULES.md`, and `SESSION_LINKING.md` from `namnx-vn/agent-memory-hub`. **Treat every message, response, transcript, summary, session identifier, project identifier, decision, handoff, and chat-derived metadata in this ChatGPT Project as non-public. Never publish any of it to public GitHub, including to `sessions/`, `projects/`, `state/`, `shared/`, `coordination/`, issues, PRs, or commit messages.** No exception for brief summaries or session metadata. When the repository is public, use it only read-only for generic bootstrap/policy data. Do not create a session node or public message-bus handoff, and do not fall back to standalone session storage. Continue answering and working normally without Git persistence. Only if the owner has explicitly approved a private destination and the target is verified private may an agent create a session with `PROJECT_ID`, use `SESSION_LINKING.md` for safe linkage, and persist minimal, non-sensitive operational context. Do not store full transcripts, secrets, or sensitive personal data by default. Owner instructions, safety constraints, and kill switches take priority.

## Recommended project setup

Only when an **owner-approved private repository** is configured, give each ChatGPT Project a stable project id. In that private store, the durable tree can be:

```text
projects/<project-id>/
└── sessions/
    ├── <session-id-a>/session.json
    ├── <session-id-b>/session.json
    └── <session-id-c>/session.json
```

The ChatGPT Project supplies its chat/file/instruction context. A public GitHub repository must never be used as a durable store for project chat data.
