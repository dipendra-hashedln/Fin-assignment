from fastapi import FastAPI, Path
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class LeaveService:
    async def approve_leave(self, leave_id: int) -> bool:
        # dummy implementation, replace with actual logic
        return True

class LeaveResponse(BaseModel):
    approved: bool

leave_service = LeaveService()

@app.patch("/api/lms/leaves/{leave_id}/approve")
async def approve_leave(leave_id: int = Path(..., description="Leave ID")):
    approved = await leave_service.approve_leave(leave_id)
    return LeaveResponse(approved=approved)