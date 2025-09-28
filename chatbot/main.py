import os

import chainlit as cl
import google.generativeai as genai
from dotenv import load_dotenv
from google.generativeai.types import Content, Part

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("❌ GOOGLE_API_KEY not found. Please set it in .env or environment.")

genai.configure(api_key=api_key)

MODEL_NAME = "gemini-2.5-flash"

SYSTEM_INSTRUCTION = (
    "You are a warm, empathetic, human-like assistant. "
    "Speak in a natural, friendly way, show positive emotions, and encourage the user."
)

model = genai.GenerativeModel(
    model_name=MODEL_NAME,
    system_instruction=SYSTEM_INSTRUCTION
)

history: list[Content] = []


@cl.on_message
async def on_message(message: cl.Message):
    global history

    user_content = Content(
        role="user",
        parts=[Part.from_text(message.content)]
    )
    history.append(user_content)

    try:
        response = model.generate_content(
            contents=history,
            generation_config={"max_output_tokens": 500}
        )

        if not response.candidates:
            reply = "I couldn't generate a response for that prompt."
        else:
            model_content = response.candidates[0].content
            model_content.role = "model"
            history.append(model_content)
            reply = response.text

    except Exception as e:
        reply = f"⚠️ An API Error occurred: {e}"

    await cl.Message(content=reply).send()


load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("❌ GOOGLE_API_KEY not found. Please set it in .env or environment.")

genai.configure(api_key=api_key)

MODEL_NAME = "gemini-2.5-flash"

SYSTEM_INSTRUCTION = (
    "You are a warm, empathetic, human-like assistant. "
    "Speak in a natural, friendly way, show positive emotions, and encourage the user."
)

model = genai.GenerativeModel(
    model_name=MODEL_NAME,
    system_instruction=SYSTEM_INSTRUCTION
)

history: list[Content] = []


@cl.on_message
async def on_message(message: cl.Message):
    global history

    user_content = Content(
        role="user",
        parts=[Part.from_text(message.content)]
    )
    history.append(user_content)

    try:
        response = model.generate_content(
            contents=history,
            generation_config={"max_output_tokens": 500}
        )

        if not response.candidates:
            reply = "I couldn't generate a response for that prompt."
        else:
            model_content = response.candidates[0].content
            model_content.role = "model"
            history.append(model_content)
            reply = response.text

    except Exception as e:
        reply = f"⚠️ An API Error occurred: {e}"

    await cl.Message(content=reply).send()
