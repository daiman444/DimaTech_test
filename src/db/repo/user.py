from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from schemas.auth import UserAuth

from db.models import User


class UserRepo:
    @staticmethod
    async def add_user(
        session: AsyncSession,
        user = UserAuth,
    ) -> User:
        user = User(
            email=user.email,
            password=user.password,
        )
        session.add(user)
        await session.commit()
        await session.refresh(user)
        return user
    
    @staticmethod
    async def get_user_auth(
        session: AsyncSession,
        user_auth = UserAuth
    ) -> User:
        result = await session.execute(
            select(User)
            .where(
                User.email == user_auth.email
            )
        )
        return result.scalars().first()

    @staticmethod
    async def get_user(
        session: AsyncSession,
        user_id: int,
    ) -> User:
        result = await session.execute(
            select(User)
            .options(selectinload(User.invoices))
            .where(
                User.id == user_id
            )
        )
        return result.scalars().first()

    @staticmethod
    async def get_users(
        session: AsyncSession,
    ) -> list[User]:
        result = await session.execute(
            select(User).where(
                User.is_admin.is_(False),
                )
            )
        return result.scalars().all()
