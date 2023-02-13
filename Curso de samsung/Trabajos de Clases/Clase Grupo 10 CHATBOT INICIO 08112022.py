#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Lista de Librerias necesarias para crear un CHATBOT

# numpy manejo de datos (pandas)
# nltk Es una libreria que sirve para interpretar lenguaje natural
# tensorflow #Libreria para Machine Learning o aprendizaje automatico. 
# tflearn 
# random


# In[13]:


import nltk
from nltk.stem.lancaster import LancasterStemmer
import tensorflow
import tflearn
import random 
import json 

with open("intents.json") as file:
    data = json.load(file)
    
#data

words=[] #Sera el conjunto de palabras 
labels=[] #Seran los clasificadores de las frases, titulos a legendas 
docs_x=[]
docs_y=[]

for intents in data['intents']:
    for patterns in intents['patterns']:
        wrds=nltk.word_tokenize(patterns)
        words.extend(wrds)
        docs_x.append(wrds)
        docs_y.append(intents['tag'])
        
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

print (docs_y) #Me estoy quedando con las palabras individuales y separadas por frases


print ("")
print ("")
print ("")

print (labels) #Me estoy quedando con las palabras individuales y separadas por frases


# In[ ]:




