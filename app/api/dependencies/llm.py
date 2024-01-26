from app.llm.embeddings import Embeddings
from typing import  Callable


embeddings = Embeddings()

def get_embeddings():
    def _get_embedding()->Callable[[], Embeddings]:
        return embeddings
    return _get_embedding