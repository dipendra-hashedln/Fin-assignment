from app.main import app
import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_get_pod_details():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/api/pods/123/details")
        assert response.status_code == 200