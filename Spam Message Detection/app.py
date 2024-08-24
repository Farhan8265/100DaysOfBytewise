import streamlit as st
import pickle
import string
import numpy as np
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import requests
from io import BytesIO

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')

ps = PorterStemmer()

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

# Load TF-IDF Vectorizer from your GitHub repository
vectorizer_url = "https://github.com/Farhan8265/100DaysOfBytewise/raw/main/vectorizer.pkl"
response = requests.get(vectorizer_url)
vectorizer = pickle.load(BytesIO(response.content))

# Load Model from your GitHub repository
model_url = "https://github.com/Farhan8265/100DaysOfBytewise/raw/main/model.pkl"
response = requests.get(model_url)
model = pickle.load(BytesIO(response.content))

st.title("Spam Message Detection")
input_msg = st.text_input("Enter the message: ")

if st.button('Predict'):
    # Preprocessing
    transform_msg = transform_text(input_msg)

    # Vectorization
    vector_input = vectorizer.transform([transform_msg])

    # Prediction
    result = model.predict(vector_input)[0]

    # Display Result
    if result == 1:
        st.header("It's a Spam Message")
    else:
        st.header("It's Not a Spam Message")
