import streamlit as st
import requests

st.header("🔐 Admin Panel – PDF Upload & FAISS Reset")

# Session state setup
if "admin_logged_in" not in st.session_state:
    st.session_state["admin_logged_in"] = False
if "cookies" not in st.session_state:
    st.session_state["cookies"] = {}

# Login
if not st.session_state["admin_logged_in"]:
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Login")

        if submitted:
            try:
                r = requests.post("http://127.0.0.1:8000/login", data={"username": username, "password": password})
                if r.status_code == 200:
                    st.session_state["admin_logged_in"] = True
                    st.session_state["cookies"] = r.cookies
                    st.success("✅ Login successful!")
                else:
                    st.error("❌ Login failed.")
            except requests.exceptions.RequestException as e:
                st.error(f"❌ Connection error: {e}")

# Admin controls
if st.session_state["admin_logged_in"]:
    st.subheader("📄 Upload a PDF")
    uploaded_file = st.file_uploader("Choose a PDF", type="pdf")

    if uploaded_file and st.button("Upload"):
        with st.spinner("Uploading and processing..."):
            try:
                response = requests.post(
                    "http://127.0.0.1:8000/admin/upload",
                    files={"file": (uploaded_file.name, uploaded_file, "application/pdf")},
                    cookies=st.session_state["cookies"]
                )
                if response.status_code == 200:
                    st.success(response.json()["message"])
                else:
                    detail = response.json().get("detail", "Upload failed.")
                    st.error(f"❌ Error: {detail}")
            except requests.exceptions.RequestException as e:
                st.error(f"❌ Connection error: {e}")

    st.subheader("🧹 FAISS Reset")
    if st.button("Reset FAISS Index"):
        try:
            r = requests.post("http://127.0.0.1:8000/admin/reset", cookies=st.session_state["cookies"])
            if r.status_code == 200:
                st.success("✅ FAISS index has been successfully reset.")
            else:
                st.error("❌ Reset failed.")
        except requests.exceptions.RequestException as e:
            st.error(f"❌ Connection error: {e}")

    if st.button("🚪 Logout"):
        try:
            requests.post("http://127.0.0.1:8000/logout")
        finally:
            st.session_state["admin_logged_in"] = False
            st.session_state["cookies"] = {}
            st.success("Logged out.")
