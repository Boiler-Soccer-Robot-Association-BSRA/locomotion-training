# OP3 interfaces to define

Use this outline to agree on what each component receives, produces, and needs from the others. Fill in concrete fields, dimensions, rates, gains, and thresholds as the OP3 model is validated.

The approach is **OP3 model -> fixed-pose PD baseline -> direct locomotion training**. The policy supplies joint-position offsets from a nominal pose; zero action selects the PD-only baseline. Track design decisions and implementation work in GitHub Issues.

When an interface changes, update this document, shared types/configuration, affected callers, and tests in the same PR. Have contributors on both sides review it.

## Robot model

Describe the physical model and the information other components need to use it.

- **Assets:** MJCF entry point, referenced assets, source/license, and model revision.
- **Mapping:** joint/actuator names and order, torso/foot identifiers, nominal pose, and physical limits. Explain gearing and sign changes between joint torques and actuator inputs; validate names and dimensions when loading.
- **Conventions:** axis directions, world/body frames, quaternion order, velocity measurement locations, units, and required conversions.

## PD controller

Define how policy actions become joint targets and how the shared controller tracks them.

- **Inputs:** action shape, dtype, joint order, bounds, per-joint offset scales, and clipping. Specify which joints remain fixed.
- **Control:** nominal pose plus offset -> joint target -> PD feedback -> bounded actuator command. Record gains and their units, torque limits, and required joint feedback.
- **Timing:** PD update period and target holding between policy updates. The fixed-pose baseline and learned policy must use the same controller and settings.

## Environment

Define the simulation loop and the state shared with the policy, rewards, and evaluation.

- **State and observations:** named state fields for rewards/metrics and a separate policy observation layout. Specify sources, shapes, dtypes, units, frames, normalization, and any simulation-only fields. Supply synthetic states for independent tests.
- **Stepping:** physics timestep, policy period, physics steps per action, and when state, rewards, and metrics are sampled.
- **Commands:** forward-speed units, frame, range, sampling, and update schedule, including zero speed. Explain the future `(vx, vy, wz)` convention and how commands enter observations and evaluation.
- **Episodes:** reset pose/state, randomization, seeds, horizon, and fall criteria. Distinguish termination from time-limit truncation; reset controller history, previous actions, and metric accumulators. Validate physical thresholds against the model.

## Rewards

Specify the reward function's inputs, calculations, and outputs so it can be developed independently of simulator indexing.

- **Inputs:** required state, command, current/previous action, and which simulation step each value represents.
- **Components:** velocity tracking, uprightness, effort, and smoothness, with units, signs, weights, and time scaling. Distinguish actuator effort from policy action magnitude.
- **Outputs and checks:** scalar total plus named components for logging. Test formulas with controlled states before tuning weights in simulation. Balance incentives belong within locomotion training.

## Training and evaluation

Define how experiments are constructed, saved, compared, and reproduced.

- **Configuration and checkpoints:** shared environment-construction entry point, configuration sections, and validation rules. Save model/interface revisions, joint order, control/reward settings, seed, and software versions. Specify how to restore normalization and reject incompatible models or observation/action layouts; keep generated artifacts outside tracked source.
- **Metrics and comparisons:** per-step information and report fields for falls, upright time, tracking error, return, and episode length, including units and aggregation. Define seeds, commands, and disturbances; compare PD-only and learned controllers under matching conditions. Distinguish synthetic tests from measured simulations.
- **Integration checks:** tests for shapes, units, mappings, reset/step behavior, `check_env`, and a short train/save/reload/evaluate cycle.
