#!/usr/bin/env python
# coding: utf-8

# In[29]:


#Ejercicio
#Escribir una función que reciba un diccionario con las notas de los alumnos de un curso y devuelva una serie 
#con las notas de los alumnos aprobados ordenadas de mayor a menor. 1-10 => 5

import pandas as pd

#Recibe un diccionario
def notasAprobadas(notas):
    notas=pd.Series(notas) #Conviertiendo notas en una serie y lo guarda en notas.
    return notas[notas>=5].sort_values(ascending=True)

notas = {'Julian':9.5, 'Felipe': 4, 'Andrea':8, 'Joseph': 2.5, 'Bobi':5, 'Artur':6.5} #Diccionario de notas

print(notas) #Estoy imprimiendo en Diccionario

print(notasAprobadas(notas)) 


#notasAprobas = notasAprobadas(notas)
#print(notasAprobas)    


# In[42]:


#Escribir un programa que pregunte al usuario por las ventas de un rango de años y muestre por pantalla una serie con 
#los datos de las ventas indexada por los años, antes y después de aplicarles un descuento del 10%.

import pandas as pd

AñoInicio = int(input('Introduce el año inicial: '))
AñoFinal = int(input('Introduce el año final: '))
ventas={}

for i in range(AñoInicio, AñoFinal+1):
    ventas[i]=float(input('Introduce las ventas del año: '+str(i)+':'))
    
ventasaños=pd.Series(ventas)
print('Ventas netas\n', ventasaños)
print('Ventas Descuento\n', ventasaños*0.9)







# In[50]:


#El fichero titanic.csv contiene información sobre los pasajeros del Titanic. Crear un dataframe con Pandas y a partir 
#de él generar los siguientes diagramas.

#Diagrama de sectores con los fallecidos y supervivientes.
#Histograma con las edades.
#Diagrama de barras con el número de personas en cada clase.
#Diagrama de barras con el número de personas fallecidas y supervivientes en cada clase.
#Diagrama de barras con el número de personas fallecidas y supervivientes acumuladas en cada clase.

import pandas as pd 
import matplotlib.pyplot as plt 

# Creamos un dataframe a partir del fichero csv
df_titanic = pd.read_csv('titanic.csv')
# Creamos la figura y los ejes
fig, ax = plt.subplots()
# Diagrama de sectores de falleccidos y supervivientes
df_titanic.Survived.value_counts().plot(kind = "pie", labels = ["Muertos", "Supervivientes"], title = "Distribución de supervivientes")
plt.show()


# In[54]:


df_titanic.Age.plot(kind="hist", title= "Histograma de edades")
plt.show()


# In[55]:


df_titanic.groupby("Pclass").size().plot(kind = "bar", title = "Número de personas por clase")
plt.show()


# In[ ]:




