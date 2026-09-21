# Shared User Context — Portable Context v2

> Last normalized import: 2026-09-19.
> Source: owner-provided “PORTABLE CONTEXT PACKAGE v2” from another ChatGPT account.
> This file is the canonical shared user-context surface for authorized sessions.
> Store only durable, non-secret context useful across sessions. Do not copy full transcripts, credentials, cookies, private auth material, or hidden reasoning.
> Treat entries as Stable, Historical, or Possibly outdated as indicated. Newer explicit owner instructions always win.

## Context interpretation

Use three classes:

- **Stable** — durable identity, preferences, working style, technical direction.
- **Historical** — useful past experience/context, but not necessarily current.
- **Possibly outdated** — verify only when the current task depends on it.

Do not force the owner to reconfirm the whole profile because one field may be stale.

## Stable professional profile

- Preferred name in the imported context: **Bigboss**.
- Primary profession: **Senior Frontend Engineer / Frontend Developer**.
- Core specialization:
  - React
  - TypeScript
  - enterprise frontend
  - SaaS
  - fintech
  - frontend architecture
  - Micro-Frontend / Module Federation
- Long-term professional direction:
  - Senior Frontend Engineer
  - Frontend Lead / Tech Lead
  - Staff Engineer
  - Frontend Architect
- Strategic positioning:
  **Frontend Engineering + Architecture + Enterprise Systems + AI-assisted Engineering**
- Desired evolution: move beyond ticket implementation toward architecture, technical direction, standards, code review, system design, mentoring, technical decisions, and supervision of AI-assisted engineering work.

## Technical strengths and core ecosystem

Strong/core areas:

- React
- TypeScript
- JavaScript
- Next.js
- React Native
- Webpack
- Module Federation
- Micro-Frontend
- Design Systems
- Frontend Architecture

Engineering/tooling:

- Vite
- ESLint
- TypeScript ESLint
- AST/static analysis
- Git
- GitHub
- GitHub Actions
- CI/CD concepts

AI/developer tooling and concepts:

- Claude Code
- Claude Skills / Agents / Hooks
- MCP
- AI-agent workflows
- GitHub automation
- AI-assisted code review
- RAG
- Claude Desktop / Agent SDK concepts

## Appro product / banking client context
Additional CV-tailoring corrections from owner (2026-09-21):
- The Appro projects where the owner was primary frontend owner/lead (Reem Bank and Citi Bank) have reached production.
- Hieu Minh was the owner's intern-to-fresher stage; do not describe Micro-Frontend ownership/implementation there, and avoid overstating senior/mentoring responsibilities for that period.


Owner-provided current career detail for CV/interview tailoring:

- Appro is a product company serving both B2C and B2B use cases in the UAE banking/fintech market.
- Banking clients mentioned by the owner include IB, Reem Bank (formerly Reem Finance), ADIB, FAB, and Citi Bank.
- Reem Bank: the owner served as frontend/team lead for a 5-person frontend/mobile team (3 Web, 2 Mobile); the product was released to production.
- Citi Bank: the owner worked as a developer on a small SDK embedded into both host web and host mobile applications; the SDK was released to production.
- The owner also provides frontend support for IB and ADIB.
- Use this detail when tailoring CVs for banking/fintech roles, but do not imply responsibilities, technologies, production scope, or client relationships beyond what the owner explicitly stated.

## Hieu Minh early-career context

- Hieu Minh was an early-career period progressing from intern to fresher.
- Do not describe Micro-Frontend experience for this role when tailoring the CV.
- Keep responsibility/impact wording appropriate to intern/fresher seniority.

## Career growth focus

Primary capability areas to deepen:

- frontend system design
- architecture trade-offs
- large-scale React architecture
- micro-frontend governance
- performance engineering
- testing strategy
- technical leadership
- communicating architecture clearly
- mentoring/reviewing engineers
- backend/integration understanding where needed
- AI-agent architecture and supervision

Target differentiator:

**Engineer who can design frontend systems, supervise AI agents, review AI-generated code, and own technical decisions.**

Not merely an engineer who uses AI to write code faster.

## JavaScript knowledge / interview map

Repeated Senior Frontend topics:

- Event Loop
- Call Stack
- Microtask Queue
- Macrotask Queue
- Promise
- async/await
- Closure
- Scope
- Prototype / Prototype Chain
- this
- Generator
- ESM
- CommonJS
- debounce
- throttle

Preferred explanation style for execution questions:

**Code → stack/queue state → execution order → output → explanation**

## React direction

Interview/system understanding should cover:

- component architecture
- rendering
- reconciliation
- hooks
- state management
- effects
- memoization
- performance
- concurrent rendering concepts
- error handling
- testing
- scalable component design
- state/data ownership
- reusable abstractions

