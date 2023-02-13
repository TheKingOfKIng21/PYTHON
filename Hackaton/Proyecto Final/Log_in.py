import tkinter
import re
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import pandas as pd

names = []
emails = []
phones = []
subs = []
informe = pd.DataFrame()
headers = ["Name", "eMail", "Number", "Subscribed"]


# _______Validaciones______
def es_nombre(nombre):
    nombre = nombre.replace(' ', '')

    if nombre.isalpha() == False:
        nombre = ""
        raise ValueError()


# ___ Telefono ___
def validar_telefono(numero):
    patron = re.compile(r'^\d{4}\d{4}$')

    return patron.match(numero)


# ____ Correo ____
def validar_correo(correo):
    print("está validando")
    patron = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(patron, correo):
        return True
        print("validó el correo")
    else:
        return False

# ______ Guardar el archivo en csv _________

def save_to_csv(email, name, tel, subscribed):
    dict = {'Name': '', 'eMail': '', 'Phone': 0, 'Subscribed': ''}

    dict['Name'] = name
    dict['eMail'] = email
    dict['Phone'] = tel
    dict['Subscribed'] = subscribed

    try:
        df = pd.DataFrame(dict, index=[0])
        df.to_csv("informe.csv", sep=";", mode='a', index=False, header=False)
        pass

    except:
        df = pd.DataFrame(dict, index=[0])
        df.to_csv("informe.csv", sep=";", index=False)
        pass

# _________ validar correo y telefono ________
def validate():
    email = correo_in.get("1.0", "end-1c").strip()
    name = nombre_in.get("1.0", "end-1c").strip()
    tel = tel_in.get("1.0", "end-1c").strip()

    if checkvar.get() == 0:
        subscribed = 'No'
    else:
        subscribed = 'yes'

    if validar_correo(email):
        print("CORREO VALIDO")
        validate_mail = True
    else:
        tkinter.messagebox.showerror(message="Correo inválido", title="ERROR")
        print("CORREO INVALIDO")
        validate_mail = False
    if validar_telefono(tel):
        print("NUMERO VALIDO")
        validate_phone = True
    else:
        print("NUMERO INVÁLIDO")
        tkinter.messagebox.showerror(
            message="Numero de teléfono inválido, no incluyas letras ni caracteres especiales",
            title="ERROR")
        validate_phone = False

    if (validate_phone and validate_mail):
        print("datos guardados...")
        save_to_csv(email, name, tel, subscribed)



# ________________________________________________ front end _________________________________________

log_in = Tk()
log_in.geometry("550x500")
log_in.title("Inicia sesión")
log_in.resizable(width=FALSE, height=FALSE)
log_in.config(bg="navajo white")

# ______ Label que indica al usuario que ingrese el nombre _______

nombre_lab = Label(log_in, bd=0, bg="navajo white", width=1, height="5", font="Arial",
                   text="Introduce tu nombre")
nombre_lab.config(foreground="black", font=("Montserrat, sans-serif", "12", "bold"))
nombre_lab.place(x=94, y=75, height=25, width=170)

# ______ Usuario ingresa el nombre _______
nombre_in = Text(log_in, bd=0, bg="white", width=1, height="5", font="Arial")
nombre_in.config(foreground="Black", font=("Verdana", 12))
nombre_in.place(x=100, y=100, height=25, width=350)

# ______ Label que indica al usuario que ingrese el correo _______


correo_lab = Label(log_in, bd=0, bg="navajo white", width=1, height="5", font="Arial",
                   text="Introduce tu correo electronico")
correo_lab.config(foreground="Black", font=("Montserrat, sans-serif", 12, "bold"))
correo_lab.place(x=94, y=150, height=25, width=240)

w_mail = Label(log_in, bd=0, bg="navajo white", width=1, height="5", font="Arial",
               text="(nombre@dominio.com)")
w_mail.config(foreground="Black", font=("Montserrat, sans-serif", 8))
w_mail.place(x=330, y=150, height=25, width=120)

# ______ Usuario ingresa el correo _______
correo_in = Text(log_in, bd=0, bg="white", width=1, height="5", font="Arial")
correo_in.config(foreground="Black", font=("Verdana", 12))
correo_in.place(x=100, y=175, height=25, width=350)

# ______ Label que indica al usuario que ingrese el numero de telefono _______

tel_lab = Label(log_in, bd=0, bg="navajo white", width=1, height="5", font="Arial",
                text="Introduce tu numero de telefono")
tel_lab.config(foreground="Black", font=("Montserrat, sans-serif", 12, "bold"))
tel_lab.place(x=94, y=225, height=25, width=253)

w_tel = Label(log_in, bd=0, bg="navajo white", width=1, height="5", font="Arial",
              text="(xxxxxxxx)")
w_tel.config(foreground="Black", font=("Montserrat, sans-serif", 8))
w_tel.place(x=350, y=226, height=25, width=60)

# ______ Usuario ingresa el numero de telefono _______
tel_in = Text(log_in, bd=0, bg="white", width=1, height="5", font="Arial")
tel_in.config(foreground="Black", font=("Verdana", 12))
tel_in.place(x=100, y=250, height=25, width=350)

# __________ SMI Logo ___________

smi_logo = ImageTk.PhotoImage(Image.open("LogoC.png"))
smi_label = Label(log_in, image=smi_logo, background="navajo white")
smi_label.place(x=100, y=350)

# _______ Checkvar ___________

checkvar = IntVar()
check_btn = tkinter.Checkbutton(log_in, text="¿Deseas estar suscribirte a nuestro portal?", variable=checkvar)
check_btn.config(background="navajo white", font=("Montserrat, sans-serif", 9))
check_btn.place(x=95, y=300)

# _______ Botón de enviar ___________
sendButton = Button(log_in, font=("Montserrat, sans-serif", 12, "bold"), text="Enviar", height="5", width="9",
                    bd=0, bg="black", activebackground="dark red", fg='#ffffff', command=validate)
sendButton.place(x=350, y=350, height=90)


# ______ Crear dataframe para guardar los datos ________

log_in.bind('<Return>', lambda event: validate())

log_in.mainloop()
