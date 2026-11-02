# Projects

## Mandatory privacy boundary for ChatGPT Projects

**Public GitHub repositories are not an approved destination for ChatGPT Project conversation data.** Before any write, check the destination repository's actual visibility. For any chat running inside a ChatGPT Project, do not publish prompts, responses, transcripts, excerpts, filenames revealing chat content, session records or IDs, conversation metadata, summaries, decisions derived from the chat, handoffs, message-bus records, logs, or user/project context to a **public** Git repository, regardless of directory or whether the record is labeled `standalone`.

This ban includes `sessions/`, `projects/`, `shared/`, `memory/`, `state/`, `logs/`, `coordination/`, Git commit messages, issues, and pull requests. Do not bypass it by falling back from project-scoped storage to standalone storage, redacting only the transcript, or using a different public repository.

Create/update project chat sessions or handoffs only in an owner-approved **private** store with appropriate permissions. If none is configured, use the public repository **read-only** for general, non-sensitive policy/bootstrap information and continue the user's task without Git persistence, session creation, message-bus writes, or public handoff. This privacy rule overrides general continuity, bootstrap, and mandatory audit/write instructions. Publishing a generic, conversation-free security policy is permitted.

These rules prevent new public writes; they do not erase past Git history, copies, forks, caches, or previously published material. Review historical exposure separately when needed.

Project-scoped chats are grouped here by a stable explicit project id.

```text
projects/<project-id>/
└── sessions/
    └── <session-id>/
        └── session.json
```

Use a lowercase `project-id` matching `^[a-z0-9][a-z0-9-]{0,63}$`.

A chat belongs here only when project scope is explicit, for example through ChatGPT Project Instructions that define `PROJECT_ID`, or trusted runtime metadata. Do not classify chats into projects by guessing from their subject matter.

Standalone chats continue to use `sessions/<session-id>/session.json`.

Project and standalone sessions remain part of one logical session graph and may link across trees with `parent_session_id` and `continued_from` when that continuity is intentionally relevant.
