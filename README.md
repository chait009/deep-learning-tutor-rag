This project uses content from Dive into Deep Learning by Aston Zhang, Zachary C. Lipton, Mu Li, and Alexander J. Smola.

The book is available under the Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0) license.

The sample and reference code from the D2L project is provided under its modified MIT license.

Original project:

https://github.com/d2l-ai/d2l-en

This project is not affiliated with or maintained by the D2L authors. It uses the book as the knowledge source for learning and demonstrating a RAG application.

## Deep Learning Tutor RAG

This is a Retrieval-Augmented Generation (RAG) project I built to better understand how a real RAG application works from end to end.

The application uses content from the open-source **Dive into Deep Learning (D2L)** book and allows users to ask deep learning questions in simple English.

Instead of asking an LLM to answer from its own knowledge, the application first searches the D2L content for relevant information and then sends that context to the LLM. This helps keep the answers more focused and grounded in the source material.

---

## What This Project Does

A user can ask questions such as:

```text
What is gradient descent?
```

or:

```text
Explain convolutional neural networks in simple terms.
```

The application:

1. Searches the D2L book for relevant sections.
2. Retrieves the most relevant chunks.
3. Sends those chunks along with the user's question to the LLM.
4. Generates an answer based on the retrieved context.
5. Shows the source information and similarity scores.

---

## Architecture

```text
Dive into Deep Learning Book
          |
          v
    Document Loader
          |
          v
      Text Chunking
          |
          v
Hugging Face Embeddings
          |
          v
 Qdrant Vector Database
          |
          v
      User Question
          |
          v
   Similarity Search
          |
          v
 Relevant D2L Context
          |
          v
      OpenAI LLM
          |
          v
 Grounded Tutor Answer
```

---

## Tech Stack

- Python
- LangChain
- OpenAI API
- Hugging Face Sentence Transformers
- Qdrant
- FastAPI
- Streamlit
- Docker
- Dive into Deep Learning (D2L)

---

## Project Structure

```text
deep-learning-tutor-rag/
│
├── app/
│   ├── api/
│   │   └── main.py
│   │
│   ├── generation/
│   │   └── generator.py
│   │
│   ├── ingestion/
│   │   ├── chunker.py
│   │   └── document_loader.py
│   │
│   ├── rag/
│   │   └── pipeline.py
│   │
│   └── vectorstore/
│
├── data/
│
├── scripts/
│
├── streamlit_app.py
├── requirements.txt
├── Dockerfile
├── .env.example
└── README.md
```

---

## How the RAG Pipeline Works

### 1. Load the D2L Content

The project uses the open-source **Dive into Deep Learning** repository as the knowledge source.

The document loader reads the book content and keeps useful metadata such as the file name and chapter information.

---

### 2. Split the Documents

Large documents cannot be sent directly to the embedding model or LLM.

The text is split into smaller chunks using LangChain's `RecursiveCharacterTextSplitter`.

The chunking strategy also tries to respect Markdown headings so that related content stays together as much as possible.

Current settings:

```text
Chunk size: 1200
Chunk overlap: 200
```

---

### 3. Create Embeddings

Each text chunk is converted into an embedding using a Hugging Face sentence-transformer model.

Embeddings convert text into numerical vectors so that similar pieces of text can be found using similarity search.

---

### 4. Store Embeddings in Qdrant

The embeddings and their document metadata are stored in **Qdrant**.

Qdrant acts as the vector database for the application.

When a user asks a question, the application searches Qdrant for chunks that are semantically similar to the question.

---

### 5. Retrieve Relevant Context

The RAG pipeline retrieves the most relevant chunks from Qdrant.

The application also uses a similarity threshold so that very weak search results are not automatically sent to the LLM.

This helps reduce unrelated answers.

---

### 6. Generate the Answer

The retrieved D2L content is passed to the OpenAI model along with the user's question.

The prompt tells the model to answer using the provided context and avoid making up information that is not available in the retrieved documents.

If useful context cannot be found, the application can tell the user that the answer was not found in the available material.

---

## FastAPI Backend

The project exposes the RAG system through a FastAPI API.

Main endpoints:

```text
GET /health
POST /ask
```

Example request:

```json
{
  "question": "What is gradient descent?"
}
```

The API returns the generated answer along with source information.

---

## Streamlit Interface

A simple Streamlit interface is included so the RAG application can be tested without manually sending API requests.

The interface allows users to:

- Ask deep learning questions
- View the generated answer
- See which source documents were retrieved
- View retrieval similarity scores

---

## Running the Project Locally

### 1. Clone the Repository

```bash
git clone https://github.com/chait009/deep-learning-tutor-rag.git
cd deep-learning-tutor-rag
```

---

### 2. Create a Virtual Environment

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Mac/Linux:

```bash
python -m venv .venv
source .venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure Environment Variables

Create a `.env` file based on `.env.example`.

Add your OpenAI API key:

```text
OPENAI_API_KEY=your_api_key_here
```

Do not commit your real API key to GitHub.

---

### 5. Build the Vector Database

Run the ingestion process to load the D2L documents, create chunks and embeddings, and store them in Qdrant.

---

### 6. Start the FastAPI Backend

```bash
uvicorn app.api.main:app --reload
```

FastAPI will run at:

```text
http://localhost:8000
```

API documentation:

```text
http://localhost:8000/docs
```

---

### 7. Start the Streamlit App

Open another terminal and run:

```bash
streamlit run streamlit_app.py
```

Streamlit will normally run at:

```text
http://localhost:8501
```

---

## Running With Docker

The project is also containerized with Docker.

Build the image:

```bash
docker build -t deep-learning-tutor-rag .
```

Run the container:

```bash
docker run --env-file .env -p 8000:8000 -p 8501:8501 deep-learning-tutor-rag
```

This makes it easier to run the application with the same environment across different machines.

---

## Deployment

The project is Dockerized and can be deployed to a cloud platform if needed.

I currently run the application locally instead of keeping a permanent public deployment online because the application uses external LLM APIs and would require ongoing infrastructure and API costs.

The repository contains the code

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/a191cde4-889f-438b-aec7-c55703c3a075" />


## Example

Question:

```text
Explain
