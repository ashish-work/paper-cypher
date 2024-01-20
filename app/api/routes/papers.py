from fastapi import APIRouter, Body, Depends, HTTPException
from starlette.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from app.api.dependencies.database import get_repository
from app.db.repositories.papers import PapersRepository
from app.resources import strings

from app.models.schemas.papers import PaperInResponse, PaperRequest
from app.services.papers import check_paper_exists

router = APIRouter()

@router.post(
        "",
        status_code=HTTP_201_CREATED,
        response_model=PaperInResponse,
        name="paper:embed_paper"
)
async def embed_pdf(
    paper_request: PaperRequest = Body(..., embed=True),
    paper_repo: PapersRepository = Depends(get_repository(PapersRepository))
) -> PaperInResponse:
    """
    Parse PDF
    Extract metadata
    Get Embeddings from LLM
    Create chunks
    Store embedding in database
    Upload PDF to s3
    Store pdf in database
    """
    # check if paper is already embedded
    # if not check_if_paper_exists()

    # parse pdf 
    # create embedding
    # store 
    paper_exists:bool = await check_paper_exists(paper_repo, paper_request.title)
    if paper_exists:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail=strings.PAPER_EXISTS
        )

    return PaperInResponse(
        id=1,
        title=paper_request.title,
        url="test"
    )