from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession

from db.models import User
from db.repo.user import UserRepo
from db.session import async_session
from schemas.user_schemas import UserSchema, UsersSchema


class UserService:
    @staticmethod
    async def get_user(
        user_id: int,
        session: AsyncSession = Depends(async_session),
    ):
        user: User = await UserRepo.get_user(
            session=session,
            user_id=user_id,
        )
        if user.invoices:
            user.invoices = [invoice.id for invoice in user.invoices]

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
