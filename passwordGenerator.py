import random
import string
import tkinter as tk
import tkinter.messagebox

root = tk.Tk()

minuscula = list(string.ascii_lowercase) #Letras en minuscula
mayuscula = list(string.ascii_uppercase) #Letras en mayuscula
signos = list(string.punctuation) #Signos y simbolos
numeros = [i for i in string.digits] #Numeros del 0 al 9
todo = [minuscula, mayuscula, signos, numeros] #Lista de todos los caracteres

password = "" #String de la contraseña para concatenar los caracteres

def generador(password):
    i = 0 #Variable auxiliar para el indice de la lista
    z = random.randint(8,20)

    while True:
        x = random.randint(0,len(todo) - 1)
        if x == 0:
            j = todo[0]
            k = random.randint(0,len(todo[0]) - 1)
            password += j[k]
        elif x == 1:
            j = todo[1]
            k = random.randint(0,len(todo[1]) - 1)
            password += j[k]
        elif x == 2:
            j = todo[2]
            k = random.randint(0,len(todo[2]) - 1)
            password += j[k]
        elif x == 3:
            j = todo[3]
            k = random.randint(0,len(todo[3]) - 1)
            password += j[k]
        i += 1
        if i == z:
            break
    return password

def mensaje():
    tk.messagebox.showinfo("Contraseña", generador(password))

generar = tkinter.Button(root,fg="black",bg="grey",text="Generar contraseña",command=lambda: mensaje())
generar.pack()

root.mainloop()




