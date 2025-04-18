from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class LoginRequest(BaseModel):
    username: str
    password: str

class LoginResponse(BaseModel):
    message: str

class AuthService:
    async def login(self, username: str, password: str) -> str:
        # dummy implementation, replace with actual login logic
        return "Logged in successfully"

auth_service = AuthService()

@app.post("/api/auth/login")
async def login(login_request: LoginRequest, service: AuthService = Depends()):
    message = await service.login(login_request.username, login_request.password)
    return LoginResponse(message=message)