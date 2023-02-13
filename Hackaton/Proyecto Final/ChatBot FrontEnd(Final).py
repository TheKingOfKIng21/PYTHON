import tkinter
from tkinter import *
import nltk
from nltk.stem.lancaster import LancasterStemmer
import tensorflow
import tflearn
import random
import numpy as np
import pickle

stemmer = LancasterStemmer()


def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]
    s_words = nltk.word_tokenize(s)  # Convierto la frase ingresada por el usuario en palabras
    s_words = [stemmer.stem(word.lower()) for word in s_words]
    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1

    return np.array(bag)

def chatbot_response(msg):
    import json
    with open('pintents.json') as file:
        data = json.load(file)

    try:
        with open("data.pickle", "rb") as f:
            words, labels, training, output, data = pickle.load(f)

        with open('pintents.json') as file:
            data2 = json.load(file)

        if data != data2:
            raise Exception("El Archivo json ha cambiado")
        model.load("newmodel.tflearn")

    except:
        print("Estoy dentro del EXCEPT")

        words = []  # Palabras sin deferenciar la frase a la que pertenecen
        labels = []  # Titulos, legendas.
        docs_x = []
        docs_y = []

        for intents in data['intents']:
            for patterns in intents['patterns']:
                wrds = nltk.word_tokenize(patterns)  # Convierte una frase a un conjunto de palabras
                words.extend(wrds)
                docs_x.append(wrds)
                docs_y.append(intents["tag"])

                if intents['tag'] not in labels:
                    labels.append(intents['tag'])

        words = [stemmer.stem(w.lower()) for w in words if w != "?"]

        words = sorted(list(set(words)))  # Organizando el conjunto de paralabras de forma no repetiva y ordenada.

        labels = sorted(labels)

        training = []
        output = []

        out_empty = [0 for _ in range(len(labels))]

        # Este ciclo for se encarga de analizar todas y cada una de las palabras en todas y cada una de las frases

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

        training = np.array(
            training)  # Contiene la informacion preparada con la cual se va a alimentar el sistema referentes a las palabras
        output = np.array(
            output)  # Contiene la informacion preparada con la cual se va a alimentar el sistema referente a la categorizacion

        with open("data.pickle", "wb") as f:
            pickle.dump((words, labels, training, output, data), f)

        tensorflow.compat.v1.reset_default_graph()
        net = tflearn.input_data(shape=[None, len(training[0])])
        net = tflearn.fully_connected(net, 8)
        net = tflearn.fully_connected(net, 8)

        net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
        net = tflearn.regression(net)

        model = tflearn.DNN(net)

        try:
            model.load("newmodel.tflearn")
        except:
            model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)
            model.save("newmodel.tflearn")

        results = model.predict([bag_of_words(msg, words)])
        results_index = np.argmax(results)  # La funcion argmax obtiene la probabilidad mas alta.

        tag = labels[results_index]

        for tg in data["intents"]:
            if tg['tag'] == tag:
                responses = tg['responses']

        return (random.choice(responses))


def send():
    msg = EntryBox.get("1.0", 'end-1c').strip()
    print("mensaje captado: ", EntryBox.get("1.0", "end-1c"))

    print("\nborrando....")
    EntryBox.delete("0.0", END)
    print("mensaje borrado: ", EntryBox.get("1.0", "end-1c"))

    res = chatbot_response(msg)

    if msg != "":
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "You: " + msg + " \n\n")
        ChatLog.config(foreground="black", font=("Verdana", 12))
        ChatLog.insert(END, "ChatBot: " + res + " \n\n")
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)

base = Tk()

base.title("Chatbot (Atención al usuario)")
base.geometry("400x500")
base.config(bg="navajo white")
base.resizable(width=FALSE, height=FALSE)  # Mantiene fija la ventana.

ChatLog = Text(base, bd=0, bg="white", width=8, height="50", font="Arial")
ChatLog.config(foreground="Black", font=("Verdana", 12) )  # foreground cambia el color de la letra
ChatLog.insert(END, "Bienvenido\n\n")
ChatLog.place(x=6, y=6, height=386, width=370)
ChatLog.config(state=DISABLED)  # bloquea la entrada de texto(lo hace de solo lectura)

scrollbar = Scrollbar(base, command=ChatLog.yview(), cursor="heart")
ChatLog['yscrollcommand'] = scrollbar.set
scrollbar.place(x=376, y=6, height=386)

EntryBox = Text(base, bg="white", height="5", width=29, font="Arial")
EntryBox.place(x=6, y=401, height=90, width=265)

SendButton = Button(base, font=("Verdana", 12), text="Send", height="5", width="9",
                bd=0, bg="blue", activebackground="gold", fg='#ffffff', command=send)
SendButton.place(x=282, y=401, height=90)

base.bind('<Return>', lambda event: send())

#  Primer parameter: posición
#  ChatLog.grid(column=0, row=0)

base.mainloop()
