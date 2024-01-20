from asyncpg.connection import Connection
from sqlalchemy.orm import Session


class BaseRepository:
    def __init__(self, db:Session) -> None:
        self.__db = db

    
    @property
    def session(self) -> Session:
        return self.__db