from app.main import app
import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_assign_employee_to_pod():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/api/pods/assign", json={"employee_id": 1, "pod_id": 1})
        assert response.status_code == 200