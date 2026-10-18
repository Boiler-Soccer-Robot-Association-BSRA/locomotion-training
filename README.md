# BSRA Locomotion Training

Boiler Soccer Robot Association — reinforcement learning and simulation experiments.

**RL Lead:** Quinn Winkler · **Programming Director:** Adhitya Vasudevan

## Purpose and current status

Build an OP3 locomotion baseline in simulation while learning robot modeling, feedback control, reinforcement learning, and evaluation. This is a learning repository whose models, measurements, and lessons will inform a future locomotion repository.

**Implemented:** a self-contained [Humanoid-v5 example](examples/humanoid_v5/README.md) with a MuJoCo smoke check, configurable PPO training, checkpoint save/load, TensorBoard logging, evaluation reports, and configuration tests.

**Planned:** the OP3 MJCF model, fixed-pose PD baseline, locomotion environment, rewards, training, and evaluation. Their root folders currently contain scope READMEs. No OP3 controller or trained OP3 policy is included yet.

## OP3 roadmap

1. **Validate the OP3 MJCF.** Establish model provenance, joint/actuator mappings, inertials, contacts, reset, and simulation stepping.
2. **Establish a PD standing baseline.** Track a fixed nominal pose with bounded joint control and measure its limitations.
3. **Train locomotion directly.** PPO produces joint-position offsets from that pose, tracked by the same PD controller. Start with forward-speed tracking on flat ground, then add turning.

Zero policy action selects the nominal pose. Balance is learned within the locomotion task; there is no separate learned-balance milestone or standing-policy checkpoint prerequisite. Hardware deployment and extensive domain randomization are outside the initial baseline.

Read [ARCHITECTURE.md](docs/ARCHITECTURE.md) for the design and fill in [INTERFACES.md](docs/INTERFACES.md) with the contributors who consume each interface. Model development, controller implementation, rewards, and metrics can proceed in parallel once their shared inputs and outputs are agreed. Physical integration and reward tuning require the actual model.

## Setup and runnable example

Use **Python 3.12** (the team's baseline is **3.12.3**) and [uv](https://docs.astral.sh/uv/). The dependency configuration targets Linux x86-64, Windows through WSL2 Ubuntu x86-64, and Apple Silicon macOS. macOS runtime verification is pending. On WSL2, clone under a Linux filesystem path such as `~/dev/`.

Run all commands from the repository root:

```bash
git clone https://github.com/Boiler-Soccer-Robot-Association-BSRA/locomotion-training.git
cd locomotion-training
uv sync
uv run pytest
uv run python -m examples.humanoid_v5.smoke
uv run python -m examples.humanoid_v5.train --total-timesteps 512
uv run python -m examples.humanoid_v5.evaluate --episodes 3
```

The example uses Gymnasium's generic humanoid and built-in reward. Its short runs verify the pipeline only; they do not demonstrate OP3 standing or walking. See the [example README](examples/humanoid_v5/README.md) for configuration, checkpoints, and TensorBoard commands.

All example outputs are written to the ignored `artifacts/examples/humanoid_v5/` directory. Keep trained weights, datasets, and large assets in approved artifact storage. Direct dependency pins live in `pyproject.toml`, and the resolved dependency versions are recorded in `uv.lock`. Linux installation and the short example cycle have been verified; macOS runtime verification remains pending.

## Repository layout

```text
.github/CODEOWNERS      Default reviewer: @grmpn
.gitignore             Local tooling, credentials, caches, and artifacts
pyproject.toml         Shared Python dependencies and test configuration
uv.lock                Resolved dependency versions
examples/humanoid_v5/  Runnable example, its config, and its tests
robot_models/         OP3 MJCF and provenance (planned)
controllers/          Shared OP3 PD controller (planned)
environments/         OP3 Gymnasium environment (planned)
rewards/              OP3 locomotion reward functions (planned)
configs/              OP3 experiment configuration (planned)
training/             OP3 locomotion training (planned)
evaluation/           OP3 baseline comparisons and metrics (planned)
tests/                OP3 tests (planned)
docs/                 Architecture, interfaces, model checklist, experiment log
```

## Contributing and planning

Use focused branches and reviewed PRs; see [CONTRIBUTING.md](CONTRIBUTING.md). GitHub Issues are the shared task tracker. The optional local drafting file `docs/ISSUES_TO_CREATE.md` is ignored and is not included in fresh clones.

- Start with the [first sprint](docs/FIRST_SPRINT.md) and [OP3 model checklist](docs/OP3_MODEL_CHECKLIST.md).
- Define inputs, outputs, units, and acceptance checks in [INTERFACES.md](docs/INTERFACES.md) before integrating dependent modules.
- Record measured results and failure cases in [the experiment log](docs/EXPERIMENT_LOG.md).

Local `AGENTS.md`, `CLAUDE.md`, environment secrets, and editor state are ignored. Share project requirements through the tracked documentation.

## Related repositories and references

- [BSRA RL](https://github.com/Boiler-Soccer-Robot-Association-BSRA/RL): onboarding and learning resources.
- [BSRA CV](https://github.com/Boiler-Soccer-Robot-Association-BSRA/CV): soccer perception research.
- Future robot software will own production inference and hardware control.
- [Gymnasium Humanoid](https://gymnasium.farama.org/environments/mujoco/humanoid/), [Stable-Baselines3 PPO](https://stable-baselines3.readthedocs.io/en/master/modules/ppo.html), [MuJoCo](https://mujoco.readthedocs.io/), and [ROBOTIS OP3](https://github.com/ROBOTIS-GIT/ROBOTIS-OP3).

## Licensing

Proposed MIT license for BSRA-authored starter code; see [LICENSE](LICENSE). External models, datasets, and weights retain their own licenses and provenance. Confirm club approval before publishing or combining externally sourced models.
