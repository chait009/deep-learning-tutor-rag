from app.ingestion.document_loader import load_d2l_documents
from app.ingestion.chunker import split_documents


def main():
    print("Loading D2L documents...")

    documents = load_d2l_documents()

    print(f"Documents loaded: {len(documents)}")

    print("\nSplitting documents into chunks...")

    chunks = split_documents(documents)

    print(f"Chunks created: {len(chunks)}")

    if chunks:
        first_chunk = chunks[0]

        print("\nFirst chunk")
        print("=" * 60)

        print(f"Chapter: {first_chunk.metadata.get('chapter')}")
        print(f"Source: {first_chunk.metadata.get('source')}")
        print(f"Characters: {len(first_chunk.page_content)}")

        print("\nContent:")
        print("-" * 60)

        print(first_chunk.page_content)


if __name__ == "__main__":
    main()