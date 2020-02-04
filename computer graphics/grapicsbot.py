import streamlit as st
import io
import random
import string # to process standard python strings
import warnings
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings
warnings.filterwarnings('ignore')

import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('popular', quiet=True) # for downloading packages
#nltk.download('punkt') # first-time use only
#nltk.download('wordnet') # first-time use only
st.title("EXAMINATION BOT")
st.header("Artificial Intelligence chatbot to help you learn for examination")

def chatty():
    f=open('graphics.txt','r',errors = 'ignore')
    raw=f.read()
    raw = raw# converts to lowercase
    sent_tokens = nltk.sent_tokenize(raw)# converts to list of sentences 
    word_tokens = nltk.word_tokenize(raw)# converts to list of words

    lemmer = nltk.stem.WordNetLemmatizer()
    #WordNet is a semantically-oriented dictionary of English included in NLTK.
    def LemTokens(tokens):
        return [lemmer.lemmatize(token) for token in tokens]
    remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

    def LemNormalize(text):
        return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

    GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey", "ok",)
    GREETING_RESPONSES = ["hi", "hey", "cool", "hi there", "hello", "I am glad! You are talking to me", "alright"]
    def greeting(sentence):
    
        for word in sentence.split():
            if word.lower() in GREETING_INPUTS:
                return random.choice(GREETING_RESPONSES)


    def response(user_response):
        robo_response=''
        sent_tokens.append(user_response)
        TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
        tfidf = TfidfVec.fit_transform(sent_tokens)
        vals = cosine_similarity(tfidf[-1], tfidf)
        idx=vals.argsort()[0][-2]
        flat = vals.flatten()
        flat.sort()
        req_tfidf = flat[-2]
        if(req_tfidf==0):
            robo_response=robo_response+"I am sorry! I don't understand you"
            st.info(robo_response )
            return robo_response
        else:
            robo_response = robo_response+sent_tokens[idx]
            st.info(robo_response )
            return robo_response 

    flag=True
    print("ROBO: My name is Robo. I will answer your queries about Artificial Intelligence. If you want to exit, type Bye!")
    st.info("ROBO: My name is Robo. I will answer your queries about Artificial Intelligence. If you want to exit, type Bye!")
    while(flag==True):
        word=st.sidebar.text_input("USER", "Hello", key=None)
        user_response = word
        st.success(word)
        user_response=user_response.lower()
        if(user_response!='bye'):
            if(user_response=='thanks' or user_response=='thank you' ):
                flag=False
                print("ROBO: You are welcome..")
                st.info("ROBO: You are welcome..")
            else:
                if(greeting(user_response)!=None):
                    print("ROBO: "+greeting(user_response))
                    st.info("ROBO: "+greeting(user_response))
                else:
                    print("ROBO: ",end="")
                    print(response(user_response))
                    sent_tokens.remove(user_response)
        else:
            flag=False
            print("ROBO: Bye! take care..")
            st.info("ROBO: Bye! take care..")
if __name__ == "__main__":
    chatty()
