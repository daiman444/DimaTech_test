from typing import Dict

from pydantic import BaseModel


class PaymentSchema(BaseModel):
    id: int
    invoice_id: int
    transaction_id: str
    amount: int
    signature: str

    model_config = {
        "from_attributes": True,
    }


class PaymentsSchema(BaseModel):
    payments: Dict[int, PaymentSchema]
