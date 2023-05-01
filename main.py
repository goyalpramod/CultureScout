import textrazor
from dotenv import load_dotenv
import os

load_dotenv()
textrazor.api_key = os.getenv("TEXT_RAZOR_API_KEY")

client = textrazor.TextRazor(extractors=["entities", "topics"])

def get_entities(text:str):
    try:
        response = client.analyze(text=text)
        return response
    # TODO: when exception occurs issue occurs in process_output
    except textrazor.TextRazorAnalysisException as ex:
        return ex

def process_output(response:textrazor.Entity or textrazor.TextRazorAnalysisException):
    if type(response) == textrazor.TextRazorAnalysisException:
        print("Failed to analyze with error:{exception}").format(exception=textrazor.TextRazorAnalysisException)
        return
    for entity in response.entities():
        # print(entity.id, entity.dbpedia_types, entity.wikipedia_link)
        yield entity.dbpedia_types

ans = list(process_output(get_entities("Facebook")))
print(ans)
# for entity in response.entities():
#     print(entity.id, entity.relevance_score, entity.confidence_score, entity.freebase_types)