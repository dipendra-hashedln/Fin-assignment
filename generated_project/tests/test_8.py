from app.main import app
import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_login():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/api/auth/login", json={"username": "test_user", "password": "test_password"})
        assert response.status_code == 200