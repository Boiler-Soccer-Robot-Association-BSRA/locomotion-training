"""Fast tests that work without installing heavyweight RL dependencies."""
import json
from pathlib import Path

import pytest

from examples.humanoid_v5.common import DEFAULT_CONFIG, load_config, validate_config


def test_config_is_valid():
    cfg = load_config()
    assert cfg["environment_id"] == "Humanoid-v5"
    assert cfg["batch_size"] <= cfg["n_steps"]


def test_missing_key_rejected():
    cfg = load_config()
    cfg.pop("seed")
    with pytest.raises(ValueError, match="Missing config key"):
        validate_config(cfg)


def test_invalid_batch_size_rejected():
    cfg = load_config()
    cfg["batch_size"] = 70
    with pytest.raises(ValueError, match="evenly divide"):
        validate_config(cfg)


def test_load_config_custom_path(tmp_path: Path):
    cfg = load_config(DEFAULT_CONFIG)
    file = tmp_path / "settings.json"
    file.write_text(json.dumps(cfg), encoding="utf-8")
    assert load_config(file) == cfg


def test_default_config_is_independent_of_working_directory(tmp_path: Path, monkeypatch):
    expected = load_config()
    monkeypatch.chdir(tmp_path)
    assert load_config() == expected
