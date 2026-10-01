# Deep Learning Tutor RAG

This is a small RAG project I built using the **Dive into Deep Learning (D2L)** book as the knowledge source.

The idea is simple: instead of asking an LLM a deep learning question directly, the application first searches the D2L content, finds the most relevant sections, and then uses that context to generate the answer.

I built this mainly to understand how a real RAG pipeline works end to end will end more features in future

## What this project does

When a user asks a question like:

```text
What is dropout?
```

the application:

1. Searches the D2L book content
2. Finds the most relevant text
3. Sends that text along with the question to the LLM
4. Generates an answer based on the retrieved content

This helps keep the response closer to the actual source instead of depending only on what the model already knows.

## Tech used

- Python
- LangChain
- Hugging Face embeddings
- FAISS
- FastAPI
- Docker
- D2L open-source book

## Project structure

```text
deep-learning-tutor-rag/
│
├── app/
│   ├── ingestion/
│   ├── retrieval/
│   ├── rag/
│   └── api/
│
├── scripts/
├── tests/
├── requirements.txt
├── Dockerfile
└── README.md
```

## Setup

Clone this repository:

```bash
git clone https://github.com/chait009/deep-learning-tutor-rag.git
cd deep-learning-tutor-rag
```

Create a virtual environment:

```cmd
python -m venv .venv
```

Activate it on Windows:

```cmd
.venv\Scripts\activate
```

Install the packages:

```cmd
pip install -r requirements.txt
```

## Download the D2L repository

The application reads the source content directly from the D2L repository.

I keep it outside the main project folder.

```cmd
cd D:\
git clone https://github.com/d2l-ai/d2l-en.git
```

My folder structure looks like this:

```text
D:\
├── deep-learning-tutor-rag
└── d2l-en
```

## Running the ingestion

Go back to the project folder:

```cmd
cd D:\deep-learning-tutor-rag
```

Then run:

```cmd
python -m app.ingestion.document_loader
```

This loads the D2L content so it can later be chunked, embedded, and searched.

## How the RAG flow works

The flow is roughly:

```text
D2L documents
      ↓
Text chunks
      ↓
Embeddings
      ↓
FAISS
      ↓
User question
      ↓
Relevant chunks retrieved
      ↓
LLM
      ↓
Final answer
```

I used LangChain to connect the retrieval and generation parts instead of building every part manually.

## Example

Question:

```text
Explain
