import tkinter as tk
from tkinter import *
from tkinter import PhotoImage
from tkinter import ttk
from csv import DictWriter
import os
from tkinter import messagebox

root = Tk()
root.title('ChatBot - Log in User')
root.geometry('400x520+100+30')
root.resizable(width=FALSE, height=FALSE)

# Crear objeto de imagen
image = PhotoImage(file="i2.png")

# Crear una etiqueta para mostrar la imagen
background_label = Label(root, image=image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

#creacion de  labels
label1 = ttk.Label(root,text="Nombre:")
label1.grid(row=1,column=0,sticky=tk.W)

label2 = tk.Label(root,text="Correo:")
label2.grid(row=2,column=0,sticky=tk.W)

label3 = tk.Label(root,text="Telefono :")
label3.grid(row=3,column=0,sticky=tk.W)

#creacion de Entry box 

entrybox_1_var = tk.StringVar()
entrybox_1 = ttk.Entry(root, width = 16, textvariable = entrybox_1_var)
entrybox_1.grid(row=1,column=1,sticky=tk.W)
entrybox_1.focus()

entrybox_2_var = tk.StringVar()
entrybox_2 = tk.Entry(root, width = 16, textvariable = entrybox_2_var)
entrybox_2.grid(row=2,column=1,sticky=tk.W)

entrybox_3_var = tk.StringVar()
entrybox_3 = tk.Entry(root, width = 16, textvariable = entrybox_3_var)
entrybox_3.grid(row=3,column=1,sticky=tk.W)


#creacion de boton de check 
checkvar = IntVar()
check_btn = ttk.Checkbutton(root,text='Presiones si desea estar informado de nuestro nuevos productos',variable=checkvar)
check_btn.grid(row=6, columnspan=3)

def action():
    user_name = entrybox_1_var.get() 
    user_email = entrybox_2_var.get()
    user_tel = entrybox_3_var.get()

    if checkvar.get()==0:
        Subscribed = 'No'
    else:
        Subscribed = 'yes'
    
 
# writing to csv file

    with open("st_records.csv",'a', newline='') as f:
        dict_writer = DictWriter(f, fieldnames=['UserName','User email address','User cellphone','subscribed'])

        if os.stat("st_records.csv").st_size==0: #checks if file contains the header or not
            DictWriter.writeheader(dict_writer)

        dict_writer.writerow({'UserName': user_name,'User email address': user_email, 'User cellphone': user_tel,'subscribed':Subscribed })

        messagebox.showinfo('Message','Record added Sucessfully')  #creating message box


    name =  entrybox_1.delete(0,tk.END)
    age = entrybox_2.delete(0,tk.END)
    email = entrybox_3.delete(0,tk.END)

    
#creacion de boton de registro
submit_btn = tk.Button(root,text='Submit', command= action)
submit_btn.grid(row=8,columnspan=3)


root.mainloop()    