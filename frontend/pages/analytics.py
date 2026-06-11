import streamlit as st
import pandas as pd

st.title("📊 Analytics Dashboard")

col1, col2 = st.columns(2)

with col1:
    st.metric("Average OCR Time", "2.3 sec")

with col2:
    st.metric("Average Summary Length", "180 words")

st.divider()

st.subheader("Documents Processed Per Day")

chart_data = pd.DataFrame(
    {"Day": ["Mon", "Tue", "Wed", "Thu", "Fri"], "Documents": [10, 15, 8, 20, 25]}
)

st.bar_chart(chart_data.set_index("Day"))
