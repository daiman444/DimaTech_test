from fastapi.security import HTTPBearer

from pydantic import(
    PostgresDsn,
    field_validator,
    ValidationInfo,
)
from pydantic_settings import BaseSettings

from core.app_logging import logging

logger = logging.getLogger("SETTINGS")


class AppSettings(BaseSettings):
    HASH_SALT: str
    WEBHOOK_SECRET_KEY: str


class OAuthSettings(BaseSettings):
    OAUTH_SECRET_KEY: str
    OAUTH_ALGORITHM: str
    OAUTH_TOKEN_EXPIRE: int
    OAUTH_TOKEN_URL: str


class PgSettings(BaseSettings):
    POSTGRES_DRV: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_SERVER: str
    POSTGRES_PORT: int
    POSTGRES_DB: str
    POSTGRES_URL: PostgresDsn | None = None

    @field_validator("POSTGRES_URL")
    def pg_url_validate(
        cls,
        v,
        values: ValidationInfo,
    ) -> PostgresDsn:
        data = values.data
        url_data = {
            "scheme": data.get("POSTGRES_DRV"),
            "username": data.get("POSTGRES_USER"),
            "password": data.get("POSTGRES_PASSWORD"),
            "host": data.get("POSTGRES_SERVER"),
            "port": data.get("POSTGRES_PORT"),
            "path": data.get("POSTGRES_DB"),
        }
        return PostgresDsn.build(**url_data)
    
security = HTTPBearer()
logger.info("HTTPBearer created")    

appsettings = AppSettings()
logger.info("AppStiings created")

oauth_settings = OAuthSettings()
logger.info("OAuthSettings created")

pgsettings = PgSettings()
logger.info("PgSettings created")
