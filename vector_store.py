import numpy as np
from document_loader import DocumentLoader
from text_splitter import TextSplitter
from embedding_model import EmbeddingModel

class VectorStore:
    """ A vectors database in memory"""

    def __init__(self):
        self.text_chunks = []
        self.embeddings = None

    def add_documents(self, text_chunks: list[str], embeddings: np.ndarray):
        """Saves texts fragments and its embeddings"""
        self.text_chunks = text_chunks
        self.embeddings = embeddings
        print("Documents and embeddings have been added to the Vector Store. ")

    @staticmethod
    def _cosine_similarity(vec1: np.ndarray, vec2: np.ndarray) -> float:
        """Calculates cosine similiarity between two vectors"""
        dot_product = np.dot(vec1, vec2)
        norm_vec1 = np.linalg.norm(vec1)
        norm_vec2 = np.linalg.norm(vec2)
        if norm_vec1 == 0 or norm_vec2 == 0:
            return 0.0
        return dot_product / (norm_vec1 * norm_vec2)

    def find_relevant_chunks(self, query_embedding: np.ndarray, top_k: int = 5) -> list[tuple[str, float]]:
        """Finds the 'top_k' more relevant fragments for a query embedding. """
        if self.embeddings is None:
            return []
        
        similarities = []
        for i, doc_embedding in enumerate(self.embeddings):
            # iterating over all the embeddings to calcualte cosine similarity
            similarity = self._cosine_similarity(query_embedding, doc_embedding)
            # saves cosine similarity in a list 
            similarities.append((self.text_chunks[i], similarity))
        
        # Order similiarity in descending order
        similarities.sort(key=lambda x: x[1], reverse=True)
        return similarities[:top_k]


