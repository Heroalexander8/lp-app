
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Lista de Compras")
root.geometry("300x500")

root.iconbitmap("./icons/shop.ico")

label_producto = tk.Label(root, text="Producto:")
label_producto.pack()

entry_producto = tk.Entry(root)
entry_producto.pack()

label_precio = tk.Label(root, text="Precio:")
label_precio.pack()
entry_precio = tk.Entry(root)
entry_precio.pack()

label_lista_productos = tk.Label(root, text="Lista de Productos")
label_lista_productos.pack()
lista_productos = tk.Listbox(root)
lista_productos.pack()


def agregar():
    producto = entry_producto.get()
    precio = entry_precio.get()
    if producto != "" and precio != "":
        lista_productos.insert(tk.END, producto + " - " + precio)
        entry_producto.delete(0, tk.END)
        entry_precio.delete(0, tk.END)
    else:
        messagebox.showwarning(
            "Error", "Debe ingresar un producto y su precio")


def total():
    total = 0
    for producto in lista_productos.get(0, tk.END):
        total += float(producto.split(" - ")[1])
    messagebox.showinfo("Total", "El total de la compra es: S/." + str(total))


def igv():
    igv = 0
    for producto in lista_productos.get(0, tk.END):
        igv += float(producto.split(" - ")[1])
    messagebox.showinfo("IGV", "El IGV de la compra es: S/." + str(igv*0.18))


def subtotal():
    subtotal = 0
    for producto in lista_productos.get(0, tk.END):
        subtotal += float(producto.split(" - ")[1])
    messagebox.showinfo(
        "Subtotal", "El subtotal de la compra es: S/." + str(subtotal*0.82))


boton_agregar = tk.Button(root, text="Agregar", command=agregar)
boton_agregar.pack()

lbl_subtotal = tk.Button(root, text="Subtotal", command=subtotal)
lbl_subtotal.pack()

lbl_igv = tk.Button(root, text="IGV", command=igv)
lbl_igv.pack()


boton_total = tk.Button(root, text="Total", command=total)
boton_total.pack()

boton_limpiar = tk.Button(root, text="Limpiar",
                          command=lambda: lista_productos.delete(0, tk.END))
boton_limpiar.pack()

boton_salir = tk.Button(root, text="Salir", command=root.quit)
boton_salir.pack()

root.mainloop()
