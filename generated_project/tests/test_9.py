from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_user_details():
    response = client.get("/api/auth/user")
    assert response.status_code == 200