# models/prestamo.py
class Prestamo:
    def __init__(self, id, fecha_prestamo, fecha_entrega, id_libro, id_usuario, devuelto):
        self.id = id
        self.fecha_prestamo = fecha_prestamo
        self.fecha_entrega = fecha_entrega
        self.id_libro = id_libro
        self.id_usuario = id_usuario
        self.devuelto = devuelto
