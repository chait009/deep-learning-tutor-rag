from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from app.rag.pipeline import DeepLearningTutorRAG


app = FastAPI(
    title="Deep Learning Tutor RAG",
    description=(
        "A RAG-based deep learning tutor using the "
        "Dive into Deep Learning book."
    ),
    version="1.0.0",
)


rag = DeepLearningTutorRAG(
    top_k=4
)


class QuestionRequest(BaseModel):
    question: str = Field(
        min_length=3,
        max_length=1000,
        description="Machine learning or deep learning question",
    )


@app.get("/")
def root():
    return {
        "message": "Deep Learning Tutor RAG API is running."
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/ask")
def ask_question(request: QuestionRequest):
    try:
        result = rag.ask(
            question=request.question
        )

        return result

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error),
        )

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=f"RAG request failed: {str(error)}",
        )