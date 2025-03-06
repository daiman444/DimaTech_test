import jwt

from fastapi.security import(
    OAuth2PasswordBearer,
)

from core.settings import oauth_settings
from schemas.user_schemas import UserSchema, AdminSchema


class OAuth:
    def __init__(
        self,
        secret_key: str,
        algorithm: str,
        token_expire: int,
        tokenurl: str,
    ) -> None:
        self.secret_key = secret_key
        self.algorithm = algorithm
        self.token_expire = token_expire
        self.oauth_scheme = OAuth2PasswordBearer(
            tokenUrl=tokenurl,
        )
    
    async def encode_token(
        self,
        data: dict,
    ) -> None:
        return jwt.encode(
            payload=data,
            key=self.secret_key,
            algorithm=self.algorithm,
        )
    
    async def decode_token(
        self,
        token: str
    ) -> UserSchema | AdminSchema:
        user_data = jwt.decode(
            jwt=token,
            key=self.secret_key,
            algorithms=[self.algorithm],
        )
        return user_data

oauth = OAuth(
    secret_key=oauth_settings.OAUTH_SECRET_KEY,
    algorithm=oauth_settings.OAUTH_ALGORITHM,
    token_expire=oauth_settings.OAUTH_TOKEN_EXPIRE,
    tokenurl=oauth_settings.OAUTH_TOKEN_URL,
)
