from app.db.errors import EntityDoesNotExist
from app.db.repositories.papers import PapersRepository


async def check_paper_exists(repo:PapersRepository, slug:str) -> bool:
    try:
        await repo.get_paper_by_name(slug)
    except EntityDoesNotExist:
        return False
    return True