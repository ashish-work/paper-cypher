
from app.core.config import get_app_settings
from langchain_community.llms import Ollama
from langchain.embeddings import GPT4AllEmbeddings

app_settings = get_app_settings()

class Base:
    def __init__(self):
        self.__api_key=app_settings.llm_api_key
        self.__llm = Ollama(model="llama2", temperature=0, stream=False)
        self.__llm