from fastapi import FastAPI

from api.v1.auth import auth_router
from api.v1.user import user_router
from api.v1.invoice import invoice_router
from api.v1.webhook import webhook_router
from core.app_logging import logging
from middlewares.auth import AuthMiddleware

logger = logging.getLogger("MAIN")


def create_app():
    app = FastAPI()
    app.add_middleware(
        AuthMiddleware,
    )
    app.include_router(
        router=auth_router,
        prefix="/api/auth",
    )
    app.include_router(
        router=user_router,
        prefix="/api/user"
    )
    app.include_router(
        router=invoice_router,
        prefix="/api/invoice"
    )
    app.include_router(
        router=webhook_router,
        prefix="/api"
    )

    logger.info("Created App")
    return app
