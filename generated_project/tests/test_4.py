from app.main import app
import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_approve_leave():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.patch("/api/lms/leaves/1/approve", json={"approved": True})
        assert response.status_code == 200