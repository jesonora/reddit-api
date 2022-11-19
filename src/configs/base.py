"""Base settings class contains only important fields."""
from typing import Dict
from pydantic import BaseModel, BaseSettings
from ..utils.logging import StandardFormatter, ColorFormatter


class LoggingConfig(BaseModel):
    version: int
    disable_existing_loggers: bool = False
    formatters: Dict
    handlers: Dict
    loggers: Dict


class Settings(BaseSettings):
    PROJECT_NAME: str = "reddit_nlp"
    PROJECT_SLUG: str = "reddit_nlp"

    DEBUG: bool = True
    API_STR: str = "/api/v1"

    # ######################## Logging Configuration ###########################
    # logging configuration for the project logger, uvicorn loggers
    LOGGING_CONFIG: LoggingConfig = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "colorFormatter": {"()": ColorFormatter},
            "standardFormatter": {"()": StandardFormatter},
        },
        "handlers": {
            "consoleHandler": {
                "class": "logging.StreamHandler",
                "level": "DEBUG",
                "formatter": "colorFormatter",
                "stream": "ext://sys.stdout",
            },
        },
        "loggers": {
            "reddit_nlp": {
                "handlers": ["consoleHandler"],
                "level": "DEBUG",
            },
            "uvicorn": {"handlers": ["consoleHandler"]},
        },
    }
