from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from core.oauth import oauth
from db.session import async_session
from services.user import UserService
from schemas.auth import Token
from src.schemas.user_schemas import UserSchema, AdminSchema


user_router = APIRouter()


@user_router.get(
    path="/get_user",
    response_model=UserSchema | AdminSchema,
)
async def get_user(
    token: Token,
    session: AsyncSession,
) -> UserSchema | AdminSchema:
    user_data = 

