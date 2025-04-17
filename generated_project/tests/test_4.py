import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

@pytest.mark.asyncio
async def test_approve_leave():
    leave_id = 1
    response = client.patch(f"/api/lms/leaves/{leave_id}/approve")
    assert response.status_code == 200