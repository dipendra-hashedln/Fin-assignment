import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

@pytest.mark.asyncio
async def test_recommend_employee():
    pod_id = 1
    employee_id = 1
    response = client.post(f"/api/pods/{pod_id}/recommend", json={"employee_id": employee_id})
    assert response.status_code == 200