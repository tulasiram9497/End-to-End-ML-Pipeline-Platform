"""Custom exceptions used throughout the project."""

from __future__ import annotations


class AutoMLForgeError(Exception):
    """Base exception for all project-specific errors."""


class ConfigurationError(AutoMLForgeError):
    """Raised when configuration is missing or invalid."""


class DatasetValidationError(AutoMLForgeError):
    """Raised when a dataset is invalid for ML use."""


class ModelTrainingError(AutoMLForgeError):
    """Raised when model training fails."""


class InferenceError(AutoMLForgeError):
    """Raised when inference fails."""
