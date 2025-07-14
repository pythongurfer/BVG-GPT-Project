# BVG-GPT: Factual AI Chatbot for Berlin Public Transport

![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![Libraries](https://img.shields.io/badge/Libraries-SentenceTransformers%20%7C%20NumPy%20%7C%20PyPDF2-orange.svg)
![Concept](https://img.shields.io/badge/Concept-RAG%20%7C%20Vector%20Search-green.svg)

A sophisticated, retrieval-based AI engine designed to answer questions about Berlin's public transport system (BVG) by using official documents as a source of truth. This project serves as a foundational step in creating a "hallucination-free" chatbot, focusing on the core **Retrieval-Augmented Generation (RAG)** pipeline.

---

## The Problem

Finding specific, accurate information within dense official documents—like tariff regulations or transport conditions—is often tedious and inefficient. Furthermore, general-purpose Large Language Models (LLMs) can "hallucinate" or provide outdated information, making them unreliable for factual queries.

## The Solution

This project implements the **Retrieval** component of a RAG system from scratch. Instead of asking an LLM a question directly, this engine first performs a semantic search over a database of official BVG documents. It finds and extracts the most relevant text snippets that contain the answer, ensuring that any subsequent response is grounded in factual, verifiable data.

### How It Looks In Action

*(This shows the output of the current retrieval engine)*



## 🏛️ System Architecture & Design

This project was built following **Object-Oriented Programming (OOP)** principles to ensure the system is modular, scalable, and easy to maintain. Each core component of the RAG pipeline is encapsulated in its own class with a single responsibility.

![RAG Pipeline Diagram](https://i.imgur.com/L5nN1uH.png)

1.  **`DocumentLoader`**: Responsible for ingesting multiple PDF files from a specified directory and handling potential file errors gracefully.
2.  **`TextSplitter`**: Takes the raw text from all documents and divides it into smaller, overlapping chunks suitable for embedding.
3.  **`EmbeddingModel`**: A wrapper for a `sentence-transformers` model. Its sole job is to convert text chunks into high-dimensional vector embeddings.
4.  **`VectorStore`**: A simple, in-memory database that stores the text chunks and their corresponding vector embeddings. It exposes a method to find the most relevant chunks for a new query vector using **Cosine Similarity**.
5.  **`RAGSystem`**: The main orchestrator class that initializes and coordinates all the other components to process documents and answer user queries.

---

## 🛠️ Tech Stack

* **Python 3.10+**
* **Sentence-Transformers**: For generating state-of-the-art text embeddings.
* **NumPy**: For efficient numerical operations and vector calculations (Cosine Similarity).
* **PyPDF2**: For extracting text content from PDF documents.
* **Object-Oriented Design**: Core principle for building the system architecture.

---

## 🚀 Getting Started

### Prerequisites

-   Python 3.10 or higher
-   `pip` package manager

### Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/bvg-gpt.git](https://github.com/your-username/bvg-gpt.git)
    cd bvg-gpt
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    *(You will need to create a `requirements.txt` file for this step)*
    ```bash
    pip install sentence-transformers numpy PyPDF2
    ```

4.  **Add your data:**
    -   Create a folder named `data` in the root of the project.
    -   Place all the BVG-related PDF documents you want to query inside the `data` folder.

5.  **Run the application:**
    ```bash
    python main.py
    ```
    The script will automatically process the PDFs and then prompt you with example questions.


---
🌐 General Use Case: AI Chatbot for Internal Knowledge Retrieval
Any organization that relies on dense, official, or technical documents can benefit from a RAG-based chatbot. Instead of employees or customers struggling to search through manuals, policies, or FAQs, they can simply ask a question and receive a fact-based, source-grounded answer.

🏢 How This Applies to Other Companies
1. Airlines / Transport Operators
Documents: Baggage rules, flight conditions, safety policies, fare charts.

Use: Customers or agents can query rules ("Can I bring a bike on board?") and get answers from airline policy documents.

Benefit: Reduces call center load, improves customer experience.

2. Banks & Financial Institutions
Documents: Loan terms, privacy policies, compliance documents, product brochures.

Use: Helpdesk bots that give exact answers about fees, eligibility, or terms of service.

Benefit: Ensures regulatory compliance by eliminating hallucinations in customer responses.

3. Insurance Companies
Documents: Policy documents, claims procedures, exclusions lists.

Use: Assist customers or agents in quickly finding details on what's covered or not.

Benefit: Fewer disputes, faster claims processing.

4. Legal Firms / Compliance Departments
Documents: Laws, regulations, case documents, contracts.

Use: Internal research assistant that helps staff retrieve exact clauses or precedents.

Benefit: Saves hours of manual legal research; improves precision.

5. Healthcare Providers
Documents: Treatment guidelines, insurance contracts, patient care protocols.

Use: Internal support for doctors/nurses ("What’s the protocol for XYZ?") or for patients ("Is XYZ covered by insurance?").

Benefit: Improves care quality, reduces administrative burden.

6. Tech Companies (Product Support)
Documents: API documentation, user manuals, release notes, bug reports.

Use: Developer or customer assistant that fetches code examples or troubleshooting steps.

Benefit: Cuts support tickets; improves developer onboarding.



## 📬 Contact

* **GitHub:** [pythongurfer](https://github.com/pythongurfer)
