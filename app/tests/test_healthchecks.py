from fastapi.testclient import TestClient


def test_healthcheck_readiness(test_client: TestClient):
    """Test /healthchecks/ GET endpoint."""

    response = test_client.get("/healthchecks/readiness")
    assert response.status_code == 200
    assert response.json() == "OK 👍"
