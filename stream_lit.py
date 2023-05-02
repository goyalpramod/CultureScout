import streamlit as st
from main import make_output
from summarization import make_summary


st.title("CultureScout NLP Tool 🤖")

# taking user inputs for context search
st.write("Enter Text You Need Help With:")
user_input = st.text_input("Text Here:", "")

if st.button("🔎 Search It!"):
    def predict_sentiment(data:str):
        ans = make_output(user_input)
        return ans
    st.table(predict_sentiment(user_input))

# taking user inputs for summarization
st.write("Enter Text You Need to Summarize:")
user_input1 = st.text_area("Text Here:", "")

if st.button("🪄 Summarize"):
    def summarize(data:str):
        ans1 = make_summary(user_input1)
        return ans1
    st.write(summarize(user_input1))