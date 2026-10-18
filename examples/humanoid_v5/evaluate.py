"""Evaluate a saved PPO benchmark policy and report episodic reward/length."""
from __future__ import annotations

import argparse
import json
import statistics
from datetime import datetime, timezone
from pathlib import Path

import gymnasium as gym
from stable_baselines3 import PPO
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.monitor import Monitor

from examples.humanoid_v5.common import ARTIFACT_ROOT, DEFAULT_CONFIG, load_config


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate Humanoid-v5 PPO checkpoint")
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    parser.add_argument("--checkpoint", type=Path, default=ARTIFACT_ROOT / "checkpoints" / "humanoid_ppo_baseline.zip")
    parser.add_argument("--episodes", type=int, default=None)
    args = parser.parse_args()
    cfg = load_config(args.config)
    n_episodes = args.episodes or cfg["eval_episodes"]
    if n_episodes <= 0:
        parser.error("--episodes must be positive")
    if not args.checkpoint.is_file():
        parser.error(f"Checkpoint not found: {args.checkpoint}. Train a baseline first.")

    env = Monitor(gym.make(cfg["environment_id"]))
    try:
        env.reset(seed=cfg["seed"] + 1000)
        model = PPO.load(str(args.checkpoint), env=env, device=cfg["device"])
        rewards, lengths = evaluate_policy(
            model, env, n_eval_episodes=n_episodes,
            deterministic=True, return_episode_rewards=True,
        )
    finally:
        env.close()

    report = {
        "environment_id": cfg["environment_id"],
        "checkpoint": str(args.checkpoint),
        "episodes": n_episodes,
        "seed": cfg["seed"] + 1000,
        "mean_episode_reward": statistics.mean(rewards),
        "std_episode_reward": statistics.pstdev(rewards),
        "mean_episode_length": statistics.mean(lengths),
        "episode_rewards": rewards,
        "episode_lengths": lengths,
        "note": "Generic humanoid benchmark; reward is NOT a measure of OP3 walking success",
    }
    output = ARTIFACT_ROOT / "results" / "evaluations" / (datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ") + ".json")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    print(f"Saved evaluation report to {output}")


if __name__ == "__main__":
    main()
