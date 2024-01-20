from enum import Enum

# from pydantic import BaseSettings
from pydantic_settings import BaseSettings

class AppEnvTypes(Enum):
    prod: str = "prod"
    stage: str = "stage"
    dev: str = "dev"


class BaseAppSettings(BaseSettings):
    app_env: AppEnvTypes = AppEnvTypes.dev

    class Config:
        env_file = ".env"
        extra="allow"