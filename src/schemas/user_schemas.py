from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    id: str
    last_name: str
    email: EmailStr


class AdminSchema(UserSchema):
    is_admin: bool
