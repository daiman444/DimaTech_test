from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from db.models import Invoice


class InvoiceRepo:
    @staticmethod
    async def add_invoice(
        session: AsyncSession,
        user_id: int,
        balance: int = 0,
        need_commit: bool | None = True,
    ) -> Invoice:
        invoice = Invoice(
            user_id=user_id,
            balance=balance,
        )
        session.add(invoice)
        if need_commit:
            await session.commit()
        else:
            await session.flush()
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
    
    async def update_invoice(
        session: AsyncSession,
        invoice_id: int,
        amount: int = 0
    ) -> Invoice | None:
        invoice: Invoice = await InvoiceRepo.get_invoice(
            session=session,
            invoice_id=invoice_id
        )
        if invoice:
            invoice.balance += amount
            await session.flush()
        return invoice
    
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
