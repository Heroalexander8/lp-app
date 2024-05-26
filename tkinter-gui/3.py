import random
import tkinter as tk
from tkinter import messagebox


def lanzar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    if dado1 > dado2:
        resultado = "Ganaste"
    elif dado1 < dado2:
        resultado = "Perdiste"
    else:
        resultado = "Empate"
    return messagebox.showinfo(
        "Resultado", f"Dado 1: {dado1}\nDado 2: {dado2}\n{resultado}")


root = tk.Tk()
root.title("Juego de dados")
root.geometry("100x100")
root.resizable(False, False)
root.config(bg="light blue")
root.iconbitmap("./icons/dado.ico")

btn_lanzar_dados = tk.Button(root, text="Lanzar dados", command=lanzar_dados)
btn_lanzar_dados.pack(pady=20)


root.mainloop()
