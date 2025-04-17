from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class PodDetailsResponse(BaseModel):
    pod_id: int
    details: str

class PodService:
    def get_pod_details(self, pod_id: int):
        return {"pod_id": pod_id, "details": "dummy details"}

pod_service = PodService()

@app.get("/api/pods/{pod_id}/details")
async def get_pod_details(pod_id: int):
    return pod_service.get_pod_details(pod_id)