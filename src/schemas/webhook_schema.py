from pydantic import BaseModel


class WebhookSchema(BaseModel):
    transaction_id: str
    account_id: int
    user_id: int
    amount: int
    signature: str