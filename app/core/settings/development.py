import logging

from app.core.settings.app import AppSettings

class DevAppSettings(AppSettings):
    debug: bool = True
    database_url: str = "postgresql://postgres:postgres@localhost/postgres"
    logging_level: int = logging.DEBUG

    class Config(AppSettings.Config):
        env_file = ".env"
