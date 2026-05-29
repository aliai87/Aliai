import streamlit as st
import google.generativeai as genai

# اپنی Google AI Studio API Key یہاں ڈالیں
genai.configure(api_key="import os
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])")

st.title("AliAI - Your Intelligent Companion")
user_input = st.text_input("Ask your question:")

if st.button("Get Answer"):
    if user_input:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(user_input)
        st.write(response.text)
    else:
        st.warning("Please enter a question first!")
