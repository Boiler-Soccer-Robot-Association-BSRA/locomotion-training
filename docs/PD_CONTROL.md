# OP3 PD control (planned)

Implement a shared joint PD controller as part of the OP3 package. The fixed-pose standing baseline and locomotion policy will use the same controller, gains, limits, and actuator mapping. Zero policy action selects the nominal pose.

Define the contract in [INTERFACES.md](INTERFACES.md#pd-controller) before implementation. The policy will supply joint-position offsets; the controller will update feedback at each physics step.
