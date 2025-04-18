from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserService:
    def get_current_user(self):
        return {"username": "john_doe"}

class UserResponse(BaseModel):
    username: str

user_service = UserService()

@app.get("/api/auth/user", response_model=UserResponse)
async def get_current_user():
    return user_service.get_current_user()