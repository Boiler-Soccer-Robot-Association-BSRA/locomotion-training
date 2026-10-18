# OP3 interfaces to define

This is the shared specification outline for the planned OP3 implementation. Each section describes what its owners need to agree on and document before dependent code is integrated. The concrete fields, dimensions, rates, gains, and thresholds remain to be filled in from the validated model.

The agreed control approach is **OP3 model -> fixed-pose PD baseline -> direct locomotion training**. The policy produces bounded joint-position offsets from a nominal pose, tracked by the same PD controller as the baseline. Zero policy action selects that pose. Balance is learned within locomotion; there is no separate learned-balance milestone. See [ARCHITECTURE.md](ARCHITECTURE.md) for the design rationale.

## Model and actuator mapping

**Owners: model and controller contributors.** Record the MJCF entry point, referenced assets, provenance/version, joint and actuator names, controlled-joint order, torso/foot identifiers, nominal pose, and physical limits. Define the mapping between policy joints, simulator state, and actuator inputs, including any gearing or sign changes. Validate names and dimensions at model load time.

## Coordinate frames and units

**Owners: model and environment contributors.** Define axis directions, world/body frames, quaternion order, and where velocities are measured. Specify units for angles, angular/linear velocities, forces, torques, and time; state the required conversions at module boundaries. Avoid ambiguous names such as `velocity` without a frame and unit.

## Actions and PD control

**Owners: controller and environment contributors.** Specify action shape, dtype, joint ordering, bounds, per-joint offset scales, and clipping. Define how nominal pose plus policy offset becomes a joint target and how PD feedback produces bounded actuator commands. Record gain units, torque limits, and which joints remain fixed. Both baseline and policy evaluation must use this implementation and configuration.

## Simulation and control timing

**Owners: model, controller, and environment contributors.** Choose the physics timestep, PD update period, policy update period, and number of physics steps per policy action. State when state is sampled and rewards/metrics are computed, how targets are held between policy updates, and whether reward terms are scaled by elapsed simulation time.

## Robot state and policy observations

**Owners: environment, reward, and evaluation contributors.** List the named state fields available to rewards/metrics and separately define the policy observation layout. For each field, specify source, shape, dtype, units, frame, and normalization. Identify any simulation-only information excluded from policy observations. Supply representative synthetic states so rewards and metrics can be tested before the MJCF is complete.

## Motion commands

**Owners: environment and training contributors.** Define the initial forward-speed command's units, frame, allowed range, sampling, and update schedule, including a zero-speed command. Reserve and explain the future `(vx, vy, wz)` convention for planar velocity and yaw rate. Document how commands appear in observations and evaluation scenarios.

## Reset and episode endings

**Owners: environment and evaluation contributors.** Specify reset pose/state, randomization, seeding, episode horizon, and fall criteria. Distinguish task termination from time-limit truncation. Define resets for controller history, previous actions, and metric accumulators; choose physical thresholds only after model validation.

## Reward inputs and outputs

**Owners: reward and environment contributors.** Define the function inputs, reward-component names, scalar total, weighting, sign conventions, and time scaling. State which step's state/action is used and how previous actions are supplied. Explain velocity tracking, uprightness, effort, and smoothness calculations; distinguish actuator effort from policy action magnitude. Return individual components for logging and test formulas with controlled states before tuning weights in simulation.

## Evaluation and metrics

**Owners: evaluation and environment contributors.** Define per-step information fields and the report schema, including fall counts/rates, upright time, tracking error, return, and episode length. State units, aggregation, evaluation seeds, command scenarios, and disturbances. Ensure PD-only and learned controllers share conditions; distinguish synthetic tests from measured simulations.

## Configuration and checkpoints

**Owners: training and evaluation contributors.** Specify the shared environment-construction entry point, configuration sections, and validation rules. Record model revision, interface version, joint ordering, control settings, reward settings, seed, and software versions with checkpoints. Define how evaluation restores observation normalization and detects incompatible models or action/observation layouts. Keep generated artifacts outside tracked source.

## Validation and interface changes

**Owners: all affected contributors.** Define contract tests for shapes, units, mappings, and reset/step behavior, plus `check_env` and a short train/save/reload/evaluate check. Interface changes should update this document, shared types/configuration, affected callers, and tests in the same PR, with review from the contributors on both sides of the boundary.
