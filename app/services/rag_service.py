from typing import List
from app.services.embedding_service import get_embedding
from app.repositories.vector_repository import VectorRepository
from app.utils.prompt_helper import build_prompt
from app.core.llm_client import generate_answer

def ask_question(question: str, top_k: int = 3) -> str:
    question_embedding = get_embedding(question)
    repo = VectorRepository()
    results = repo.search(question_embedding, top_k=top_k)

    if not results:
        return "❗ No relevant content was found for this question."

    context_chunks = []
    for chunk, _ in results:
        source = f"{chunk.source_file or 'Unknown PDF'} – Page {chunk.page_number or '?'}"
        context_chunks.append((chunk.content, source))

    prompt = build_prompt(question, context_chunks)
    answer = generate_answer(prompt)
    return answer
