import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document
from typing import IO, List

from app.helpers.helpers import get_file_path


def extract_pdf_text(paper_name:str)->List[Document]:
    file_abs_path: str = get_file_path(paper_name)
    loader = PyPDFLoader(str(file_abs_path))
    pages = loader.load_and_split()
    return pages
