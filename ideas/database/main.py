import sqlite3

# tabla usuario

# Creación de tabla
# abrir conexion
#   apuntador o curssos
#   ejecución de la sentencia
#   comprometer
# fin de conexión 

def crear_tabla_estudiante():
    conexion = sqlite3.connect("estudiantes.db")
    cursor = conexion.cursor()
    cursor.execute("CREATE TABLE estudiante (id INTEGER PRIMARY KEY, nombre TEXT, semestre INTEGER, email TEXT)")
    conexion.commit()
    conexion.close()
    
def insertar_estudiante(nombre, edad, email):
    conexion = sqlite3.connect("estudiantes.db")
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO estudiante (nombre, semestre, email) VALUES (?, ?, ?)", (nombre, semestre, email))
    conexion.commit()
    conexion.close()
    
def obtener_estudiantes():
    conexion = sqlite3.connect("estudiantes.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM estudiante")
    estudiantes = cursor.fetchall()
    conexion.close()
    return estudiantes

def obtener_estudiante_por_id(id):
    conexion = sqlite3.connect("estudiantes.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM estudiante WHERE id = ?", (id,))
    estudiante = cursor.fetchone()
    conexion.close()
    return estudiante

def actualizar_estudiante(id, nombre, semestre, email):
    conexion = sqlite3.connect("estudiantes.db")
    cursor = conexion.cursor()
    cursor.execute("UPDATE estudiante SET nombre = ?, semestre = ?, email = ? WHERE id = ?", (nombre, semestre, email, id))
    conexion.commit()
    conexion.close()
    
def eliminar_estudiante(id):
    conexion = sqlite3.connect("estudiantes.db")
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM estudiante WHERE id = ?", (id,))
    conexion.commit()
    conexion.close()
    


def crear_tabla_usuario():
    conexion = sqlite3.connect("usuarios.db")
    cursor = conexion.cursor()
    cursor.execute(
        "CREATE TABLE usuario (id INTEGER PRIMARY KEY, nombre TEXT, edad INTEGER, email TEXT)")
    conexion.commit()
    conexion.close()

# crear, leer, actualizar y borrar CRUD
def insertar_usuario(nombre, edad, email):
    conexion = sqlite3.connect("usuarios.db")
    cursor = conexion.cursor()
    cursor.execute(
        "INSERT INTO usuario (nombre, edad, email) VALUES (?, ?, ?)", (nombre, edad, email))
    conexion.commit()
    conexion.close()


def obtener_usuarios():
    conexion = sqlite3.connect("usuarios.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM usuario")
    usuarios = cursor.fetchall()
    conexion.close()
    return usuarios


def obtener_usuario_por_id(id):
    conexion = sqlite3.connect("usuarios.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM usuario WHERE id = ?", (id,))
    usuario = cursor.fetchone()
    conexion.close()
    return usuario


def actualizar_usuario(id, nombre, edad, email):
    conexion = sqlite3.connect("usuarios.db")
    cursor = conexion.cursor()
    cursor.execute(
        "UPDATE usuario SET nombre = ?, edad = ?, email = ? WHERE id = ?", (nombre, edad, email, id))
    conexion.commit()
    conexion.close()


def eliminar_usuario(id):
    conexion = sqlite3.connect("usuarios.db")
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM usuario WHERE id = ?", (id,))
    conexion.commit()
    conexion.close()




# Relacionar estudiante con usuario

def relacionar_estudiante_usuario(id_estudiante, id_usuario):
    conexion = sqlite3.connect("estudiantes.db")
    cursor = conexion.cursor()
    cursor.execute("UPDATE estudiante SET id_usuario = ? WHERE id = ?", (id_usuario, id_estudiante))
    conexion.commit()
    conexion.close()
    
def obtener_estudiante_con_usuario():
    conexion = sqlite3.connect("estudiantes.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM estudiante")
    estudiantes = cursor.fetchall()
    conexion.close()
    return estudiantes

def obtener_estudiante_con_usuario_por_id(id):
    conexion = sqlite3.connect("estudiantes.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM estudiante WHERE id = ?", (id,))
    estudiante = cursor.fetchone()
    conexion.close()
    return estudiante

crear_tabla_estudiante()

