# Suggested initial GitHub Issues for the RL lead

Create these in the repository's **Issues** tab; assign only after confirming members and Quinn's GitHub username. Due dates are proposed checkpoints, not guarantees.

## Issue 1 — Verify starter MuJoCo + PPO pipeline (October 22)
**Acceptance:** At least one supported machine runs `uv sync`, `uv run pytest`, `uv run python -m training.smoke`, a short `training.train` and `evaluation.evaluate`; report OS, commands, metrics and limitations. Investigate failures rather than asserting this is a learned walking demo.

## Issue 2 — Research and validate candidate humanoid model (October 22)
**Acceptance:** Compare at least one OP3 model source and one supported temporary fallback; cite source/commit/license; enumerate joints, actuators, masses, contacts; select a next implementation path or record blockers. Use `docs/OP3_MODEL_CHECKLIST.md`.

## Issue 3 — Design custom standing environment (October 22 draft; October 29 implementation target)
**Acceptance:** Document observations, actions, coordinate frames, simulation/control frequencies, reset/termination, reward components; implement a Gymnasium wrapper only after the robot model is validated. Add `check_env` validation and deterministic smoke tests once implemented.

## Issue 4 — Define evaluation protocol and experiment tracking (October 22)
**Acceptance:** Specify evaluation seeds, episode horizon, comparison baseline, mean/variance of returns and lengths, upright time/fall counts, and intended velocity-tracking metrics. Extend `evaluation/` and `docs/EXPERIMENT_LOG.md` where appropriate.

## Issue 5 — Train initial standing/balance policy (October 29 target)
**Depends on:** validated robot model + custom environment + reward. **Acceptance:** Saved checkpoint in external/ignored artifact storage, exact reproducible config, training/eval plots, failure analysis. Do not claim success solely from a positive reward curve.

## Issue 6 — Design BSRA velocity-command interface (November target)
**Acceptance:** Agree on `(vx, vy, wz)` reference frame/units/rates with Programming Director and future `robot-software` stack; document constraints and mock I/O tests, independent of final locomotion performance.
