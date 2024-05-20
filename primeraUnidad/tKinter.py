from tkinter import *
from tkinter import ttk

root = Tk()  # creando una ventana
frm = ttk.Frame(root, padding=10)  # creando un frame
frm.grid()  # agregando el frame a la ventana
root.title("Hello, World!")  # titulo de la ventana
root.geometry("300x100")
root.resizable(False, False)
ttk.Label(frm, text="Utiliza el boton quit para salir del programa").grid(
    column=0, row=3)  # creando un label con grid
ttk.Button(frm, text="Quit", command=root.destroy).grid(
    column=0, row=0)  # creando un boton con grid
root.mainloop()  # bucle principal
