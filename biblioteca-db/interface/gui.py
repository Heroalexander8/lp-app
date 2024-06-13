
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

    def view_books(self):
        libros = self.db_manager.get_all_libros()
        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Ver Libros")

        for libro in libros:
            libro_label = tk.Label(
                self.new_window, text=f"Título: {libro[1]}, Autor ID: {libro[2]}, Género: {libro[3]}, Año: {libro[4]}")
            libro_label.pack()
