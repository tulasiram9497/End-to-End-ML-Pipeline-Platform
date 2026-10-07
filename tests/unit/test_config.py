from automl_forge.config import AppSettings, load_config


def test_load_config_reads_yaml_file() -> None:
    config = load_config("configs/default.yaml")

    assert config["project"]["name"] == "AutoML Forge"
    assert config["logging"]["level"] == "INFO"


def test_app_settings_has_defaults() -> None:
    settings = AppSettings()

    assert settings.app_name == "AutoML Forge"
    assert settings.environment == "development"
    assert settings.log_level == "INFO"
