# Contributing to BSRA Locomotion Training

**Owner:** Quinn Winkler (RL lead). **Oversight:** BSRA Programming Director.

1. Read `README.md`, `docs/ARCHITECTURE.md`, `docs/INTERFACES.md`, and the linked GitHub Issue.
2. Work on a small branch: `feat/<short-name>`, `fix/<short-name>`, `exp/<short-name>`, or `docs/<short-name>`.
3. Make one logical change per pull request. Do not commit directly to `main`.
4. Run `uv run pytest` from the repository root. For changes to the Humanoid example's simulation integration, also run `uv run python -m examples.humanoid_v5.smoke`; OP3 changes must add and run their own model/environment checks.
5. For training changes, include the exact command, config, seed, metrics, and relevant logs in the PR description.
6. Request one reviewer other than the author; merge only after review and required CI pass.
7. Never commit trained weights, raw datasets, videos, personal tokens, or large meshes. Keep experiment artifacts in ignored local folders or approved shared artifact storage.
8. Document external model/data sources, licensing, conversion steps, and robot-model assumptions.
9. Use `docs/EXPERIMENT_LOG.md` to track and compare substantive training runs.
10. Update `docs/INTERFACES.md`, shared types/configuration, affected callers, and tests together when changing module interfaces. Request review from contributors on both sides of the boundary.

The default code owner is `@grmpn`; see [.github/CODEOWNERS](.github/CODEOWNERS). Keep the runnable Humanoid reference self-contained under `examples/humanoid_v5/`; root implementation folders are for OP3 work.

GitHub Issues are the shared task tracker. The optional local `docs/ISSUES_TO_CREATE.md` draft is ignored, along with local agent instructions and secrets. Do not force-add these files. `uv.lock` and reviewed model/configuration sources should remain tracked.

## Branch and pull request examples

```bash
git switch main
git pull
git switch -c feat/op3-model-research
# edit files; test
git add .
git commit -m "Document candidate OP3 model source and simulation requirements"
git push -u origin feat/op3-model-research
```

Then open a PR on GitHub; do not merge your own PR without independent review.

## Definition of done

A task is done only when its acceptance criteria are met, relevant tests pass, reproduction steps work, the README/docs remain accurate, and a reviewer approves the PR.
