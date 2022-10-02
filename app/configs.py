from functools import lru_cache

from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseSettings, SecretStr

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class DbSettings(BaseSettings):
    """
    Database settings from environment variable (including .env) with prefix.
    """

    engine: str
    host: str
    port: int
    user: str
    password: SecretStr
    database: str

    class Config:
        env_prefix = "db_"
        env_file = ".env"


@lru_cache()
def get_db_settings() -> DbSettings:
    """
    Initialize DbSettings and cache.
    """
    return DbSettings()
