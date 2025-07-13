BVG-GPT: Factual AI Chatbot for Berlin Public Transport
A sophisticated, retrieval-based AI engine designed to answer questions about Berlin's public transport system (BVG) by using official documents as a source of truth. This project serves as a foundational step in creating a "hallucination-free" chatbot, focusing on the core Retrieval-Augmented Generation (RAG) pipeline.

The Problem
Finding specific, accurate information within dense official documents—like tariff regulations or transport conditions—is often tedious and inefficient. Furthermore, general-purpose Large Language Models (LLMs) can "hallucinate" or provide outdated information, making them unreliable for factual queries.

The Solution
This project implements the Retrieval component of a RAG system from scratch. Instead of asking an LLM a question directly, this engine first performs a semantic search over a database of official BVG documents. It finds and extracts the most relevant text snippets that contain the answer, ensuring that any subsequent response is grounded in factual, verifiable data.

How It Looks In Action
(This shows the output of the current retrieval engine)

> python main.py

==================================================
❓ Question from the user: kann ich ein Fahrrad mitnehmen?
==================================================
Generating embeddings for 1 text fragments...
Embeddings generated.

✅ Top 5 relevant fragments found:

--- Fragment 1 (Similarity: 0.4427) ---
n-Karten Fahrrad werden ausgegeben:
a) für das VBB-Gesamtnetz mit aufgedrucktem Gültigkeitsdatum und
b) für die Tarifbereiche Berlin und die kreisfreien Städte im Vorverkauf zur Entwertung bei Fahrt-
antritt bzw. im Verkehrsmittel zum sofortigen Fahrtantritt bestimmt.
Für die einmalige Mitnahme eines Fahrrades gemäß Anlage 4, Tabelle 3 ist ein Einzelfahrausweis
Fahrrad zu lösen. Anstelle mehrerer Einzelfahrausweise Fahrrad kann auch eine 24-Stunden-Karte
Fahrrad gelöst werden.
...


🏛️ System Architecture & Design
This project was built following Object-Oriented Programming (OOP) principles to ensure the system is modular, scalable, and easy to maintain. Each core component of the RAG pipeline is encapsulated in its own class with a single responsibility.

DocumentLoader: Responsible for ingesting multiple PDF files from a specified directory and handling potential file errors gracefully.

TextSplitter: Takes the raw text from all documents and divides it into smaller, overlapping chunks suitable for embedding.

EmbeddingModel: A wrapper for a sentence-transformers model. Its sole job is to convert text chunks into high-dimensional vector embeddings.

VectorStore: A simple, in-memory database that stores the text chunks and their corresponding vector embeddings. It exposes a method to find the most relevant chunks for a new query vector using Cosine Similarity.

RAGSystem: The main orchestrator class that initializes and coordinates all the other components to process documents and answer user queries.

🛠️ Tech Stack
Python 3.10+

Sentence-Transformers: For generating state-of-the-art text embeddings.

NumPy: For efficient numerical operations and vector calculations (Cosine Similarity).

PyPDF2: For extracting text content from PDF documents.

Object-Oriented Design: Core principle for building the system architecture.

🚀 Getting Started
Prerequisites
Python 3.10 or higher

pip package manager

Installation & Setup
Clone the repository:

git clone https://github.com/your-username/bvg-gpt.git
cd bvg-gpt


Create a virtual environment (recommended):

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install dependencies:

pip install -r requirements.txt


Add your data:

Create a folder named data in the root of the project.

Place all the BVG-related PDF documents you want to query inside the data folder.

Run the application:

python main.py


The script will automatically process the PDFs and then prompt you with example questions.

🎓 Key Learnings & Challenges
Deep Dive into RAG: Gained a practical, hands-on understanding of how Retrieval-Augmented Generation works at a fundamental level, without relying on high-level abstractions like LangChain.

Vector Semantics: Implemented and analyzed the effectiveness of Cosine Similarity vs. other distance metrics for understanding textual relevance in a high-dimensional vector space.

Robust Engineering: Faced and solved real-world data challenges, such as handling corrupted or unreadable PDFs, by building robust error-handling into the data loading pipeline.

OOP for AI Systems: Solidified the value of object-oriented design for building complex, multi-stage AI systems, where each component can be tested, improved, or replaced independently.

🔮 Future Improvements
This project provides a solid foundation. The next logical steps are:

[Generation] Integrate a Large Language Model (e.g., Gemini, Llama 3) to consume the retrieved snippets and generate a natural, conversational answer.

[Scalability] Replace the in-memory VectorStore with a dedicated, persistent vector database like ChromRADEaDB or FAISS to handle larger datasets and faster lookups.

[Interface] Build a simple web interface using Streamlit or Flask to create an interactive chat experience.

📬 Contact
GitHub: https://github.com/pythongurfer/