# OP3 / temporary humanoid model validation checklist

A public URDF or ROS package is **not** automatically a ready-to-train MuJoCo model. Before promising OP3 walking, verify:

- [ ] Exact model identity, source repository, commit/release, and license.
- [ ] Link names, joint count, joint types, directions, limits and units.
- [ ] Masses, centers of mass and inertia tensor validity.
- [ ] Actuator types, torque/position limits, drive gains and constraints.
- [ ] Foot contact geometry, collision exclusions, ground friction and contact stability.
- [ ] Stable reset/neutral pose; deterministic simulation stepping.
- [ ] Observations for IMU-like orientation/angular velocity and joint sensors.
- [ ] Simulation time step versus policy update and inner control loop.
- [ ] Action-to-actuator mapping; safe limits and emergency termination conditions.
- [ ] Stand/balance test before locomotion training.
- [ ] Versioned conversion pipeline and tests for visual/physical plausibility.

The CV repo mentions SUSTAINA-OP2; the RL roadmap mentions ROBOTIS OP3. Resolve whether each is a temporary development reference versus intended BSRA hardware with the Programming Director before assuming they are interchangeable.
