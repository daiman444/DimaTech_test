from sqlalchemy.ext.asyncio import AsyncSession

from db.repo.invoice import InvoiceRepo
from db.repo.payment import PaymentRepo

from schemas.webhook_schema import WebhookSchema


class WebhookService:
    @staticmethod
    async def add_payment_from_webhook(
        session: AsyncSession,
        webhook_data: WebhookSchema,
    ) -> None:
        payment = await PaymentRepo.get_payment_from_tx(
            session=session,
            tx_id=webhook_data.transaction_id,
        )
        if payment:
            raise ValueError("Has payment")
        invoice = await InvoiceRepo.update_invoice(
            session=session,
            invoice_id=webhook_data.account_id,
            amount=webhook_data.amount
        )
        if invoice is None:
            await InvoiceRepo.add_invoice(
                session=session,
                user_id=webhook_data.user_id,
                balance=webhook_data.amount,
                need_commit=False,
            )     
        await PaymentRepo.add_payment(
            session=session,
            invoice_id=webhook_data.account_id,
            transaction_id=webhook_data.transaction_id,
            amount=webhook_data.amount,
            signature=webhook_data.signature,
        )
