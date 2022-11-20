"""Configuration interface, provides a function `get_settings` to get the
used settings instance for the web service."""

from .base import Settings


def get_settings():
    """Get different settings object according to different values of
    environment variable `MODE`, and use cache to speed up the execution.

    Not implemented, could be added for test, etc.

    Returns:
        object: The instance of the current used settings class.
    """
    return Settings()
