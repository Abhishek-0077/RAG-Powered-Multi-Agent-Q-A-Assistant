# RAG-Powered Multi-Agent Q&A Assistant

## Overview
The **RAG-Powered Multi-Agent Q&A Assistant** is a chatbot application designed to intelligently route user queries to the appropriate processing pipeline. It leverages **sentence embeddings**, **ChromaDB** for vector storage and retrieval, and a **language model (LLM)** to generate precise answers. The workflow is structured to handle different types of queries, such as calculations, definitions, or general knowledge retrieval, and display all steps in a chatbot interface.

---

## Workflow

### 1. **User Input**
- The user provides a query through the chatbot interface.

### 2. **Sentence Embedding**
- The query is embedded into a vector representation using the **`SentenceTransformer`** model (`all-MiniLM-L6-v2`).

### 3. **Intent Classification**
- The embedded query is compared against pre-stored intent vectors in the **`intent_classifier`** collection (stored in ChromaDB).
- The nearest intent is determined using vector similarity.
- Based on the intent, the query is routed to one of the following pipelines:
  - **Calculator**: For mathematical calculations.
  - **Dictionary**: For definitions or explanations.
  - **RAG (Retrieval-Augmented Generation)**: For general knowledge or document-based queries.

### 4. **Processing Pipelines**
#### a. **Calculator**
- If the intent is classified as "calculator," the query is routed to a dedicated API call or function to perform the calculation.

#### b. **Dictionary**
- If the intent is classified as "dictionary," the query is routed to a dictionary API or function to fetch the definition or explanation.

#### c. **RAG (Retrieval-Augmented Generation)**
- If the intent is classified as "RAG," the following steps are performed:
  1. **Document Retrieval**:
     - The query embedding is compared against pre-stored document embeddings in the **`chunks_storage`** collection (stored in ChromaDB).
     - The top 3 most relevant documents are retrieved.
  2. **Answer Generation**:
     - The retrieved documents are passed as context to a **language model (LLM)**.
     - The LLM generates a precise answer based on the query and the retrieved context.

### 5. **Chatbot Interface**
- All steps, including the classification, routing, and final answer generation, are displayed in the chatbot interface for transparency and user understanding.

---

## Project Structure

### Key Components
1. **`app.py`**:
   - The main Flask application that handles user input, routing, and rendering the chatbot interface.

2. **`model_For_Rag.py`**:
   - Contains functions for embedding queries, retrieving top documents, and classifying intents using ChromaDB.

3. **ChromaDB Collections**:
   - **`chunks_storage`**: Stores document embeddings for retrieval in the RAG pipeline.
   - **`intent_classifier`**: Stores intent embeddings for query classification.

4. **Language Model**:
   - A pre-trained LLM is used for generating answers in the RAG pipeline.

---

## How It Works

1. **Input**: The user enters a query in the chatbot.
2. **Embedding**: The query is embedded using `SentenceTransformer`.
3. **Intent Classification**: The query is classified into one of three categories:
   - Calculator
   - Dictionary
   - RAG
4. **Routing**:
   - **Calculator**: Calls a calculation function or API.
   - **Dictionary**: Fetches a definition or explanation.
   - **RAG**: Retrieves top documents and generates an answer using the LLM.
5. **Output**: The chatbot displays the result along with the steps taken to process the query.

---

## Installation

### Prerequisites
- Python 3.8 or higher
- Required Python libraries:
  - `flask`
  - `chromadb`
  - `sentence-transformers`
  - `transformers`
  - `torch`

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/RAG-Powered-Multi-Agent-Q-A-Assistant.git
   cd RAG-Powered-Multi-Agent-Q-A-Assistant
