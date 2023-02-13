#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import email.utils
import re

def validate_email(arg_email):
    is_valid = True
    EMAIL_REGEX = re.compile(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$")
    is_valid = False if not EMAIL_REGEX.match(arg_email) else True
    if is_valid:
        print("Email is valid")
        return is_valid
    else:
        print("Invalid Email")
        return is_valid


#Que solo escriba en letras 
#Nombre = input("Ingrese su Nombre completo \n")
#print(f"{Nombre}")

#correo = input("Ingrese su correo \n")
#print(f"{Correo}"

#solo escriba numeros o inhabilitar el teclado alfanumerico 
#numero = int(input("Numero de telefono \n+507 "))
#print(f"+507 {numero}")


# In[1]:


import email.utils
import re

def validate_email(arg_email):
    is_valid = True
    EMAIL_REGEX = re.compile(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$")
    is_valid = False if not EMAIL_REGEX.match(arg_email) else True
    print("Email is valid" if is_valid else "Invalid email address.")

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
        pass
# Jos3 Moreno no se acepta por el numero
# 21ewq321 Solo se aceptan valores numericos
# Jose Moreno R valido para nombre completo 
while is_valid:

    validate_email(input("Correo electronico"))

#validate_email("alvisonhunter@outlook.com") # This email address is valid
#validate_email("alvisondr.com") # missing an @
#validate_email("alvison@@peachtreelightscapes.com") # Double @ in the email
#validate_email("alvison.hunter@concentrixcom") # missing the dot

#solo escriba numeros o inhabilitar el teclado alfanumerico 

numero = int(input("Numero de telefono \n+507 "))
#print(f"+507 {numero}")


# In[ ]:




