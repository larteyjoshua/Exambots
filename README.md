# Building a Simple Exambot from Scratch in Python (using NLTK)

![Alt text](https://cdn-images-1.medium.com/max/800/1*pPcVfZ7i-gLMabUol3zezA.gif)

History of chatbots dates back to 1966 when a computer program called ELIZA was invented by Weizenbaum. It imitated the language of a psychotherapist from only 200 lines of code. You can still converse with it here: [Eliza](http://psych.fullerton.edu/mbirnbaum/psych101/Eliza.htm?utm_source=ubisend.com&utm_medium=blog-link&utm_campaign=ubisend). 

On similar lines let's create a very basic exambot utlising the Python's NLTK library.It's a very simple bot with hardly any cognitive skills,but still a good way to get into NLP and get to know about chatbots.


# Outline
* [Motivation](#motivation)
* [Pre-requisites](#pre-requisites)
* [How to run](#how-to-run)


## Motivation
The idea of this project was not to create some SOTA chatbot with exceptional cognitive skills but just to utilise and test my Python skills.This was one of my very first projects, created  when I just stepped into the world of NLP and I thought of creating a simple chatbot just to make use of my newly acquired knowledge.




## Pre-requisites
**NLTK(Natural Language Toolkit)**

[Natural Language Processing with Python](http://www.nltk.org/book/) provides a practical introduction to programming for language processing.

For platform-specific instructions, read [here](https://www.nltk.org/install.html)


### Installation of NLTK
```
pip install nltk
```
### Installing required packages
After NLTK has been downloaded, install required packages
```
import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('popular', quiet=True) # for downloading popular packages
nltk.download('punkt') 
nltk.download('wordnet') 
```


**Stremalit(Deployment tool)**

Streamlit is an open-source Python library that makes it easy to build beautiful apps for machine learning.

Install Streamlit, import it, write some code, and run your script. Streamlit watches for changes on each save and updates automatically, visualizing your output while you’re coding. Code runs from top to bottom, always from a clean state, and with no need for callbacks. It’s a simple and powerful app model that lets you build rich UIs incredibly quickly. 
For platform-specific instructions, read [here](https://docs.streamlit.io)


### Installation of streamlit
```
pip install streamlit
```
## How to run
To run any of the Exambot, 
1. Clone the project and 
2. Extract the files into a folder
3. Open the terminal or the cmd in the parent folder
4. cd into a particular topic folder 
5. Type "streamlit run 'topicName.py'" 
6. Ensure all require are downloaded. 
7. Enjoy the exambot as it run in the browser

```
