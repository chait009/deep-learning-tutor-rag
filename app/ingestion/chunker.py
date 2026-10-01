from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document


def split_documents(
    documents: list[Document],
    chunk_size: int = 1200,
    chunk_overlap: int = 200,
) -> list[Document]:
    """
    Split large documents into smaller chunks for retrieval.
    """

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=[
            "\n## ",
            "\n### ",
            "\n#### ",
            "\n\n",
            "\n",
            " ",
            "",
        ],
    )

    chunks = text_splitter.split_documents(documents)

    return chunks