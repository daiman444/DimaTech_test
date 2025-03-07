from sqlalchemy.ext.asyncio import AsyncSession

from core.oauth import oauth
from core.pass_hash import pass_hash
from db.repo.user import UserRepo
from schemas.auth import UserAuth
from schemas.user_schemas import UserSchema


class AuthService:
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
        user_auth = UserSchema.model_validate(new_user)
        return await oauth.encode_token(
            data=user_auth.__dict__
        )

    @staticmethod
    async def signin(
        session: AsyncSession,
        user_auth: UserAuth,
    ) -> str:
        user_data = await UserRepo.get_user_auth(
            session=session,
            user_auth=user_auth,
        )
        check_passwd = pass_hash.pass_check(
            password=user_auth.password,
            password_hash=user_data.password
        )
        if check_passwd:
            user_auth = UserSchema.model_validate(user_data)
            return await oauth.encode_token(
                data=user_auth.__dict__
            )
