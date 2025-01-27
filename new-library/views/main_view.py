import tkinter as tk
from tkinter import ttk
from controllers.libro_controller import LibroController
from controllers.usuario_controller import UsuarioController
from controllers.prestamo_controller import PrestamoController
from controllers.categoria_controller import CategoriaController
from controllers.rol_controller import RolController

from views.libro_view import LibroView
from views.usuario_view import UsuarioView
from views.prestamo_view import PrestamoView
from views.categoria_view import CategoriaView
from views.rol_view import RolView




class MainView:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Biblioteca")

        self.libro_controller = LibroController('./Biblioteca')
        self.usuario_controller = UsuarioController('./Biblioteca')
        self.prestamo_controller = PrestamoController('./Biblioteca')
        self.categoria_controller = CategoriaController('./Biblioteca')
        self.rol_controller = RolController('./Biblioteca')
        self.create_widgets()

    def create_widgets(self):
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill='both')

        # Frame y vista de Libros
        self.frame_libros = ttk.Frame(self.notebook)
        self.notebook.add(self.frame_libros, text='Libros')
        self.libro_view = LibroView(self.frame_libros, self.libro_controller)

        # Frame y vista de Usuarios
        self.frame_usuarios = ttk.Frame(self.notebook)
        self.notebook.add(self.frame_usuarios, text='Usuarios')
        self.usuario_view = UsuarioView(self.frame_usuarios, self.usuario_controller)

        # Frame y vista de Préstamos
        self.frame_prestamos = ttk.Frame(self.notebook)
        self.notebook.add(self.frame_prestamos, text='Préstamos')
        self.prestamo_view = PrestamoView(self.frame_prestamos, self.prestamo_controller)

        # Frame y vista de Categorías
        self.frame_categorias = ttk.Frame(self.notebook)
        self.notebook.add(self.frame_categorias, text='Categorías')
        self.categoria_view = CategoriaView(self.frame_categorias, self.categoria_controller)

        # Frame y vista de Roles
        self.frame_roles = ttk.Frame(self.notebook)
        self.notebook.add(self.frame_roles, text='Roles')
        self.rol_view = RolView(self.frame_roles, self.rol_controller)

if __name__ == '__main__':
    root = tk.Tk()
    app = MainView(root)
    root.mainloop()
