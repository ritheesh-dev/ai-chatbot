import streamlit as st
import requests

st.title("Local AI Chat")
prompt = st.text_input("Ask me anything:")

if st.button("Send"):
    if prompt:
        try:
            # Added a timeout in case the backend is down
            res = requests.post("http://localhost:8000/chat", params={"user_input": prompt}, timeout=120)
            if res.status_code == 200:
                st.write(res.json()['response'])
            else:
                st.error("Backend error. Please check if FastAPI is running.")
        except requests.exceptions.ConnectionError:
            st.error("Could not connect to the backend. Did you run 'uvicorn main:app'?")
    else:
        st.warning("Please enter a prompt.")    

