from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Employee(BaseModel):
    id: int

class RecommendationResponse(BaseModel):
    recommended_employees: List[Employee]

class PodService:
    async def recommend_employee(self, pod_id: int, employee_id: int) -> List[Employee]:
        # dummy implementation, replace with actual logic
        return [Employee(id=1), Employee(id=2)]

pod_service = PodService()

@app.post("/api/pods/{pod_id}/recommend")
async def recommend_employee(pod_id: int, employee: Employee):
    recommended_employees = await pod_service.recommend_employee(pod_id, employee.id)
    return RecommendationResponse(recommended_employees=recommended_employees)