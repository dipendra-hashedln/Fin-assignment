from fastapi import FastAPI, status
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class LeaveRequest(BaseModel):
    employee_id: int
    leave_type: str
    start_date: str
    end_date: str
    reason: str

class LeaveService:
    async def apply_leave(self, leave_request: LeaveRequest) -> None:
        # dummy implementation, replace with actual logic
        pass

leave_service = LeaveService()

@app.post("/api/lms/leaves/apply", status_code=status.HTTP_201_CREATED)
async def apply_leave(leave_request: LeaveRequest):
    await leave_service.apply_leave(leave_request)
    return {"message": "Leave applied successfully"}