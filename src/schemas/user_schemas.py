from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    id: str
    last_name: str
    email: EmailStr
    exp: int


class AdminSchema(UserSchema):
    is_admin: bool
