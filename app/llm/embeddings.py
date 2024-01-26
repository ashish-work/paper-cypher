from typing import List
from langchain.embeddings import OllamaEmbeddings



class Embeddings:
    def __init__(self):
        self.__embeddings = OllamaEmbeddings()

    
    def embed_document(self, documents:List[str]) -> List[float]:
        query_result = self.__embeddings.embed_query(documents)
        return query_result