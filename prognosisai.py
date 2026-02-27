import streamlit as st
import requests

# Website ka Title
st.set_page_config(page_title="PrognosisAI", page_icon="🤖")
st.title("🤖 PrognosisAI")
st.caption("Developed by Hammad x Code")

# Chat History Initialize karna
if "messages" not in st.session_state:
    st.session_state.messages = []

# Purani chat dikhana
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User ka sawal lena
if prompt := st.chat_input("Ask PrognosisAI "):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # AI ka jawab nikalna (Ollama se raabta)
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""

        url = "https://randa-unapprehended-appeasably.ngrok-free.dev/api/generate"
        data = {
            "model": "prognosisAI",
            "prompt": prompt,
            "stream": False
        }

        try:
            response = requests.post(url, json=data)
            full_response = response.json()['response']
            response_placeholder.markdown(full_response)
        except:
            full_response = "Sorry, Ollama se connect nahi ho pa raha."
            response_placeholder.markdown(full_response)


    st.session_state.messages.append({"role": "assistant", "content": full_response})
