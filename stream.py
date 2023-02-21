import streamlit as st
from get_data import *
import pandas as pd

st.write("""
# SAP Blog Scrap
""")

dat_ = st.selectbox("Choose URL", ["https://blogs.sap.com/"])

d = pd.read_csv("sap.csv")
st.table(d)

# st.download_button(
#     label="Download data as CSV",
#     data=d,
#     file_name='sap.csv',
#     mime='text/csv',
# )
data_as_csv= d.to_csv(index=False).encode("utf-8")
st.download_button(
    "Download data as CSV",
    data_as_csv,
    "sap-blog.csv",
    "text/csv",
    key="download-tools-csv",
)