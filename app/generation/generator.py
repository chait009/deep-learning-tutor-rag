import os

from dotenv import load_dotenv
from langchain_core.documents import Document
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI


load_dotenv()


def format_context(documents: list[Document]) -> str:
    """
    Combine retrieved D2L chunks into one context string.
    """

    context_parts = []

    for index, document in enumerate(documents, start=1):
        chapter = document.metadata.get(
            "chapter",
            "Unknown chapter"
        )

        source = document.metadata.get(
            "source",
            "Unknown source"
        )

        context_parts.append(
            f"""
Source {index}
Chapter: {chapter}
File: {source}

{document.page_content}
"""
        )

    return "\n".join(context_parts)


def generate_answer(
    question: str,
    documents: list[Document],
) -> str:
    """
    Generate a simple tutor-style answer using
    retrieved D2L book content.
    """

    if not question.strip():
        raise ValueError("Question cannot be empty.")

    if not documents:
        return (
            "I could not find enough information in the "
            "Dive into Deep Learning book to answer this question."
        )

    api_key = os.getenv("OPENAI_API_KEY")
    model_name = os.getenv("OPENAI_MODEL")

    if not api_key:
        raise ValueError(
            "OPENAI_API_KEY was not found in the .env file."
        )

    if not model_name:
        raise ValueError(
            "OPENAI_MODEL was not found in the .env file."
        )

    context = format_context(documents)

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """
You are a friendly deep learning tutor.

Your job is to explain machine learning and deep learning
concepts in simple human language.

Use only the provided context from the
Dive into Deep Learning book.

Rules:

1. Answer the user's question using the provided context.
2. Explain difficult concepts in simple language.
3. Use a small example when it helps.
4. Avoid unnecessary technical jargon.
5. If you use a technical term, explain what it means.
6. Do not invent information that is not supported by the context.
7. If the context does not contain enough information, clearly say so.
8. Do not copy long paragraphs directly from the book.
9. Keep the explanation clear and educational.
"""
            ),
            (
                "human",
                """
Context:

{context}

Question:

{question}

Explain the answer like a tutor teaching a student.
"""
            ),
        ]
    )

    model = ChatOpenAI(
        model=model_name,
    )

    chain = (
        prompt
        | model
        | StrOutputParser()
    )

    answer = chain.invoke(
        {
            "context": context,
            "question": question,
        }
    )

    return answer