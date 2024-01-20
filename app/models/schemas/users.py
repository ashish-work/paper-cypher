from app.models.schemas.common import Base


class Users(Base):
    id: int
    name: str

    class Config:
        orm_mode = True