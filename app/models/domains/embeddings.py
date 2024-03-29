from sqlalchemy import Column, ForeignKey, Integer, String
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
    content = Column(String)
    vector = Column(Vector(4096))

    paper = relationship("Paper", back_populates="embeddings")

