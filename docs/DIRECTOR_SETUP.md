# Repository administration and handoff

## Repository layout and ownership

The project now lives directly at the Git repository root. Clone the repository and run commands there; no extracted starter subdirectory is needed.

The tracked [.github/CODEOWNERS](../.github/CODEOWNERS) assigns all files to `@grmpn`. Confirm that the account has repository write access. CODEOWNERS supplies review ownership; requiring that approval before merging is a separate GitHub ruleset/branch-protection setting. See [GitHub's CODEOWNERS documentation](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners).

## GitHub configuration

- Enable Issues and prefer squash merging with automatic deletion of merged branches.
- Give contributors the access required by club governance. Protect `main` with PR review and disallow force pushes.
- Require an independent reviewer. If code-owner approval is required, account for PRs authored by the sole code owner, who cannot approve their own PR.
- CI is not configured in this starter. Add a workflow and verify its check names before making checks required.
- Confirm repository visibility and licensing with the club before publication.

GitHub Issues are the shared task tracker. `docs/ISSUES_TO_CREATE.md` is an optional local, ignored drafting file; it is not available in fresh clones. When creating tasks, include their dependencies, affected sections of [INTERFACES.md](INTERFACES.md), and acceptance checks. Assign owners to OP3 model validation, interfaces, the PD baseline, environment, rewards, and evaluation before scheduling locomotion experiments.

## Runtime verification

From the repository root on a supported machine:

```bash
uv sync
uv run pytest
uv run python -m examples.humanoid_v5.smoke
uv run python -m examples.humanoid_v5.train --total-timesteps 512
uv run python -m examples.humanoid_v5.evaluate --episodes 3
```

Keep the resolved `uv.lock` in version control after validation. These commands exercise the generic Humanoid example; they do not validate OP3. Record the platform, commands, results, and limitations.

## Team handoff

Use [the first sprint](FIRST_SPRINT.md), [architecture](ARCHITECTURE.md), and [interface outline](INTERFACES.md) to organize work. The critical path is OP3 MJCF validation, a measured fixed-pose PD baseline, and direct locomotion training using joint-position offsets through the same controller. The RL onboarding repository stays separate.
