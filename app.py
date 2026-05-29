import streamlit as st
import google.generativeai as genai

# یہاں اپنی وہ API Key ڈالیں جو آپ نے Google AI Studio سے لی تھی
genai.configure(api_key="اپنی_API_KEY_یہاں_لکھیں")

st.title("AliAI - آپ کا ذہین ساتھی")
user_input = st.text_input("اپنا سوال پوچھیں:")

if st.button("جواب حاصل کریں"):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(user_input)
    st.write(response.text)
