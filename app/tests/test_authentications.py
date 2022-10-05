from fastapi.testclient import TestClient

from app.models import UserModel
from app.services.authentications import verify_access_token


def test_token_endpoint_success(test_client: TestClient, user_entry: UserModel):
    """
    Test "/token" endpoint.
    """
    endpoint = "/token"
    payload = {"username": "username", "password": "password", "grant_type": "password"}
    headers = {"content-type": "application/x-www-form-urlencoded"}

    response = test_client.post(endpoint, data=payload, headers=headers)
    assert response.status_code == 200

    resp_json = response.json()
    assert resp_json["accessToken"]
    assert resp_json["tokenType"] == "bearer"

    user_id = verify_access_token(resp_json["accessToken"])
    assert user_id == user_entry.id


def test_token_endpoint_success_without_oauth2(test_client: TestClient, user_entry: UserModel):
    """
    Test "/token" endpoint.
    """
    endpoint = "/token"
    payload = {"username": "username", "password": "password"}

    response = test_client.post(endpoint, data=payload)
    assert response.status_code == 200

    resp_json = response.json()
    assert resp_json["accessToken"]
    assert resp_json["tokenType"] == "bearer"

    user_id = verify_access_token(resp_json["accessToken"])
    assert user_id == user_entry.id


def test_token_endpoint_failed(test_client: TestClient):
    """
    Test "/token" endpoint.
    """
    endpoint = "/token"
    payload = {"username": "anon", "password": "secret", "grant_type": "password"}
    headers = {"content-type": "application/x-www-form-urlencoded"}

    response = test_client.post(endpoint, data=payload, headers=headers)
    assert response.status_code == 401

    assert response.json() == {"detail": "Incorrect username or password"}
