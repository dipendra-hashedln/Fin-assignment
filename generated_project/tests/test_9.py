from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_current_user():
    response = client.get("/api/auth/user")
    assert response.status_code == 200