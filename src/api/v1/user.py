from fastapi import APIRouter, Depends, Request, HTTPException

from sqlalchemy.ext.asyncio import AsyncSession

from core.settings import security
from db.session import async_session
from services.user import UserService
from schemas.user_schemas import UserSchema, UserSchemaInvoices, UsersSchema

user_router = APIRouter()


@user_router.get(
    path="/get_user",
    dependencies=[Depends(security)],
    response_model=UserSchemaInvoices,
)
async def get_user(
    requset: Request,
    user_id: int | None = None,
    session: AsyncSession = Depends(async_session),
) -> UserSchemaInvoices:
    if user_id is None:
        user_id = requset.state.user.get("id")
    if  not requset.state.user.get("is_admin"):
        raise HTTPException(
            status_code=403,
            detail="Forbidden"
        )
    user_data: UserSchemaInvoices = await UserService.get_user(
        user_id=user_id,
        session=session
    )
    return user_data

@user_router.get(
    path="/get_users",
    dependencies=[Depends(security)],
    response_model=UsersSchema,
)
async def get_users(
    request: Request,
    session: AsyncSession = Depends(async_session),
) -> UsersSchema:
    if not request.state.user.get("is_admin"):
        raise HTTPException(
            status_code=403,
            detail="Forbidden"
        )
    users_list = await UserService.get_users(
        session=session,
    )
    return users_list
