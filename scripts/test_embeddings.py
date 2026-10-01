from app.embeddings.embedding_model import get_embedding_model


def main():
    print("Loading embedding model...")

    embeddings = get_embedding_model()

    text = "Gradient descent helps minimize the loss function."

    print("\nCreating embedding...")

    vector = embeddings.embed_query(text)

    print("\nEmbedding created successfully.")
    print(f"Text: {text}")
    print(f"Vector dimensions: {len(vector)}")

    print("\nFirst 10 values:")
    print(vector[:10])


if __name__ == "__main__":
    main()