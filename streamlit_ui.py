import streamlit as st
import requests
import uuid

API_BASE = "http://127.0.0.1:8000"

st.title("Chatbot Framework Dashboard")

page = st.sidebar.selectbox("Choose Page", ["Chatbot", "Admin", "Contact"])

if "session_id" not in st.session_state:
    st.session_state["session_id"] = str(uuid.uuid4())

if page == "Chatbot":
    st.header("User Chatbot")
    msg = st.text_input("You:")
    if st.button("Send"):
        res = requests.post(f"{API_BASE}/user/chat", json={
            "session_id": st.session_state["session_id"],
            "message": msg
        })
        st.json(res.json())

elif page == "Admin":
    st.header("All Conversations")
    res = requests.get(f"{API_BASE}/admin/conversations")
    st.json(res.json())

elif page == "Contact":
    st.header("Contact Form")
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")
    if st.button("Submit"):
        res = requests.post(f"{API_BASE}/contact", json={
            "name": name, "email": email, "message": message
        })
        st.json(res.json())