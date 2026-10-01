import os

import requests
import streamlit as st


API_URL = os.getenv(
    "API_URL",
    "http://127.0.0.1:8000/ask",
)


st.set_page_config(
    page_title="Deep Learning Tutor RAG",
    page_icon="🧠",
    layout="centered",
)


st.title("🧠 Deep Learning Tutor")

st.write(
    "Ask questions about machine learning and deep learning "
    "using the Dive into Deep Learning book."
)


question = st.text_area(
    "Ask your question",
    placeholder="Example: Explain backpropagation in simple terms",
    height=120,
)


if st.button("Ask Tutor"):
    if not question.strip():
        st.warning("Please enter a question.")

    else:
        with st.spinner("Searching the book..."):
            try:
                response = requests.post(
                    API_URL,
                    json={
                        "question": question
                    },
                    timeout=120,
                )

                response.raise_for_status()

                result = response.json()

                st.subheader("Answer")

                st.write(
                    result.get(
                        "answer",
                        "No answer returned.",
                    )
                )

                sources = result.get(
                    "sources",
                    [],
                )

                if sources:
                    st.subheader("Sources")

                    for index, source in enumerate(
                        sources,
                        start=1,
                    ):
                        chapter = source.get(
                            "chapter",
                            "Unknown chapter",
                        )

                        file_path = source.get(
                            "file",
                            "Unknown source",
                        )

                        score = source.get(
                            "score",
                        )

                        with st.expander(
                            f"Source {index}: {chapter}"
                        ):
                            st.write(file_path)

                            if score is not None:
                                st.write(
                                    f"Similarity score: {score}"
                                )

            except requests.exceptions.ConnectionError:
                st.error(
                    "Could not connect to the RAG API."
                )

            except requests.exceptions.Timeout:
                st.error(
                    "The request took too long. Please try again."
                )

            except requests.exceptions.HTTPError:
                st.error(
                    f"API error: {response.text}"
                )

            except Exception as error:
                st.error(
                    f"Something went wrong: {str(error)}"
                )