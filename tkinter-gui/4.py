# programa que genere la serie de Fibonacci hasta un número dado por el usuario
# en tkinter
# +

import tkinter as tk
import tkinter.messagebox as mb


def fibonacci():
    try:
        n = int(entry.get())
        if n < 0:
            mb.showerror("Error", "El número debe ser positivo")
        else:
            a, b = 0, 1
            while a <= n:
                label["text"] += str(a) + " "
                a, b = b, a+b
    except ValueError:
        mb.showerror("Error", "Introduce un número entero")


root = tk.Tk()
root.title("Serie de Fibonacci")
root.geometry("400x200")
root.resizable(False, False)
root.config(bg="light blue")

label = tk.Label(root, text="Serie de Fibonacci: ", bg="light blue")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=10)

button = tk.Button(root, text="Generar serie", command=fibonacci)
button.pack(pady=10)

root.mainloop()
