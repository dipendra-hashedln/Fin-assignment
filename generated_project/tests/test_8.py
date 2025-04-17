from fastapi.testclient import TestClient
import json

def test_login_user(client: TestClient):
    data = {
        "username": "test_user",
        "password": "test_password"
    }
    response = client.post("/api/auth/login", data=json.dumps(data))
    assert response.status_code == 200