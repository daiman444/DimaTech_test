from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession

from core.oauth import oauth
from db.models import Invoice
from db.repo.invoice import InvoiceRepo
from db.session import async_session
from schemas.invoices_schemas import(
    InvoiceSchema,
    InvoicesSchema,
    InvoiceWithPaymentsSchema,
)


class InvoiceService:
    @staticmethod
    async def add_invoice(
        user_id: int,
        balance: int = 0,
        session: AsyncSession = Depends(async_session),
    ) -> InvoiceSchema:
        invoice: Invoice = await InvoiceRepo.add_invoice(
            session=session,
            user_id=user_id,
            balance=balance
        )
        return InvoiceSchema.model_validate(invoice)

    @staticmethod
    async def get_invoice(
        invoice_id: int,
        session: AsyncSession = Depends(async_session),
    ) -> InvoiceWithPaymentsSchema:
        invoice: Invoice = await InvoiceRepo.get_invoice(
            invoice_id=invoice_id,
            session=session
        )
        if invoice.payments:
            invoice.payments = [payments.id for payments in invoice.payments]
        return InvoiceWithPaymentsSchema.model_validate(invoice)
    
    @staticmethod
    async def get_invoices(
        user_id: int,
        session: AsyncSession = Depends(async_session),
    ) -> InvoicesSchema:
        invoices_list: list[Invoice] = await InvoiceRepo.get_invoices(
            session=session,
            user_id=user_id,
        )
        invoices = {}
        for invoice in invoices_list:
            invoices[invoice.id] = InvoiceSchema.model_validate(invoice)
        return InvoicesSchema(invoices = invoices)
