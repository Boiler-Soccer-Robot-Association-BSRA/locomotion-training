# Custom environments (planned)

**Status: not implemented.** The starter uses Gymnasium's standard `Humanoid-v5`. The planned OP3 environment will train locomotion directly using joint-position offsets from a nominal pose, tracked by the same PD controller as the fixed-pose standing baseline. No separate learned-balance environment or training milestone is required.

Agree on the shared state/action interfaces in [INTERFACES.md](../docs/INTERFACES.md) early so environment structure, rewards, and metrics can be developed in parallel. Validate physical integration against the OP3 model and shared `controllers/` PD implementation, with documented observation/action spaces, resets, terminations, and `stable_baselines3.common.env_checker.check_env` tests. See [ARCHITECTURE.md](../docs/ARCHITECTURE.md) for the control approach and [the Humanoid example](../examples/humanoid_v5/README.md) for runnable reference code.
