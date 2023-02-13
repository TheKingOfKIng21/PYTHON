import json
import pickle
import numpy as np
import nltk
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Conv2D, Flatten, Dense,Dropout
from tensorflow.keras.optimizers import SGD

ignore_words=["?","¿","!","¡"]
data_file=open("intents.json")
intents= json.load(data_file)

words=[]
classes=[]
documents=[]

for intent in intents["intents"]:
    for pattern in intents["patterns"]:
        w= nltk.word_tokenize(pattern)
        words.extend(w)
        documents.append((w,intents["tag"]))
        if intent["tag"] not in classes:
            classes.append(intent["tag"])


from nltk.stem import SnowballStemmer
stemmer = SnowballStemmer('spanish')
words = [stemmer.stem(w.loer())for w in words if w not in ignore_words]
pickle.dump(words,open("words.pkl","wb"))
pickle.dump(classes,open("classes.pkl","wb"))