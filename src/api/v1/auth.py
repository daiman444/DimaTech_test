from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from db.session import async_session
from services.auth import AuthService
from schemas.auth import UserAuth, TokenResponse

auth_router = APIRouter()


@auth_router.post(
    path="/signup",
    response_model=TokenResponse,
)
async def register_user(
    user_data: UserAuth,
    session: AsyncSession =  Depends(async_session),
) -> TokenResponse:
    token = await AuthService.register_user(
        session=session,
        user=user_data
    )
    return TokenResponse(access_token=token)

@auth_router.post(
    path="/signin",
    response_model=TokenResponse,
)
async def auth_user(
    user_data: UserAuth,
    session: AsyncSession =  Depends(async_session),
) -> TokenResponse:
    token = await AuthService.auth_user(
        session=session,
        user=user_data
    )
    return TokenResponse(access_token=token)
