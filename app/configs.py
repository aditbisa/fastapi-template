import json
from functools import lru_cache
from pathlib import Path
from typing import Dict

from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseSettings, SecretStr

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class DbSettings(BaseSettings):
    """
    Database settings.
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


class JwtSettings(BaseSettings):
    """
    JWT settings.
    """

    secret_key: SecretStr
    expire_minutes: int

    class Config:
        env_prefix = "jwt_"
        env_file = ".env"


@lru_cache()
def get_jwt_settings() -> JwtSettings:
    """
    Initialize JwtSettings and cache.
    """
    return JwtSettings()


@lru_cache()
def get_user_roles_config() -> Dict:
    """
    Load and cache user roles.
    """
    fpath = Path(__file__).parent / "user_roles.json"
    with fpath.open("r") as file:
        config = json.load(file)
    return config
