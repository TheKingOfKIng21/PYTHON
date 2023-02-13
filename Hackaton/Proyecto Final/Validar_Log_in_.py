#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import re
##Nombre
nombre = ""
while not nombre:
    try:
        nombre = input("Ingrese nombre: ") 
        nombre = nombre.replace(' ', '')
        if nombre.isalpha()== False:
            nombre = ""
            raise ValueError()
    except ValueError:
        print("el nombre no puede contener numeros o signos")
        passnombre = ""

##Correo
def es_correo_valido(correo):
    patron = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(patron, correo):
        return True
    else:
        return False

while True:
    correo = input("Ingresa tu dirección de correo electrónico: ")
    if es_correo_valido(correo):
        print("La dirección de correo es válida.")
        break
    else:
        print("La dirección de correo no es válida, por favor vuelve a ingresar.")
 
def es_telefono(numero):
    patron = re.compile(r'^\d{4}\d{4}$')
    return patron.match(numero)

while True:
    numero = input("Ingrese un número de teléfono: ")
    if es_telefono(numero):
        print("Es un número de teléfono válido.")
        break
    else:
        print("No es un número de teléfono válido. Intente nuevamente.")