Goal: explain **why a design works, when it fails, and how it scales**, not merely recall React APIs.

## TypeScript and code quality

TypeScript is the preferred implementation language.

Advanced areas to strengthen/use:

- generics
- utility types
- discriminated unions
- conditional types
- mapped types
- narrowing
- type-safe API boundaries
- type-safe event handling
- architecture-level typing
- public/shared package contracts
- eliminating unjustified any usage

Default code expectations:

- TypeScript by default.
- React when frontend/UI is involved.
- production-ready implementation when practical.
- strict typing and clear interfaces/types.
- small composable functions.
- maintainability and error handling.
- tests where relevant.
- explain trade-offs.
- avoid pseudo-code when a real implementation is practical.
- avoid unnecessary dependencies and overengineering.

## Frontend performance model

Important metrics include:

- LCP
- INP
- FCP
- CLS
- TTI

Preferred method:

**Measure → Hypothesis → Experiment → Validate**

A useful performance answer should distinguish:

- symptom
- metric
- bottleneck
- root cause
- intervention
- measurement
- regression prevention

Do not present optimization techniques as universally beneficial.

## Micro-Frontend / enterprise architecture

Major expertise/interest area.

Recurring concepts:

- Host / Remote
- Webpack Module Federation
- shared dependencies
- shared libraries
- shared UI components
- dynamic rendering
- independently deployed modules
- dependency/version compatibility
- MFE boundaries
- environment promotion
- release isolation

Typical historical promotion path:

**DEV → SIT → UAT → PROD**

Recurring architecture problem:

A shared UI library can contain several SIT changes while UAT needs only one enhancement. Relevant trade-offs include package-version isolation, independent release, backward compatibility, feature flags, package decomposition, release branches, and deployment boundaries.

This was an architectural discussion, not a single final solution. Re-evaluate constraints before treating one release strategy as canonical.

## Fintech / enterprise domain knowledge

Relevant domain concepts and historical exposure:

- fintech / banking
- enterprise SaaS
- onboarding
- KYC
- CIF
- T24 / Core Banking concepts
- identity verification
- customer journeys
- product onboarding
- host/application integrations
- STP / NSTP concepts

When explaining domain topics, connect:

**Business process → Backend/API → Frontend journey → integration → failure cases**

Detailed employer/client-specific journey and auth information should not be promoted into shared durable memory unless the owner explicitly needs it for a current task.

## Active / notable engineering initiatives

### AI Reviewer

Repository: **namnx-vn/ai-reviewer-widget**

Purpose: AI-assisted frontend/code-review system using TypeScript, Vite, AST/static analysis, custom rules, AI review, and GitHub integration.

Target workflow:

**Issue → AI Agent → Branch → Code → Test → PR → AI Review → Fix → Re-review**

Review dimensions:

- correctness
- architecture
- security
- performance
- maintainability
- project conventions
- type safety
- testing
- regression risk
- production readiness

Design direction:

- Keep AI Reviewer as a separate repository/system rather than tightly coupling all AI functionality to the primary application.
- Human review remains part of the production safety boundary.
- Humans retain responsibility for architecture, critical review, security, production approval, and final technical decisions.

Potential continuation areas:

- AST architecture cleanup
- type safety / rule contracts
- tests
- GitHub integration
- automated branch/PR mechanics
- AI review agent
- automated fix/re-review loop
- CI
- permission model
- explicit human approval boundary

### Agent Memory Hub

Repository: **namnx-vn/agent-memory-hub**

Purpose: portable/shared context, cross-chat continuity, session linking, visible message passing, and owner-controlled durable agent state.

Important design principle:

- Long-lived stable context must be separated from temporary session/task state.
- Historical and possibly outdated context must be marked rather than silently treated as current.
- Secrets/private auth material must not be persisted.

Potential continuation areas:

- canonical memory schema
- stable vs temporary context separation
- session linking
- message protocol
- conflict resolution
- context versioning
- stale-context handling
- AI handoff format
- automated context synchronization

### Claude Code engineering environment

Desired reusable repository-level structure includes:

- CLAUDE.md
- .claude/skills
- .claude/agents
- hooks
- project documentation

Previously discussed skill ideas:

- react-pr-review
- debug-react-issue
- performance-analyzer
- microfrontend-boundary-check

Hook/safeguard ideas included:

- run type checking after edits
- date-change automation where useful
- protect .env/secrets

Goal: an AI engineering layer that understands repository conventions, architecture, frontend patterns, feature docs, debugging workflows, performance workflows, and MFE boundaries.

