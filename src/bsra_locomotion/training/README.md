# OP3 locomotion training (planned)

Implement PPO locomotion training here after the OP3 model, PD baseline, environment, rewards, and evaluation are integrated. The policy will learn joint-position offsets from a nominal pose; there is no separate learned-balance milestone.

Use the shared environment construction and checkpoint contract in [INTERFACES.md](../../../docs/INTERFACES.md). For a runnable training reference, see [the Humanoid example](../../../examples/humanoid_v5/README.md).
