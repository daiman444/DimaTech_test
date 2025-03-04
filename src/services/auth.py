from datetime import datetime, timedelta

from fastapi import Depends, Security

from sqlalchemy.ext.asyncio import AsyncSession

from core.oauth import oauth


class AuthService:
    @staticmethod
    async def create_access_token(
        data: dict,
        expires_delta: timedelta,
    ) -> str:
        to_encode = data.copy()
        expire = datetime.now() + expires_delta
        to_encode.update({"exp": expire})
        return oauth.encode_token(data=to_encode)

    @ staticmethod
    async def register_user(
        session: AsyncSession,
        email: str,
        password: str,
    ) -> str:
        user = 