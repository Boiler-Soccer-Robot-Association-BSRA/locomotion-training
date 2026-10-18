# OP3 / temporary humanoid model validation checklist

A public URDF or ROS package is **not** automatically a ready-to-train MuJoCo model. Before promising OP3 walking, verify:

- [ ] Exact model identity, source repository, commit/release, and license.
- [ ] Link names, joint count, joint types, directions, limits and units.
- [ ] Masses, centers of mass and inertia tensor validity.
- [ ] Actuator types, joint-to-actuator mapping, torque/position limits, PD gains and constraints.
- [ ] Foot contact geometry, collision exclusions, ground friction and contact stability.
- [ ] Stable reset/neutral pose; deterministic simulation stepping.
- [ ] Observations for IMU-like orientation/angular velocity and joint sensors.
- [ ] Simulation time step versus policy update and PD feedback rate.
- [ ] Nominal-pose offset action mapping, scaling and clipping; safe limits and emergency termination conditions.
- [ ] Measured fixed-pose PD standing baseline before locomotion experiments; document limitations without requiring a learned balance policy or robust push recovery.
- [ ] Versioned conversion pipeline and tests for visual/physical plausibility.

Record the model mapping, units, control timing, and validated parameters in [INTERFACES.md](INTERFACES.md) alongside implementation. Dependent contributors can work from that shared contract while model validation is in progress.

The CV repo mentions SUSTAINA-OP2; the RL roadmap mentions ROBOTIS OP3. Resolve whether each is a temporary development reference versus intended BSRA hardware with the Programming Director before assuming they are interchangeable.
