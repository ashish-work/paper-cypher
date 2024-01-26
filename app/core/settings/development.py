import logging

from pydantic import SecretStr

from app.core.settings.app import AppSettings

class DevAppSettings(AppSettings):
    debug: bool = True
    database_url: str = ""
    logging_level: int = logging.DEBUG
    llm_api_key: SecretStr = ""

    class Config(AppSettings.Config):
        env_file = ".env"
