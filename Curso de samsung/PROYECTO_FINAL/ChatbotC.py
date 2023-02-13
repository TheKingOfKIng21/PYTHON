#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Importamos las librerias previamente instaladas. 

import nltk
from nltk.stem.lancaster import LancasterStemmer #Este es un modulo que se encuentra en la libreria NLTK que nos proporciona las herramientas necesarias para el lenguaje natural
import tensorflow
import tflearn

#Agregamos dos librerias adicionales para responderle al usuario.
import random #Sirve para responder aleatoriamene cuando ya conoces la categoria a la que corresponde la frase ingresada por el usuario. 
import numpy as np
import pickle #Libreria que sirve para guardar temporales de manera permanente.

stemmer=LancasterStemmer()

#Esta parte del codigo sirve para cargar los datos almacenados en el archivo intents.json
#Recordar: El archivo .json es la base de datos inicial con la cual se alimentará el sistema 
# y en el cual se pueden agregar nuevas formas de saludar, responder, categorias etc. 
import json
with open('intents.json') as file:
    data = json.load(file)

print("Esta es la primera informacion sin procesar")
data


#Con el bloque siguiente lo que hacemos es obtener cada una de las palabras que tenemos en el 
#archivo .json y convertirlas en el lenguaje natural, adicionalmente obtengo las catergorias. 


try:
    with open("data.pickle", "rb") as f:
        words, labels, training, output = pickle.load(f)
        print("Estoy dentro del TRY")
        print(words)
        print("")
        print("")
        print(labels)
        print("")
        print("")
        print(training)
        print("")
        print("")
        print(output)
        model.load("model.tflearn")       


except:
    
    #En caso de un error se ejectuta por aqui. 
    
    print("Estoy dentro del EXCEPT")

    words=[] #Palabras sin deferenciar la frase a la que pertenecen 
    labels=[] #Titulos, legendas.
    docs_x=[]
    docs_y=[]

    #Con este ciclo for estoy recorriendo todo el archivo json y tomando cada una de las frases para 
    #convertirlas en palabras. 

    #Con ese for llenare la variable que guarda las palabra
    for intents in data['intents']:
        for patterns in intents['patterns']:
            wrds = nltk.word_tokenize(patterns) #Convierte una frase a un conjunto de palabras
            words.extend(wrds)
            docs_x.append(wrds)
            docs_y.append(intents["tag"])


            if intents['tag'] not in labels:
                labels.append(intents['tag'])

    print (words)
    print ("")
    print ("")
    print ("")

    print (docs_x) #Me estoy quedando con las palabras individuales y separadas por frases
    print ("")
    print ("")
    print ("")
    print (docs_y) #Me estoy quedando con las categorias a las cuales pertenecen cada una de las frases 

    print ("")
    print ("")
    print ("")
    print (labels)
    
    #La informacion y los codigos contenidos en esta celda sirven para recorrer todas las palabras extraidas
    #del archivo .json y convertirlas en el lenguaje natural. Adicionalmente con la funcion list y sorted 
    #logramos eliminar las palabras repetidas y ordenarlas. 

    print (words)
    print ("")
    print ("")
    print ("")

    words=[stemmer.stem(w.lower()) for w in words if w != "?"]

    print (words)
    print ("")
    print ("")
    print ("")

    words = sorted(list(set(words))) #Organizando el conjunto de paralabras de forma no repetiva y ordenada.

    print (words)
    print ("")
    print ("")
    print ("")
    
    labels = sorted(labels)

    print (labels)


    #['greeting', 'goodbye', 'thanks', 'hours', 'payments', 'opentoday']


    #A continuacion se crean dos variables llamadas training y output

    #Deben asemejar a training con las palabras osea words.
    #Deben asemejar a output con las categorias osea labels.

    training=[]
    output=[]

    out_empty = [0 for _ in range (len(labels))]

    #print (out_empty)


    print ("")
    print ("")


    print (docs_x)

    #Este ciclo for se encarga de analizar todas y cada una de las palabras en todas y cada una de las frases


    for x, doc in enumerate(docs_x):
        bag = []

        wrds=[stemmer.stem(w.lower()) for w in doc]

        for w in words:
            if w in wrds:
                #print ("Entre por UNO")
                #print ("Este es w")
                #print (w)
                #print ("Este es wrds")
                #print (wrds)
                #print ("Este es words")
                #print (words)
                bag.append(1)
            else:

                #print ("Entre por DOS")
                #print ("Este es w")
                #print (w)
                #print ("Este es wrds")
                #print (wrds)
                #print ("Este es words")
                #print (words)
                bag.append(0)

            output_row = out_empty[:]
            output_row[labels.index(docs_y[x])] = 1

            training.append(bag)
            output.append(output_row)
        
        
        
    #Todo el codigo anterior es necesario para llegar a las dos 
    #variables "Finales" que alimentaran el sistema de machine
    #Learning llamadas training y output las cuales formaran 
    #parte de la capa de alimentacion. 

    training = np.array(training) #Contiene la informacion preparada con la cual se va a alimentar el sistema referentes a las palabras
    output = np.array(output) #Contiene la informacion preparada con la cual se va a alimentar el sistema referente a la categorizacion

    with open ("data.pickle", "wb") as f:
        pickle.dump((words, labels, training, output), f)

    print ("Esto es training")
    print (training) #palabras codificadas
    print ("")
    print ("")
    print (output) #Categorizacion "Tags" codificados
    
    #tensorflow.reset_default_graph() #Es la primera vez que utilizo la libreria tensorflow en el codigo y estoy utilizando
    #una funcion de esa libreria llamada reset_default_graph

    tensorflow.compat.v1.reset_default_graph()

    #Con esta linea estoy creando mi primera capa o capa 0 o capa de alimentacion
    net = tflearn.input_data(shape=[None, len(training[0])]) 


    #Con esta linea estoy creando mi primera capa de red neuronal Circulos negros
    net = tflearn.fully_connected(net, 8)


    #Con esta linea estoy creando mi segunda capa de red neuronal Circulos rojos
    net = tflearn.fully_connected(net, 8)


    #Continuacion 
    #Capa de decisión Circulos verdes

    #Otro modelo de regresion es sigmoid
    net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
    net = tflearn.regression(net)

    #Esta linea se encarga de construir el modelo final a partir de las especificaciones anteriores
    model = tflearn.DNN(net)
    
    try:
        model.load("model.tflearn")
    except:       

        #Hasta el momento hemos configurado nuestro modelo, es hora de entrenarlo con nuestros datos. 
        #Para eso usaremos las siguientes lineas de codigo

        model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)
        model.save("model.tflearn")
        

