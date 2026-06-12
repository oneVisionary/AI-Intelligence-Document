import streamlit as st
import time
from services.api import upload_document, get_document_status

def show_upload_page():

    uploaded_file = st.file_uploader("Choose a file", type=["pdf", "png", "jpg", "jpeg"])

    if uploaded_file:

        st.success(uploaded_file.name)

        if st.button("Process Document"):

            with st.spinner("Uploading document..."):
                result = upload_document(uploaded_file)

            document_id = result["id"]

            status_placeholder = st.empty()
            summary_placeholder = st.empty()

            while True:

                document = get_document_status(document_id)

                status = document.get("status")

                if status == "processing":
                    status_placeholder.info("⏳ OCR and summarization in progress...")
                    time.sleep(2)

                elif status == "completed":

                    status_placeholder.success("✅ Document processed successfully")

                    summary_placeholder.subheader("Summary")

                    summary_placeholder.write(document.get("summary", "No summary found"))

                    break

                elif status == "failed":

                    status_placeholder.error("❌ Processing failed")
                    break

                else:
                    status_placeholder.warning(f"Unknown status: {status}")
                    break
