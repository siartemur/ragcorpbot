import os
import pickle
import faiss
import numpy as np
from typing import List, Tuple

from app.models.document_chunk import DocumentChunk
from app.config.settings import INDEX_PATH, META_PATH
from app.config.logger_config import setup_logger
from app.admin.admin_logger import log_reset

logger = setup_logger("vector_repo")

class VectorRepository:
    def __init__(self, dim: int = 1536, index_path: str = INDEX_PATH, meta_path: str = META_PATH):
        self.dim = dim
        self.index_path = index_path
        self.meta_path = meta_path

        self.index = faiss.IndexFlatL2(dim)
        self.metadata: List[DocumentChunk] = []

        # Load previously saved FAISS index and metadata if available
        if os.path.exists(index_path) and os.path.exists(meta_path):
            self.index = faiss.read_index(index_path)
            with open(meta_path, "rb") as f:
                self.metadata = pickle.load(f)
            logger.info("Existing FAISS index and metadata loaded.")

    def add_embeddings(self, embeddings: List[List[float]], chunks: List[DocumentChunk]):
        np_vectors = np.array(embeddings).astype("float32")
        self.index.add(np_vectors)
        self.metadata.extend(chunks)
        self.save()
        logger.info(f"{len(chunks)} chunks added to FAISS index.")

    def search(self, query_embedding: List[float], top_k: int = 5) -> List[Tuple[DocumentChunk, float]]:
        query_vector = np.array([query_embedding]).astype("float32")
        distances, indices = self.index.search(query_vector, top_k)

        results = []
        for i, idx in enumerate(indices[0]):
            if idx < len(self.metadata):
                results.append((self.metadata[idx], distances[0][i]))
        return results

    def save(self):
        os.makedirs(os.path.dirname(self.index_path), exist_ok=True)
        faiss.write_index(self.index, self.index_path)
        with open(self.meta_path, "wb") as f:
            pickle.dump(self.metadata, f)
        logger.info("FAISS index and metadata saved.")

    def reset_index(self):
        self.index = faiss.IndexFlatL2(self.dim)
        self.metadata = []
        self.save()
        log_reset()
