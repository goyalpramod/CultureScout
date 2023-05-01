import json
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

def process_output(response:textrazor.TextRazorResponse or textrazor.TextRazorAnalysisException):
    if type(response) == textrazor.TextRazorAnalysisException:
        print("Failed to analyze with error:{exception}").format(exception=textrazor.TextRazorAnalysisException)
        return
    for entity in response.entities():
        yield(entity.id, entity.dbpedia_types, entity.wikipedia_link)
        output_dict = {"id": entity.id, 
                       "type": entity.dbpedia_types, 
                       "wiki link": entity.wikipedia_link}
        # return output_dict
        json_object = json.dumps(output_dict, indent=4)
        return(json_object)

# process_output(get_entities("Instagram"))

# st.json(process_output(get_entities(input)))

# st.dataframe(out_dict)
# print(ans)
# for entity in response.entities():
#     print(entity.id, entity.relevance_score, entity.confidence_score, entity.freebase_types)