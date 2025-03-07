from typing import Dict

from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    id: int
    name: str | None = None
    last_name: str | None = None
    email: EmailStr
    is_admin: bool | None = None

    model_config = {
        "from_attributes": True
    }

class UserSchemaInvoices(UserSchema):
    invoices: list[int] | None = None


class UsersSchema(BaseModel):
    users: Dict[int, UserSchema] | None = None

    model_config = {
        "from_attributes": True
    }
