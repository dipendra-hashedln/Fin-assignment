from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse

app = FastAPI()

class PodDetailsResponse(BaseModel):
    pod_id: str
    details: str

class PodService:
    async def get_pod_details(self, pod_id: str):
        return {"pod_id": pod_id, "details": "dummy details"}

pod_service = PodService()

@app.get("/api/pods/{pod_id}/details", response_class=JSONResponse)
async def get_pod_details(pod_id: str):
    pod_details = await pod_service.get_pod_details(pod_id)
    return PodDetailsResponse(**pod_details)