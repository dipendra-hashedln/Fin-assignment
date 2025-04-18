from pydantic import BaseModel

class Leaves(BaseModel):
    id: str
    start_date: str
    end_date: str
    reason: str
    status: str

class Pods(BaseModel):
    id: str
    name: str

class PodMembers(BaseModel):
    id: str
    pod_id: str
    user_id: str
    role: str

class Users(BaseModel):
    id: str
    email: str
    password: str
    role: str