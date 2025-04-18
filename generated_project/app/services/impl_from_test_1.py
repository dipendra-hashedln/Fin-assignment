from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class DashboardTile(BaseModel):
    id: int
    name: str

class DashboardService:
    async def get_tiles(self):
        return [DashboardTile(id=1, name="Tile 1"), DashboardTile(id=2, name="Tile 2")]

dashboard_service = DashboardService()

@app.get("/api/dashboard/tiles", response_model=list[DashboardTile])
async def get_dashboard_tiles():
    return await dashboard_service.get_tiles()