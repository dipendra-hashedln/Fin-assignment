from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse

app = FastAPI()

class AssignEmployeeRequest(BaseModel):
    employee_id: int
    pod_id: int

class PodService:
    async def assign_employee(self, employee_id: int, pod_id: int):
        # dummy implementation, replace with actual logic
        return {"message": "Employee assigned to pod successfully"}

pod_service = PodService()

@app.post("/api/pods/assign", response_class=JSONResponse)
async def assign_employee_to_pod(assign_request: AssignEmployeeRequest):
    result = await pod_service.assign_employee(assign_request.employee_id, assign_request.pod_id)
    return JSONResponse(content=result, status_code=200)