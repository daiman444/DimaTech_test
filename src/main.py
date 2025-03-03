from fastapi import FastAPI

from core.app_logging import logging

logger = logging.getLogger("MAIN")


def create_app():
    app = FastAPI()

    logger.info("Created App")
    return app
