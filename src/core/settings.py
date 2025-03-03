from pydantic import(
    PostgresDsn,
    field_validator,
    ValidationInfo,
)
from pydantic_settings import BaseSettings


class PgSettings(BaseSettings):
    POSTGRES_URL: PostgresDsn | None = None


pgsettings = PgSettings()