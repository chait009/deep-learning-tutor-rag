from pathlib import Path
from langchain_core.documents import Document


D2L_PATH = Path("../""d2l-en")


def load_d2l_documents() -> list[Document]:
    if not D2L_PATH.exists():
        raise FileNotFoundError(
            f"D2L repository not found: {D2L_PATH.resolve()}"
        )

    markdown_files = list(D2L_PATH.glob("chapter_*/*.md"))

    if not markdown_files:
        raise FileNotFoundError(
            "No D2L chapter Markdown files were found."
        )

    documents = []

    for file_path in markdown_files:
        text = file_path.read_text(
            encoding="utf-8",
            errors="ignore"
        )

        if not text.strip():
            continue

        document = Document(
            page_content=text,
            metadata={
                "source": str(file_path),
                "file_name": file_path.name,
                "chapter": file_path.parent.name,
            }
        )

        documents.append(document)

    return documents


if __name__ == "__main__":
    docs = load_d2l_documents()

    print(f"Loaded documents: {len(docs)}")

    if docs:
        print("\nFirst document")
        print("----------------")

        print(f"Chapter: {docs[0].metadata['chapter']}")
        print(f"Source: {docs[0].metadata['source']}")
        print(f"Characters: {len(docs[0].page_content)}")

        print("\nPreview:")
        print(docs[0].page_content[:500])