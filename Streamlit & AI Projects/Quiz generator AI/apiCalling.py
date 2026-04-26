from google import genai
from dotenv import load_dotenv
import os

load_dotenv();

apiKey = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=apiKey)

def note_generator(images):
    prompt = "summarize this note in no more than 100 words, add necessary markdown to format the text";
    
    response = client.models.generate_content(
        model = "gemini-3-flash-preview",
        contents=[images,prompt]
    )
    
    return response.text

def quiz_generator(images, difficultyLevel):
    prompt = f"make 5 quiz questions from the content of these images maintaining difficulty level {difficultyLevel}, among three options Easy, Medium, Hard";
    
    response = client.models.generate_content(
        model = "gemini-3-flash-preview",
        contents=[images,prompt]
    )
    
    return response.text
