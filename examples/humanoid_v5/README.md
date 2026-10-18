# Humanoid-v5 PPO example

This is a runnable reference for the full simulation -> training -> checkpoint -> evaluation workflow. It uses Gymnasium's generic humanoid and built-in reward. It does not implement the planned OP3 model, PD controller, or residual joint-position interface.

## What to learn

- `common.py` loads and validates JSON configuration without simulator dependencies.
- `smoke.py` resets the simulator and takes five random-action steps.
- `train.py` builds a PPO policy, records configuration/TensorBoard logs, and saves a checkpoint.
- `evaluate.py` reloads that checkpoint and writes episode rewards and lengths to JSON.
- `tests/` exercises configuration validation and path handling.

Use these scripts as a reference when implementing the OP3 modules in the repository root. Keep this example self-contained so it remains useful for onboarding.

## Run from the repository root

Use the root Python 3.12 / `uv` environment; the example has no separate dependency installation.

```bash
uv sync
uv run pytest
uv run python -m examples.humanoid_v5.smoke
uv run python -m examples.humanoid_v5.train --total-timesteps 512
uv run python -m examples.humanoid_v5.evaluate --episodes 3
uv run tensorboard --logdir artifacts/examples/humanoid_v5/runs/training
```

The [default configuration](configs/baseline.json) requests 2,048 timesteps, uses seed 42 and CPU execution, and evaluates three episodes. Pass `--config path/to/config.json` to training or evaluation to use another configuration. The configuration validator deliberately restricts this example to `Humanoid-v5`.

## Generated outputs

All outputs are under the ignored `artifacts/examples/humanoid_v5/` directory:

```text
checkpoints/humanoid_ppo_baseline.zip   Latest training checkpoint
runs/training/<run-id>/                Configuration and TensorBoard logs
results/evaluations/<timestamp>.json   Evaluation reports
```

Training replaces the default checkpoint each time. Archive checkpoints in approved artifact storage when comparing experiments. To evaluate an archived checkpoint:

```bash
uv run python -m examples.humanoid_v5.evaluate --checkpoint path/to/policy.zip --episodes 3
```

These short runs verify the pipeline only. Reward and episode length do not establish OP3 standing or walking performance.
