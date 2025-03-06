from datetime import datetime, timedelta

from sqlalchemy.ext.asyncio import AsyncSession

from core.oauth import oauth
from core.pass_hash import pass_hash
from db.repo import UserRepo
from schemas.auth import UserAuth


class AuthService:
    @staticmethod
    async def create_access_token(
        data: dict,
    ) -> str:
        expire = datetime.now() + timedelta(minutes=oauth.token_expire)
        data.update({"exp": expire})
        return await oauth.encode_token(data=data)

    @ staticmethod
    async def signup(
        session: AsyncSession,
        user_data: UserAuth
    ) -> str:
        user_data.password = pass_hash.pass_hash(user_data.password)
        new_user = await UserRepo.add_user(
            session=session,
            user=user_data
        )
        return await AuthService.create_access_token(
            data={
                "id": new_user.id,
                "email": new_user.email,
            }
        )

    @staticmethod
    async def signin(
        user_auth: UserAuth,
        session: AsyncSession,
    ) -> str:
        user_data = await UserRepo.get_user(
            session=session,
            auth_user=user_auth,
        )
        check_passwd = pass_hash.pass_check(
            password=user_auth.password,
            password_hash=user_data.password
        )
        if check_passwd:
            return await AuthService.create_access_token(
                data={
                    "id": user_data.id,
                    "email": user_data.email
                }
            )
