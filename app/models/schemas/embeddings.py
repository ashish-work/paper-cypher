from app.models.schemas.common import Base


class Embeddings(Base):
    id: str
    paper_id: int
    chunk_number: int

    class Config:
        orm_mode = True