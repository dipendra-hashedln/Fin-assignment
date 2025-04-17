import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_pod_details():
    response = client.get("/api/pods/123/details")
    assert response.status_code == 200