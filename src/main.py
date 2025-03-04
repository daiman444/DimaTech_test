from fastapi import FastAPI

from api.v1.auth import auth_router
from core.app_logging import logging

logger = logging.getLogger("MAIN")


def create_app():
    app = FastAPI()
    app.include_router(
        router=auth_router
    )

    logger.info("Created App")
    return app
