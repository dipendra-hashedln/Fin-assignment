from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class LeaveStatusResponse(BaseModel):
    status: str

class LeaveService:
    def get_leave_status(self):
        return {"status": "active"}

leave_service = LeaveService()

@app.get("/api/lms/leaves/status", response_model=LeaveStatusResponse)
async def retrieve_leave_status():
    return leave_service.get_leave_status()