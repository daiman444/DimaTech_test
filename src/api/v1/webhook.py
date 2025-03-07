from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.ext.asyncio import AsyncSession

from core.webhook_checking import check_webhook
from core.settings import security
from db.session import async_session
from services.webhook import WebhookService
from schemas.webhook_schema import WebhookSchema

webhook_router = APIRouter()


@webhook_router.post(
    path="/webhook",
    dependencies=[Depends(security)],
)
async def webhook(
    webhook_data: WebhookSchema = Depends(check_webhook),
    session: AsyncSession = Depends(async_session),
) -> None:
    if webhook_data is None:
        raise HTTPException(
            status_code=400,
            detail="Bad request",
        )
    await WebhookService.add_payment_from_webhook(
        session=session,
        webhook_data=webhook_data,
    )
