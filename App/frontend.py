import streamlit as st
import requests

st.title("Local AI Chat")
prompt = st.text_input("Ask me anything:")

if st.button("Send"):
    res = requests.post("http://localhost:8000/chat", params={"user_input": prompt})
    st.write(res.json()['response'])