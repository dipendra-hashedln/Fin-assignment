import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

@pytest.mark.asyncio
async def test_apply_leave():
    response = client.post("/api/lms/leaves/apply", json={
        "employee_id": 1,
        "leave_type": "Annual Leave",
        "start_date": "2022-01-01",
        "end_date": "2022-01-05",
        "reason": "Going on vacation"
    })
    assert response.status_code == 201