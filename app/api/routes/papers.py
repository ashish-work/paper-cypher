from typing import List
from fastapi import APIRouter, Body, Depends, HTTPException, UploadFile
from starlette.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from app.api.dependencies.database import get_repository
from app.api.dependencies.llm import get_embeddings
from app.db.repositories.embeddings import EmbeddingRepository
from app.db.repositories.papers import PapersRepository
from app.helpers.helpers import get_file_path
from app.llm.chunker import get_text_chunks
from app.llm.embeddings import Embeddings
from app.resources import strings

from app.models.schemas.papers import PaperInResponse, PaperRequest
from app.services.papers import check_paper_exists
from app.services.pdf_extractor import extract_pdf_text
from langchain_core.documents import Document

router = APIRouter()

@router.post(
        "",
        status_code=HTTP_201_CREATED,
        response_model=PaperInResponse,
        name="paper:embed_paper"
)
async def embed_pdf(
    paper_file: UploadFile,
    paper_repo: PapersRepository = Depends(get_repository(PapersRepository)),
    embedding_repo: EmbeddingRepository = Depends(get_repository(EmbeddingRepository)),
    embedding: Embeddings = Depends(get_embeddings())
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
    paper_name:str = paper_file.filename
    paper_exists:bool = await check_paper_exists(paper_repo, paper_name)
    if paper_exists:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail=strings.PAPER_EXISTS
        )

    with open(paper_file.filename, "wb") as f:
        f.write(paper_file.file.read())

    documents:List[Document] = extract_pdf_text(paper_file.filename)
    paper_text = "".join([document.page_content for document in documents])
    docs:List[Document] = get_text_chunks(text=paper_text)
    saved_embeddings = []
    
    for i in range(len(docs)):
        embeddings = embedding.embed_document(documents=docs[i])
        saved_embedding = await embedding_repo.save(i, embedding=embeddings, content=docs[i].page_content)
        saved_embeddings.append(saved_embedding)
    
    await paper_repo.save(paper_name=paper_name, url="", embeddings=saved_embeddings)

    return PaperInResponse(
        id=1,
        title=paper_name,
        url="test"
    )