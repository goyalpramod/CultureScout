# CultureScout
This is a tool that provides context and summarization for input text. It is designed to make it easier to understand lengthy or complex texts by providing a brief summary and relevant context. By generating summaries and providing relevant context, the tool can help company employees and clients better understand and appreciate different cultures and perspectives.

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
Let's take this text which is an excerpt from a transcript of Barack Obama's Intervew:

"Michel Martin: So thank you for having us. Thank you for receiving us here at your office, which is amazing.  
Former President Barack Obama: It's wonderful to have you.  Have you developed any interesting COVID habits? Like some people are gardening. Mrs. Obama indicated she was learning to knit. Some of us who would kill any plant have somehow managed to manage a garden this year. Not talking about anybody in particular, just hypothetically. How about you? I have to say Michelle is not just starting to knit. She's become this extraordinary knitter, which, I told her the other day, it's kind of weird how good you've gotten at this thing. She's making sweaters and scarves and caps and —  OK. But what about you?  I cannot claim to have cultivated a new hobby, partly because I was busy finishing the book up until a couple of months ago. And then we had this campaign that I had to participate in a little more than I had anticipated. So, who knows? I may start up something."

Paste it onto the textbox:
![1](https://user-images.githubusercontent.com/92665963/236680454-c3b2262c-991f-435f-ad19-f38de1e9f97e.png)

Click on "Extract🪄"
## Sample Output
![2](https://user-images.githubusercontent.com/92665963/236680470-72c59103-21aa-4794-9a61-09ad16564e40.png)
![3](https://user-images.githubusercontent.com/92665963/236680473-1e2257d2-bc77-4d53-9b0b-c9d6c8d7cb7c.png)
![4](https://user-images.githubusercontent.com/92665963/236680475-76bb5d2e-9ea6-4d49-ba8b-04d1a945aed4.png)
