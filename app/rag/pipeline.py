from app.generation.generator import generate_answer
from app.vectorstore.vector_store import load_vector_store


class DeepLearningTutorRAG:
    """
    Main RAG pipeline for the Deep Learning Tutor.

    Flow:
    Question
        -> Qdrant retrieval
        -> similarity filtering
        -> relevant D2L chunks
        -> OpenAI
        -> tutor-style answer
    """

    def __init__(
        self,
        top_k: int = 4,
        score_threshold: float = 0.35,
    ):
        self.top_k = top_k
        self.score_threshold = score_threshold

        print("Loading vector store...")

        self.vector_store = load_vector_store()

        print("RAG pipeline ready.")

    def retrieve(self, question: str):
        """
        Retrieve relevant D2L chunks with similarity scores.
        """

        if not question.strip():
            raise ValueError(
                "Question cannot be empty."
            )

        results = self.vector_store.similarity_search_with_score(
            query=question,
            k=self.top_k,
            score_threshold=self.score_threshold,
        )

        documents = []

        for document, score in results:
            document.metadata["retrieval_score"] = round(
                float(score),
                4,
            )

            documents.append(document)

        return documents

    def ask(self, question: str) -> dict:
        """
        Retrieve relevant context and generate an answer.
        """

        documents = self.retrieve(question)

        if not documents:
            return {
                "question": question,
                "answer": (
                    "I could not find enough relevant information "
                    "in the Dive into Deep Learning book to answer "
                    "this question."
                ),
                "sources": [],
            }

        answer = generate_answer(
            question=question,
            documents=documents,
        )

        sources = []

        for document in documents:
            source = {
                "chapter": document.metadata.get(
                    "chapter",
                    "Unknown",
                ),
                "file": document.metadata.get(
                    "source",
                    "Unknown",
                ),
                "score": document.metadata.get(
                    "retrieval_score",
                    0.0,
                ),
            }

            if source not in sources:
                sources.append(source)

        return {
            "question": question,
            "answer": answer,
            "sources": sources,
        }