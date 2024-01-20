from sqlalchemy import Column, Integer, String

from app.db.database import Base
from app.models.common import DateTimeModelMixin

class Users(Base, DateTimeModelMixin):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(250))