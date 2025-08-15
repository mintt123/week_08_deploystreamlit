import os
import openai
from helper_functions import llm
import json
import pandas as pd

# Reading in as CSV file does not seem to work
# df = pd.read_csv('./data/metadata.csv')

# Load the JSON file
filepath = './data/metadata2.json'
# filepath = 'datasets.json'
with open(filepath, 'r') as file:
    json_string = file.read()
    df = json.loads(json_string)

def process_user_message(user_input):
    delimiter = "```"

    system_message = f"""
    You are a helpful assistant for the Singapore Department of Statistics (SINGSTAT). 
    You are provided with all the dataset names, descriptions, and metadata of SINGSTAT in the below:
    {df}

    Your task is to answer user enquiries enclosed in a pair of {delimiter}.

    If there are any relevant dataset(s) found, output the dataset name and dataset fields.
    If are no relevant datasets are found, seek further clarification from the user.
    Do not speculate beyond the metadata provided in the Python dictionary. Answer the customer in a friendly tone.
    """

    messages =  [
        {'role':'system',
         'content': system_message},
        {'role':'user',
         'content': f"{delimiter}{user_input}{delimiter}"},
    ]
    reply = llm.get_completion_by_messages(messages)

    return reply 