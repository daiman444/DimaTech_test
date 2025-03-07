"""
Проверочные мок-данные для транзакции
{
  "transaction_id": "5eae174f-7cd0-472c-bd36-35660f00132b",
  "user_id": 1,
  "account_id": 1,
  "amount": 100,
  "signature": "7b47e41efe564a062029da3367bde8844bea0fb049f894687cee5d57f2858bc8"
}
"""

import hashlib

from core.settings import appsettings
from schemas.webhook_schema import WebhookSchema

async def check_webhook(
    webhook_data: WebhookSchema,
) -> WebhookSchema:
    # на самом деле эта подпись не имеет значение т.к. она для разных
    # транзакий будет одна и так же т.к. составляющие стороки для
    # кодирования подписи одни и те же. 
    keys_list: list = sorted(webhook_data.__dict__.keys())
    keys_list.remove("signature")
    concatinated_str = "".join(str(webhook_data.__dict__[key]) for key in keys_list) 
    concatinated_str += appsettings.WEBHOOK_SECRET_KEY
    signature_str = hashlib.sha256(concatinated_str.encode()).hexdigest()
    if signature_str == webhook_data.signature:
        return webhook_data
