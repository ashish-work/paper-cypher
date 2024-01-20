from pydantic import BaseModel

from app.models.schemas.common import Base
from app.models.schemas.embeddings import Embeddings


class Papers(Base):
    id: int
    title: str
    url: str

    embeddings: list[Embeddings] = []

    class Config:
        orm_mode = True

class PaperRequest(BaseModel):
    title:str

    class Config:
        orm_mode = True

class PaperInResponse(BaseModel):
    id: int
    title: str
    url: str

    class Config:
        orm_mode = True