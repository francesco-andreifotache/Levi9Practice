import streamlit as st
import ollama

st.set_page_config(
    page_title="Library Chatbot",
    page_icon="🤖"
)

st.title("🤖 Library Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

# afișează istoricul
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# input utilizator
prompt = st.chat_input("Ask me about books...")

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    response = ollama.chat(
        model="qwen3:4b",
        messages=st.session_state.messages
    )

    answer = response["message"]["content"]

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    with st.chat_message("assistant"):
        st.markdown(answer)