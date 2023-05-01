import streamlit as st
from main import process_output, get_entities
import json
import requests

st.title("CultureScout NLP Tool 🤖")

# taking user inputs
st.write("Enter Text You Need Help With:")
user_input = st.text_input("Text Here:", "")

if st.button("🎯"):
    def predict_sentiment(data:str):
        ans = list(process_output(get_entities(user_input)))
        return ans
    st.write(predict_sentiment(user_input))