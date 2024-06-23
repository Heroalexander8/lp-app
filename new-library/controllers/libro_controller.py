# controllers/libro_controller.py
import sqlite3
from models.libro import Libro

class LibroController:
    def __init__(self, db_path):
        self.db_path = db_path

    def obtener_libros(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM libros")
        libros = [Libro(*row) for row in cursor.fetchall()]
        conn.close()
        return libros

    def agregar_libro(self, titulo, autor, genero, año):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO libros (titulo, autor, genero, año) VALUES (?, ?, ?, ?)",
                       (titulo, autor, genero, año))
        conn.commit()
        conn.close()

    def actualizar_libro(self, id, titulo, autor, genero, año):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("UPDATE libros SET titulo=?, autor=?, genero=?, año=? WHERE id=?",
                       (titulo, autor, genero, año, id))
        conn.commit()
        conn.close()

    def eliminar_libro(self, id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM libros WHERE id=?", (id,))
        conn.commit()
        conn.close()
