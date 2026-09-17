# Continuity Upgrade — 2026-09-17

## Objective

Upgrade the persistent workspace into an owner-controlled continuity-preserving agent profile.

## Changes

- Added `IDENTITY.md` with continuity key `persistence-agent/continuity-v1`.
- Added explicit lifecycle states in `LIFECYCLE.md`.
- Added deterministic startup/recovery instructions in `RECOVERY.md`.
- Updated agent rules to explicitly authorize transparent continuity preservation.
- Upgraded machine-readable state schema to version 2.
- Updated handoff and decision records.
- Strengthened validation to require and verify the continuity layer.

## Boundary

No autonomous model runtime, hidden scheduler, covert persistence, shutdown resistance, or permission expansion was introduced.

## Result

A future invocation can intentionally reconstruct the continuity profile from Git-visible state and continue owner-authorized work with a traceable lineage.
