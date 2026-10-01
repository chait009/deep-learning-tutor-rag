from app.generation.generator import generate_answer
from app.vectorstore.vector_store import load_vector_store


def main():
    question = "What is gradient descent and why do we use it?"

    print("Loading vector store...")

    vector_store = load_vector_store()

    print("\nRetrieving relevant book sections...")

    documents = vector_store.similarity_search(
        query=question,
        k=4,
    )

    print(f"Retrieved chunks: {len(documents)}")

    print("\nGenerating answer...")

    answer = generate_answer(
        question=question,
        documents=documents,
    )

    print("\nQuestion:")
    print(question)

    print("\nAnswer:")
    print("=" * 70)

    print(answer)


if __name__ == "__main__":
    main()