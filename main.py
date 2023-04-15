import nltk 
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()
import numpy
# import tensorflow
# import tflearn
import random
import json

with open("intents.json") as file:
    data = json.load(file)
print(data["intents"])