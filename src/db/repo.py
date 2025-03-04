from sqlalchemy.ext.asyncio import AsyncSession

from schemas.auth import AuthRequest

from .models import User


class UserRepo:
    @staticmethod
    async def add_user(
        session: AsyncSession,
        user = AuthRequest,
    ) -> User:
        user - User(
            
        )