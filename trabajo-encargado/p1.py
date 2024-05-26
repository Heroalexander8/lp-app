import tkinter as tk
from tkinter import messagebox

v1 = 0
v2 = 0
d = 0


def calcular_velocidad(v1, v2, d):
    if v1 > 0 and v2 > 0:
        t = d / (v1 + v2)
        messagebox.showinfo(
            "Tiempo", "El tiempo que tardan en encontrarse es: " + str(t) + " horas")
    else:
        messagebox.showerror("Error", "Las velocidades deben ser positivas")


root = tk.Tk()
root.title("Encuentro de dos móviles")
root.geometry("400x400")
root.resizable(False, False)
root.config(bg="light blue")

label1 = tk.Label(root, text="Velocidad del móvil 1: ", bg="light blue")
label1.pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack(pady=5)

label2 = tk.Label(root, text="Velocidad del móvil 2: ", bg="light blue")
label2.pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack(pady=5)

label3 = tk.Label(root, text="Distancia entre los móviles: ", bg="light blue")
label3.pack(pady=5)
entry3 = tk.Entry(root)
entry3.pack(pady=5)

entry3.bind("<Return>", lambda x: calcular_velocidad(
    float(entry1.get()), float(entry2.get()), float(entry3.get())))

button = tk.Button(root, text="Calcular", command=lambda: calcular_velocidad(
    float(entry1.get()), float(entry2.get()), float(entry3.get())), bg="light green")

button.pack(pady=5)

root.mainloop()
