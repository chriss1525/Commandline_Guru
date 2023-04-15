import nltk 
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()
import numpy
# import tensorflow
# import tflearn
import random
import json

# 
with open("intents.json") as file:
    data = json.load(file)

Words = []
docs = []
labels = []

# loop through intents dictionary
for intent in data:
    for pattern in intent:
        # tokenize patterns
        twords = nltk.word_tokenize(pattern)
        Words.extend(twords)
        docs.append(pattern)

        if intent["tag"] not in labels:
            labels.append("intent")
