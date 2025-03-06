from fastapi import APIRouter, Security, Depends
from fastapi.security import(
    HTTPBearer,
    HTTPAuthorizationCredentials,
)

from sqlalchemy.ext.asyncio import AsyncSession

from db.session import async_session
from services.user import UserService
from schemas.user_schemas import UserSchema, UsersSchema

user_router = APIRouter()
security = HTTPBearer()


@user_router.get(
    path="/get_user",
    response_model=UserSchema,
)
async def get_user(
    credentials: HTTPAuthorizationCredentials = Security(security),
    session: AsyncSession = Depends(async_session),
) -> UserSchema:
    token = credentials.credentials
    user_data: UserSchema = await UserService.get_user(
        token=token,
        session=session
    )
    return user_data

@user_router.get(
    path="/get_users",
    response_model=UsersSchema,
)
async def get_users(
    credentials: HTTPAuthorizationCredentials = Security(security),
    session: AsyncSession = Depends(async_session),
) -> UsersSchema:
    token = credentials.credentials
    user_data: UserSchema = await UserService.get_user(
        token=token,
        session=session
    )
    if user_data.is_admin:
        users_list = await UserService.get_users(
            session=session,
        )
        return users_list
