#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter
from tkinter import *
from tkinter import PhotoImage
from PIL import Image, ImageTk

log_in = Tk()
log_in.geometry("550x500")
log_in.title("Inicia sesión")
log_in.resizable(width=TRUE, height=TRUE)

# ______ Imagen Background _______
image = PhotoImage(file="background.png")
background_label = Label(log_in, image=image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
texto1 = "introduce tu nombre"

# ______ Label que indica al usuario que ingrese el nombre _______

nombre_lab = Label(log_in, compound=CENTER, text=texto1, image=image, padx=100, pady=70)
nombre_lab.config(foreground="black", font=("Montserrat, sans-serif", "12", "bold"))
nombre_lab.place(x=100, y=70, height=25, width=170)

# ______ Usuario ingresa el nombre _______
nombre_in = Text(log_in, bd=0, bg="white", width=1, height="5", font="Arial")
nombre_in.config(foreground="Black", font=("Verdana", 12))
nombre_in.place(x=100, y=100, height=25, width=350)

# ______ Label que indica al usuario que ingrese el correo _______

correo_lab = Label(log_in, width=1, height="5", font="Arial", compound=CENTER, image=image,
     text="Introduce tu correo electronico")
correo_lab.config(foreground="black", font=("Montserrat, sans-serif", 12, "bold"), bd=1,  background="ghost white")
correo_lab.place(x=100, y=145, height=25, width=240)

w_mail = Label(log_in, foreground="black", width=1, height="5", font="Arial", background="ghost white", compound=CENTER, image=image,
               text="(nombre@dominio.com)")
w_mail.config(foreground="Black", font=("Montserrat, sans-serif", 7))
w_mail.place(x=350, y=150, height=20, width=100)

# ______ Usuario ingresa el correo _______
correo_in = Text(log_in, bd=0, bg="white", width=1, height="5", font="Arial")
correo_in.config(foreground="Black", font=("Verdana", 12))
correo_in.place(x=100, y=175, height=25, width=350)

# ______ Label que indica al usuario que ingrese el numero de telefono _______

tel_lab = Label(log_in, bd=0, bg="ghost white", width=1, height="5", font="Arial", compound=CENTER, image=image,
                text="Introduce tu numero de telefono")
tel_lab.config(foreground="Black", font=("Montserrat, sans-serif", 12, "bold"))
tel_lab.place(x=100, y=220, height=25, width=253)

w_tel = Label(log_in, bd=0, bg="ghost white", width=1, height="5", font="Arial", compound=CENTER, image=image,
              text="(xxxxxxxx)")
w_tel.config(foreground="Black", font=("Montserrat, sans-serif", 8))
w_tel.place(x=370, y=220, height=25, width=60)

# ______ Usuario ingresa el numero de telefono _______
tel_in = Text(log_in, bd=0, bg="white", width=1, height="5", font="Arial")
tel_in.config(foreground="Black", font=("Verdana", 12))
tel_in.place(x=100, y=250, height=25, width=350)

# __________ SMI Logo ___________

smi_logo = ImageTk.PhotoImage(Image.open("LogoC.png"))
smi_label = Label(log_in, image=smi_logo, background="#FAA4A4", compound=CENTER)
smi_label.place(x=100, y=350)

# _______ Checkvar ___________

checkvar = IntVar()
check_btn = tkinter.Checkbutton(log_in, text="¿Deseas estar suscribirte a nuestro portal?",
                                variable=checkvar)
check_btn.config(background="#fa8072", font=("Montserrat, sans-serif", 9))
check_btn.place(x=95, y=300)

# _______ Botón de enviar ___________
sendButton = Button(log_in, font=("Montserrat, sans-serif", 12, "bold"),
                    text="Enviar", height="5", width="9",
                    bd=0, bg="black", activebackground="dark red",
                    fg='#FAA4A4')
sendButton.place(x=350, y=350, height=90)

# ______ Crear dataframe para guardar los datos ________


log_in.mainloop()
