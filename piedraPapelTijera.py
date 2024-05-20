
import tkinter as tk
import random


def jugar(opcion_usuario):
    opciones = ["Piedra", "Papel", "Tijera"]
    opcion_maquina = random.choice(opciones)

    if opcion_usuario == opcion_maquina:
        resultado.set("Empate")
    elif (opcion_usuario == "Piedra" and opcion_maquina == "Tijera") or \
         (opcion_usuario == "Papel" and opcion_maquina == "Piedra") or \
         (opcion_usuario == "Tijera" and opcion_maquina == "Papel"):
        resultado.set("¡Ganaste!")
    else:
        resultado.set("¡Perdiste!")


root = tk.Tk()
root.title("Piedra, Papel o Tijera")
root.geometry("300x200")

resultado = tk.StringVar()

tk.Label(root, text="Elige una opción:").pack()

piedra_btn = tk.Button(root, text="Piedra", command=lambda: jugar("Piedra"))
piedra_btn.pack()

papel_btn = tk.Button(root, text="Papel", command=lambda: jugar("Papel"))
papel_btn.pack()

tijera_btn = tk.Button(root, text="Tijera", command=lambda: jugar("Tijera"))
tijera_btn.pack()

resultado_label = tk.Label(root, textvariable=resultado)
resultado_label.pack()

root.mainloop()
