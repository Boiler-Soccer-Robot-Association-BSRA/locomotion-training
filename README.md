# BSRA Locomotion Training

Boiler Soccer Robot Association — reinforcement learning and simulation experiments.

## Purpose and current status

Build an OP3 locomotion baseline in simulation while learning robot modeling, feedback control, reinforcement learning, and evaluation. This is a learning repository whose models, measurements, and lessons will inform a future locomotion repository.

**Implemented:** a self-contained [Humanoid-v5 example](examples/humanoid_v5/) with a MuJoCo smoke check, configurable PPO training, checkpoint save/load, TensorBoard logging, evaluation reports, and configuration tests.

**Scaffolded:** the OP3 package under `src/bsra_locomotion/`, four YAML configuration files, and five test files. These are comment-only placeholders describing their future responsibilities and interactions; OP3 behavior and tests are not implemented. No OP3 XML model or trained policy is included yet.

## OP3 roadmap

1. **Validate the OP3 MJCF.** Establish model provenance, joint/actuator mappings, inertials, contacts, reset, and simulation stepping.
2. **Establish a nominal-pose standing baseline.** Use zero policy action and MuJoCo position actuators to track the nominal pose; validate mappings, limits, gains, and damping.
3. **Train locomotion directly.** PPO produces joint-position offsets from that pose. Begin with a short train/save/reload smoke test, then forward-speed tracking on flat ground in a single environment.

Zero policy action selects the nominal pose. Balance is learned within the locomotion task. MuJoCo position actuators provide the initial control behavior; no separate Python controller is planned. Parallel environments, OP3 evaluation/inference entry points, hardware deployment, and extensive domain randomization are deferred.

Read [ARCHITECTURE_SUMMARY.md](ARCHITECTURE_SUMMARY.md) for the target design and interface contracts, and [the flowcharts](docs/FLOWCHARTS.md) for initialization and runtime data flow. Physical integration and reward tuning require the actual model.

## Setup and runnable example

Use **Python 3.12** (the team's baseline is **3.12.3**) and [uv](https://docs.astral.sh/uv/). The dependency configuration targets Linux x86-64, Windows through WSL2 Ubuntu x86-64, and Apple Silicon macOS. macOS runtime verification is pending. On WSL2, clone under a Linux filesystem path such as `~/dev/`.

Run all commands from the repository root:

```bash
git clone https://github.com/Boiler-Soccer-Robot-Association-BSRA/locomotion-training.git
cd locomotion-training
uv sync
uv run python -c "import bsra_locomotion"
uv run pytest
uv run python -m examples.humanoid_v5.smoke
uv run python -m examples.humanoid_v5.train --total-timesteps 512
uv run python -m examples.humanoid_v5.evaluate --episodes 3
```

`uv sync` installs `bsra_locomotion` in editable mode. Scripts using this environment can import the package from outside `src/`. The OP3 training module is currently a placeholder and does not run training.

The example uses Gymnasium's generic humanoid and built-in reward. Its short runs verify the pipeline only; they do not demonstrate OP3 standing or walking. Its settings are in [baseline.json](examples/humanoid_v5/configs/baseline.json); run the training or evaluation module with `--help` for command options.

All example outputs are written to the ignored `artifacts/examples/humanoid_v5/` directory. Keep trained weights, datasets, and large assets in approved artifact storage. Dependency requirements live in `pyproject.toml`, and the resolved dependency versions are recorded in `uv.lock`. Linux installation and the short example cycle have been verified; macOS runtime verification remains pending.

## Repository layout

```text
src/
  bsra_locomotion/
    __init__.py
    config/
      loader.py
    robot/
      robot_state.py
    environments/
      create_environment.py
      op3_env.py
    rewards/
      calculate_rewards.py
    training/
      train.py
configs/
  op3.yaml
  environment.yaml
  rewards.yaml
  ppo.yaml
robot_models/
  op3/
    assets/            OP3 model assets (planned)
examples/humanoid_v5/   Runnable example, its config, and its tests
tests/
  test_config.py
  test_robot_state.py
  test_rewards.py
  test_op3_env.py
  test_training_smoke.py
docs/                  Architecture flowcharts
artifacts/             Generated outputs (ignored)
ARCHITECTURE_SUMMARY.md Target architecture and file responsibilities
pyproject.toml         Shared Python dependencies and test configuration
uv.lock                Resolved dependency versions
README.md              Repository overview and setup
```

Each package directory also contains an empty `__init__.py`. The OP3 Python and YAML files contain only purpose and interaction comments; the YAML files do not define usable settings yet. Robot models and assets remain to be added after validation.

## Contributing and planning

Use focused branches and reviewed PRs; see [CONTRIBUTING.md](CONTRIBUTING.md). GitHub Issues are the shared task tracker.

- Start with the [architecture summary](ARCHITECTURE_SUMMARY.md) and [flowcharts](docs/FLOWCHARTS.md).
- Agree on inputs, outputs, units, and acceptance checks using the architecture summary before integrating dependent modules.
- Record measured results, model provenance, and failure cases in the relevant issue or pull request.

Local `AGENTS.md`, `CLAUDE.md`, environment secrets, and editor state are ignored. Share project requirements through the tracked documentation.

## Related repositories and references

- [BSRA RL](https://github.com/Boiler-Soccer-Robot-Association-BSRA/RL): onboarding and learning resources.
- [BSRA CV](https://github.com/Boiler-Soccer-Robot-Association-BSRA/CV): soccer perception research.
- Future robot software will own production inference and hardware control.
- [Gymnasium Humanoid](https://gymnasium.farama.org/environments/mujoco/humanoid/), [Stable-Baselines3 PPO](https://stable-baselines3.readthedocs.io/en/master/modules/ppo.html), [MuJoCo](https://mujoco.readthedocs.io/), and [ROBOTIS OP3](https://github.com/ROBOTIS-GIT/ROBOTIS-OP3).

## Licensing

Proposed MIT license for BSRA-authored starter code; see [LICENSE](LICENSE). External models, datasets, and weights retain their own licenses and provenance. Confirm club approval before publishing or combining externally sourced models.
