import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture
def test_client():
    """Mock FastAPI client."""

    client = TestClient(app)
    return client
