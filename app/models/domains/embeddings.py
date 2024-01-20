from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from app.db.database import Base
from app.models.common import DateTimeModelMixin
from pgvector.sqlalchemy import Vector
# from app.models.domains.papers import Papers


class Embeddings(Base, DateTimeModelMixin):
    __tablename__ = "embeddings"

    id = Column(Integer, primary_key=True, autoincrement=True)
    paper_id = Column(Integer, ForeignKey('papers.id'))
    chunk_number = Column(Integer)
    vector = Column(Vector(1600))

    paper = relationship("Papers", back_populates="embeddings")

