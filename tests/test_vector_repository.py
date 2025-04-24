from app.repositories.vector_repository import VectorRepository
from app.services.embedding_service import get_embedding
from app.services.file_loader_service import load_pdf_chunks

def test_faiss_index_search():
    repo = VectorRepository()
    query = "Advanced GPT-based text analysis"
    vector = get_embedding(query)
    results = repo.search(vector, top_k=2)
    assert isinstance(results, list)
    assert all(len(result) == 2 for result in results)  # (chunk, distance)
