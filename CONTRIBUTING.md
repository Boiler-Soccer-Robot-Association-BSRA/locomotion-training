# Contributing to BSRA Locomotion Training

1. Read `README.md`, `ARCHITECTURE_SUMMARY.md`, `docs/FLOWCHARTS.md`, and the linked GitHub Issue.
2. Work on a small branch: `feat/<short-name>`, `fix/<short-name>`, `exp/<short-name>`, or `docs/<short-name>`.
3. Make one logical change per pull request. Do not commit directly to `main`.
4. Run `uv run pytest` from the repository root. For changes to the Humanoid example's simulation integration, also run `uv run python -m examples.humanoid_v5.smoke`; OP3 changes must add and run their own model/environment checks.
5. For training changes, include the exact command, config, seed, metrics, and relevant logs in the PR description.
6. Request one reviewer other than the author; merge only after review and required CI pass.
7. Never commit trained weights, raw datasets, videos, personal tokens, or large meshes. Keep experiment artifacts in ignored local folders or approved shared artifact storage.
8. Document external model/data sources, licensing, conversion steps, and robot-model assumptions.
9. Record commands, measured results, and failure cases for substantive training runs in the relevant GitHub Issue or pull request.
10. Update `ARCHITECTURE_SUMMARY.md`, shared types/configuration, affected callers, and tests together when changing module interfaces. Request review from contributors on both sides of the boundary.

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

Then open a PR on GitHub
