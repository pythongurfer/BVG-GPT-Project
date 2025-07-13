from document_loader import DocumentLoader

class TextSplitter:
    """Divides a long text in smaller chunks"""

    def __init__(self, chunk_size: int = 1000, chunk_overlap: int = 100):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def split(self, text: str) -> list[str]:
        chunks = []
        start_index = 0
        while start_index < len(text):
            end_index = start_index + self.chunk_size
            chunks.append(text[start_index:end_index])
            start_index += self.chunk_size - self.chunk_overlap
        print(f"Text divided in {len(chunks)} fragments")
        return chunks
    
