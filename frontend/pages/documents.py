import streamlit as st
import pandas as pd

st.title("📚 Documents")

data = {
    "ID": [1, 2, 3],
    "Filename": ["invoice.pdf", "report.pdf", "contract.pdf"],
    "Status": ["Processed", "Processing", "Processed"],
    "Summary": [
        "Invoice information extracted",
        "In progress",
        "Contract successfully analyzed",
    ],
}

df = pd.DataFrame(data)

st.dataframe(df, use_container_width=True)
