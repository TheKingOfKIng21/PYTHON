import tkinter
from tkinter import *
import nltk
from nltk.stem.lancaster import LancasterStemmer 
import tensorflow
import tflearn
import random 
import numpy
import pickle 
import json

stemmer=LancasterStemmer()


base = Tk()
base.title("Chatbot")
base.geometry("400x500")

def bag_of_words(s, words): 
    bag = [0 for _ in range(len(words))]
    
    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]
    
    for se in  s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i]=1
                
    return numpy.array(bag)


def chatbot_response(msg):
    
    with open("intents.json") as file:
        data = json.load(file)

    try:
        with open("data.pickle", "rb") as f:
            words, labels, training, output = pickle.load(f)
        model.load("model.tflearn")
    except:
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

        with open("data.pickle", "wb") as f:
            pickle.dump((words, labels, training, output), f)

    tensorflow.compat.v1.reset_default_graph()

    net = tflearn.input_data(shape=[None, len(training[0])])
    net = tflearn.fully_connected(net, 8)
    net = tflearn.fully_connected(net, 8)
    net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
    net = tflearn.regression(net)
    model = tflearn.DNN(net)
    try:
        model.load("model.tflearn")
    except:
        model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)
        model.save("model.tflearn")
        
        results = model.predict([bag_of_words(msg, words)])
        results_index = numpy.argmax(results)
        tag = labels[results_index]
        for tg in data["intents"]:
            if tg['tag'] == tag:
                responses = tg['responses']
        return (random.choice(responses))

def send():
    msg=EntryBox.get("1.0", 'end-1c').strip()
    EntryBox.delete("0.0", END)
    
    res=chatbot_response(msg) 
    
    if msg != '':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "You: "+msg+'\n\n')
        ChatLog.config(foreground="black", font=("Verdana",12))
        ChatLog.insert(END, "ChatBOT:" +res+'\n\n')
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)        

base.resizable(width=FALSE, height=FALSE)

ChatLog = Text(base, bd=0, bg="white", height="8", width="50", font="Arial")
ChatLog.config(foreground="black", font=("Verdana", 12))

ChatLog.insert(END, "SALUDOS BIENVENIDO"+'\n\n')
ChatLog.place(x=6, y=6, height=386, width=370)

scrollbar = Scrollbar(base, command=ChatLog.yview, cursor = "heart")
ChatLog['yscrollcommand']=scrollbar.set
scrollbar.place(x=376, y=6, height=386)
ChatLog.config(state=DISABLED)

EntryBox=Text(base, bd=0, bg="white", width="29", height="5", font="Arial")
EntryBox.place(x=6, y=401, height=90, width=265)

SendButton = Button(base, font=("Verdana", 12, 'bold'), text="Send", width="9",
                    height=5, bd=0, bg="blue", activebackground="gold", 
                    fg='#ffffff', command=send)
SendButton.place(x=282, y=401, height=90)

base.bind('<Return>', lambda event:send())
base.mainloop()