#Esta funcion se encarga de convertir la frase que el usuario ingresa en 1s y 0s para luego poderla 
#ingresar al modelo de prediccion.
def bag_of_words(s, words):
    #la variable S contiene la informacion que el usuario ingresa
    #En la variable words contengo la bolsa de palabras 
    
    bag = [0 for _ in range(len(words))]

    #"Hola como estas, puedo reservar una cita?"
    s_words = nltk.word_tokenize(s) #Convierto la frase ingresada por el usuario en palabras 
    #["Hola", "como", "estas", "puedo", "reservar", "una", "cita"]
    
    s_words = [stemmer.stem(word.lower()) for word in s_words]
    #["Hola", "como", "estar", "poder", "reservar", "una", "cita"]
    
        #Que esta contenido en la variable words?
        #["'s", 'acceiv', 'anyon', 'ar', 'bye', 'card', 'cash', 'credit', 'day', 'de', 'do',
        #'form', 'good', 'goodby', 'hello', 'help', 'hi', 'hour', 'how', 'is', 'lat', 'mastercard', 
        #'nuev', 'on', 'op', 'salud', 'see', 'tak', 'thank', 'that', 'ther', 'today', 'up', 'what', 
        #'when', 'yo', 'you']
    
    
    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1
            
    return np.array(bag)


def chat():
    print("Start talking with the bot (type quit to stop)!") #Mensaje inicial para que el usuario escriba y sepa que esta siendo leido (Escuchado)
    
    while True: #Se escucha constantemente al usuario. 
        inp = input("You: ") #Esperamos que el usuario ingrese una frase
        if inp.lower() == "quit":
            break

        #Que esta contenido en la variable words?
        #["'s", 'acceiv', 'anyon', 'ar', 'bye', 'card', 'cash', 'credit', 'day', 'de', 'do',
        #'form', 'good', 'goodby', 'hello', 'help', 'hi', 'hour', 'how', 'is', 'lat', 'mastercard', 
        #'nuev', 'on', 'op', 'salud', 'see', 'tak', 'thank', 'that', 'ther', 'today', 'up', 'what', 
        #'when', 'yo', 'you']
        #En la variable inp contengo la frase que el usuario ingresa.

        results = model.predict([bag_of_words(inp, words)])
        
        print("este es el resultado del modelo")
        print(results)
        
        results_index = np.argmax(results) #La funcion argmax obtiene la probabilidad mas alta.
        
        
        #Me devuelve el numero de la posicion donde se encuentra la probabilidad mas alta.
        print("Esta es la probabilidad mas alta")
        print(results_index)
        
        print("Estos son los labels")
        print(labels)        
        
        print("Esta es la categoria")
        print(labels[results_index])
        
        tag = labels[results_index]

        #Finalmente ingreso al archivo json particularmente a la categoria elegida por el modelo
        #y me quedo con las respuestas correspondientes. 
        for tg in data["intents"]:
            if tg['tag'] == tag:
                responses = tg['responses']

        #escogemos una respuesta al azar
        print(random.choice(responses))

chat()

#7.0317071e-07 -> 0.00000070317071
#9.9999928e-01 -> 0.99999928


# In[ ]:




