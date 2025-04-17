from fastapi import FastAPI, Path
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class LeaveApprovalRequest(BaseModel):
    approved: bool

class LeaveService:
    async def approve_leave(self, leave_id: int, approved: bool) -> None:
        # dummy implementation, replace with actual logic
        pass

leave_service = LeaveService()

@app.patch("/api/lms/leaves/{leave_id}/approve")
async def approve_leave(leave_id: int = Path(...), request: LeaveApprovalRequest):
    await leave_service.approve_leave(leave_id, request.approved)
    return {"message": "Leave approved successfully"}