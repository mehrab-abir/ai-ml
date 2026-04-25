import streamlit as st
from dotenv import load_dotenv
from google import genai
import os

load_dotenv()

st.header("LLM using Gemini API")
st.divider()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model = "gemini-3-flash-preview",
    contents = "tell me briefly about gravitational lensing"
)

st.markdown(response.text)
