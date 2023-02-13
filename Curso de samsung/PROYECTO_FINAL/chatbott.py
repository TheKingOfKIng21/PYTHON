import numpy as np 
import json
import re
import tensorflow as tf
import random
import warnings
import spacy

nlp = spacy.load("es_core_news_sm")

warnings.filterwarnings('ignore')

with open ('intents.json','rb') as file:
    data =json.load(file)

def pre_proceso(line):
    line= re.sub (r'[^a-zA-z.?!\']',' ', line)
    line= re.sub(r'[ ]+',' ',line)
    return line

inputs, targets = [], []
cls= []
intents_doe= []

for i in data['intents']:
    if i ['tag'] not in cls:
        cls.append(i['tag'])
    
    if i ['tag'] not in intents_doe:
        intents_doe[i['tag']] =[]
    
    for patterns in i['patterns']:
        inputs.append(pre_proceso(patterns))
        targets.append(i['tag'])
    
    for responses in i['responses']:
        intents_doe[i['tag']].append(responses)

def tokenizador(inp_list):
    tokenizer = tf.keras.preprocessing.text.Tokenizer(filters=)