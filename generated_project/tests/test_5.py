import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

@pytest.mark.asyncio
async def test_assign_employee_to_pod():
    response = client.post("/api/pods/assign", json={
        "employee_id": 1,
        "pod_id": 1
    })
    assert response.status_code == 200