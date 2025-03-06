from typing import Dict

from pydantic import BaseModel


class PaymentSchema(BaseModel):
    id: int
    invoice_id: int
    amount: int


class PaymentsSchema(BaseModel):
    payments: Dict[int, PaymentSchema]
