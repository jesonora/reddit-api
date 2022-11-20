"""Module containing FastAPI instance related functions and classes."""
import logging.config

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from src.configs import get_settings

from .api import api_router

settings = get_settings()


description = """
This API helps you do awesome stuff. 🚀


## Subreddit

You will be able to:

* **Get the polarization score of latest 25 comments of a specific subreddit**
"""


def create_application() -> FastAPI:
    """Create a FastAPI instance.
    Returns:
        object of FastAPI: the fast api application instance.
    """
    application = FastAPI(
        title=settings.PROJECT_NAME,
        debug=settings.DEBUG,
        description=description,
        contact={
            "name": "Jesus Sono",
            "email": "jesonora@gmail.com",
        },
        openapi_url=f"{settings.API_STR}/openapi.json",
    )

    @application.get("/")
    def get_root():
        return HTMLResponse(content="Reddit", status_code=200)

    @application.get("/livenessProbe", status_code=200)
    async def liveness_probe():
        """livenessProbe endpoint"""
        return {"message": "alive"}

    @application.get("/readinessProbe", status_code=200)
    async def readiness_probe():
        """readinessProbe endpoint"""
        return {"message": "alive"}

    application.include_router(api_router, prefix=settings.API_STR)

    # load logging config
    logging.config.dictConfig(settings.LOGGING_CONFIG)
    return application
