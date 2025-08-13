# Set up and run this Streamlit App
import streamlit as st
import pandas as pd
# from helper_functions import llm
from logics.data_read_handler import process_user_message

#password protect
from helper_functions.utility import check_password

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="My Streamlit App"
)
# endregion <--------- Streamlit App Configuration --------->

st.title("Welcome to our Chatbot")
st.write("This is a proof-of-concept chatbot to answer questions on the datasets we have in our department. Please refer to the About Us tab for more information") 

# Check if the password is correct.  
if not check_password():  
     st.stop()


form = st.form(key="form")
form.subheader("Prompt")

user_prompt = form.text_area("Please enter your question here (e.g. What datasets are available from ACRA?)", height=150)

if form.form_submit_button("Submit"):
    
    st.toast(f"User Input Submitted - {user_prompt}")

    st.divider()

    response = process_user_message(user_prompt)
    st.write(response)

    st.divider()