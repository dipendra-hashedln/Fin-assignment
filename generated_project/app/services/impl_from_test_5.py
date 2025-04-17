from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class AssignEmployeeRequest(BaseModel):
    employee_id: int
    pod_id: int

class PodService:
    async def assign_employee(self, employee_id: int, pod_id: int):
        # dummy implementation, replace with actual logic
        return {"message": "Employee assigned to pod successfully"}

pod_service = PodService()

@app.post("/api/pods/assign")
async def assign_employee_to_pod(assign_request: AssignEmployeeRequest):
    try:
        result = await pod_service.assign_employee(assign_request.employee_id, assign_request.pod_id)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))