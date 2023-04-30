import textrazor
from dotenv import load_dotenv
import os

load_dotenv()
textrazor.api_key = os.getenv("TEXT_RAZOR_API_KEY")

client = textrazor.TextRazor(extractors=["entities", "topics"])
response = client.analyze_url("http://www.bbc.co.uk/news/uk-politics-18640916")

for entity in response.entities():
    print(entity.id, entity.relevance_score, entity.confidence_score, entity.freebase_types)