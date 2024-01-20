from fastapi import APIRouter
from app.api.routes import papers

router = APIRouter()
router.include_router(papers.router, tags=["papers"], prefix="/paper")