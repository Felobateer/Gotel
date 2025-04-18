from pydantic import BaseModel, EmailStr
from datetime import datetime


class SignupRequest(BaseModel):
    name: str
    email: EmailStr
    password: str

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    user_id: str
    name: str
    email: EmailStr
    created_at: str  

class UserResponseWithToken(BaseModel):
    user: UserResponse
    token: str
