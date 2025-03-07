from fastapi import(
    APIRouter,
    Depends,
    Request,
    HTTPException,
)

from sqlalchemy.ext.asyncio import AsyncSession

from core.settings import security
from db.session import async_session

from schemas.invoices_schemas import(
    InvoiceSchema,
    InvoicesSchema,
    InvoiceWithPaymentsSchema,
)
from services.invoice import InvoiceService

invoice_router = APIRouter()

async def chec_user_id(
    request: Request,
    user_id: int | None = None,
) -> int:
    if user_id is None:
        user_id = request.state.user.get("id")
    if user_id != request.state.user.get("id"):
        if not request.state.user.get("is_admin"):
            raise HTTPException(
                status_code=403,
                detail="Forbidden"
            )
    return user_id

@invoice_router.get(
    path="/add_invoice",
    dependencies=[Depends(security)],
    response_model=InvoiceSchema,
)
async def add_invoice(
    user_id: int = Depends(chec_user_id),
    session: AsyncSession = Depends(async_session),
) -> InvoiceSchema:
    invoice = await InvoiceService.add_invoice(
        user_id=user_id,
        session=session,
    )
    return invoice

@invoice_router.get(
    path="/get_invoice",
    dependencies=[Depends(security)],
    response_model=InvoiceWithPaymentsSchema,
)
async def get_invoice(
    invoice_id: int,
    user_id: int = Depends(chec_user_id),
    session: AsyncSession = Depends(async_session),
) -> InvoiceWithPaymentsSchema:
    if user_id:
        invoice = await InvoiceService.get_invoice(
            invoice_id=invoice_id,
            session=session,
        )
    return invoice

@invoice_router.get(
    path="/get_invoices",
    dependencies=[Depends(security)],
    response_model=InvoicesSchema,
)
async def get_invoices(
    user_id: int = Depends(chec_user_id),
    session: AsyncSession = Depends(async_session),
) -> InvoicesSchema:
    invoices = await InvoiceService.get_invoices(
        user_id=user_id,
        session=session,
    )
    return invoices
