import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.middlewares.authentications import AuthMiddleware
from app.models import UserModel
from app.services.authentications import create_access_token


@pytest.fixture
def setup_middleware() -> FastAPI:
    """
    Setup FastAPI with middleware.
    """
    app = FastAPI()
    app.add_middleware(AuthMiddleware)

    @app.get("/")
    def index():
        return {"message": "Hello World"}

    return app


@pytest.fixture
def test_client(setup_middleware: FastAPI) -> TestClient:
    """
    Mock FastAPI client with middleware.
    """
    client = TestClient(setup_middleware)
    return client


@pytest.fixture
def valid_token(user_entry: UserModel):
    """
    Create valid token.
    """
    token = create_access_token(user_entry)
    return token


def test_valid_token(test_client: TestClient, valid_token: str):
    """
    Test AuthMiddleware.
    """
    headers = {"Authorization": f"Bearer {valid_token}"}
    response = test_client.get("/", headers=headers)
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_invalid_token(test_client: TestClient):
    """
    Test AuthMiddleware.
    """
    headers = {"Authorization": "Bearer invalidToken012345"}
    response = test_client.get("/", headers=headers)
    assert response.status_code == 401
    assert response.json() == {"detail": "Could not validate credentials"}
