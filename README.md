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