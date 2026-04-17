from google import genai
from dotenv import load_dotenv
from gtts import gTTS
import os, io


#loading enviornment
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

# client inintialize

client = genai.Client(api_key=api_key)


## note generator

def notes_generator(images):
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[images,"Summerize the pictures and make a note in 100 words, add proper markdown and emojis to make it more attractive"],
    )
    return response.text
## text cleaner 
import re

def clean_text(text):
    text = re.sub(r'\*\*|__|\*|_|`|#{1,6}|---|>', '', text)
    text = re.sub(r'[^\x00-\x7F]+', '', text)
    text = re.sub(r'\n+', ' ', text)
    text = re.sub(r' +', ' ', text)
    
    return text.strip()

## audio generator
def audio_generator(text):
    speech = gTTS(text,lang="en",slow=False)
    audio_buffer = io.BytesIO()
    speech.write_to_fp(audio_buffer)
    return audio_buffer

## quiz generator
def quiz_generator(images, difficulty):
    prompt = f"Generate a quiz with 3 questions based on the above images. The quiz should be of {difficulty} level.USe proper markdown. keep 4 answers to choose from and in the end mention the correct answer."
    
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[images,prompt],
    )
    return response.text

