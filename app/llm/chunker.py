from typing import List
from langchain.text_splitter import LatexTextSplitter
from langchain_core.documents import Document

latex_splitter = LatexTextSplitter(chunk_size=100, chunk_overlap=0)

def get_text_chunks(text:str) -> List[Document]:
    docs = latex_splitter.create_documents([text])
    return docs