from pydantic import(
    PostgresDsn,
    field_validator,
    ValidationInfo,
)
from pydantic_settings import BaseSettings

from core.app_logging import logging

logger = logging.getLogger("SETTINGS")


class AppSettings(BaseSettings):
    ...


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
    

appsettings = AppSettings()
logger.info("AppStiings created")

pgsettings = PgSettings()
logger.info("PgSettings created")
