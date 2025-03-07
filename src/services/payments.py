from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession

from core.oauth import oauth
from db.models import Payment
from db.repo.payment import PaymentRepo
from db.session import async_session
from schemas.payments_schemas import PaymentSchema, PaymentsSchema


class PaymentService:
    @staticmethod
    async def add_payment(
        session: AsyncSession,
        invoice_id: int,
        transaction_id: str,
        amount: int,
        signature: str,
    ) -> None:
        await PaymentRepo.add_payment(
            session=session,
            invoice_id=invoice_id,
            transaction_id=transaction_id,
            amount=amount,
            signature=signature,
        )

    @staticmethod
    async def get_payment(
        payment_id: int,
        session: AsyncSession = Depends(async_session),
    ):
        payment: Payment = await PaymentRepo.get_payment(
            session=session,
            payment_id=payment_id,
        )
        if payment:
            return PaymentSchema.model_validate(payment)
        raise ValueError("Not payment")
    
    async def get_payments(
        user_id: int,
        session: AsyncSession = Depends(async_session),
    ):
        payment_list: list[Payment] = await PaymentRepo.get_payments(
            session=session,
            user_id=user_id,
        )
        if payment_list:
            payments = {}
            for payment in payment_list:
                payments[payment.id] = PaymentSchema.model_validate(payment)
            return PaymentsSchema(payments==payments)
        raise ValueError("Not payments")
