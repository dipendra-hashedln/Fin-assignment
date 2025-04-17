from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse

app = FastAPI()

class LeaveRequest(BaseModel):
    employee_id: int
    leave_type: str
    start_date: str
    end_date: str

class LeaveService:
    async def apply_leave(self, leave_request: LeaveRequest):
        # dummy implementation, replace with actual logic
        return {"message": "Leave applied successfully"}

leave_service = LeaveService()

@app.post("/api/lms/leaves/apply", status_code=201)
async def apply_leave(leave_request: LeaveRequest):
    await leave_service.apply_leave(leave_request)
    return JSONResponse(content={"message": "Leave applied successfully"}, status_code=201)