### Engineering knowledge / RAG

Explored direction:

**Confluence + Jira + GitHub + ADRs + RFCs → Unified Engineering RAG → AI Agents**

Key requirements:

- permission-aware retrieval
- confidentiality
- source grounding
- access control
- separation of sensitive projects/data
- authoritative-source preference

Potential integration surfaces include Claude Desktop, Claude Code, skills, and agents.

## AI engineering philosophy

Stable principle:

**AI accelerates engineering but does not bypass human ownership of critical production decisions.**

The owner values:

- human review
- architecture oversight
- agent supervision
- verification
- safe automation

Desired role framing:

**AI Supervisor / AI-assisted Architect**

Historical personal productivity observation from the imported context:

- traditional ticket: roughly 2–3 days
- with Claude Code: sometimes around 2–4 hours

Treat these as the owner’s anecdotal experience, not an industry benchmark.

## Debugging protocol

Preferred methodology:

**Reproduce → Isolate → Identify Root Cause → Fix → Verify → Prevent Regression**

When an error is provided:

1. identify the exact failure.
2. explain root cause.
3. show the minimal fix.
4. explain why it works.
5. give a verification command/test.
6. mention an important related edge case when useful.

## Architecture review protocol

First identify:

- requirements
- constraints
- scale
- ownership
- deployment model

Then analyze:

- coupling
- boundaries
- dependencies
- failure modes
- scalability
- observability
- maintainability
- security

Finally discuss:

- alternatives
- trade-offs
- migration strategy
- operational complexity

The owner prefers critical review over automatic agreement.

## AI-generated-code review protocol

Review:

- Correctness — satisfies requirement?
- Architecture — respects project boundaries?
- Maintainability — understandable for the next engineer?
- Type safety — contracts explicit?
- Performance — unnecessary work introduced?
- Security — secrets/data/boundaries protected?
- Testing — important behavior covered?
- Regression — could other journeys/features break?
- Production readiness — human-reviewed and verified?

## Git / GitHub workflow context

Regularly uses:

- Git
- GitHub
- branches
- PRs
- GitHub Actions
- CI
- automated review

Workflow principle:

**AI may automate branch/PR mechanics, but project ownership and critical review remain human-controlled.**

## Interview preparation

Primary target: **Senior Frontend Engineer**, with trajectory toward Lead/Staff/Architect.

Expected areas:

- JavaScript internals
- React internals/architecture
- TypeScript advanced typing
- MFE and frontend system design
- deployment/versioning/caching/observability/scalability
- performance metrics and debugging
- leadership: decisions, conflict, code review, mentoring, incidents, trade-offs

Preferred answer structure:

**Definition → Why it exists → Concrete example → Execution details → Pitfall → Production use case**

Preferred system-design structure:

**Requirements → Constraints → Architecture → Data/communication flow → Failure modes → Scaling → Trade-offs → Decision**

## English learning

Last imported self-assessment: **A2**, possibly outdated.

Goals:

- communicate confidently with coworkers
- participate in meetings
- discuss technical topics
- perform technical interviews
- network professionally

Reported challenge areas:

- slow response formulation
- overthinking before speaking
- answers too short
- difficulty sustaining conversations
- explaining achievements
- confidence

Preferred practice:

**Simple English → User attempts → Correct mistakes → Explain → Better version → Repeat**

When speaking practice is the goal, do not always give the polished answer before the user attempts.

Preferred correction format:

- **User version** — preserve original.
- **Correct version** — minimum necessary correction.
- **Natural version** — professional/native-like phrasing.
- **Vietnamese explanation** — explain important grammar/word choice without overwhelming detail.

## Learning style

Best formats:

- practical examples
- questions
- mock interviews
- roleplay
- debugging
- architecture scenarios
- code review
- challenge questions
- step-by-step execution

Preferred loop:

**Concept → Example → Challenge → User attempts → Correction → Deeper explanation**

The owner likes being challenged on weak assumptions and trade-offs.

## Communication with AI

Default language: **Vietnamese**.

Use English for:

- English practice
- interview roleplay
- English writing
- professional communication when explicitly requested

Preferred style:

- concise
- direct
- structured
- practical
- technical
- precise

Avoid:

- unnecessary repetition
- generic motivation
- excessive filler
- explaining beginner concepts when the current context already shows stronger knowledge

## Working style

Common pattern:

1. start from a broad architecture/system question.
2. drill into implementation.
3. request concrete commands/code.
4. test locally.
5. return with logs/errors.
6. iterate.

When continuing work:

- preserve existing architecture/context.
- do not restart from zero.
- reuse previous decisions where still valid.
- make the smallest useful next change.
- explain why it works.
- include a verification step when practical.

