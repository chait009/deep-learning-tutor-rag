from pathlib import Path

from langchain_core.documents import Document
from langchain_qdrant import QdrantVectorStore

from app.embeddings.embedding_model import get_embedding_model


COLLECTION_NAME = "d2l_book"
QDRANT_PATH = Path("data/qdrant")


def create_vector_store(
    documents: list[Document],
) -> QdrantVectorStore:
    """
    Create a local Qdrant vector store and add the D2L chunks.
    """

    if not documents:
        raise ValueError("No documents were provided.")

    QDRANT_PATH.mkdir(
        parents=True,
        exist_ok=True,
    )

    embeddings = get_embedding_model()

    vector_store = QdrantVectorStore.from_documents(
        documents=documents,
        embedding=embeddings,
        path=str(QDRANT_PATH),
        collection_name=COLLECTION_NAME,
    )

    return vector_store


def load_vector_store() -> QdrantVectorStore:
    """
    Load the existing local Qdrant collection.
    """

    if not QDRANT_PATH.exists():
        raise FileNotFoundError(
            "Qdrant database not found. Build the index first."
        )

    embeddings = get_embedding_model()

    vector_store = QdrantVectorStore.from_existing_collection(
        embedding=embeddings,
        path=str(QDRANT_PATH),
        collection_name=COLLECTION_NAME,
    )

    return vector_store