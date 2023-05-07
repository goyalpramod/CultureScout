# CultureScout
This is a tool that provides context and summarization for input text. It is designed to make it easier to understand lengthy or complex texts by providing a brief summary and relevant context.

As context it provides the most accurate term for each important entity in the text and also provides wikipedia link for each (if available).

We have used Textrazor API to analyse the input text and find context and wikipedia links. Also, pandas, numpy, plotly and matplotlib.pyplot has been used for analytics.
We have used Replicate API to summarise the input text and gives a 3-4 liner body of text mentioning the overall information in the input text

## Installation
To use the tool, you need to have Python 3 installed on your machine. Clone the repository and navigate to the project directory in the terminal. Then, install the required packages by running:
```
pip install -r requirements.txt
```
## Usage
To use the tool, initalise terminal and pass on:
```
streamlit run app.py
```
This opens the browser with streamlit app running on your local system. If you want to check it online, hop on to this [LINK](https://goyalpramod-culturescout-app-7wqkwe.streamlit.app/)

## Sample Usage
Let's take this text which is an excerpt from Tim Cook's Keynote speech from Global Privacy Summit:
```
Cook reflected on Apple's ongoing commitment to privacy, which the company has repeatedly described as a fundamental human right.

"The fight to protect privacy is not an easy one, but it is one of the most essential battles of our time," said Cook. "We at Apple are proud to stand alongside all those who are working to advance privacy rights around the world. As a company, we are profoundly inspired by what technology can make possible, but we know too that technology is neither inherently good, nor inherently bad. It is what we make of it. It is a mirror that reflects the ambitions of the people who use it, the people who build it, and the people who regulate it."
```
Paste it onto the textbox:

Click on "Extract🪄"

## Sample Output
