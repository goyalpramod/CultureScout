import streamlit as st
import textrazor
from dotenv import load_dotenv
import os
import pandas as pd
import replicate
import plotly.express as px

load_dotenv()
REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")

# text_ = """Alice: Hi there, is this Bob?
# # Bob: Yes, speaking. Who's calling?
# # Alice: Hey Bob, it's Alice from Acme Inc. We met at the conference last month.
# # Bob: Oh, hey Alice! Good to hear from you. How can I help you today?
# # Alice: Well, I was just calling because I wanted to touch base with you about that project we discussed at the conference. I was hoping we could set up a meeting to talk about it in more detail.
# # Bob: Absolutely, I'd be happy to. When were you thinking?
# # Alice: How about next Tuesday at 10 am?
# # Bob: That works for me. Where should we meet?
# # Alice: We can meet at our office in downtown. Here's the address: 123 Main St. Suite 400.
# # Bob: Great. And just to confirm, your mobile number is still (555) 123-4567, right?
# # Alice: Yes, that's correct.
# # Bob: Perfect. I'll put the meeting in my calendar and send you a confirmation email with all the details.
# # Alice: Sounds good, thanks Bob. Looking forward to it!"""

replicate.Client(api_token=REPLICATE_API_TOKEN)

def make_summary(text_):
    output = replicate.run(
        "replicate/flan-t5-xl:7a216605843d87f5426a10d2cc6940485a232336ed04d655ef86b91e020e9210",
        input={"prompt": """Write the summary extract any useful information like name, number, and organization of the following conversation {text_to_summarize} """.format(text_to_summarize = text_)},
        max_length = 500,
        temperature = 0.7,
        top_p = 0.95,
        repetition_penalty = 1,
    )
    return " ".join(output)

load_dotenv()
textrazor.api_key = os.getenv("TEXT_RAZOR_API_KEY")

client = textrazor.TextRazor(extractors=["entities", "topics"])

def make_output(text:str):
    response = client.analyze(text=text)
    df = pd.DataFrame()
    for entity in response.entities():
        output_dict = {"id":  "".join(list(entity.id or "None")), 
                       "type": ", ".join(list(entity.dbpedia_types or "None")), 
                       "wiki link": "".join(list(entity.wikipedia_link or "None"))}
        df2 = pd.DataFrame.from_records([output_dict])
        # df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        df = pd.concat([df, df2], ignore_index=True)
        # print(entity.id)
        df1 = df.drop_duplicates()

    return(df)

st.title("CultureScout NLP Tool 🤖")

# taking user inputs for context search
st.write("***Enter Text You Need Help With:***")
user_input = st.text_area("Text Here:", "")

if st.button("Extract🪄"):
    def predict_sentiment(data:str):
        ans = make_output(user_input)
        return ans
    df = predict_sentiment(user_input)
    df = df.drop_duplicates()
    st.write("Context and Mentions")
    st.table(df)
    st.write("")

    id_df = predict_sentiment(user_input)['id']
    id_freq = id_df.value_counts()
    most_common_id = id_df.value_counts().index[0]

    type_df = predict_sentiment(user_input)['type']
    type_freq = type_df.value_counts(normalize=True)
    most_common_type = type_df.value_counts().index[0]

    p = px.pie(type_freq, values=type_freq.values, names=type_freq.index)
    # p.title('Object Frequencies')
    st.write("Analysis on id")
    st.bar_chart(id_freq)
    st.write("Analysis on type")
    st.plotly_chart(p)

    st.write(f"Most appeared id is {most_common_id}.")
    st.write(f"Most appeared type is {most_common_type}.")
    st.write("""
             """)
    st.write("*Summary of the input*")
    st.write(make_summary(user_input))
