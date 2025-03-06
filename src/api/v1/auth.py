from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from db.session import async_session
from services.auth import AuthService
from schemas.auth import UserAuth, Token

auth_router = APIRouter()


@auth_router.post(
    path="/signup",
    response_model=Token,
)
async def register_user(
    user_data: UserAuth,
    session: AsyncSession =  Depends(async_session),
) -> Token:
    token = await AuthService.register_user(
        session=session,
        user=user_data
    )
    return Token(access_token=token)

@auth_router.post(
    path="/signin",
    response_model=Token,
)
async def auth_user(
    user_data: UserAuth,
    session: AsyncSession =  Depends(async_session),
) -> Token:
    token = await AuthService.auth_user(
        session=session,
        user=user_data
    )
    return Token(access_token=token)
