
from typing import List
from fastapi import APIRouter, Depends
from starlette.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from app.api.dependencies.database import get_repository
from app.api.dependencies.llm import get_embeddings
from app.db.repositories.embeddings import EmbeddingRepository
from app.llm.embeddings import Embeddings
from langchain import hub
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.documents import Document
from langchain_community.llms import Ollama
from langchain_community.vectorstores import Chroma
from app.llm.estimator import get_token_count
from app.models.schemas.chats import ChatRequest, ChatResponse


from langchain.schema.retriever import BaseRetriever
from typing import List


router = APIRouter()


@router.post(
        "",
        status_code=HTTP_201_CREATED,
        response_model=ChatResponse,
        name="chat:query"
)
async def chat(
        req:ChatRequest, 
        embedding_repo: EmbeddingRepository = Depends(get_repository(EmbeddingRepository)),
        embedding: Embeddings = Depends(get_embeddings())
    ):
    query_embeddings = embedding.embed_document([req.query])
    matching_content = await embedding_repo.find_similar_content(query_embeddings)
    prompt = hub.pull("rlm/rag-prompt")
    llm = Ollama(model="llama2")

    class Retriever(BaseRetriever):
        def _get_relevant_documents(self, query: str) -> List[Document]:
            return [Document(page_content=doc) for doc in matching_content ]

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    retriever = Retriever()
    rag_chain = (
       { "context": retriever | format_docs, "question": RunnablePassthrough() }
       | prompt
       | llm
       | StrOutputParser()
    )
    context = format_docs(retriever._get_relevant_documents(""))
    prompt.format(context=context, question=req.query)

    ans = rag_chain.invoke(req.query)

    token_count = get_token_count(ans)
    print(f'token_count:{token_count}')
    return ChatResponse(
        ans=ans
    )