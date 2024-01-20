import enum

from sqlalchemy import Column, Enum, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from app.db.database import Base
from app.models.common import DateTimeModelMixin

class MessageSource(enum.Enum):
    user = "user"
    llm = "llm"

class ChatMessages(Base, DateTimeModelMixin):
    __tablename__ = "chat_messages"

    id = Column(Integer, primary_key=True)
    chat_id = Column(UUID(as_uuid=True), ForeignKey("chats.id"))
    source = Column(Enum(MessageSource))
    content = Column(String(1000))
