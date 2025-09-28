import os

import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI, OpenAIError

# Load environment variables
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    st.error("GROQ_API_KEY not found in .env file or Streamlit Secrets.")
    st.stop()

# Initialize Groq client (OpenAI-compatible)
client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)

MODEL_NAME = "llama-3.3-70b-versatile"  # change if needed

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! 😊 I'm your assistant. How can I help you today?"}
    ]

st.title("🤖 I Am Grok Chatbot")
st.markdown("Powered by Groq — with memory & emotions")

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Handle user input
if prompt := st.chat_input("Enter your message"):
    # Save user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    # Stream assistant response
    with st.chat_message("assistant"):
        response_container = st.empty()
        reply = ""
        try:
            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=[
                             {"role": "system",
                              "content": "You are a friendly, empathetic assistant. "
                                         "Respond warmly, with natural human-like emotions, encouragement, and enthusiasm."}
                         ] + st.session_state.messages,  # <-- Pass full history for memory
                max_tokens=500,
                stream=True
            )

            # Stream chunks to UI
            for chunk in response:
                if chunk.choices and chunk.choices[0].delta.content:
                    content = chunk.choices[0].delta.content
                    reply += content
                    response_container.write(reply)

        except OpenAIError as e:
            reply = f"API Error: {str(e)}"
            response_container.write(reply)
        except Exception as e:
            reply = f"Unexpected Error: {str(e)}"
            response_container.write(reply)

        # Save assistant reply
        st.session_state.messages.append({"role": "assistant", "content": reply})
