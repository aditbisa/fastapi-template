def test_db_settings(monkeypatch):
    """
    Test database settings.
    """
    monkeypatch.setenv("DB_DATABASE", "test_db")

    from app.configs import get_db_settings

    settings = get_db_settings()
    assert settings.engine == "mariadb+mariadbconnector"
    assert settings.database == "test_db"
