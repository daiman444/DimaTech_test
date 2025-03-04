from pydantic import BaseModel, EmailStr


class UserRegister(BaseModel):
    name: str
    last_name: str
    email: EmailStr
    password: str


class AuthResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