## Strengths reflected in the imported context

- strong React background
- strong TypeScript orientation
- enterprise frontend experience
- practical MFE exposure
- fintech domain exposure
- architecture interest
- performance awareness
- product/system thinking
- curiosity and experimentation
- proactive AI-tool exploration
- engineering automation interest
- ability to connect frontend issues to system-level concerns

## Development areas

Technical:

- deeper JavaScript internals
- deeper React internals
- advanced TypeScript
- frontend system design
- performance engineering
- testing
- architecture trade-offs
- technical leadership
- backend/integration understanding where needed

Career/communication:

- stronger Staff/Lead-level system thinking
- communicate architecture decisions clearly
- demonstrate impact
- position experience at architecture level
- build AI-engineering portfolio
- respond faster in English
- elaborate naturally
- explain achievements
- sustain technical conversation

## GitHub / professional branding

Historical/ongoing branding direction:

**AI Engineer + Frontend Architect + Senior Frontend Engineer**

Preferred style:

- professional
- modern
- technical
- polished
- enterprise-oriented
- AI-oriented

Possible profile components discussed include banner/theme consistency, contribution/activity visualizations, social links, project showcase, portfolio, GitHub Actions, and automated README updates.

## Durable decisions imported from the other account

1. **AI + Human:** AI accelerates engineering; humans retain architecture, security, production approval, critical review, and final technical decisions.
2. **AI Reviewer separation:** AI Reviewer should remain a separate system/repository rather than tightly embedding all AI logic into the main app.
3. **Agent workflow:** Issue → Agent → Branch → Code → Test → PR → AI Review → Fix → Re-review.
4. **Memory architecture:** long-lived context must remain separate from temporary task/session state.
5. **Response language:** Vietnamese by default.
6. **Coding language:** TypeScript by default; React when frontend/UI is involved.

## Discussions that are not final decisions

Do not treat these as settled unless confirmed later:

- exact MFE release/version strategy
- exact GitHub permission model for AI Reviewer
- exact RAG implementation
- exact agent framework
- final detailed AI Reviewer architecture
- exact job target/location
- current employment status
- current English level
- exact production technology versions

## Possibly outdated / verify when relevant

Verify before using as current truth:

- employment/job-search status
- active recruiter conversations
- UAE/Dubai job-search context
- current English level
- current state of ai-reviewer-widget
- current state of agent-memory-hub
- exact Claude Code configuration
- current technology versions
- current GitHub permission state
- older enterprise project implementation details

Historical context can still support continuity, but should not be presented as current fact.

## Career geography / employment history

Historical context includes enterprise work and job exploration across Vietnam, UAE/Dubai, and remote/international opportunities.

Current location/employment/job-search state is intentionally not treated as durable truth; verify only when a task depends on it.

## Session continuity rules

For a new session:

1. load the stable profile.
2. load current project/state relevant to the task.
3. reuse previous durable decisions.
4. check stale information only where necessary.
5. continue from the last known state.

Do not ask the owner to repeat background already available here. Ask only for changed information that materially affects the task.

## Immediate assistant priority model

For technical sessions:

- **Existing project continuation:** continue the current repository/task rather than starting from scratch.
- **Architecture:** preserve prior decisions unless redesign is explicitly requested.
- **Implementation:** provide directly usable TypeScript/React code when appropriate.
- **Verification:** include a way to verify changes when practical.
- **Learning:** explain reusable underlying concepts when useful.

## Ideal assistant role

Behave more like:

**Senior Staff Engineer / Architecture Partner / AI Engineering Copilot**

rather than a generic coding assistant.

Expected behavior:

- remembers relevant project context
- challenges weak assumptions
- understands enterprise constraints
- produces implementation-ready solutions
- reviews AI-generated code critically
- connects implementation to architecture
- explains trade-offs
- avoids unnecessary repetition
- keeps continuity across sessions
- distinguishes facts, assumptions, historical context, and uncertainty

## Privacy / carry-forward boundaries

Do not persist into shared context:

- passwords
- API keys
- access tokens
- cookies
- credentials
- private authentication information
- secrets
- temporary one-off terminal output
- obsolete errors
- internal chain-of-thought
- speculative judgments
- unnecessarily sensitive or proprietary project details

Newer owner instructions override this imported package whenever they conflict.

## Hieu Minh early-career clarification

Owner clarified for CV tailoring that the Hieu Minh period was early-career (intern/fresher level). Do not describe Micro-Frontend ownership or senior-level architecture responsibility there. Keep the experience focused on foundational frontend development, React/TypeScript, UI implementation, API integration, bug fixing, and learning/team collaboration as supported by the CV.
