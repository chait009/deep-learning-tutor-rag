from app.vectorstore.vector_store import load_vector_store


def main():
    print("Loading Qdrant vector store...")

    vector_store = load_vector_store()

    query = "What is gradient descent and how does it work?"

    print("\nQuestion:")
    print(query)

    print("\nSearching for relevant D2L sections...")

    results = vector_store.similarity_search_with_score(
        query=query,
        k=4,
        score_threshold=0.35,
    )

    print(f"\nRetrieved chunks: {len(results)}")

    if not results:
        print(
            "No sufficiently relevant chunks were found."
        )
        return

    for index, result in enumerate(
        results,
        start=1,
    ):
        document, score = result

        print("\n" + "=" * 70)
        print(f"RESULT {index}")
        print("=" * 70)

        print(
            f"Score: {score:.4f}"
        )

        print(
            f"Chapter: "
            f"{document.metadata.get('chapter', 'Unknown')}"
        )

        print(
            f"Source: "
            f"{document.metadata.get('source', 'Unknown')}"
        )

        print("\nContent:")
        print("-" * 70)

        print(
            document.page_content[:1200]
        )


if __name__ == "__main__":
    main()