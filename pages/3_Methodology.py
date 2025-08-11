import streamlit as st

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="My Streamlit App"
)
# endregion <--------- Streamlit App Configuration --------->

st.title("Methodology")

st.write("Step 1. Data sources are extracted offline and converted into easily readable text/JSON format to form the Knowledge Base.")
st.write("Step 2. LLMs has been pretrained by OpenAI. We set API calls to the LLM along with system prompts and guides for the LLM to use our Knowledge Base. We used a low temperature for LLM to reduce speculation since our use case needs to output factual information to the user.")
st.write("Step 3. Safeguards have been set in place to password protect the APP as well as ringfence the user's prompt for a more accurate response.")
st.image("Flowchart.jpg")