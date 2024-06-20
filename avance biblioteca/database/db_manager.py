import sqlite3
from sqlite3 import Error


class DatabaseManager:
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = None
        self.create_connection()

    def create_connection(self):
        db_file = self.db_file
        try:
            self.conn = sqlite3.connect(self.db_file)
        except Error as e:
            print(e)

    def get_all_books(self):
        query = "SELECT * FROM libro"
        cur = self.conn.cursor()
        cur.execute(query)
        return cur.fetchall()

    def get_all_authors(self):
        query = "SELECT * FROM autores"
        cur = self.conn.cursor()
        cur.execute(query)
        return cur.fetchall()

    def get_all_loans(self):
        query = "SELECT * FROM prestamos"
        cur = self.conn.cursor()
        cur.execute(query)
        return cur.fetchall()

    def search_book(self, id_libro, titulo):
        query = "SELECT * FROM libro WHERE id_libro = ? OR titulo LIKE ?"
        cur = self.conn.cursor()
        cur.execute(query, (id_libro, f'%{titulo}%'))
        return cur.fetchall()

    def search_book_by_id(self, id_libro):
        query = "SELECT * FROM libro WHERE id_libro = ?"
        cur = self.conn.cursor()
        cur.execute(query, (id_libro,))
        return cur.fetchall()

    def add_book(self, titulo, id_autor, genero, anio_publicacion):
        query = "INSERT INTO libro (titulo, autor_id, genero, anio_publicacion) VALUES (?, ?, ?, ?)"
        cur = self.conn.cursor()
        cur.execute(query, (titulo, id_autor, genero, anio_publicacion))
        self.conn.commit()

    def add_author(self, nombre, apellido):
        query = "INSERT INTO autores (nombre_autor, apellido_autor) VALUES (?, ?)"
        cur = self.conn.cursor()
        cur.execute(query, (nombre, apellido))
        self.conn.commit()

    def add_loan(self, fecha_prestamo, fecha_entrega, libros_idlibro):
        query = "INSERT INTO prestamos (fecha_prestamo, fecha_entrega, libros_idlibro) VALUES (?, ?, ?)"
        cur = self.conn.cursor()
        cur.execute(query, (fecha_prestamo, fecha_entrega, libros_idlibro))
        self.conn.commit()

    def delete_loan(self, id_prestamo):
        query = "DELETE FROM prestamos WHERE id_prestamo = ?"
        cur = self.conn.cursor()
        cur.execute(query, (id_prestamo,))
        self.conn.commit()
