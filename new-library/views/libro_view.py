# views/libro_view.py
import tkinter as tk
from tkinter import ttk
from controllers.libro_controller import LibroController


class LibroView:
    def __init__(self, root, libro_controller):
        self.root = root
        self.libro_controller = libro_controller
        self.create_widgets()
        self.cargar_libros()

    def create_widgets(self):
        self.tree = ttk.Treeview(self.root, columns=(
            "ID", "Titulo", "Autor", "Genero", "Año"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Titulo", text="Titulo")
        self.tree.heading("Autor", text="Autor")
        self.tree.heading("Genero", text="Genero")
        self.tree.heading("Año", text="Año")
        self.tree.pack(expand=True, fill='both')

        self.btn_nuevo = ttk.Button(
            self.root, text="Nuevo Libro", command=self.nuevo_libro)
        self.btn_nuevo.pack(side="left")

        self.btn_actualizar = ttk.Button(
            self.root, text="Actualizar Libro", command=self.actualizar_libro)
        self.btn_actualizar.pack(side="left")

        self.btn_eliminar = ttk.Button(
            self.root, text="Eliminar Libro", command=self.eliminar_libro)
        self.btn_eliminar.pack(side="left")

    def cargar_libros(self):
        for libro in self.libro_controller.obtener_libros():
            self.tree.insert('', 'end', values=(
                libro.id, libro.titulo, libro.autor, libro.genero, libro.año))

    def nuevo_libro(self):
        # logica para nuevo libro
        self.nuevo_libro = tk.Toplevel(self.root)
        self.nuevo_libro.title("Nuevo Libro")
        self.nuevo_libro.geometry("400x400")
        self.nuevo_libro.transient(self.root)
        self.nuevo_libro.grab_set()

        titulo = self.nuevo_libro.Label(self.nuevo_libro, text="Titulo")
        titulo.pack()
        self.entry_titulo = self.nuevo_libro.Entry(self.nuevo_libro)
        self.entry_titulo.pack()

        autor = self.nuevo_libro.Label(self.nuevo_libro, text="Autor")
        autor.pack()
        self.entry_autor = self.nuevo_libro.Entry(self.nuevo_libro)
        self.entry_autor.pack()

        genero = self.nuevo_libro.Label(self.nuevo_libro, text="Genero")
        genero.pack()
        self.entry_genero = self.nuevo_libro.Entry(self.nuevo_libro)
        self.entry_genero.pack()

        año = self.nuevo_libro.Label(self.nuevo_libro, text="Año")
        año.pack()
        self.entry_año = self.nuevo_libro.Entry(self.nuevo_libro)
        self.entry_año.pack()

        btn_guardar = self.nuevo_libro.Button(
            self.nuevo_libro, text="Guardar", command=self.guardar_libro)
        btn_guardar.pack()

    def actualizar_libro(self):
        # logica para actualizar libro
        self.actualizar_libro = tk.Toplevel(self.root)
        self.actualizar_libro.title("Actualizar Libro")
        self.actualizar_libro.geometry("400x400")
        self.actualizar_libro.transient(self.root)
        self.actualizar_libro.grab_set()

        titulo = self.actualizar_libro.Label(
            self.actualizar_libro, text="Titulo")
        titulo.pack()
        self.entry_titulo = self.actualizar_libro.Entry(self.actualizar_libro)
        self.entry_titulo.pack()

        autor = self.actualizar_libro.Label(
            self.actualizar_libro, text="Autor")
        autor.pack()
        self.entry_autor = self.actualizar_libro.Entry(self.actualizar_libro)
        self.entry_autor.pack()

        genero = self.actualizar_libro.Label(
            self.actualizar_libro, text="Genero")
        genero.pack()
        self.entry_genero = self.actualizar_libro.Entry(self.actualizar_libro)
        self.entry_genero.pack()

        año = self.actualizar_libro.Label(self.actualizar_libro, text="Año")
        año.pack()
        self.entry_año = self.actualizar_libro.Entry(self.actualizar_libro)
        self.entry_año.pack()

        btn_actualizar = self.actualizar_libro.Button(
            self.actualizar_libro, text="Actualizar", command=self.actualizar)

    def eliminar_libro(self):
        # logica para eliminar libro
        self.eliminar_libro = tk.Toplevel(self.root)
        self.eliminar_libro.title("Eliminar Libro")
        self.eliminar_libro.geometry("400x400")
        self.eliminar_libro.transient(self.root)
        self.eliminar_libro.grab_set()

        titulo = self.eliminar_libro.Label(
            self.eliminar_libro, text="Titulo")
        titulo.pack()
        self.entry_titulo = self.eliminar_libro.Entry(self.eliminar_libro)
        self.entry_titulo.pack()

        btn_eliminar = self.eliminar_libro.Button(
            self.eliminar_libro, text="Eliminar", command=self.eliminar)

    def guardar_libro(self):
        titulo = self.entry_titulo.get()
        autor = self.entry_autor.get()
        genero = self.entry_genero.get()
        año = self.entry_año.get()
        self.libro_controller.guardar_libro(titulo, autor, genero, año)

    def actualizar(self):
        titulo = self.entry_titulo.get()
        autor = self.entry_autor.get()
        genero = self.entry_genero.get()
        año = self.entry_año.get()
        self.libro_controller.actualizar_libro(titulo, autor, genero, año)

    def eliminar(self):
        titulo = self.entry_titulo.get()
        self.libro_controller.eliminar_libro(titulo)
