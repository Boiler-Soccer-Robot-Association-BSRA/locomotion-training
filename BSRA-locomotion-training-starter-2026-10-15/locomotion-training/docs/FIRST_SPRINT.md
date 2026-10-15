# Week 1 after onboarding: October 15–22, 2026

Lead: Quinn Winkler. Aim: turn the starter framework into a verified starting point for BSRA humanoid locomotion.

## Meeting handoff checklist (October 15)
- [ ] RL members have repo access and know the PR workflow.
- [ ] Read the README and understand generic Humanoid-v5 vs. OP3.
- [ ] Assign a person to each of Issues #1–#4 (see `docs/ISSUES_TO_CREATE.md`; issue numbers may differ).
- [ ] Confirm who will smoke-test Linux/WSL2 and macOS environments.
- [ ] Define the demo and report format for October 22.

## Expected by Thursday October 22
1. Reproduce the starter smoke check on at least one supported development machine.
2. Run a short PPO training/evaluation cycle and record the command, run config, reward, episode length, and limitations. No claim of walking success required.
3. Document candidate physical robot models and recommend a temporary simulation model based on verified assets and licenses.
4. Write a draft observation/action interface for standing and velocity-commanded walking, and decide how a future custom Gymnasium environment will connect to the model.
5. Open focused PRs for actual modifications; document blockers in Issues.

## October 31 stretch goal
A validated custom humanoid simulation and initial standing/balance learning experiment. Recognizable learned locomotion depends on actual model, reward and training progress and is not guaranteed in October.
