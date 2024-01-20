from app.models.schemas.common import Base


class Chats(Base):
    id: str
    user_id: str
    paper_id: str

    class Config:
        orm_mode = True