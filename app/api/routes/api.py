from fastapi import APIRouter
from app.api.routes import papers, chats

router = APIRouter()
router.include_router(papers.router, tags=["papers"], prefix="/paper")
router.include_router(chats.router, tags=["chats"], prefix="/chat")