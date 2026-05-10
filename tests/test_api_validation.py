from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_search_endpoint_rejects_missing_required_fields():
    response = client.post("/api/search", json={})

    assert response.status_code in [400, 422]
