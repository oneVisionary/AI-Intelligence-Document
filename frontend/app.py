import streamlit as st

st.set_page_config(page_title="AI Document Intelligence", page_icon="📄", layout="wide")

st.title("📄 AI Document Intelligence Platform")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Documents", 120)

with col2:
    st.metric("Processed", 95)

with col3:
    st.metric("Pending", 20)

with col4:
    st.metric("Failed", 5)

st.divider()

st.subheader("Recent Activity")

st.dataframe(
    [
        {
            "Filename": "invoice_01.pdf",
            "Status": "Processed",
            "Upload Time": "2 min ago",
        },
        {
            "Filename": "contract.pdf",
            "Status": "Processing",
            "Upload Time": "5 min ago",
        },
    ],
    use_container_width=True,
)
