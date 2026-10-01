from app.ingestion.document_loader import load_d2l_documents
from app.ingestion.chunker import split_documents
from app.vectorstore.vector_store import create_vector_store


def main():
    print("Loading D2L documents...")

    documents = load_d2l_documents()

    print(f"Documents loaded: {len(documents)}")

    print("\nSplitting documents...")

    chunks = split_documents(documents)

    print(f"Chunks created: {len(chunks)}")

    print("\nCreating embeddings and Qdrant index...")

    create_vector_store(chunks)

    print("\nVector index created successfully.")


if __name__ == "__main__":
    main()