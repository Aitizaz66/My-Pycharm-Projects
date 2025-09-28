import os

import chainlit as cl
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Use the latest supported Gemini model
model = genai.GenerativeModel("gemini-2.5-flash-lite")


@cl.on_message
async def on_message(message: cl.Message):
    try:
        response = model.generate_content(message.content)
        reply = response.text
    except Exception as e:
        reply = f"Error: {e}"

    await cl.Message(content=reply).send()
