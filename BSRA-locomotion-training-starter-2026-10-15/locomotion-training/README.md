# BSRA Locomotion Training

Boiler Soccer Robot Association — Reinforcement Learning development repository  
**RL Lead:** Quinn Winkler · **Programming Director:** Adhitya Vasudevan

## Mission

Build a reproducible simulation, reinforcement learning, and evaluation foundation for humanoid locomotion. Our eventual objective is a command-conditioned policy for stable walking and turning in simulation, with sim-to-real considerations for BSRA's future soccer robot.

**Repository status (October 15, 2026): starter framework.** This is NOT a finished locomotion system, an OP3 simulator, or robot-deployable control software.

## What's included now

- **Implemented:** Gymnasium `Humanoid-v5` MuJoCo smoke check, configurable Stable-Baselines3 PPO training, checkpoint save/load, episodic reward and episode-length evaluation, experiment configuration, fast config tests, and basic CI.
- **Planned:** validated OP3/other humanoid model, custom Gymnasium environment, standing and velocity tracking rewards, measured fall/standing metrics, domain randomization, and integration with BSRA robot control.

The default `Humanoid-v5` task trains generic forward locomotion. A short training run **only verifies infrastructure**; do not report that BSRA's robot can walk because a command succeeded.

## Relation to other BSRA repositories

- [RL](https://github.com/Boiler-Soccer-Robot-Association-BSRA/RL): CartPole onboarding, orientation, and learning resources (keep unchanged).
- [CV](https://github.com/Boiler-Soccer-Robot-Association-BSRA/CV): soccer-field perception and detector research.
- `robot-software` (future): ROS 2 runtime packages, motion interfaces, hardware drivers, and **production inference** of trained policies. We train here; we do not put the complete robot runtime in this repository.

## Setup (supported baseline platforms)

Match the existing RL team's environment: **Python 3.12.3** and [uv](https://docs.astral.sh/uv/). Supported targets for this starter are **Linux x86-64**, **Windows via WSL2 Ubuntu x86-64**, and **Apple Silicon macOS** (macOS runtime smoke test pending). Windows members should use Ubuntu inside WSL2 and clone under a Linux filesystem path such as `~/dev/`.

```bash
git clone https://github.com/Boiler-Soccer-Robot-Association-BSRA/locomotion-training.git
cd locomotion-training
uv sync
uv run pytest
uv run python -m training.smoke
```

After first `uv sync`, **commit the generated `uv.lock` file** for fully reproducible dependencies. This starter is provided without a verified cross-platform lockfile; the lead should run `uv lock` on a supported platform before treating dependency resolution as frozen.

## Run a minimal training + evaluation cycle

```bash
# Small, NOT converged; verifies data flow and saved checkpoint.
uv run python -m training.train --total-timesteps 512

# Evaluates the just-saved policy for a few episodes.
uv run python -m evaluation.evaluate --checkpoint checkpoints/humanoid_ppo_baseline.zip --episodes 3

# Optional: view logs (TensorBoard is a project dependency).
uv run tensorboard --logdir runs/training
```

The default number of timesteps in `configs/humanoid_ppo_baseline.json` is also intentionally small. **Neither 512 nor 2048 timesteps is evidence of a usable locomotion policy.** Actual learning requires careful model, reward, observation, training-budget and evaluation design.

## Directory map

```text
configs/          JSON experiment configuration
training/         shared config code, simulator smoke, PPO trainer
evaluation/       saved-policy evaluation and JSON metrics
environments/     custom Gymnasium environments (planned)
rewards/          custom reward definitions (planned)
robot_models/     validated OP3 or other model provenance (planned)
tests/            fast config tests
docs/             architecture, first sprint, model checklist, experiment log, Issues
.github/          CI, PR template, CODEOWNERS placeholder, Issues templates
```

**Generated locally (ignored by Git):** `checkpoints/` for policies, `runs/` for training logs, and `results/` for metrics. Use approved shared storage for larger artifacts. **Do not upload weights or datasets to git.**

## How Quinn and the team should proceed

1. Review [the first sprint](docs/FIRST_SPRINT.md) and [initial suggested Issues](docs/ISSUES_TO_CREATE.md).
2. Validate the starter on a supported machine and record any errors honestly.
3. Select/validate a temporary physical humanoid model using [the model checklist](docs/OP3_MODEL_CHECKLIST.md).
4. Create the first custom standing/balance environment, observation/action interface, rewards, and tests.
5. Run controlled PPO experiments; record metrics in [the experiment log](docs/EXPERIMENT_LOG.md).
6. Coordinate velocity-commanded locomotion interfaces with `robot-software` once the runtime architecture is established.

## Working agreement

Use feature branches and PR review; see [CONTRIBUTING.md](CONTRIBUTING.md). One reviewed PR should be the unit of delivery. Associate development tasks with GitHub Issues.

## References

- Gymnasium Humanoid-v5: https://gymnasium.farama.org/environments/mujoco/humanoid/
- Stable-Baselines3 PPO: https://stable-baselines3.readthedocs.io/en/master/modules/ppo.html
- MuJoCo: https://mujoco.readthedocs.io/
- ROBOTIS OP3 source: https://github.com/ROBOTIS-GIT/ROBOTIS-OP3
- BSRA onboarding: https://github.com/Boiler-Soccer-Robot-Association-BSRA/RL

## Licensing

Proposed MIT license for BSRA-authored starter code (see LICENSE). Third-party robot models, datasets, and training weights retain their own licenses and provenance; get club approval before publishing or combining externally sourced models.
