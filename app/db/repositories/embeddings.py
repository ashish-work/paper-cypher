from typing import List
from app.db.errors import EntityDoesNotExist
from app.db.repositories.base import BaseRepository
from sqlalchemy.orm import Session
from app.models.domains.embeddings import Embeddings

from app.models.domains.papers import Paper


class EmbeddingRepository(BaseRepository):
    similarity_threshold:float = 0.8
    async def get_paper_by_name(self, paper_name:str) -> Paper:
        matching_paper = self.session.query(Paper).filter(Paper.title == paper_name).first()
        if not matching_paper:
            raise EntityDoesNotExist
        return matching_paper
    

    async def save(self, chunk:int, embedding:List[float], content:str) -> Embeddings:
        embedding = Embeddings(chunk_number=chunk, vector=embedding, content=content)
        self.session.add(embedding)
        self.session.commit()
        return embedding
    

    async def find_similar_content(self, query_embedding:List[float]) -> List[str]:
        matching_embeddings = self.session.query(Embeddings, Embeddings.vector.cosine_distance(query_embedding).label("distance")).filter(Embeddings.paper_id==6, Embeddings.vector.cosine_distance(query_embedding) > self.similarity_threshold).order_by("distance").limit(500).all()
        matching_content = []
        embedding:Embeddings
        for embedding, _ in list(matching_embeddings):
            matching_content.append(embedding.content)
        return matching_content