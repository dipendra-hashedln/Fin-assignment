import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_dashboard_tiles():
    response = client.get("/api/dashboard/tiles")
    assert response.status_code == 200