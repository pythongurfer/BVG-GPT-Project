from sentence_transformers import SentenceTransformer
import numpy as np
from document_loader import DocumentLoader
from text_splitter import TextSplitter

class EmbeddingModel:
    """A wrapper for the embeddings model"""
    def __init__(self, model_name: str = 'all-MiniLM-L6-v2'):
        print("Loading the embeddings model...")
        self.model = SentenceTransformer(model_name)
        print("Model loaded.")
    def get_embeddings(self, texts: list[str]) -> np.ndarray:
        """Converts a list of text chunks into embeddings"""
        print(f"Generating embeddings for {len(texts)} text fragments...")
        embeddings = self.model.encode(texts, convert_to_tensor = False)
        print("Embeddings generated. ")
        return np.array(embeddings)
                                       
