from typing import Generator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import MetaData
from sqlalchemy.orm import Session


@pytest.fixture
def test_client() -> TestClient:
    """
    Mock FastAPI client.
    """
    from app.main import app

    client = TestClient(app)
    return client


@pytest.fixture
def session(monkeypatch) -> Generator[Session, None, None]:
    """
    Mock session with test database.
    """
    monkeypatch.setenv("DB_DATABASE", "test_db")

    from app.database import SessionLocal, engine
    from app.models import Base

    metadata: MetaData = Base.metadata
    metadata.bind = engine
    metadata.drop_all()
    metadata.create_all()
    session = SessionLocal()

    yield session

    session.close()
