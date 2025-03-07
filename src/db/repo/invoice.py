from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from db.models import Invoice
from schemas.invoices_schemas import InvoiceSchema


class InvoiceRepo:
    @staticmethod
    async def add_invoice(
        session: AsyncSession,
        user_id: int,
        balance: int
    ) -> Invoice:
        invoice = Invoice(
            user_id=user_id,
            balance=balance,
        )
        session.add(invoice)
        await session.commit()
        await session.refresh(invoice)
        return invoice
    
    async def get_invoice(
        session: AsyncSession,
        invoice_id: int,
    ) -> Invoice:
        result = await session.execute(
            select(Invoice)
            .options(selectinload(Invoice.payments))
            .where(
                Invoice.id==invoice_id
            )
        )
        return result.scalars().first()
    
    async def get_invoices(
        session: AsyncSession,
        user_id: int,
    ) -> Invoice:
        result = await session.execute(
            select(Invoice)
            .where(
                Invoice.user_id==user_id
            )
        )
        return result.scalars().all()
