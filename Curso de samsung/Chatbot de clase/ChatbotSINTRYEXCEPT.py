

import nltk
from nltk.stem.lancaster import LancasterStemmer
import tensorflow
import tflearn

import random
import numpy as np

stemmer=LancasterStemmer()


import json
with open('intents.json') as file:
    data = json.load(file)

print("Esta es la primera informacion sin procesar")
data

words=[] #Palabras sin deferenciar la frase a la que pertenecen 
labels=[] #Titulos, legendas.
docs_x=[]
docs_y=[]

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


training=[]
output=[]

out_empty = [0 for _ in range (len(labels))]

#print (out_empty)


print ("")
print ("")


print (docs_x)

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

#Hasta el momento hemos configurado nuestro modelo, es hora de entrenarlo con nuestros datos. 
#Para eso usaremos las siguientes lineas de codigo

model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)
model.save("model.tflearn")

def bag_of_words(s, words): 
    #la funcion recibe dos parametros el primero es la frase que el usuario ingreso (s)
    #El segundo parametro es la bolsa de palabras creada previamente para alimentar el modelo (word)
    bag = [0 for _ in range(len(words))]
    
    s_words = nltk.word_tokenize(s) #¿Que hace la funcion word_tokenize? #Convierte una frase a un conjunto de palabras
    s_words = [stemmer.stem(word.lower()) for word in s_words]
    
    for se in  s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i]=1
                
    return np.array(bag)





def chat():
    
    print("Start talking with the bot (type quit to stops)!")
    while True:
        inp = input("You: ")
        if inp.lower() == "quit" or inp.lower() == "salir":
            break
        
        FraseCodificada=[bag_of_words(inp, words)]
        result = model.predict(FraseCodificada)
        results_index = np.argmax(result)
        tag = labels[results_index] #Con esta linea busco la categorizacion a la cual corresponde la frase ingresada
        
        for tg in data["intents"]:
            if tg['tag']==tag:
                responses = tg['responses']
                
        #print(random.choice(responses))
        
        print(result)
        print(results_index)    
        
             

            
chat()


# In[ ]:




