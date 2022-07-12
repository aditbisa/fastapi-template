from fastapi.testclient import TestClient


def test_readiness_healthcheck(test_client: TestClient):
    """Test /healthchecks/ GET endpoint."""

    response = test_client.get(f"/healthchecks/")
    assert response.status_code == 200
    assert response.json() == "OK 👍"
