# views/categoria_view.py
import tkinter as tk
from tkinter import ttk
from controllers.categoria_controller import CategoriaController

class CategoriaView:
    def __init__(self, root, categoria_controller):
        self.root = root
        self.categoria_controller = categoria_controller
        self.create_widgets()
        self.cargar_categorias()

    def create_widgets(self):
        self.tree = ttk.Treeview(self.root, columns=(
            "ID", "Nombre"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.pack(expand=True, fill='both')

        self.btn_nueva = ttk.Button(
            self.root, text="Nueva Categoria", command=self.nueva_categoria)
        self.btn_nueva.pack(side="left")

        self.btn_actualizar = ttk.Button(
            self.root, text="Actualizar Categoria", command=self.actualizar_categoria)
        self.btn_actualizar.pack(side="left")

        self.btn_eliminar = ttk.Button(
            self.root, text="Eliminar Categoria", command=self.eliminar_categoria)
        self.btn_eliminar.pack(side="left")

    def cargar_categorias(self):
        for categoria in self.categoria_controller.obtener_categorias():
            self.tree.insert('', 'end', values=(
                categoria.id, categoria.nombre))

    def nueva_categoria(self):
        self.nueva_categoria_window = tk.Toplevel(self.root)
        self.nueva_categoria_window.title("Nueva Categoria")
        self.nueva_categoria_window.geometry("200x200")

        self.lbl_nombre = ttk.Label(self.nueva_categoria_window, text="Nombre")
        self.lbl_nombre.pack()
        self.entry_nombre = ttk.Entry(self.nueva_categoria_window)
        self.entry_nombre.pack()

    def actualizar_categoria(self):
        self.actualizar_categoria_window = tk.Toplevel(self.root)
        self.actualizar_categoria_window.title("Actualizar Categoria")
        self.actualizar_categoria_window.geometry("200x200")

        self.lbl_nombre = ttk.Label(self.actualizar_categoria_window, text="Nombre")
        self.lbl_nombre.pack()
        self.entry_nombre = ttk.Entry(self.actualizar_categoria_window)
        self.entry_nombre.pack()

    def eliminar_categoria(self):
        self.eliminar_categoria_window = tk.Toplevel(self.root)
        self.eliminar_categoria_window.title("Eliminar Categoria")
        self.eliminar_categoria_window.geometry("200x200")

        self.lbl_id = ttk.Label(self.eliminar_categoria_window, text="ID")
        self.lbl_id.pack()
        self.entry_id = ttk.Entry(self.eliminar_categoria_window)
        self.entry