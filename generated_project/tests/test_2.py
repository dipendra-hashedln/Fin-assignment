from app.main import app
import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_apply_leave():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/api/lms/leaves/apply", json={"employee_id": 1, "leave_type": "annual", "start_date": "2022-01-01", "end_date": "2022-01-05"})
        assert response.status_code == 201