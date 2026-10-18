# Week 1 after onboarding: October 15–22, 2026

Lead: Quinn Winkler. Aim: turn the starter framework into a verified starting point for BSRA humanoid locomotion.

## Meeting handoff checklist (October 15)
- [ ] RL members have repo access and know the PR workflow.
- [ ] Read the README and understand generic Humanoid-v5 vs. OP3.
- [ ] Assign GitHub Issues for the OP3 model, shared interfaces, PD baseline, environment, rewards, and evaluation; reference the relevant sections of [INTERFACES.md](INTERFACES.md).
- [ ] Confirm who will smoke-test Linux/WSL2 and macOS environments.
- [ ] Define the demo and report format for October 22.

## Expected by Thursday October 22
1. Reproduce `uv run python -m examples.humanoid_v5.smoke` from the repository root on at least one supported development machine.
2. Run the [Humanoid example's](../examples/humanoid_v5/README.md) short PPO training/evaluation cycle and record the command, run config, reward, episode length, and limitations. No claim of walking success required.
3. Document the OP3 model source/license and MJCF conversion path; demonstrate model-loading progress or record concrete blockers.
4. Fill in the relevant sections of [INTERFACES.md](INTERFACES.md): nominal-pose offset actions, shared PD controller configuration, state fields, and forward-speed commands. Begin reward and metric tests against synthetic states while the model is developed.
5. Open focused PRs for actual modifications; document blockers in Issues.

## October 31 stretch goal
A validated OP3 simulation, a measured fixed-pose PD standing baseline, and an initial locomotion training/evaluation experiment. Proceed directly from the PD baseline to locomotion training; no learned-balance milestone or standing-policy checkpoint is required. Recognizable learned locomotion depends on actual model, reward, and training progress and is not guaranteed in October.
