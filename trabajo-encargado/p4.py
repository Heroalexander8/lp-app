import tkinter as tk

numeros = []


def agregar():
    numero = int(entry.get())
    numeros.append(numero)
    entry.delete(0, tk.END)


def mayor_menor():
    mayor = max(numeros)
    menor = min(numeros)
    label.config(text=f"Mayor: {mayor}\nMenor: {menor}")


root = tk.Tk()
root.geometry("300x300")
root.title("Mayor y Menor")
root.config(bg="blue")
root.resizable(0, 0)

entry = tk.Entry(root, font=("Arial", 16))
entry.pack(padx=10, pady=10, fill=tk.X)

button = tk.Button(root, text="Agregar", font=("Arial", 16), command=agregar)
button.pack(padx=10, pady=10, fill=tk.X)

label = tk.Label(root, font=("Arial", 16))
label.pack(padx=10, pady=10, fill=tk.X)

button = tk.Button(root, text="Mayor y Menor",
                   font=("Arial", 16), command=mayor_menor)
button.pack(padx=10, pady=10, fill=tk.X)


root.mainloop()
