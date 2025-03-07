import hashlib

from core.settings import appsettings
from schemas.webhook_schema import WebhookSchema

async def check_webhook(
    webhook_data: WebhookSchema,
) -> WebhookSchema:
    keys_list: list = sorted(webhook_data.__dict__.keys())
    keys_list.remove("signature")
    keys_list.append(appsettings.WEBHOOK_SECRET_KEY)
    concatinated_str = "".join(key for key in keys_list)
    calc_signature = hashlib.sha256(concatinated_str.encode()).hexdigest()
    if calc_signature == webhook_data.signature:
        return webhook_data
