import streamlit as st
import time
from dotenv import load_dotenv
from google import genai
import os

load_dotenv()

st.header("LLM using Gemini API")
st.divider()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

prompt = st.text_input("Ask something")

def stream_text(text):
    for word in text.split(" "):
        yield word + " "
        time.sleep(0.05)

if prompt: 
    response = client.models.generate_content(
        model = "gemini-3-flash-preview",
        contents = prompt
    )

    st.write_stream(stream_text(response.text))
