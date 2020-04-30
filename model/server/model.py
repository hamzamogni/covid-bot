import numpy
import requests
import json
import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

import os
import io
import string as s

class Net():
  def __init__(self, message):
    self.message = message

    if all((True if x in s.printable + "éèçàùäëüïö" else False for x in message)):
      self.lang = "latin"
    else:
      self.lang = "arabic"


  def bag_of_words(self, s, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1
            
    return numpy.array(bag)


  def main(self):
    if self.lang == "latin":
      data = json.load(io.open(os.getenv("JSON_LATIN"), 'r', encoding='utf-8-sig'))
    else:
      data = json.load(io.open(os.getenv("JSON_ARAB"), 'r', encoding='utf-8-sig'))

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

    input = self.bag_of_words(self.message, words)
    input = numpy.reshape(input, (1, input.shape[0]))
    my_data = json.dumps({"signature_name": "serving_default", "instances": input.tolist()})


    headers = {"content-type": "application/json"}
    if self.lang == "latin":
      json_response = requests.post(os.getenv("MODEL_LATIN_URL"), data=my_data, headers=headers)
    else:
      json_response = requests.post(os.getenv("MODEL_ARAB_URL"), data=my_data, headers=headers)
    

    results = json.loads(json_response.text)

    results = results["predictions"]
    results_index = numpy.argmax(results)
    tag = labels[results_index]

    if results[0][results_index] > 0.7:
      for tg in data["intents"]:
          if tg['tag'] == tag:
              responses = tg['responses']
      

      return json.dumps({
        "status": "success",
        "confidence": results[0][results_index],
        "messages": responses
        })
    else:
      return json.dumps({
        "status": "error",
        "messages": ["المعذرة لم استطع ان افهم سؤالك ، هل يمكنك إعادة صياغته"]
        })