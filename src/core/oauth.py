from datetime import datetime, timedelta
import jwt
from jwt import(
    ExpiredSignatureError,
    InvalidTokenError,
    InvalidAlgorithmError,
    InvalidKeyError,
)

from fastapi import HTTPException
from fastapi.security import(
    OAuth2PasswordBearer,
)

from core.settings import oauth_settings


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
    ) -> str:
        try:
            expire = datetime.now() + timedelta(minutes=oauth.token_expire)
            data.update({"exp": expire})
            return jwt.encode(
                payload=data,
                key=self.secret_key,
                algorithm=self.algorithm,
            )
        except TypeError:
            raise HTTPException(
                status_code=500,
                detail="Invalid payload",
            )
        except InvalidAlgorithmError:
            raise HTTPException(
                status_code=500,
                detail="Unsupported JWT algorithm"
            )
        except InvalidKeyError:
            raise HTTPException(
                status_code=500,
                detail="Invalid key for JWT algorithm"
            )
    
    async def decode_token(
        self,
        token: str
    ) -> dict:
        try:
            return jwt.decode(
                jwt=token,
                key=self.secret_key,
                algorithms=[self.algorithm],
            )
        except ExpiredSignatureError:
            raise HTTPException(
                status_code=401,
                detail="Token has expired"
            )
        except InvalidTokenError:
            raise HTTPException(
                status_code=401,
                detail="Unvalid Token"
            )

oauth = OAuth(
    secret_key=oauth_settings.OAUTH_SECRET_KEY,
    algorithm=oauth_settings.OAUTH_ALGORITHM,
    token_expire=oauth_settings.OAUTH_TOKEN_EXPIRE,
    tokenurl=oauth_settings.OAUTH_TOKEN_URL,
)
