# views/usuario_view.py
import tkinter as tk
from tkinter import ttk
from controllers.usuario_controller import UsuarioController

class UsuarioView:
    def __init__(self, root, usuario_controller):
        self.root = root
        self.usuario_controller = usuario_controller
        self.create_widgets()
        self.cargar_usuarios()

    def create_widgets(self):
        self.tree = ttk.Treeview(self.root, columns=("ID", "Nombre", "Apellido", "Email", "DNI", "Celular", "Rol"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Apellido", text="Apellido")
        self.tree.heading("Email", text="Email")
        self.tree.heading("DNI", text="DNI")
        self.tree.heading("Celular", text="Celular")
        self.tree.heading("Rol", text="Rol")
        self.tree.pack(expand=True, fill='both')
        
        self.btn_nuevo = ttk.Button(self.root, text="Nuevo Usuario", command=self.nuevo_usuario)
        self.btn_nuevo.pack(side="left")
        
        self.btn_actualizar = ttk.Button(self.root, text="Actualizar Usuario", command=self.actualizar_usuario)
        self.btn_actualizar.pack(side="left")
        
        self.btn_eliminar = ttk.Button(self.root, text="Eliminar Usuario", command=self.eliminar_usuario)
        self.btn_eliminar.pack(side="left")

    def cargar_usuarios(self):
        for usuario in self.usuario_controller.obtener_usuarios():
            self.tree.insert('', 'end', values=(usuario.id, usuario.nombre, usuario.apellido, usuario.email, usuario.dni, usuario.celular, usuario.rol))

    def nuevo_usuario(self):
        # Aquí iría la lógica para añadir un nuevo usuario
        pass

    def actualizar_usuario(self):
        # Aquí iría la lógica para actualizar un usuario existente
        pass

    def eliminar_usuario(self):
        # Aquí iría la lógica para eliminar un usuario
        pass
