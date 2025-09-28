import os

import chainlit as cl
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Use the Gemini model with system instruction for friendliness
model = genai.GenerativeModel(
    "gemini-2.5-flash-lite",
    system_instruction=(
        "You are a warm, friendly, empathetic assistant. "
        "Speak in a natural, conversational way, use positive emotions, "
        "and encourage the user. Respond like a supportive human friend."
    )
)


@cl.on_message
async def on_message(message: cl.Message):
    try:
        response = model.generate_content(message.content)
        reply = response.text
    except Exception as e:
        reply = f"⚠️ Error: {e}"

    await cl.Message(content=reply).send()
