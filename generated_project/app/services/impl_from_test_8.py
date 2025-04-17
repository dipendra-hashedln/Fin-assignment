from fastapi import FastAPI, Depends
from pydantic import BaseModel
from fastapi.responses import JSONResponse

app = FastAPI()

class LoginData(BaseModel):
    username: str
    password: str

class AuthService:
    def authenticate(self, username: str, password: str):
        # dummy implementation, always returns True
        return True

auth_service = AuthService()

@app.post("/api/auth/login")
def login_user(data: LoginData):
    if auth_service.authenticate(data.username, data.password):
        return JSONResponse(status_code=200, content={"message": "Logged in successfully"})
    else:
        return JSONResponse(status_code=401, content={"message": "Invalid credentials"})