
import tkinter as tk
from tkinter import messagebox
from database.db_manager import DatabaseManager


class LibraryGUI:
    def __init__(self, root, db_manager):
        self.root = root
        self.db_manager = db_manager
        self.root.title("Biblioteca")
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Bienvenido a la Biblioteca")
        self.label.pack()

        self.add_book_button = tk.Button(
            self.root, text="Añadir Libro", command=self.add_book)
        self.add_book_button.pack()

        self.view_books_button = tk.Button(
            self.root, text="Ver Libros", command=self.view_books)
        self.view_books_button.pack()

        self.prestamo_button = tk.Button(
            self.root, text="Prestamo", command=self.prestamo)
        self.prestamo_button.pack()

        self.anadir_autor_button = tk.Button(
            self.root, text="Añadir Autor", command=self.anadir_autor)
        self.anadir_autor_button.pack()

        self.view_authors_button = tk.Button(
            self.root, text="Ver Autores", command=self.view_authors)
        self.view_authors_button.pack()

        self.view_prestamos_button = tk.Button(
            self.root, text="Ver Prestamos", command=self.view_prestamos)
        self.view_prestamos_button.pack()

        self.eliminar_libro_button = tk.Button(
            self.root, text="Eliminar Libro", command=self.eliminar_libro)
        self.eliminar_libro_button.pack()

        self.eliminar_autor_button = tk.Button(
            self.root, text="Eliminar Autor", command=self.eliminar_autor)
        self.eliminar_autor_button.pack()

        self.eliminar_prestamo_button = tk.Button(
            self.root, text="Eliminar Prestamo", command=self.eliminar_prestamo)
        self.eliminar_prestamo_button.pack()

        self.exit_button = tk.Button(
            self.root, text="Salir", command=self.root.quit)

    def add_book(self):
        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Añadir Libro")

        self.title_label = tk.Label(self.new_window, text="Título")
        self.title_label.pack()
        self.title_entry = tk.Entry(self.new_window)
        self.title_entry.pack()

        self.author_label = tk.Label(self.new_window, text="Autor")
        self.author_label.pack()
        self.author_entry = tk.Entry(self.new_window)
        self.author_entry.pack()

        self.genre_label = tk.Label(self.new_window, text="Género")
        self.genre_label.pack()
        self.genre_entry = tk.Entry(self.new_window)
        self.genre_entry.pack()

        self.year_label = tk.Label(self.new_window, text="Año de Publicación")
        self.year_label.pack()
        self.year_entry = tk.Entry(self.new_window)
        self.year_entry.pack()

        self.submit_button = tk.Button(
            self.new_window, text="Añadir", command=self.submit_book)
        self.submit_button.pack()

    def submit_book(self):
        titulo = self.title_entry.get()
        autor_id = self.author_entry.get()
        genero = self.genre_entry.get()
        anio_publicacion = self.year_entry.get()
        if titulo and autor_id and genero and anio_publicacion:
            self.db_manager.add_libro(
                titulo, autor_id, genero, anio_publicacion)
            messagebox.showinfo("Éxito", "Libro añadido correctamente")
            self.new_window.destroy()
        else:
            messagebox.showwarning(
                "Error", "Todos los campos son obligatorios")

    def submit_author(self):
        nombre = self.title_entry.get()
        apellido = self.author_entry.get()
        if nombre and apellido:
            self.db_manager.add_autor(nombre, apellido)
            messagebox.showinfo("Éxito", "Autor añadido correctamente")
            self.new_window.destroy()
        else:
            messagebox.showwarning(
                "Error", "Todos los campos son obligatorios")

    def submit_prestamo(self):
        titulo = self.title_entry.get()
        autor = self.author_entry.get()
        genero = self.genre_entry.get()
        anio_publicacion = self.year_entry.get()
        if titulo and autor and genero and anio_publicacion:
            self.db_manager.add_libro(
                titulo, autor, genero, anio_publicacion)
            messagebox.showinfo("Éxito", "Libro añadido correctamente")
            self.new_window.destroy()
        else:
            messagebox.showwarning(
                "Error", "Todos los campos son obligatorios")

    def prestamo(self):
        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Prestamo")
        self.title_label = tk.Label(self.new_window, text="Título")
        self.title_label.pack()
        self.title_entry = tk.Entry(self.new_window)
        self.title_entry.pack()
        self.author_label = tk.Label(self.new_window, text="Autor")
        self.author_label.pack()
        self.author_entry = tk.Entry(self.new_window)
        self.author_entry.pack()
        self.genre_label = tk.Label(self.new_window, text="Género")
        self.genre_label.pack()
        self.genre_entry = tk.Entry(self.new_window)
        self.genre_entry.pack()
        self.year_label = tk.Label(self.new_window, text="Año de Publicación")
        self.year_label.pack()
        self.year_entry = tk.Entry(self.new_window)
        self.year_entry.pack()
        self.submit_button = tk.Button(
            self.new_window, text="Añadir", command=self.submit_prestamo)
        self.submit_button.pack()

    def anadir_autor(self):
        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Añadir Autor")
        self.title_label = tk.Label(self.new_window, text="Nombre")
        self.title_label.pack()
        self.title_entry = tk.Entry(self.new_window)
        self.title_entry.pack()
        self.author_label = tk.Label(self.new_window, text="Apellido")
        self.author_label.pack()
        self.author_entry = tk.Entry(self.new_window)
        self.author_entry.pack()
        self.submit_button = tk.Button(
            self.new_window, text="Añadir", command=self.submit_author)
        self.submit_button.pack()

    def view_authors(self):
        autores = self.db_manager.get_all_autores()
        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Ver Autores")
        for autor in autores:
            autor_label = tk.Label(
                self.new_window, text=f"Código:{autor[0]}, Nombre: {autor[1]}, Apellido: {autor[2]}")
            autor_label.pack()

    def view_prestamos(self):
        prestamos = self.db_manager.get_all_prestamos()
        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Ver Prestamos")
        for prestamo in prestamos:
            prestamo_label = tk.Label(
                self.new_window, text=f"Libro ID: {prestamo[1]}, Usuario ID: {prestamo[2]}, Fecha: {prestamo[3]}")
            prestamo_label.pack()

    def view_books(self):
        libros = self.db_manager.get_all_libros()
        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Ver Libros")

        for libro in libros:
            libro_label = tk.Label(
                self.new_window, text=f"Título: {libro[1]}, Autor ID: {libro[2]}, Género: {libro[3]}, Año: {libro[4]}")
            libro_label.pack()

    def eliminar_libro(self):
        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Eliminar Libro")
        self.title_label = tk.Label(self.new_window, text="ID")
        self.title_label.pack()
        self.title_entry = tk.Entry(self.new_window)
        self.title_entry.pack()
        self.submit_button = tk.Button(
            self.new_window, text="Eliminar", command=self.submit_eliminar_libro)
        self.submit_button.pack()

    def submit_eliminar_libro(self):
        libro_id = self.title_entry.get()
        if libro_id:
            self.db_manager.delete_libro(libro_id)
            messagebox.showinfo("Éxito", "Libro eliminado correctamente")
            self.new_window.destroy()
        else:
            messagebox.showwarning(
                "Error", "Todos los campos son obligatorios")

    def eliminar_autor(self):
        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Eliminar Autor")
        self.title_label = tk.Label(self.new_window, text="ID")
        self.title_label.pack()
        self.title_entry = tk.Entry(self.new_window)
        self.title_entry.pack()
        self.submit_button = tk.Button(
            self.new_window, text="Eliminar", command=self.submit_eliminar_autor)
        self.submit_button.pack()

    def submit_eliminar_autor(self):
        autor_id = self.title_entry.get()
        if autor_id:
            self.db_manager.delete_autor(autor_id)
            messagebox.showinfo("Éxito", "Autor eliminado correctamente")
            self.new_window.destroy()
        else:
            messagebox.showwarning(
                "Error", "Todos los campos son obligatorios")

    def eliminar_prestamo(self):
        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Eliminar Prestamo")
        self.title_label = tk.Label(self.new_window, text="ID")
        self.title_label.pack()
        self.title_entry = tk.Entry(self.new_window)
        self.title_entry.pack()
        self.submit_button = tk.Button(
            self.new_window, text="Eliminar", command=self.submit_eliminar_prestamo)
        self.submit_button.pack()

    def submit_eliminar_prestamo(self):
        prestamo_id = self.title_entry.get()
        if prestamo_id:
            self.db_manager.delete_prestamo(prestamo_id)
            messagebox.showinfo("Éxito", "Prestamo eliminado correctamente")
            self.new_window.destroy()
        else:
            messagebox.showwarning(
                "Error", "Todos los campos son obligatorios")
