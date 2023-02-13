import nltk 
from nltk.stem.lancaster import LancasterStemmer
stemmer= LancasterStemmer()

import numpy as np
import tflearn as t
import tensorflow as tf
import random 

import json
with open ('intents.json') as file:
    data= json.load(file)

words =[]
labels=[]
docks_x=[]
docks_y=[]

for intent in data['intents']:
    for patterns in intent['patterns']:
        wrds= nltk.word_tokenize(patterns)
        words.extend(wrds)
        docks_x.extend(wrds)
        docks_y.extend(intent["tag"])
    if intent['tag'] not in labels:
        labels.append(intent['tag'])

words= [stemmer.stem(w.lower())for w in words if w !="?"]
words= sorted(list(set(words)))

labels= sorted(labels)

training=[]
output=[]

out_empty=[0 for _ in range(len(labels))]

for x, doc in enumerate(docks_x):
    bag=[]
    
    wrds =[stemmer.stem(w.lower()) for w in doc]
    
    for w in words:
        if w  in wrds:
            bag.append(1)
        else:
            bag.append(0)
    
    output_row= out_empty[:]
    output_row[labels.index(docks_y[x])]=1
    
    training.append(bag)
    output.append(output_row)

training= np.array(training)
output= np.array(output)

tf.reset_default_graph()

net= t.input_data(shape=[None, len(training[0])])
net= t.fully_connected(net,8)
net= t.fully_connected(net,8)
net = t.fully_connected(net, len(output[0]), activation="softmax")
net = t.regression(net)

model= t.DNN(net)

model.fit(training,output,n_epoch=8000,batch_size=8,show_metric=True)
model.save("model.tflearn")

def bag_of_words(s,words): 
    bag =[0 for _ in range(len(words))] 
    s_words =nltk.word_tokenize(s) 
    s_words =[stemmer.stem(words.lower()) for words in s_words]
    for se in s_words:
        for i , w in enumerate(words):
            if w== se:
                bag[i]=1
    return np.array(bag)


def chat():
    
    while True:
        inp = input("you:")
        if inp.lower()=="quit" or inp.lower()=="salir":
            break
        frasecodificada=[bag_of_words(inp,words)] 
        result= model.predict(frasecodificada)
        result_index = np.argmax(result)
        tag =labels[result_index]
        for tg in data["intents"]:
            if tg['tag']==tag:
                responses=tg['responses']
        print(random.choice(responses))
chat()





