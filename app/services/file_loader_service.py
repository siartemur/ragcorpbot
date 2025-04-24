import os
import pdfplumber
from typing import List
from app.models.document_chunk import DocumentChunk

def load_pdf_chunks(file_path: str, max_chunk_length: int = 500) -> List[DocumentChunk]:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"PDF could not find: {file_path}")

    chunks: List[DocumentChunk] = []

    with pdfplumber.open(file_path) as pdf:
        for page_number, page in enumerate(pdf.pages, start=1):
            text = page.extract_text()
            if not text:
                continue

            parts = _split_text(text, max_chunk_length)
            for index, part in enumerate(parts):
                chunks.append(DocumentChunk(
                    content=part.strip(),
                    page_number=page_number,
                    chunk_index=index,
                    source_file=os.path.basename(file_path)
                ))

    return chunks

def _split_text(text: str, max_length: int) -> List[str]:
    words = text.split()
    chunks = []
    current = []

    for word in words:
        current.append(word)
        if sum(len(w) for w in current) > max_length:
            chunks.append(" ".join(current))
            current = []

    if current:
        chunks.append(" ".join(current))

    return chunks
