from typing import AsyncGenerator, Callable, Type
from asyncpg.connection import Connection
from fastapi import Depends
from starlette.requests import Request
from asyncpg.pool import Pool
from app.db.database import SessionLocal
from sqlalchemy.orm import Session

from app.db.repositories.base import BaseRepository

# def _get_db_pool(request: Request) -> Pool:
#     return request.app.state.pool



# async def _get_connection_from_pool(
#         pool: Pool = Depends(_get_db_pool)
# ) -> AsyncGenerator[Connection, None]:
#     async with pool.acquire() as conn:
#         yield conn

    
def get_repository(
    repo_type: Type[BaseRepository],
) -> Callable[[Session], BaseRepository]:
    def _get_repo(
            db: Session = Depends(_get_db)
    ) -> BaseRepository:
        return repo_type(db)
    
    return _get_repo


def _get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()