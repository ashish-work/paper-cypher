from app.db.errors import EntityDoesNotExist
from app.db.repositories.base import BaseRepository
from sqlalchemy.orm import Session

from app.models.domains.papers import Papers


class PapersRepository(BaseRepository):
    async def get_paper_by_name(self, paper_name:str) -> Papers:
        matching_paper = self.session.query(Papers).filter(Papers.title == paper_name).first()
        if not matching_paper:
            raise EntityDoesNotExist
        return matching_paper