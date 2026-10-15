# Director's GitHub setup and handoff (October 15, 2026)

## A. Create empty repository

1. Open https://github.com/new and set owner to `Boiler-Soccer-Robot-Association-BSRA`.
2. Name the repository `locomotion-training`.
3. Description: `Humanoid locomotion simulation, reinforcement learning, training, and evaluation for BSRA's autonomous soccer robots.`
4. Choose Public only with club approval (otherwise choose Private). Leave GitHub's README/.gitignore/license checkboxes off because this starter includes them. Confirm MIT licensing with the club before publishing.
5. Create the empty repository. If the owner is unavailable, ask an organization owner to grant repository creation or create the empty repository.

## B. Push these starter files

Extract the zip. From a terminal INSIDE the extracted `locomotion-training` folder (not its parent):

```bash
git init -b main
git add .
git commit -m "Initialize BSRA locomotion training starter"
git remote add origin https://github.com/Boiler-Soccer-Robot-Association-BSRA/locomotion-training.git
git push -u origin main
```

Configure git identity and authenticate to GitHub if prompted. If repo was initialized with a README, do not force push over it; begin with an empty repo or merge histories deliberately.

## C. Confirm repository configuration

- Settings → General: enable Issues; prefer Squash merging and automatic delete of head branches. No need to turn the repo into a GitHub Pages site.
- Settings → Collaborators & teams: add Quinn's **actual GitHub username** with Maintain (recommended) and other RL members with Write. Choose appropriate organization-level teams if available. Follow the club's governance for permission levels.
- Settings → Rules → Rulesets (or Settings → Branches if using branch protection): protect `main`; require a pull request, at least one independent approving review, and passing **Fast CI / static-tests** once that check has run at least once. Disallow force pushes. Be mindful of plan/visibility restrictions.
- Code → .github/CODEOWNERS: replace the commented example with Quinn's verified GitHub handle in a PR. A commented placeholder does not provide automatic review requests.
- About (gear icon): add tags such as `robocup`, `reinforcement-learning`, `mujoco`, `humanoid-robotics`, `pytorch`, `ppo`.
- Issues tab: create the tasks from `docs/ISSUES_TO_CREATE.md`; identify the lead and first sprint owners.

## D. Request a runtime check (on a supported machine)

```bash
uv sync
uv run pytest
uv run python -m training.smoke
uv run python -m training.train --total-timesteps 512
uv run python -m evaluation.evaluate --checkpoint checkpoints/humanoid_ppo_baseline.zip --episodes 3
uv lock
```

Commit and push the generated `uv.lock` after verifying installation. This zip intentionally does not include an unverified lockfile. The scripts run the **generic Gymnasium Humanoid-v5**, not an OP3 robot. The 512-step training command demonstrates code plumbing only.

## E. Give Quinn the handoff

Send the repository URL and ask Quinn to (a) accept access, (b) assign the first GitHub Issues, (c) validate the repo's runtime commands, and (d) lead robot-model evaluation and a custom standing/balance environment. Plan to demo the initial pipeline and model-selection findings at the October 22 meeting. The RL onboarding repository stays separate.
