"""Minimal physics-only check (not a training or walking test)."""
from __future__ import annotations

import gymnasium as gym

from training.common import load_config


def main() -> None:
    config = load_config()
    env = gym.make(config["environment_id"])
    try:
        obs, info = env.reset(seed=config["seed"])
        print("Environment:", config["environment_id"])
        print("Observation shape:", obs.shape)
        print("Action shape:", env.action_space.shape)
        print("Reset information:", sorted(info.keys()))
        for step in range(5):
            action = env.action_space.sample()
            obs, reward, terminated, truncated, info = env.step(action)
            print(f"Step {step + 1}: reward={reward:.3f}, terminated={terminated}, truncated={truncated}")
            if terminated or truncated:
                obs, info = env.reset()
        print("Smoke check passed: simulation reset and stepped. This does not demonstrate locomotion.")
    finally:
        env.close()


if __name__ == "__main__":
    main()
