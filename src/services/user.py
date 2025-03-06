from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession

from core.oauth import oauth
from db.models import User
from db.repo import UserRepo
from db.session import async_session
from schemas.auth import Token
from schemas.user_schemas import UserSchema, UsersSchema


class UserService:
    @staticmethod
    async def get_user(
        token: Token,
        session: AsyncSession = Depends(async_session),
    ):
        auth_user = await oauth.decode_token(token=token)
        user: User = await UserRepo.get_user(
            session=session,
            auth_user=auth_user,
        )
        return UserSchema.model_validate(user)
    
    async def get_users(
        session: AsyncSession = Depends(async_session),
    ):
        users_list = await UserRepo.get_users(
            session=session,
        )
        if users_list:
            users_data = {}
            for user in users_list:
                users_data[user.id] = UserSchema.model_validate(user)
            
            return UsersSchema(users=users_data)
        raise ValueError("Not users")
