"""Configuration loading for AutoML Forge."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

from automl_forge.exceptions import ConfigurationError


def load_config(config_path: str | Path) -> dict[str, Any]:
    """Load a YAML configuration file.

    Args:
        config_path: Relative or absolute path to the YAML file.

    Returns:
        The parsed YAML content as a dictionary.

    Raises:
        ConfigurationError: If the file cannot be found or parsed.
    """
    path = Path(config_path)
    if not path.exists():
        raise ConfigurationError(f"Configuration file not found: {path}")

    try:
        with path.open("r", encoding="utf-8") as file:
            config = yaml.safe_load(file) or {}
    except yaml.YAMLError as exc:  # pragma: no cover - defensive catch
        raise ConfigurationError(f"Invalid YAML in {path}: {exc}") from exc

    if not isinstance(config, dict):
        raise ConfigurationError(f"Configuration file must contain a mapping: {path}")

    return config


@dataclass(slots=True)
class AppSettings:
    """Application defaults loaded from the project config."""

    app_name: str = "AutoML Forge"
    environment: str = "development"
    log_level: str = "INFO"
    random_seed: int = 42
    config_path: str | Path = "configs/default.yaml"
    extra: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        config = load_config(self.config_path)
        project = config.get("project", {})
        logging_cfg = config.get("logging", {})
        env_cfg = config.get("environment", {})

        self.app_name = str(project.get("name", self.app_name))
        self.environment = str(env_cfg.get("type", self.environment))
        self.log_level = str(logging_cfg.get("level", self.log_level))
        self.random_seed = int(config.get("random_seed", self.random_seed))
        self.extra = {k: v for k, v in config.items() if k not in {"project", "logging", "environment", "random_seed"}}
