import uvicorn
from fastapi import FastAPI
from inputText import InputText


app = FastAPI(title="A conversation analysis API",
    description="An API which takes in a text from the user and responds .")


@app.get('/')
def index():
    return {'message':'Hello World!'}

@app.post('/predict')
def predict_sentiment(data:InputText):
    pass


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)