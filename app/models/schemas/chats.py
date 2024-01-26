from pydantic import BaseModel
from app.models.schemas.common import Base


class Chats(Base):
    id: str
    user_id: str
    paper_id: str

    class Config:
        orm_mode = True


class ChatRequest(BaseModel):
    query:str

    class Config:
        orm_mode = True

class ChatResponse(BaseModel):
    ans: str

    class Config:
        orm_mode = True
