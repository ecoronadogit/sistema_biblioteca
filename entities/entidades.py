class Lector:
    id_lector =None
    nombre =None

    def __init__(self, id_lector, nombre):
        self.id_lector = id_lector
        self.nombre = nombre


class TituloEditorial:
    isbn =None
    titulo =None
    editorial =None

    def __init__(self, isbn, titulo, editorial):
        self.isbn = isbn
        self.titulo = titulo
        self.editorial = editorial

class Libro:
    id_libro =None
    isbn =None
    disponible =None

    def __init__(self, id_libro, isbn, disponible):
        self.id_libro = id_libro
        self.isbn = isbn
        self.disponible = disponible


class Prestamo:
    id_prestamo =None
    id_lector =None
    id_libro =None
    fecha_prestamo =None
    fecha_devolucion =None

    def __init__(self, id_prestamo, id_lec, id_lib, fecha_prest, fecha_devol):
        self.id_prestamo = id_prestamo
        self.id_lector = id_lec
        self.id_libro = id_lib
        self.fecha_prestamo = fecha_prest
        self.fecha_devolucion = fecha_devol
