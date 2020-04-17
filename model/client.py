# -*-coding: utf-8 -*-

import sys
import numpy
import requests
import json
import random
import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()


def gen_words_labels(data):
  pass

  return words, labels


def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1
            
    return numpy.array(bag)



message = sys.argv[1]

# with open("/srv/http/cobot/ml/dataar.json", encoding = "utf-8") as file:
#     data = json.load(file)

import io
data = json.load(io.open('/srv/http/cobot/ml/dataar.json', 'r', encoding='utf-8-sig'))

words = []
labels = []

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        wrds = nltk.word_tokenize(pattern)

        words.extend(wrds)


    if intent["tag"] not in labels:
        labels.append(intent["tag"])

words = [stemmer.stem(w.lower()) for w in words if w != "?"]
words = sorted(list(set(words)))
labels = sorted(labels)

input = bag_of_words(message, words)
input = numpy.reshape(input, (1, input.shape[0]))
my_data = json.dumps({"signature_name": "serving_default", "instances": input.tolist()})


headers = {"content-type": "application/json"}
json_response = requests.post('http://35.211.212.220:5000/v1/models/cobot:predict', data=my_data, headers=headers)

results = json.loads(json_response.text)

results = results["predictions"]
results_index = numpy.argmax(results)
tag = labels[results_index]

if results[0][results_index] > 0.7:
  for tg in data["intents"]:
      if tg['tag'] == tag:
          responses = tg['responses']
  
  
  ret = json.dumps({
    "status": "success",
    "prediction": results[0][results_index],
    "confidence": random.choice(responses)
    })
  print(ret)
else:
  ret = json.dumps({
    "status": "error",
    "message": "sorry I couldn't get what you mean!"
    })
  print(ret)
