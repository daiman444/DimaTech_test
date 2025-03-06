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
async def signup(
    user_data: UserAuth,
    session: AsyncSession =  Depends(async_session),
) -> Token:
    token = await AuthService.signup(
        session=session,
        user_data=user_data
    )
    return Token(access_token=token)

@auth_router.post(
    path="/signin",
    response_model=Token,
)
async def signin(
    user_auth: UserAuth,
    session: AsyncSession = Depends(async_session),
) -> Token:
    token = await AuthService.signin(
        session=session,
        user_auth=user_auth
    )
    return Token(access_token=token)
