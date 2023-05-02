import replicate
from dotenv import load_dotenv
import os

load_dotenv()
REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")

text_ = """Alice: Hi there, is this Bob?
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
Alice: Sounds good, thanks Bob. Looking forward to it!"""

replicate.Client(api_token=REPLICATE_API_TOKEN)
output = replicate.run(
    "replicate/flan-t5-xl:7a216605843d87f5426a10d2cc6940485a232336ed04d655ef86b91e020e9210",
    input={"prompt": """Write the summary extract any useful information like name, number, and organization of the following conversation {text_to_summarize} """.format(text_to_summarize = text_)},
    max_length = 500,
    temperature = 0.7,
    top_p = 0.95,
    repetition_penalty = 1,
)
# The replicate/flan-t5-xl model can stream output as it's running.
# The predict method returns an iterator, and you can iterate over that output.
for item in output:
    # https://replicate.com/replicate/flan-t5-xl/versions/7a216605843d87f5426a10d2cc6940485a232336ed04d655ef86b91e020e9210/api#output-schema
    print(item)