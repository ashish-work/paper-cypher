from app.db.errors import EntityDoesNotExist
from app.db.repositories.base import BaseRepository
from sqlalchemy.orm import Session
from app.models.domains.embeddings import Embeddings

from app.models.domains.papers import Paper


class PapersRepository(BaseRepository):
    async def get_paper_by_name(self, paper_name:str) -> Paper:
        matching_paper = self.session.query(Paper).filter(Paper.title == paper_name).first()
        if not matching_paper:
            raise EntityDoesNotExist
        return matching_paper
    
    async def save(self, paper_name:str, url:str, embeddings: Embeddings) -> Paper:
        paper: Paper = Paper(title=paper_name, url="")
        paper.embeddings.extend(embeddings)
        self.session.add(paper)
        self.session.commit()
        return paper