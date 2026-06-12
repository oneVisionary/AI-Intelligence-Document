import streamlit as st
import pandas as pd
from services.api import get_all_document


def show_documents_page():
    st.title("📚 Documents")

    documents = get_all_document()

    if not documents:
        st.info("No documents found.")
    else:
        df = pd.DataFrame(documents)

        with st.container():
            st.dataframe(
                df[
                    [
                        "document_id",
                        "original_filename",
                        "status",
                        "file_size",
                        "created_at",
                    ]
                ],
                use_container_width=True,
                height=500,
                hide_index=True,
            )
