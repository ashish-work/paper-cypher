
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.database import Base
from app.models.common import DateTimeModelMixin

from app.models.domains.embeddings import Embeddings


class Paper(Base, DateTimeModelMixin):
    __tablename__ = "papers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(250))
    url = Column(String(250))

    embeddings = relationship("Embeddings", back_populates="paper")
    