

import tkinter as tk
from tkinter import messagebox

vector_nombres_animales = []


def agregar_animal(nombre):
    vector_nombres_animales.append(nombre)
    entry.delete(0, tk.END)


def buscar_animal(nombre):
    if nombre in vector_nombres_animales:
        indice = vector_nombres_animales.index(nombre)
        return f"{vector_nombres_animales[indice - 1]},  , {vector_nombres_animales[indice + 1]}"
    else:
        return False


root = tk.Tk()
root.title("Animales")
root.geometry("300x300")
root.resizable(0, 0)
root.config(bg="lightblue")

label = tk.Label(root, text="Nombre del animal", bg="lightblue")
label.pack()
label.place(x=100, y=50)

entry = tk.Entry(root)
entry.pack()
entry.place(x=100, y=70)

button_agregar = tk.Button(
    root, text="Agregar", bg="lightblue", command=lambda: agregar_animal(entry.get()))
button_agregar.pack()
button_agregar.place(x=150, y=100)

button_buscar = tk.Button(root, text="Buscar", bg="lightblue", command=lambda: messagebox.showinfo(
    "Resultado", buscar_animal(entry.get())))


button_buscar.pack()
button_buscar.place(x=150, y=130)

root.mainloop()
