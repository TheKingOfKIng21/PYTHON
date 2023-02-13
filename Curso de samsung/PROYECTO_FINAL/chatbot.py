import nltk
from nltk.stem.lancaster import LancasterStemmer
import numpy as np
import tflearn 
import tensorflow as tf
import json
import pickle
import random
with open('intents.json') as intents:
    data = json.load(intents)

stemmer = LancasterStemmer()


words = []
labels = []
x_docs = []
y_docs = []

for intent in data['intents']:
    for pattern in intent['patterns']:
        wrds = nltk.word_tokenize(pattern)
        words.extend(wrds)
        x_docs.append(wrds)
        y_docs.append(intent['tag'])

        if intent['tag'] not in labels:
            labels.append(intent['tag'])

words = [stemmer.stem(w.lower()) for w in words if w not in "?"]
words = sorted(list(set(words)))
labels = sorted(labels)

training = []
output = []
out_empty = [0 for _ in range(len(labels))]

for x, doc in enumerate(x_docs):
    bag = []
    wrds = [stemmer.stem(w) for w in doc]
    for w in words:
        if w in wrds:
            bag.append(1)
        else:
            bag.append(0)



    output_row = out_empty[:]
    output_row[labels.index(y_docs[x])] = 1

    training.append(bag)
    output.append(output_row)


training = np.array(training)
output = np.array(output)


net = tflearn.input_data(shape=[None, len(training[0])])
net = tflearn.fully_connected(net, 16)
net = tflearn.fully_connected(net, 16)
net = tflearn.fully_connected(net, 16)
net = tflearn.fully_connected(net, len(output[0]), activation='softmax')
net = tflearn.regression(net)

model = tflearn.DNN(net)
model.fit(training, output, n_epoch=10000, batch_size=8, show_metric=True)
model.save('model.tflearn')


def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]
    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for s_word in s_words:
        for i, w in enumerate(words):
            if w == s_word:
                bag[i] = 1

    return np.array(bag)


def chat():
    print("The bot is ready to talk!!(Type 'quit' to exit)")
    while True:
        inp = input("\nYou: ")
        if inp.lower() == 'quit':
            break

        results = model.predict([bag_of_words(inp, words)])

        results_index = np.argmax(results)

        tag = labels[results_index]


        for tg in data['intents']:

            if tg['tag'] == tag:
                responses = tg['responses']
            print("Bot:" + random.choice(responses))


chat()