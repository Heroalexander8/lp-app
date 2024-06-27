# views/rol_view.py
import tkinter as tk
from tkinter import ttk
from controllers.rol_controller import RolController

class RolView:
    def __init__(self, root, rol_controller: RolController):
        self.root = root
        self.rol_controller = rol_controller
        self.create_widgets()
        self.cargar_roles()

    def create_widgets(self):
        self.tree = ttk.Treeview(self.root, columns=("ID", "Nombre"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.pack(expand=True, fill='both')

        self.btn_nuevo = ttk.Button(self.root, text="Nuevo Rol", command=self.nuevo_rol)
        self.btn_nuevo.pack(side="left")

        self.btn_actualizar = ttk.Button(self.root, text="Actualizar Rol", command=self.actualizar_rol)
        self.btn_actualizar.pack(side="left")

        self.btn_eliminar = ttk.Button(self.root, text="Eliminar Rol", command=self.eliminar_rol)
        self.btn_eliminar.pack(side="left")

    def cargar_roles(self):
        for rol in self.rol_controller.obtener_roles():
            self.tree.insert('', 'end', values=(rol.id, rol.nombre))

    def nuevo_rol(self):
        # Aquí iría la lógica para añadir un nuevo rol
        pass
    
    def actualizar_rol(self):
        # Aquí iría la lógica para actualizar un rol existente
        pass

    def eliminar_rol(self):
        # Aquí iría la lógica para eliminar un rol
        pass