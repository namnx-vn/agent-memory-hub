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

## Status
Research architecture/planning complete; simulation implementation and hardware procurement not started.
