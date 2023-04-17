import json
import random
import numpy
import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

import tensorflow
import tflearn

# access .json file
with open("intents.json") as file:
    data = json.load(file)
print(data)

words = []
docs_1 = []
docs_2 = []
labels = []

# loop through intents dictionary
for intent in data:
    for pattern in intent:
        # break strings to tokenized words
        twords = nltk.word_tokenize(pattern)
        # add tokenized words to words list
        words.extend(twords)
        # add tokenized words to docs_1
        docs_1.append(twords)
        # add tags to docs_2
        docs_2.append(intent["tag"])

        # make sure tags appear only once in labels
        if intent["tag"] not in labels:
            labels.append("intent")

# stem words and remove question mark token
words = [stemmer.stem(w.lower()) for w in words if w not in '?']
# create sets of stemmed words, return sets to lists, then sort the lists
words = sorted(list(set(words)))
# sort labels list
labels = sorted(labels)

# initialize an empty list to store training data
training = []

# initialize an empty list to store output data
output = []

# create a list of zeros with length equal to the number of unique labels in the dataset
out_empty = [0 for _ in range(len(labels))]

# iterate over the list of preprocessed documents (docs_1)
for x, doc in enumerate(docs_1):
    # initialize an empty list to represent the bag of words for this document
    bag = []

    # stem each word in the document 
    twords = [stemmer.stem(w) for w in doc]

    # iterate over the list of unique words (words) in the dataset
    for w in words:
        # if the stemmed version of the word is present in the document
        if w in twords:
            # append 1 to the bag to indicate the presence of the word in the document
            bag.append(1)
        else:
            # append 0 to the bag to indicate the absence of the word in the document
            bag.append(0)

    # create a one-hot encoded output row for this document
    output_row = out_empty[:]
    # set the index corresponding to the correct label for this document to 1
    output_row[labels.index(docs_2[x])] = 1

    # append the bag of words for this document to the training data list
    training.append(bag)
    # append the one-hot encoded output row for this document to the output data list
    output.append(output_row)


training = numpy.array(training)
output = numpy.array(output)
