import streamlit as st

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="My Streamlit App"
)
# endregion <--------- Streamlit App Configuration --------->


st.image("who_we_are.png")
st.write("This is chatbot is designed to answers questions on the datasets available in our department. It uses our dataset metadata to enhance the output given by  that OpenAI.")

st.title("Instructions to run this app")
with st.expander("How to use this App"):
    st.write("1. The main page will prompt you for a password to unlock the application.")
    st.write("2. Once the APP has been unlocked. You can proceed to enter your prompt.")
    st.write("2. Click the 'Submit' button.")
    st.write("3. The app will generate a text completion based on your prompt.")

