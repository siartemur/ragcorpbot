import streamlit as st

st.set_page_config(page_title="RAGCorpBot", layout="wide")

st.title("🤖 RAGCorpBot – Corporate Knowledge Assistant")
st.markdown("This application uses GPT to answer questions based on internal PDF documents.")

st.divider()
st.info("👉 Use the sidebar to select a module: **Chat Interface** or **Admin Panel**.")
