
import sqlite3


class DatabaseManager:
    def __init__(self, db_path):
        self.db_path = "./Biblioteca"

    def connect(self):
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()

    def close(self):
        self.conn.close()

    def execute(self, query, params=()):
        self.connect()
        self.cursor.execute(query, params)
        self.conn.commit()
        self.close()

    def fetchall(self, query, params=()):
        self.connect()
        self.cursor.execute(query, params)
        results = self.cursor.fetchall()
        self.close()
        return results

    def fetchone(self, query, params=()):
        self.connect()
        self.cursor.execute(query, params)
        result = self.cursor.fetchone()
        self.close()
        return result

    # Métodos específicos para la tabla libro
    def add_libro(self, titulo, autor_id, genero, anio_publicacion):
        self.execute("INSERT INTO libro (titulo, autor_id, genero, anio_publicacion) VALUES (?, ?, ?, ?)",
                     (titulo, autor_id, genero, anio_publicacion))

    def get_all_libros(self):
        return self.fetchall("SELECT * FROM libro")

    # Métodos específicos para la tabla autores
    def add_autor(self, nombre, apellido):
        self.execute(
            "INSERT INTO autores (nombre, apellido) VALUES (?, ?)", (nombre, apellido))

    def get_all_autores(self):
        return self.fetchall("SELECT * FROM autores")

    # Métodos específicos para la tabla prestamos
    def add_prestamo(self, fecha_prestamo, fecha_entrega, libros_idlibro, usuarios_idusuario):
        self.execute("INSERT INTO prestamos (fecha_prestamo, fecha_entrega, libros_idlibro, usuarios_idusuario) VALUES (?, ?, ?, ?)",
                     (fecha_prestamo, fecha_entrega, libros_idlibro, usuarios_idusuario))

    def get_all_prestamos(self):
        return self.fetchall("SELECT * FROM prestamos")

    def delete_autor(self, id):
        self.execute("DELETE FROM autores WHERE id_autor = ?", (id,))

    def delete_libro(self, id):
        self.execute("DELETE FROM libro WHERE id_libro = ?", (id,))

    def delete_prestamo(self, id):
        self.execute("DELETE FROM prestamos WHERE id_prestamo = ?", (id,))
