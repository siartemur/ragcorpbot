from typing import List
from app.models.document_chunk import DocumentChunk
from app.config.settings import OPENAI_API_KEY
from openai import OpenAI

client = OpenAI(api_key=OPENAI_API_KEY)
EMBEDDING_MODEL = "text-embedding-3-small"

def get_embedding(text: str) -> List[float]:
    if not text.strip():
        return []
    response = client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=text
    )
    return response.data[0].embedding

def get_chunk_embeddings(chunks: List[DocumentChunk]) -> List[List[float]]:
    return [get_embedding(chunk.content) for chunk in chunks]
