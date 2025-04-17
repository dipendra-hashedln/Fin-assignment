from app.main import app
import pytest
from fastapi.testclient import TestClient

client = TestClient(app)

def test_retrieve_leave_status():
    response = client.get("/api/lms/leaves/status")
    assert response.status_code == 200