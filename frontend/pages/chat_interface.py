import streamlit as st
import requests

st.header("💬 Chat Interface")
st.markdown("Ask any question. GPT will respond using the uploaded internal documents.")

# Chat history
if "history" not in st.session_state:
    st.session_state["history"] = []

# Input box
question = st.chat_input("What would you like to ask?")

if question:
    with st.spinner("Getting your answer..."):
        try:
            response = requests.post(
                "http://127.0.0.1:8000/chat",
                json={"question": question}
            )
            if response.status_code == 200:
                answer = response.json()["answer"]
                st.session_state["history"].append((question, answer))
            else:
                st.error("❌ Failed to get a response from the backend.")
        except requests.exceptions.RequestException as e:
            st.error(f"❌ Connection error: {e}")

# Display chat history
for q, a in reversed(st.session_state["history"]):
    with st.chat_message("user"):
        st.markdown(q)
    with st.chat_message("assistant"):
        st.markdown(a)
