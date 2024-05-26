# programa que calcule el imc de una persona con tkinter
#

import tkinter as tk
from tkinter import messagebox


def calcular():
    try:
        categoria = ""
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())
        imc = peso / (altura ** 2)
        if imc < 18.5:
            categoria = "Bajo peso"
        elif 18.5 <= imc < 24.9:
            categoria = "Normal"
        elif 24.9 <= imc < 29.9:
            categoria = "Sobrepeso"
        elif 29.9 <= imc < 34.9:
            categoria = "Obesidad I"

        messagebox.showinfo(
            "IMC", f"Tu IMC es: {imc: .2f}\nEstás en la categoría de: {categoria}")
    except ValueError:
        messagebox.showerror("Error", "Introduce un valor válido")


root = tk.Tk()
root.title("Calculadora de IMC")
root.geometry("300x200")
root.resizable(False, False)
root.config(bg="#E0E0E0")

label_peso = tk.Label(root, text="Peso (kg):", bg="#E0E0E0")
label_peso.pack(pady=5)
entry_peso = tk.Entry(root)
entry_peso.pack(pady=5)

label_altura = tk.Label(root, text="Altura (m):", bg="#E0E0E0")
label_altura.pack(pady=5)
entry_altura = tk.Entry(root)
entry_altura.pack(pady=5)

button_calcular = tk.Button(root, text="Calcular",
                            command=calcular, bg="#4CAF50", fg="white")
button_calcular.pack(pady=5)

root.mainloop()
