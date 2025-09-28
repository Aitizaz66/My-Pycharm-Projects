import os

import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI, OpenAIError

# Load environment variables
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    st.error("GROQ_API_KEY not found in .env file.")
    st.stop()

client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)

MODEL_NAME = "llama-3.3-70b-versatile"

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I'm your assistant. How can I help you today?"}
    ]

st.title("I Am Grok Chatbot")
st.markdown("Powered by Groq")

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Handle user input
if prompt := st.chat_input("Enter your message"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    if not prompt.strip():
        response = "Error: Empty input received."
        st.session_state.messages.append({"role": "assistant", "content": response})
        with st.chat_message("assistant"):
            st.write(response)
    else:
        # Stream response
        with st.chat_message("assistant"):
            response_container = st.empty()
            reply = ""
            try:
                response = client.chat.completions.create(
                    model=MODEL_NAME,
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": prompt}
                    ],
                    max_tokens=1000,
                    stream=True
                )
                for chunk in response:
                    content = chunk.choices[0].delta.content if chunk.choices and chunk.choices[0].delta.content else ""
                    reply += content
                    response_container.write(reply)
            except OpenAIError as e:
                reply = f"API Error: {str(e)}"
                response_container.write(reply)
            except Exception as e:
                reply = f"Unexpected Error: {str(e)}"
                response_container.write(reply)
            st.session_state.messages.append({"role": "assistant", "content": reply})
