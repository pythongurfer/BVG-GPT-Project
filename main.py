from document_loader import DocumentLoader
from text_splitter import TextSplitter
from embedding_model import EmbeddingModel
from vector_store import VectorStore

class RAGSystem:
    """System that orchestrates the load, indexation and search. """
    def __init__(self, docs_directory: str):
        self.docs_directory = docs_directory
        self.vector_store = VectorStore()
        self.embedding_model = EmbeddingModel()

        self._setup()

    def _setup(self):
        """ Loads, divides and index the documents """
        # 1. Load the document 
        raw_text = DocumentLoader.load_pdfs_from_directory(self.docs_directory)

        # 2. Divides the text in fragments
        splitter = TextSplitter()
        chunks = splitter.split(raw_text)

        # 3. Generate the embedding
        embeddings = self.embedding_model.get_embeddings(chunks)

        # 4. Save in the vector store
        self.vector_store.add_documents(chunks, embeddings)

    def ask(self, question: str):
        """ Queries the system and show the relevant results. """
        print("\n" + "=" *50)
        print(f" Question from the user: {question}")
        print("="*50)

        # 1. Generate an embedding for the question
        query_embedding = self.embedding_model.get_embeddings([question])[0]

        # 2. Find the relevant fragments for the qestion
        relevant_chunks = self.vector_store.find_relevant_chunks(query_embedding, top_k=5 )

        # 3. Print the results
        print(f"\n ✅ TO {len(relevant_chunks)} relevant fragments found: \n ")
        for i, (chunk, score) in enumerate(relevant_chunks):
            print(f"---Fragment {i+1} (Similarity: {score:.4f}) ----")
            print(chunk.strip())
            print("\n")


if __name__ == "__main__":
    rag_bot = RAGSystem(docs_directory='data')

    rag_bot.ask("how much is a monthyl ticket?")
    rag_bot.ask("kann ich ein Fahrrad minnehmen?")