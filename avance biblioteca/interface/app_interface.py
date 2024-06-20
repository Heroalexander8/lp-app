import tkinter as tk
from tkinter import ttk, messagebox
from database.db_manager import DatabaseManager


class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Biblioteca")
        self.db_manager = DatabaseManager("./Biblioteca")
        self.db_manager.create_connection()
        self.create_widgets()

    def create_widgets(self):
        # Menu superior
        self.menu_frame = tk.Frame(self.root)
        self.menu_frame.pack(fill=tk.X)

        self.btn_ver_todos_libros = tk.Button(
            self.menu_frame, text="Ver todos los libros", command=self.ver_todos_libros)
        self.btn_ver_todos_libros.pack(side=tk.LEFT)

        self.btn_ver_autores = tk.Button(
            self.menu_frame, text="Ver todos los autores", command=self.ver_autores)
        self.btn_ver_autores.pack(side=tk.LEFT)

        self.btn_ver_prestamos = tk.Button(
            self.menu_frame, text="Ver todos los préstamos", command=self.ver_prestamos)
        self.btn_ver_prestamos.pack(side=tk.LEFT)

        self.btn_salir = tk.Button(
            self.menu_frame, text="Salir", command=self.root.quit)
        self.btn_salir.pack(side=tk.RIGHT)

        # Sección izquierda
        self.left_frame = tk.Frame(self.root, bd=2, relief=tk.SUNKEN)
        self.left_frame.pack(side=tk.LEFT, fill=tk.Y)

        # Buscar libro
        self.buscar_libro_frame = tk.LabelFrame(
            self.left_frame, text="Buscar Libro")
        self.buscar_libro_frame.pack(fill=tk.X, padx=10, pady=5)

        self.label_id_libro = tk.Label(self.buscar_libro_frame, text="Por ID")
        self.label_id_libro.pack()

        self.entry_id_libro = tk.Entry(self.buscar_libro_frame)
        self.entry_id_libro.pack()

        self.label_titulo = tk.Label(
            self.buscar_libro_frame, text="Por Nombre")
        self.label_titulo.pack()

        self.entry_titulo = tk.Entry(self.buscar_libro_frame)
        self.entry_titulo.pack()

        self.btn_buscar = tk.Button(
            self.buscar_libro_frame, text="Buscar Libro por nombre", command=self.buscar_libro)
        self.btn_buscar.pack()

        self.btn_buscar_por_id = tk.Button(
            self.buscar_libro_frame, text="Buscar Libro por ID", command=self.buscar_libro_por_id)
        self.btn_buscar_por_id.pack()

        # Agregar libro
        self.agregar_libro_frame = tk.LabelFrame(
            self.left_frame, text="Agregar Libro")
        self.agregar_libro_frame.pack(fill=tk.X, padx=10, pady=5)

        self.label_titulo_agregar = tk.Label(
            self.agregar_libro_frame, text="Título")
        self.label_titulo_agregar.pack()

        self.entry_titulo_agregar = tk.Entry(self.agregar_libro_frame)
        self.entry_titulo_agregar.pack()

        self.label_autor_id = tk.Label(
            self.agregar_libro_frame, text="ID Autor")
        self.label_autor_id.pack()

        self.entry_autor_id = tk.Entry(self.agregar_libro_frame)
        self.entry_autor_id.pack()

        self.label_genero = tk.Label(self.agregar_libro_frame, text="Género")
        self.label_genero.pack()

        self.entry_genero = tk.Entry(self.agregar_libro_frame)
        self.entry_genero.pack()

        self.label_anio_publicacion = tk.Label(
            self.agregar_libro_frame, text="Año Publicación")
        self.label_anio_publicacion.pack()

        self.entry_anio_publicacion = tk.Entry(self.agregar_libro_frame)
        self.entry_anio_publicacion.pack()

        

        self.btn_agregar_libro = tk.Button(
            self.agregar_libro_frame, text="Agregar Libro", command=self.agregar_libro)
        self.btn_agregar_libro.pack()

       
        
        


        # Agregar autor
        self.agregar_autor_frame = tk.LabelFrame(
            self.left_frame, text="Agregar Autor")
        self.agregar_autor_frame.pack(fill=tk.X, padx=10, pady=5)

        self.label_nombre_autor = tk.Label(
            self.agregar_autor_frame, text="Nombre Autor")
        self.label_nombre_autor.pack()

        self.entry_nombre_autor = tk.Entry(self.agregar_autor_frame)
        self.entry_nombre_autor.pack()

        self.label_apellido_autor = tk.Label(
            self.agregar_autor_frame, text="Apellido Autor")
        self.label_apellido_autor.pack()

        self.entry_apellido_autor = tk.Entry(self.agregar_autor_frame)
        self.entry_apellido_autor.pack()

        self.btn_agregar_autor = tk.Button(
            self.agregar_autor_frame, text="Agregar Autor", command=self.agregar_autor)
        self.btn_agregar_autor.pack()

        # Registrar préstamo
        self.prestamo_frame = tk.LabelFrame(self.left_frame, text="Préstamo")
        self.prestamo_frame.pack(fill=tk.X, padx=10, pady=5)

        self.label_id_libro_prestamo = tk.Label(
            self.prestamo_frame, text="ID Libro")
        self.label_id_libro_prestamo.pack()

        self.entry_id_libro_prestamo = tk.Entry(self.prestamo_frame)
        self.entry_id_libro_prestamo.pack()

        self.label_fecha_prestamo = tk.Label(
            self.prestamo_frame, text="Fecha Préstamo")
        self.label_fecha_prestamo.pack()

        self.entry_fecha_prestamo = tk.Entry(self.prestamo_frame)
        self.entry_fecha_prestamo.pack()

        self.label_fecha_entrega = tk.Label(
            self.prestamo_frame, text="Fecha Entrega")
        self.label_fecha_entrega.pack()

        self.entry_fecha_entrega = tk.Entry(self.prestamo_frame)
        self.entry_fecha_entrega.pack()

        self.btn_registrar_prestamo = tk.Button(
            self.prestamo_frame, text="Registrar Préstamo", command=self.registrar_prestamo)
        self.btn_registrar_prestamo.pack()

        # Sección derecha
        self.right_frame = tk.Frame(self.root, bd=2, relief=tk.SUNKEN)
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Resultados libros
        self.resultados_libros_frame = tk.LabelFrame(
            self.right_frame, text="Libros")
        self.resultados_libros_frame.pack(
            fill=tk.BOTH, expand=True, padx=10, pady=5)

        self.scrollbar_libros = tk.Scrollbar(self.resultados_libros_frame)
        self.scrollbar_libros.pack(side=tk.RIGHT, fill=tk.Y)

        self.treeview_libros = ttk.Treeview(self.resultados_libros_frame, columns=(
            "ID", "Título", "ID Autor", "Género", "Año"), show='headings')
        self.treeview_libros.pack(fill=tk.BOTH, expand=True)

        self.treeview_libros.heading("ID", text="ID")
        self.treeview_libros.heading("Título", text="Título")
        self.treeview_libros.heading("ID Autor", text="ID Autor")
        self.treeview_libros.heading("Género", text="Género")
        self.treeview_libros.heading("Año", text="Año")

        self.treeview_libros.config(yscrollcommand=self.scrollbar_libros.set)
        self.scrollbar_libros.config(command=self.treeview_libros.yview)

        # Resultados autores
        self.resultados_autores_frame = tk.LabelFrame(
            self.right_frame, text="Autores")
        self.resultados_autores_frame.pack(
            fill=tk.BOTH, expand=True, padx=10, pady=5)

        self.scrollbar_autores = tk.Scrollbar(self.resultados_autores_frame)
        self.scrollbar_autores.pack(side=tk.RIGHT, fill=tk.Y)

        self.treeview_autores = ttk.Treeview(self.resultados_autores_frame, columns=(
            "ID", "Nombre", "Apellido"), show='headings')
        self.treeview_autores.pack(fill=tk.BOTH, expand=True)

        self.treeview_autores.heading("ID", text="ID")
        self.treeview_autores.heading("Nombre", text="Nombre")
        self.treeview_autores.heading("Apellido", text="Apellido")

        self.treeview_autores.config(yscrollcommand=self.scrollbar_autores.set)
        self.scrollbar_autores.config(command=self.treeview_autores.yview)

        # Resultados préstamos
        self.resultados_prestamos_frame = tk.LabelFrame(
            self.right_frame, text="Préstamos")
        self.resultados_prestamos_frame.pack(
            fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        self.scrollbar_prestamos = tk.Scrollbar(self.resultados_prestamos_frame)
        self.scrollbar_prestamos.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.treeview_prestamos = ttk.Treeview(self.resultados_prestamos_frame, columns=(
            "ID Prestamo", "Fecha Préstamo", "Fecha Entrega", "ID Libro"), show='headings')

        self.treeview_prestamos.pack(fill=tk.BOTH, expand=True)
        
        self.treeview_prestamos.heading("ID Prestamo", text="ID Préstamo")
        self.treeview_prestamos.heading("Fecha Préstamo", text="Fecha Prestamo")
        self.treeview_prestamos.heading("Fecha Entrega", text="Fecha Entrega")
        self.treeview_prestamos.heading("ID Libro", text="ID Libro")
        
        self.treeview_prestamos.config(yscrollcommand=self.scrollbar_prestamos.set)
        self.scrollbar_prestamos.config(command=self.treeview_prestamos.yview)

        # Eliminar Prestamo
        
        self.eliminar_prestamo_frame = tk.LabelFrame(
            self.left_frame, text="Eliminar Prestamo")
        self.eliminar_prestamo_frame.pack(fill=tk.X, padx=10, pady=5)
        
        self.label_id_prestamo = tk.Label(
            self.eliminar_prestamo_frame, text="ID Prestamo")
        self.label_id_prestamo.pack()
        
        self.entry_id_prestamo = tk.Entry(self.eliminar_prestamo_frame)
        self.entry_id_prestamo.pack()
        
        self.btn_eliminar_prestamo = tk.Button(
            self.eliminar_prestamo_frame, text="Eliminar Prestamo", command=self.eliminar_prestamo)
        self.btn_eliminar_prestamo.pack()
        
        
    def ver_todos_libros(self):
        #limpiar libros
        for libro in self.treeview_libros.get_children():
            self.treeview_libros.delete(libro)
        libros = self.db_manager.get_all_books()
        for libro in libros:
            self.treeview_libros.insert("", "end", values=libro)
        

    def ver_autores(self):
        #limpiar autores
        for autor in self.treeview_autores.get_children():
            self.treeview_autores.delete(autor)
        autores = self.db_manager.get_all_authors()
        for autor in autores:
            self.treeview_autores.insert("", "end", values=autor)

    def ver_prestamos(self):
        #limpiar prestamos
        for prestamo in self.treeview_prestamos.get_children():
            self.treeview_prestamos.delete(prestamo)
        prestamos = self.db_manager.get_all_loans()
        for prestamo in prestamos:
            self.treeview_prestamos.insert("", "end", values=prestamo)

    def buscar_libro(self):
        #limpiar libros
        for libro in self.treeview_libros.get_children():
            self.treeview_libros.delete(libro)
        id_libro = self.entry_id_libro.get()
        titulo = self.entry_titulo.get()
        libros = self.db_manager.search_book(id_libro, titulo)
        for libro in libros:
            self.treeview_libros.insert("", "end", values=libro)
    
    def buscar_libro_por_id(self):
        #limpiar libros
        for libro in self.treeview_libros.get_children():
            self.treeview_libros.delete(libro)
        id_libro = self.entry_id_libro.get()
        libros = self.db_manager.search_book_by_id(id_libro)
        for libro in libros:
            self.treeview_libros.insert("", "end", values=libro)

    def agregar_libro(self):
        titulo = self.entry_titulo_agregar.get()
        id_autor = self.entry_autor_id.get()
        genero = self.entry_genero.get()
        anio_publicacion = self.entry_anio_publicacion.get()
        self.db_manager.add_book(titulo, id_autor, genero, anio_publicacion)
        messagebox.showinfo("Éxito", "Libro agregado exitosamente")

    def agregar_autor(self):
        nombre = self.entry_nombre_autor.get()
        apellido = self.entry_apellido_autor.get()
        self.db_manager.add_author(nombre, apellido)
        messagebox.showinfo("Éxito", "Autor agregado exitosamente")

    def registrar_prestamo(self):
        fecha_prestamo = self.entry_fecha_prestamo.get()
        fecha_entrega = self.entry_fecha_entrega.get()
        libros_idlibro = self.entry_id_libro_prestamo.get()
        self.db_manager.add_loan(fecha_prestamo, fecha_entrega, libros_idlibro)
        messagebox.showinfo("Éxito", "Préstamo registrado exitosamente")

    def eliminar_prestamo(self):
        id_prestamo = self.entry_id_prestamo.get()
        self.db_manager.delete_loan(id_prestamo)
        messagebox.showinfo("Éxito", "Préstamo eliminado exitosamente")
