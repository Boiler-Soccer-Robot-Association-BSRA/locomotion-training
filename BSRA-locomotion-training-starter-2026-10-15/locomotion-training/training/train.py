"""Reproducible starter PPO experiment on Gymnasium Humanoid-v5.

A small-step run proves plumbing only. It does NOT produce a walking policy.
"""
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

import gymnasium as gym
from stable_baselines3 import PPO
from stable_baselines3.common.monitor import Monitor

from training.common import DEFAULT_CONFIG, ROOT, load_config


def main() -> None:
    parser = argparse.ArgumentParser(description="Train an initial Humanoid-v5 PPO benchmark")
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    parser.add_argument("--total-timesteps", type=int, default=None,
                        help="Override config for a quick plumbing test")
    args = parser.parse_args()

    cfg = load_config(args.config)
    timesteps = args.total_timesteps or cfg["total_timesteps"]
    if timesteps <= 0:
        parser.error("--total-timesteps must be positive")

    run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run_dir = ROOT / "runs" / "training" / run_id
    run_dir.mkdir(parents=True, exist_ok=True)
    checkpoints = ROOT / "checkpoints"
    checkpoints.mkdir(exist_ok=True)
    checkpoint_base = checkpoints / "humanoid_ppo_baseline"

    run_cfg = dict(cfg, total_timesteps=timesteps, run_id=run_id,
                   note="Temporary generic humanoid benchmark; not an OP3 controller")
    (run_dir / "config.json").write_text(json.dumps(run_cfg, indent=2) + "\n", encoding="utf-8")

    env = Monitor(gym.make(cfg["environment_id"]))
    try:
        env.reset(seed=cfg["seed"])
        model = PPO(
            "MlpPolicy", env, verbose=1, seed=cfg["seed"],
            n_steps=cfg["n_steps"], batch_size=cfg["batch_size"],
            n_epochs=cfg["n_epochs"], learning_rate=cfg["learning_rate"],
            gamma=cfg["gamma"], device=cfg["device"],
            tensorboard_log=str(run_dir / "tensorboard"),
        )
        print(f"Starting benchmark: {cfg['environment_id']}, requested timesteps: {timesteps}")
        model.learn(total_timesteps=timesteps, progress_bar=False)
        model.save(str(checkpoint_base))
    finally:
        env.close()

    print(f"Saved policy: {checkpoint_base}.zip")
    print(f"Run metadata and TensorBoard logs: {run_dir}")
    print("WARNING: passing this run does not mean the model has learned to walk.")


if __name__ == "__main__":
    main()
