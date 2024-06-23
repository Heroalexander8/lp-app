# models/usuario.py
class Usuario:
    def __init__(self, id, nombre, apellido, email, dni, celular, rol):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.dni = dni
        self.celular = celular
        self.rol = rol
