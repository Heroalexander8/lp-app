# views/main_view.py
import tkinter as tk
from tkinter import ttk
from controllers.libro_controller import LibroController
from controllers.usuario_controller import UsuarioController
from controllers.prestamo_controller import PrestamoController
from views.libro_view import LibroView
from views.usuario_view import UsuarioView
from views.prestamo_view import PrestamoView


class MainView:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Biblioteca")

        self.libro_controller = LibroController('database/Biblioteca')
        self.usuario_controller = UsuarioController('database/Biblioteca')
        self.prestamo_controller = PrestamoController('database/Biblioteca')

        self.create_widgets()

    def create_widgets(self):
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill='both')

        self.frame_libros = ttk.Frame(self.notebook)
        self.frame_usuarios = ttk.Frame(self.notebook)
        self.frame_prestamos = ttk.Frame(self.notebook)

        self.notebook.add(self.frame_libros, text='Libros')
        self.notebook.add(self.frame_usuarios, text='Usuarios')
        self.notebook.add(self.frame_prestamos, text='Préstamos')

        # Crear las vistas específicas para cada pestaña
        self.libro_view = LibroView(self.frame_libros, self.libro_controller)
        self.usuario_view = UsuarioView(
            self.frame_usuarios, self.usuario_controller)
        self.prestamo_view = PrestamoView(
            self.frame_prestamos, self.prestamo_controller)


if __name__ == '__main__':
    root = tk.Tk()
    app = MainView(root)
    root.mainloop()
