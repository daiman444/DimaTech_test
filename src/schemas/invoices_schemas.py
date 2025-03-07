from typing import Dict

from pydantic import BaseModel


class InvoiceSchema(BaseModel):
    id: int
    user_id: int
    balance: int
    
    model_config = {
        "from_attributes": True,
    }

class InvoiceWithPaymentsSchema(InvoiceSchema):
    payments: list[int] | None = None

class InvoicesSchema(BaseModel):
    invoices: Dict[int, InvoiceSchema]
