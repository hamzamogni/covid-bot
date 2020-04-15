import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

import numpy
import tflearn
import tensorflow as tf
from tensorflow import keras
import random
import json
import pickle

import nltk


####
# FIRST CELL
####

with open("dataar.json", encoding = "utf-8") as file:
    data = json.load(file)


words = []
labels = []
docs_x = []
docs_y = []

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        wrds = nltk.word_tokenize(pattern)
        words.extend(wrds)
        docs_x.append(wrds)
        docs_y.append(intent["tag"])

    if intent["tag"] not in labels:
        labels.append(intent["tag"])

words = [stemmer.stem(w.lower()) for w in words if w != "?"]
words = sorted(list(set(words)))

labels = sorted(labels)

training = []
output = []

out_empty = [0 for _ in range(len(labels))]

for x, doc in enumerate(docs_x):
    bag = []

    wrds = [stemmer.stem(w.lower()) for w in doc]

    for w in words:
        if w in wrds:
            bag.append(1)
        else:
            bag.append(0)

    output_row = out_empty[:]
    output_row[labels.index(docs_y[x])] = 1

    training.append(bag)
    output.append(output_row)


training = numpy.array(training)
output = numpy.array(output)

####
# SECOND CELL
####

model = keras.Sequential([
    tf.keras.layers.Dense(8, input_shape=(len(training[0]),)),
    tf.keras.layers.Dense(8),
    tf.keras.layers.Dense(len(output[0]), activation="softmax")
])

model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])
model.fit(training, output, epochs=100, batch_size=8)
model.summary()

import os

#MODEL_DIR = tempfile.gettempdir()
#version = 1
export_path = "saved_model" #os.path.join(MODEL_DIR, str(version))
#print('export_path = {}\n'.format(export_path))

tf.saved_model.save(
    model,
    export_path,
    signatures=None,
)

####
# THIRD CELL
####

def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1
            
    return numpy.array(bag)


def chat():
    print("Start talking with the bot (type quit to stop)!")
    while True:
        inp = input("You: ")
        if inp.lower() == "quit":
            break

        my_data = bag_of_words(inp, words)
        my_data = numpy.reshape(my_data, (1, my_data.shape[0]))

        results = model.predict(my_data) 
        results_index = numpy.argmax(results)
        tag = labels[results_index]

        if results[0][results_index] > 0.7:
          for tg in data["intents"]:
              if tg['tag'] == tag:
                  responses = tg['responses']
          print(random.choice(responses), results[0][results_index])
          #print(results)
        else:
          print("I didn't get your idea!!! Try again...")
