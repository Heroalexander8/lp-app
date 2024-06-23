# views/prestamo_view.py
import tkinter as tk
from tkinter import ttk
from controllers.prestamo_controller import PrestamoController


class PrestamoView:
    def __init__(self, root, prestamo_controller):
        self.root = root
        self.prestamo_controller = prestamo_controller
        self.create_widgets()
        self.cargar_prestamos()

    def create_widgets(self):
        self.tree = ttk.Treeview(self.root, columns=(
            "ID", "FechaPrestamo", "FechaEntrega", "IDLibro", "IDUsuario", "Devuelto"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("FechaPrestamo", text="Fecha Préstamo")
        self.tree.heading("FechaEntrega", text="Fecha Entrega")
        self.tree.heading("IDLibro", text="ID Libro")
        self.tree.heading("IDUsuario", text="ID Usuario")
        self.tree.heading("Devuelto", text="Devuelto")
        self.tree.pack(expand=True, fill='both')

        self.btn_nuevo = ttk.Button(
            self.root, text="Nuevo Préstamo", command=self.nuevo_prestamo)
        self.btn_nuevo.pack(side="left")

        self.btn_actualizar = ttk.Button(
            self.root, text="Actualizar Préstamo", command=self.actualizar_prestamo)
        self.btn_actualizar.pack(side="left")

        self.btn_eliminar = ttk.Button(
            self.root, text="Eliminar Préstamo", command=self.eliminar_prestamo)
        self.btn_eliminar.pack(side="left")

    def cargar_prestamos(self):
        for prestamo in self.prestamo_controller.obtener_prestamos():
            self.tree.insert('', 'end', values=(prestamo.id, prestamo.fecha_prestamo,
                             prestamo.fecha_entrega, prestamo.id_libro, prestamo.id_usuario, prestamo.devuelto))

    def nuevo_prestamo(self):
        # Aquí iría la lógica para añadir un nuevo préstamo
        pass

    def actualizar_prestamo(self):
        # Aquí iría la lógica para actualizar un préstamo existente
        pass

    def eliminar_prestamo(self):
        # Aquí iría la lógica para eliminar un préstamo
        pass
