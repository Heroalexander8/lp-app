
import tkinter as tk
from tkinter import messagebox


def calcular():
    try:
        monto = float(caja_monto.get())
        if monto < 1000 and monto <= 3000:
            tasa = 40
        elif monto > 3000 and monto <= 4000:
            tasa = 30
        elif monto > 5000:
            tasa = 20
        else:
            tasa = 0
        messagebox.showinfo("Resultado", f"La tasa de interes es: {tasa}%",)
        messagebox.showinfo(
            "Resultado", f"El monto total a pagar es: {monto + (monto * tasa / 100)}")
    except ValueError:
        messagebox.showerror("Error", "El monto debe ser un numero")


app = tk.Tk()
app.title("Tasa de interes")
app.geometry("300x200")

etiqueta_monto = tk.Label(app, text="Monto del prestamo:")
etiqueta_monto.pack()

caja_monto = tk.Entry(app)
caja_monto.pack()

boton_calcular = tk.Button(app, text="Calcular", command=calcular)
boton_calcular.pack()
boton_calcular.config(bg="blue", fg="white")
boton_salir = tk.Button(app, text="Salir", command=app.quit)
boton_salir.pack()

app.mainloop()
