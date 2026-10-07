"""Project logging configuration."""

from __future__ import annotations

import logging
from typing import Any


def get_logger(name: str, level: str | int | None = None) -> logging.Logger:
    """Return a configured logger instance.

    Args:
        name: Logger name.
        level: Logging level; defaults to INFO.

    Returns:
        A configured logger.
    """
    logger = logging.getLogger(name)
    if level is not None:
        logger.setLevel(level)
    else:
        logger.setLevel(logging.INFO)

    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
        logger.addHandler(handler)

    logger.propagate = False
    return logger


def configure_logging(level: str | int = "INFO") -> None:
    """Configure the root logger for the project."""
    logging.basicConfig(level=level, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
