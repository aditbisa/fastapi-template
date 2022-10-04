from typing import Generator

import dotenv
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import MetaData
from sqlalchemy.orm import Session

from app.main import app


@pytest.fixture
def test_client() -> TestClient:
    """
    Mock FastAPI client.
    """
    client = TestClient(app)
    return client


@pytest.fixture
def session(monkeypatch) -> Generator[Session, None, None]:
    """
    Mock session with test database.
    """
    monkeypatch.setenv("DB_DATABASE", "test_db")
    dotenv_file = dotenv.find_dotenv()
    dotenv.set_key(dotenv_file, "DB_DATABASE", "test_db")

    from app.database import SessionLocal, engine
    from app.models import Base

    metadata: MetaData = Base.metadata
    metadata.bind = engine
    metadata.drop_all()
    metadata.create_all()
    session = SessionLocal()

    yield session

    session.close()
