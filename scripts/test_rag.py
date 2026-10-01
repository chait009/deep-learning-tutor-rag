from app.rag.pipeline import DeepLearningTutorRAG


def main():
    rag = DeepLearningTutorRAG(
        top_k=4
    )

    question = (
        "Explain backpropagation in simple terms."
    )

    print("\nQuestion:")
    print(question)

    print("\nSearching the D2L book and generating answer...")

    result = rag.ask(question)

    print("\nAnswer:")
    print("=" * 70)

    print(result["answer"])

    print("\nSources:")
    print("=" * 70)

    for index, source in enumerate(
        result["sources"],
        start=1,
    ):
        print(
            f"{index}. {source['chapter']}"
        )

        print(
            f"   {source['file']}"
        )


if __name__ == "__main__":
    main()