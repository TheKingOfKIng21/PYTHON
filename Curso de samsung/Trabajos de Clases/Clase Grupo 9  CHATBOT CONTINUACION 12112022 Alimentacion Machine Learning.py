#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Lista de Librerias necesarias para crear un CHATBOT

# numpy manejo de datos 
# nltk Es una libreria que sirve para interpretar lenguaje natural
# tensorflow
# tflearn
# random


# In[ ]:


pip install nltk


# In[ ]:


pip install tensorflow


# In[ ]:


pip install tflearn


# In[5]:


import nltk
from nltk.stem.lancaster import LancasterStemmer ## El conjunto de palabras hablantes naturales del lenguaje Ingles y Español 
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


#En words estoy almacenando todas las posibles palabras sin diferenciar entre frases 
words=[] #Palabras

#Labels estoy almacenando todas las categorias de cada frase respectivamente con docs_x
labels=[] #Titulos, legendas.


#En docs_x estoy almancenando todas las palabras pero si diferenciando entre frases.
docs_x=[] #

#En docs_y estoy almacenando todas las categorias sin diferenciar a que frase corresponde. 
docs_y=[] #

#Con ese for llenare la variable que guarda las palabra
for intents in data['intents']:
    for patterns in intents['patterns']:
        wrds = nltk.word_tokenize(patterns) #Tokenize extra las palabras contenidas en una frase.
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


# In[5]:


print (words)
print ("")
print ("")
print ("")

words=[stemmer.stem(w.lower()) for w in words if w != "?"] #Con esta linea estoy conviertiendo todas mis palabras en minusculas
#y adicionalmente obtengo la palabra en lenguaje, dialecto o tono natural.

print (words)
print ("")
print ("")
print ("")

words = sorted(list(set(words))) #Con set, list y sorted organizo mi conjunto de palabras alfabeticamente. 

print (words)
print ("")
print ("")
print ("")


# In[ ]:





# In[15]:


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

        training.append(bag) # -> Training
        output.append(output_row) # -> Labels
        
#Tenemos almacenados las posibles preguntas, realmente tenemos nuestra bolsa de palabras.     
training = np.array(training)

#Guardamos las categorizaciones de las posibles preguntas. 
output = np.array(output)


print("")
print("")

print (training)


    


# In[17]:


#tensorflow.reset_default_graph() #Es la primera vez que utilizo la libreria tensorflow en el codigo y estoy utilizando
#una funcion de esa libreria llamada reset_default_graph

tensorflow.compat.v1.reset_default_graph()

#Con esta linea estoy creando mi primera capa o capa 0 o capa de alimentacion
net = tflearn.input_data(shape=[None, len(training[0])]) 


#Con esta linea estoy creando mi primera capa de red neuronal 
net = tflearn.fully_connected(net, 8)


#Con esta linea estoy creando mi segunda capa de red neuronal 
net = tflearn.fully_connected(net, 8)


# In[ ]:




