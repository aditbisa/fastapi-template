from unittest.mock import mock_open, patch

from app.configs import get_db_settings, get_user_roles_config


def test_db_settings(monkeypatch):
    """
    Test database settings.
    """
    monkeypatch.setenv("DB_DATABASE", "test_db")

    settings = get_db_settings()
    assert settings.engine == "mariadb+mariadbconnector"
    assert settings.database == "test_db"


def test_get_user_roles_config():
    """
    Test load user roles config.
    """
    with patch("pathlib.Path.open", mock_open(read_data='{"a":1}')):
        config = get_user_roles_config()
    assert config == {"a": 1}
