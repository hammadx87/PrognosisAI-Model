import streamlit as st
import requests
import json

# 1. Page Configuration
st.set_page_config(page_title="PrognosisAI - Assistant", page_icon="🤖", layout="wide")

# 2. Custom CSS for Styling
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: white; }
    .stChatMessage { padding: 15px; border-radius: 10px; margin-bottom: 10px; }
    .stChatMessage.user { background-color: #262730; }
    .stChatMessage.assistant { background-color: #31333F; }
    .stTextInput { position: fixed; bottom: 30px; }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar Setup
with st.sidebar:
    st.title("🤖 PrognosisAI")
    st.subheader("Hammad's Personal Agent")
    st.markdown("---")
    st.success("🟢 Ollama System Status: Running (via Ngrok)")
    st.info("Model: qwen2.5-coder")

# 4. Header
st.markdown("# 🚀 PrognosisAI Chat Interface")
st.write("Hello Hammad! How can I help you today?")
st.markdown("---")

# 5. Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 6. Chat Input & Processing
if prompt := st.chat_input("Ask PrognosisAI..."):
    # User Message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Ollama API Request (Replace with your actual NGROK URL)
    ngrok_url = "https://randa-unapprehended-appeasably.ngrok-free.dev/api/generate" # <--- APNA NGROK LINK YAHAN DALEIN
    payload = {
        "model": "qwen2.5-coder",
        "prompt": prompt,
        "stream": False
    }

    with st.chat_message("assistant"):
        with st.spinner("PrognosisAI is thinking..."):
            try:
                response = requests.post(ngrok_url, json=payload)
                response.raise_for_status()
                response_data = response.json()
                answer = response_data.get("response", "Error: No response from model.")
                st.markdown(answer)
                st.session_state.messages.append({"role": "assistant", "content": answer})
            except Exception as e:
                st.error(f"Error: {e}")
