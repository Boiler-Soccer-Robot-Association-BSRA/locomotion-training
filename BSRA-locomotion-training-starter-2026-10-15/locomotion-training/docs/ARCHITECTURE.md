# Locomotion training architecture (Fall 2026)

## CURRENT implemented baseline

`Gymnasium Humanoid-v5` -> `MuJoCo physics` -> `Stable-Baselines3 PPO` -> `checkpoints/` -> `evaluation/evaluate.py` -> JSON evaluation results.

This is a **generic humanoid tutorial/benchmark environment**. It does **not** represent BSRA's future robot or implement command-conditioned locomotion. Training at the default low timestep count verifies the plumbing only; it does not prove stable standing or walking.

## FUTURE target

1. Select and validate an OP3 or other approved temporary humanoid model, distinct from BSRA's eventual CAD/URDF.
2. Build a custom Gymnasium environment with observations (joint positions and velocities, body orientation, angular velocity, target planar velocity) and actions (joint targets through actuator/controller interface).
3. Define and test standing, termination, velocity tracking, smoothness, and effort rewards.
4. Train a reproducible policy and report fall rate, standing time, command-tracking error, mean episode length, and return; compare against a baseline.
5. Add domain randomization, sim-to-sim validation, and deployment-format export where appropriate.
6. Coordinate a future motion command interface with `robot-software`. The training stack remains separate from production policy inference and hardware control.

## Ownership

- The RL lead owns the model, observations/actions/rewards, and experiment quality.
- The Programming Director owns cross-team integration expectations and repository standards.
- Hardware/control parameters must be reviewed with the hardware/electrical/design teams when known.

## Model integration principle

Do not assume the existing ROBOTIS OP3 model is directly compatible with MuJoCo; validate kinematics, actuator behavior, inertials, contacts and units. Do not represent an unrelated Gymnasium humanoid as OP3.
