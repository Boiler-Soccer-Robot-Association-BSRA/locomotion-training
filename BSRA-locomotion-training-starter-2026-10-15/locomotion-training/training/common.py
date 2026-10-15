"""Small, dependency-free configuration utilities used by the starter scripts."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG = ROOT / "configs" / "humanoid_ppo_baseline.json"


def validate_config(cfg: dict) -> dict:
    """Reject common mistakes before an expensive training run starts."""
    required = {
        "environment_id": str,
        "seed": int,
        "total_timesteps": int,
        "n_steps": int,
        "batch_size": int,
        "n_epochs": int,
        "learning_rate": (float, int),
        "gamma": (float, int),
        "device": str,
        "eval_episodes": int,
    }
    for key, expected_type in required.items():
        if key not in cfg:
            raise ValueError(f"Missing config key: {key}")
        if not isinstance(cfg[key], expected_type) or isinstance(cfg[key], bool):
            raise ValueError(f"Invalid type for config key: {key}")
    if cfg["environment_id"] != "Humanoid-v5":
        raise ValueError("The starter only validates Humanoid-v5; implement and test another environment before changing it")
    for key in ("total_timesteps", "n_steps", "batch_size", "n_epochs", "eval_episodes"):
        if cfg[key] <= 0:
            raise ValueError(f"{key} must be positive")
    if (cfg["n_steps"] % cfg["batch_size"]) != 0:
        raise ValueError("batch_size must evenly divide n_steps for this single-environment starter")
    if not (0 < cfg["gamma"] <= 1):
        raise ValueError("gamma must be in (0, 1]")
    if cfg["learning_rate"] <= 0:
        raise ValueError("learning_rate must be positive")
    return cfg


def load_config(path: str | Path = DEFAULT_CONFIG) -> dict:
    with Path(path).open(encoding="utf-8") as file:
        config = json.load(file)
    if not isinstance(config, dict):
        raise ValueError("Config file must contain a JSON object")
    return validate_config(config)
