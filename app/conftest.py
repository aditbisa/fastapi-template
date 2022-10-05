import os
from typing import Generator
from unittest.mock import patch

import pytest
from dotenv import dotenv_values
from fastapi.testclient import TestClient
from sqlalchemy import MetaData
from sqlalchemy.orm import Session

# Patch environment variable without specify test env_file in pydantic config
envs = dotenv_values(".env")
envs.update({"DB_DATABASE": "test_db"})
patch.dict(os.environ, envs).start()

from app.database import SessionLocal, engine  # noqa: E402
from app.main import app  # noqa: E402
from app.models import Base, UserModel  # noqa: E402


@pytest.fixture
def test_client() -> TestClient:
    """
    Mock FastAPI client.
    """
    client = TestClient(app)
    return client


@pytest.fixture
def session() -> Generator[Session, None, None]:
    """
    Mock session with test database.
    """
    metadata: MetaData = Base.metadata
    metadata.bind = engine
    metadata.drop_all()
    metadata.create_all()
    session = SessionLocal()

    yield session

    session.close()


@pytest.fixture
def user_entry(session: Session):
    """
    Mock user.
    """
    user = UserModel(
        username="username",
        password="password",
    )
    session.add(user)
    session.commit()
    return user
