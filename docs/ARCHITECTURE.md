# Locomotion training architecture (Fall 2026)

## CURRENT implemented baseline

The runnable reference is isolated in [`examples/humanoid_v5/`](../examples/humanoid_v5/README.md):

`Gymnasium Humanoid-v5` -> `MuJoCo physics` -> `Stable-Baselines3 PPO` -> example checkpoint -> `examples/humanoid_v5/evaluate.py` -> JSON results.

Its configuration and tests live with the example. Generated checkpoints, logs, and reports live under the ignored `artifacts/examples/humanoid_v5/` directory. The root implementation folders are reserved for OP3 work.

This is a **generic humanoid tutorial/benchmark environment**. It does **not** represent BSRA's future robot or implement command-conditioned locomotion. Training at the default low timestep count verifies the plumbing only; it does not prove stable standing or walking.

## Planned OP3 milestones

This repository focuses on a simulation locomotion baseline and team learning. The OP3 control path below is planned, not implemented by the current Humanoid scripts.

1. **Validate the OP3 model.** Produce an MJCF with documented provenance, plausible inertials and contacts, explicit joint/actuator mappings, and reproducible reset and stepping.
2. **Establish a PD standing baseline.** Track a fixed nominal joint pose, verify bounded joint control, and measure standing behavior and failure cases. Fixed-pose PD is not a guarantee of balance; robust disturbance recovery is not a prerequisite for moving on.
3. **Train locomotion directly.** Train PPO to adjust joint targets for forward-speed tracking on flat ground, then add turning. Balance is learned within the locomotion task; there is no separate learned-balance milestone or pretrained standing policy requirement.

## Planned control interface

The policy outputs bounded joint-position offsets relative to a fixed nominal pose. The same PD controller tracks targets for both the PD-only baseline and the learned policy:

```text
target_angles = clip(nominal_pose + action_scale * policy_action, joint_limits)
joint_torques = clip(kp * (target_angles - joint_angles) - kd * joint_velocities,
                    torque_limits)
```

Here `clip` means applying the configured lower and upper bounds per joint. Joint angles and target offsets use radians. The PD implementation must map joint torques to the model's actuators explicitly. Gains, action scales, limits, and the nominal pose are shared configuration, validated against the OP3 model.

This is residual joint-position control: the offset is relative to the nominal pose, not a time-varying walking controller or an additional torque correction. Zero policy action gives the PD-only nominal-pose baseline. Keep the PD loop active throughout training and evaluation, updating feedback at each physics step while holding policy targets between policy updates.

## Parallel development and integration

- Fill in the sections of [INTERFACES.md](INTERFACES.md) with the contributors who produce and consume each interface. It is the shared specification for the planned OP3 modules.
- Agree early on joint order, action scaling, observation fields, coordinate frames, units, simulation/policy periods, and command meanings. Start with a forward-speed command; document the future `(vx, vy, wz)` convention.
- Keep MuJoCo indexing in `environments/` and shared PD control in `controllers/`, with one explicit joint-to-actuator mapping. Reward functions consume named state quantities and actions; metric calculations consume the same state definitions.
- Reward and metric calculations can be implemented against synthetic states before the MJCF is complete. Physical thresholds, reward tuning, and model-backed acceptance checks require the actual OP3 model.
- Training and evaluation should share environment construction and the PD implementation. Before experiments, verify reset/step behavior, reward and metric outputs, and a short train/save/reload/evaluate cycle.
- Report fall rate, upright time, command-tracking error, episode length, and return. Compare the learned policy with zero policy actions using the same model, controller gains, commands, and evaluation conditions. Save model/configuration revisions alongside checkpoints.

Hardware deployment, extensive domain randomization, and production inference are future work outside the initial baseline. Preserve the model provenance, reproducible experiments, and lessons for the future locomotion repository.

## Ownership

- The RL lead owns the model, observations/actions/rewards, and experiment quality.
- The Programming Director owns cross-team integration expectations and repository standards.
- Hardware/control parameters must be reviewed with the hardware/electrical/design teams when known.

## Model integration principle

Do not assume the existing ROBOTIS OP3 model is directly compatible with MuJoCo; validate kinematics, actuator behavior, inertials, contacts and units. Do not represent an unrelated Gymnasium humanoid as OP3.
