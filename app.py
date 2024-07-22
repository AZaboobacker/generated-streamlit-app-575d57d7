# Required Libraries
import streamlit as st
import openai
import requests
from streamlit_ace import st_ace

# Application header
st.title('Indoor Tennis Court Finder')

# Application text
st.write("This application helps you find indoor tennis courts near your location. For a more precise search, please enter your own OpenAI API key.")

# API Key input
api_key = st.text_input("OpenAI API Key", "Enter Key")

# Create request to OpenAI API
def get_tennis_courts(api_key):
    openai.api_key = api_key
    response = openai.chat.completions.create(
        model='gpt-3', 
        messages=[
            {'role': 'system', 'content': 'You are a helpful assistant.'}, 
            {'role': 'user', 'content': 'Find indoor tennis courts near me'}
        ]
    )
    message_content = response.choices[0].message['content'].strip()
    return message_content

with st.spinner('Finding indoor tennis courts near you...'):
    try: 
        courts = get_tennis_courts(api_key)
        st.success("Found tennis courts: {}".format(courts))

    except:
        st.error("An error occurred. Please check your OpenAI API key.")
    

# CSS Addition for Modern Look
st.markdown(
    """
    <style>
    .reportview-container {
        flex-direction: column;
        background: #4B6A9B;
    }
    .element-container {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-grow: 1
    }
    .block-container {
        display: flex;
        justify-content: space-around;
        align-items: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)