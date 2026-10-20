# Robotis Lab — durable project brief

Last updated: 2026-10-19T09:15:54.663Z
Project ID: `robotis-lab`.

## Authorized objective
Research and incrementally build an autonomous human-shaped biped robot, starting at ~25 cm. First deliverable: Webots RL-H25 physical simulation, then a supported real prototype with Arduino Uno and low-cost actuators, then bounded local autonomous exploration.

## Known constraints and decisions
- Existing project context: user has Arduino Uno and miscellaneous components, not yet confirmed inventory. Initial physical budget goal roughly 3,000,000 VND; laptop/desktop assumed existing but must verify.
- Simulation-first; Python/Webots stable release; 10 leg DOF (hip roll & pitch, knee pitch, ankle pitch & roll on each leg), head/arms initially passive to preserve mass/budget.
- PC host for planning, perception, and optional OpenAI/Claude API; Arduino Uno + PCA9685 for deterministic servo command/low-level controls. No LLM/API in safety-critical real-time motion loop.
- Independent safety supervisor, E-STOP, servo power separate from Uno, common ground, watchdog, joint limits, tilt/fall checks, harness for hardware testing.
- Under ~3m VND, full reliable unsupported biped walking is not guaranteed; do not purchase 10 servos until inventory, torque/power budget, one-servo bench test and price validation.
- Webots MVP -> stand 30s -> weight shift -> gait >=5 steps -> obstacle STOP -> supported hardware -> bounded exploration and high-level AI intents.
- UI if needed later: React/TypeScript; robotics backend Python.

## 2026-10-19 planning outputs
The assistant prepared a downloadable package `robotis-lab-blueprint-v1.zip` containing concise ChatGPT Project instructions, full project instructions and a 24-week implementation plan. This repository holds the concise durable decisions; files themselves were generated in the chat, not committed to the memory hub.

## Next steps
1. Confirm inventory, host OS and available fabrication/3D-printing options.
2. Create dedicated Robotis Lab *code* repository if the owner asks; don't confuse it with the persistence hub.
3. Implement a genuine Webots RL-H25 .wbt + .proto + Python controller and testing instructions; mark code untested unless executed successfully.
4. Use bench-tested torque/load/power data to refine BOM; don't assert current hardware prices without a current quote.

## Sprint 01 implementation status (2026-10-19)
Source bundle generated in ChatGPT artifact `robotis-lab-sprint01.zip` (22 files; not committed to this hub). Contains Webots .wbt world, RLH25.proto generated from config, 10 actuated leg DOF, 11 Physics nodes, initial standing targets, all specified simulated sensors, CSV+JSON logs, unit/fake-controller tests, and smoke/analysis scripts.

Verification: Python compileall PASS, offline generated model/config structure PASS, 20 unittest cases PASS (normal, obstacle, non-finite IMU, simulated E-STOP and static log analysis). Genuine Webots runtime NOT available in authoring environment; world parser compatibility, contacts and 30-second standing are UNVERIFIED. Do not describe this as dynamically balanced or walking.

Next action: unpack source on machine with Webots R2025a+; `python tools/generate_model.py`; `python tools/verify_project.py`; `python -m unittest discover -s tests -v`; `python tools/smoke_webots.py`. Capture exact Webots version, warnings, run CSV/JSON and 5 distinct P2 stand trials before moving to gait. Do not purchase hardware yet.

## Status
P1 source scaffold + offline tests complete; real Webots acceptance pending; hardware not started.

## Real Webots run — 2026-10-20 (user macOS, Webots R2025a)
- World and RLH25 PROTO load; Python controller starts and reports STAND. Rendering initially black but now resolved; robot is visible in front view.
- Log at t=332.46s reports `state=FAULT reason=excessive_tilt root_height=0.184m roll=-0.000 pitch=0.522rad` (configured tilt fault 0.45rad). Later screenshot scene-tree root Y about 0.0764m (versus 0.183m initial), X≈0.393m Z≈0.578m, yaw-like rotation ≈2.61rad, suggesting subsequent collapse/drift; state latch remains FAULT even if pose later changes.
- Source confirmed: `StandController` is open-loop neutral position hold; no feedback balance. FAULT latches; diagnostic FIRST FAULT CSV samples required before attributing cause. Do not change world coordinate system (`NUE`, Y-up) solely on perspective.
- Next: reset simulation, run independent 30–60s trials, inspect `experiments/logs/` CSV around first fault and report minima/maxima/drift; then instrument X/Z/yaw if necessary, tune physics and implement bounded balancing based on measurements.

## RL-H25 v0.2 Standing & Balance source package (2026-10-20)
User authorized upgrade after real Webots R2025a screenshots (upright at one time; prior late excessive_tilt FAULT at t~332s). Built `/mnt/data/robotis-lab-v02-standing-balance.zip` (29 files), extending Sprint01 geometry unchanged. New bounded IMU pitch/roll angle PID with derivative filter/antiwindup and ankle/hip joint mixing; runtime opt-in `RL_H25_MODE=balance`; safe default `baseline`. PID sign/gains deliberately tagged unverified; joint min/max/rate limits enforced, FAULT/STOP freeze targets, simulation E_STOP disables torque. Added GPS X/Z and yaw/gyro telemetry, baseline_report strict five-trial gate (>=4/5, 30s, tilt<0.20rad, GPS drift<0.03m, no fault, unique run IDs, valid metadata), independent Webots runner, tests and docs.
Verification: Python compile PASS, static Webots PROTO structural check PASS, 42/42 offline unit/integration/fake-Webots tests PASS. Native smoke SKIP (Webots unavailable in execution container); no real user CSV available for analysis; no stability/balance claims. Archive at chat sandbox, not committed to this memory repository.
Next action: user Mac R2025a close any other Webots instances, run 5 independent `python3 tools/run_standing_trials.py --mode baseline --trials 5 --duration 32` or manually, share five CSV/JSON pairs. Run `baseline_report.py`, inspect visual foot contact, then only short opt-in balance and sign verification, followed by 5 matched balance trials. Do not proceed to gait until standing gate achieved.
