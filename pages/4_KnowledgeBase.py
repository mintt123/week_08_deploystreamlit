import streamlit as st
import pandas as pd
import json

st.title("Sorry, data not available for full display here.")
st.image("restricted.png")
st.write("But here is a sample of the structure of our datasets, data fields, and source owner:")

df2 = pd.read_csv('./data/metadata.csv')
df_display = df2.head(3)
df_display

with st.expander("You may contact us via email to request for our knowledge base."):
    st.write("Shiming")
    st.write("Wei Loon")
