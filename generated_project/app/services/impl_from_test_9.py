from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserService:
    def get_user_details(self):
        return {"user_id": 1, "username": "john_doe"}

class UserResponse(BaseModel):
    user_id: int
    username: str

user_service = UserService()

@app.get("/api/auth/user", response_model=UserResponse)
async def get_user_details():
    return user_service.get_user_details()