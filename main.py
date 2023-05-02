import textrazor
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()
textrazor.api_key = os.getenv("TEXT_RAZOR_API_KEY")

client = textrazor.TextRazor(extractors=["entities", "topics"])

def make_output(text:str):
    response = client.analyze(text=text)
    df = pd.DataFrame()
    for entity in response.entities():
        output_dict = {"id":  "".join(list(entity.id or "None")), 
                       "type": "".join(list(entity.dbpedia_types or "None")), 
                       "wiki link": "".join(list(entity.wikipedia_link or "None"))}
        df2 = pd.DataFrame.from_records([output_dict])
        # df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        df = pd.concat([df, df2], ignore_index=True)
        # print(entity.id)
        df = df.drop_duplicates()
    return(df)

df_ = make_output("""Alice: Hi there, is this Bob?
Bob: Yes, speaking. Who's calling?
Alice: Hey Bob, it's Alice from Acme Inc. We met at the conference last month.
Bob: Oh, hey Alice! Good to hear from you. How can I help you today?
Alice: Well, I was just calling because I wanted to touch base with you about that project we discussed at the conference. I was hoping we could set up a meeting to talk about it in more detail.
Bob: Absolutely, I'd be happy to. When were you thinking?
Alice: How about next Tuesday at 10 am?
Bob: That works for me. Where should we meet?
Alice: We can meet at our office in downtown. Here's the address: 123 Main St. Suite 400.
Bob: Great. And just to confirm, your mobile number is still (555) 123-4567, right?
Alice: Yes, that's correct.
Bob: Perfect. I'll put the meeting in my calendar and send you a confirmation email with all the details.
Alice: Sounds good, thanks Bob. Looking forward to it!""")

print(df_)