import streamlit as st
import time

from services.api import upload_document, get_document_status

st.title("📤 Upload Document")

uploaded_file = st.file_uploader("Choose a file", type=["pdf", "png", "jpg", "jpeg"])

if uploaded_file:

    if st.button("Process Document"):

        upload_response = upload_document(uploaded_file)

        document_id = upload_response["document_id"]

        progress = st.progress(0)
        status_text = st.empty()

        while True:

            result = get_document_status(document_id)

            status = result["status"]

            if status == "PENDING":
                status_text.info("Waiting in queue...")
                progress.progress(20)

            elif status == "PROCESSING":
                status_text.info("Generating OCR and Summary...")
                progress.progress(60)

            elif status == "COMPLETED":

                progress.progress(100)
                status_text.success("Completed")

                st.subheader("OCR Output")
                st.text_area("", result["extracted_text"], height=300)

                st.subheader("AI Summary")
                st.write(result["summary"])

                break

            elif status == "FAILED":

                st.error("Processing failed")
                break

            time.sleep(3)
