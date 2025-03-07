from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from db.models import Invoice, Payment


class PaymentRepo:
    @staticmethod
    async def add_payment(
        session: AsyncSession,
        invoice_id: int,
        transaction_id: str,
        amount: int,
        signature: str,
    ) -> Payment:
        payment = Payment(
            invoice_id=invoice_id,
            transaction_id=transaction_id,
            amount=amount,
            signature=signature,
        )
        session.add(payment)
        await session.commit()
    
    async def get_payment(
        session: AsyncSession,
        payment_id: int,
    ) -> Payment:
        result = await session.execute(
            select(Payment)
            .where(
                Payment.id==payment_id
            )
        )
        return result.scalars().first()
    
    async def get_payment_from_tx(
        session: AsyncSession,
        tx_id: int,
    ) -> Payment:
        result = await session.execute(
            select(Payment)
            .where(
                Payment.transaction_id==tx_id
            )
        )
        return result.scalars().first()
    
    async def get_payments(
        session: AsyncSession,
        user_id: int,
    ) -> list[Payment]:
        query = (
            select(Payment)
            .join(Invoice, Payment.invoice_id == Invoice.id)
            .where(Invoice.user_id == user_id)
        )
        result = await session.execute(query)
        return result.scalars().all()
