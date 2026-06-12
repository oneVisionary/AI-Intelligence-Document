import streamlit as st

from views.upload import show_upload_page
from views.documents import show_documents_page
from views.project_details import show_about

st.set_page_config(page_title="AI Document Intelligence", page_icon="📄", layout="wide")


with st.sidebar:
    st.header("Navigation")

    page = st.radio("Go to", ["🏠 Dashboard", "📤 Upload", "📚 Documents"])

if page == "🏠 Dashboard":
    show_about()

elif page == "📤 Upload":
    show_upload_page()

elif page == "📚 Documents":
    show_documents_page()
