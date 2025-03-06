from typing import Dict

from pydantic import BaseModel


class InvoiceSchema(BaseModel):
    id: int
    user_id: int
    balance: int
    payments: list[int] | None = None


class InvoicesSchema(BaseModel):
    invoices: Dict[int, InvoiceSchema]
