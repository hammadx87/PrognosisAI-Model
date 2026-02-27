import streamlit as st
from groq import Groq

# 1. Page Configuration - Pro Look
st.set_page_config(
    page_title="PrognosisAI Backend", 
    page_icon="🤖", 
    layout="centered"
)

# 2. Header for Public Viewing
st.title("🤖 PrognosisAI Agent")
st.subheader("Official Personal Agent Backend")
st.markdown("---")

# 3. Sidebar - API Key Input (Testing Purpose)
with st.sidebar:
    st.header("Settings")
    api_key = st.text_input("Enter Groq API Key", type="password")
    st.info("PrognosisAI is running on Llama3 Cloud API.")

if api_key:
    # Initialize Groq Client
    client = Groq(api_key=api_key)
    
    # 4. Personality/Agent Persona Setup
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {
                "role": "system",
                "content": "You are PrognosisAI, the official personal agent for Hammad. You are intelligent, polite, and efficient. Always address the user as Hammad and maintain a professional yet friendly tone."
            }
        ]

    # 5. Display Chat History
    for message in st.session_state.messages:
        if message["role"] != "system":
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    # 6. User Input
    if prompt := st.chat_input("Ask PrognosisAI..."):
        # Add user message to history
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # 7. AI Response
        with st.chat_message("assistant"):
            with st.spinner("PrognosisAI is thinking..."):
                try:
                    chat_completion = client.chat.completions.create(
    messages=st.session_state.messages,
    model="llama3-8b-85b-api-host-v1", # <--- YA KOI BHI NAYA ACTIVE MODEL NAME
    temperature=0.5,
                    )
                    
                    response = chat_completion.choices[0].message.content
                    st.markdown(response)
                    st.session_state.messages.append({"role": "assistant", "content": response})
                except Exception as e:
                    st.error(f"Error: {e}")
else:
    st.warning("⚠️ Please enter your Groq API Key in the sidebar to activate the agent.")

