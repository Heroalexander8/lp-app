# programa que calcule el area y perimeter de un rectangulo
# ingresando la base y la altura

import tkinter as tk
from tkinter import messagebox


def calcular():
    try:
        base = float(entrada_base.get())
        altura = float(entrada_altura.get())
        if base < 0 or altura < 0:
            messagebox.showerror("Error", "Ingrese un numero positivo")
        else:
            area = base * altura
            perimetro = 2 * (base + altura)
            messagebox.showinfo(
                "Resultado", f"Area: {area}\nPerimetro: {perimetro}")
    except ValueError:
        messagebox.showerror("Error", "Ingrese un numero valido")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrio un error: {e}")


root = tk.Tk()
root.title("Calculo de area y perimetro")
root.geometry("300x200")
root.resizable(False, False)
root.iconbitmap("./icons/rectangulo.ico")

lbl_base = tk.Label(root, text="Base")
lbl_base.pack()
entrada_base = tk.Entry(root)
entrada_base.pack()

lbl_altura = tk.Label(root, text="Altura")
lbl_altura.pack()
entrada_altura = tk.Entry(root)
entrada_altura.pack()

btn_calcular = tk.Button(root, text="Calcular", command=calcular)
btn_calcular.pack()
btn_calcular.place(x=120, y=100)

root.mainloop()
