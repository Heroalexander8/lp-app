import tkinter as tk
from tkinter import messagebox

temperaturas = []


def adicionar():
    temp = float(entry.get())
    temperaturas.append(temp)
    entry.delete(0, tk.END)
    entry.focus_set()


def media():
    if len(temperaturas) > 0:
        media = sum(temperaturas) / len(temperaturas)
        messagebox.showinfo("Media", f"La media es {media}")
    else:
        messagebox.showerror("Error", "Ninguna temperatura ingresada")


def comparar():
    mayores = 0
    menores = 0
    media = sum(temperaturas) / len(temperaturas)
    for tempe in temperaturas:
        if tempe > media:
            mayores += 1
        elif tempe < media:
            menores += 1
        else:
            messagebox.showerror("Error", "Ninguna temperatura ingresada")

    messagebox.showinfo(
        "Comparacion", f"Mayores: {mayores}\nMenores: {menores}")


root = tk.Tk()
root.title("Temperaturas")
root.geometry("300x200")
root.resizable(False, False)
root.configure(bg="white")

label = tk.Label(root, text="Digite la temperatura:", bg="white")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Adicionar", command=adicionar)
button.pack()

button2 = tk.Button(root, text="Calcular media", command=media)
button2.pack()

button3 = tk.Button(root, text="Comparar", command=comparar)
button3.pack()

root.mainloop()
