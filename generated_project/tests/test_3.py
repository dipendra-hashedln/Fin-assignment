import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_retrieve_leave_status():
    response = client.get("/api/lms/leaves/status")
    assert response.status_code == 200