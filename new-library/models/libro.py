# models/libro.py
class Libro:
    def __init__(self, id, titulo, autor, genero, año):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.año = año
