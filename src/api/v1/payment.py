from fastapi import(
    APIRouter,
    Depends,
    Request,
    HTTPException,
)

from sqlalchemy.ext.asyncio import AsyncSession

from core.settings import security
from db.session import async_session

from schemas.payments_schemas import(
    PaymentSchema,
    PaymentsSchema,
)
from services.payments import PaymentService

payment_router = APIRouter()

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


@payment_router.get(
    path="/get_paymetn",
    dependencies=[Depends(security)],
    response_model=PaymentSchema,
)
async def get_paymetn(
    paymetn_id: int,
    session: AsyncSession = Depends(async_session),
) -> PaymentSchema:
    paymetn = await PaymentService.get_payment(
        invoice_id=paymetn_id,
        session=session,
    )
    return paymetn

@payment_router.get(
    path="/get_paymetns",
    dependencies=[Depends(security)],
    response_model=PaymentsSchema,
)
async def get_invoices(
    user_id: int = Depends(chec_user_id),
    session: AsyncSession = Depends(async_session),
) -> PaymentsSchema:
    paymetns = await PaymentService.get_payments(
        user_id=user_id,
        session=session,
    )
    return paymetns
