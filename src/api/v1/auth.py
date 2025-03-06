from fastapi import APIRouter, Depends, Security
from fastapi.security import(
    HTTPBearer,
    HTTPAuthorizationCredentials,
)

from sqlalchemy.ext.asyncio import AsyncSession

from core.oauth import oauth
from db.session import async_session
from services.auth import AuthService
from schemas.auth import UserAuth, Token
from schemas.user_schemas import UserSchema, AdminSchema

auth_router = APIRouter()
security = HTTPBearer()

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
        user=user_data
    )
    return Token(access_token=token)

@auth_router.post(
    path="/signin",
    response_model=Token,
)
async def signin(
    user_data: UserAuth,
    session: AsyncSession =  Depends(async_session),
) -> Token:
    token = await AuthService.signin(
        session=session,
        user=user_data
    )
    return Token(access_token=token)

@auth_router.post(
    path="/auth",
    response_model=UserSchema | AdminSchema,
)
async def auth_user(
    credentials: HTTPAuthorizationCredentials = Security(security)
) -> UserSchema | AdminSchema:
    token = credentials.credentials
    user_data = await oauth.decode_token(token=token)
    # return AuthService.auth_user(
    #     token=access_token
    # )
    return user_data
