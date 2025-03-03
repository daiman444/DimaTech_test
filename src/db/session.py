from sqlalchemy.ext.asyncio import(
    create_async_engine,
    async_sessionmaker
)

from core.settings import pgsettings


a_engine = create_async_engine(
    url=pgsettings.POSTGRES_URL.unicode_string()
)

a_session = async_sessionmaker(
    bind=a_engine,
    autoflush=False,
)

async def async_session():
    async with a_session() as a_s:
        try:
            yield a_s
        except:
            await a_s.rollback()
            raise