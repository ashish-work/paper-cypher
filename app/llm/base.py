
from app.core.config import get_app_settings

app_settings = get_app_settings()

class Base:
    def __init__(self):
        self.__api_key=app_settings.llm_api_key