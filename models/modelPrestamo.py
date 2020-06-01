import datetime as dt
from connection.prestamoDB import PrestamoDB
from connection.libroDB import LibroDB
from connection.tituloEditorialDB import TituloEditorialDB
from entities.entidades import Prestamo, Libro, TituloEditorial

class ModelPrestamo():

    @staticmethod
    def librosPrestadosPorLector(id_lector_prestamo):
        lista_prestamos = PrestamoDB.getAll()
        lista_libros = LibroDB.getAll()
        lista_titulo_editorial = TituloEditorialDB.getAll()
        lista = [
            (x.id_prestamo,y.id_libro,z.titulo,z.editorial)
            for x in lista_prestamos for y in lista_libros for z in lista_titulo_editorial
            if x.id_libro==y.id_libro and y.isbn==z.isbn and x.id_lector==id_lector_prestamo
        ]
        return lista
    
    @staticmethod
    def librosNoDevueltosPorLector(id_lector_prestamo):
        lista_prestamos = PrestamoDB.getNoDevueltos()
        lista_libros = LibroDB.getAll()
        lista_titulo_editorial = TituloEditorialDB.getAll()
        lista = [
            (x.id_prestamo,y.id_libro,z.titulo,z.editorial)
            for x in lista_prestamos for y in lista_libros for z in lista_titulo_editorial
            if x.id_libro==y.id_libro and y.isbn==z.isbn and x.id_lector==id_lector_prestamo
        ]
        return lista

    @staticmethod    
    def prestarLibro(id_lector, id_libro):
        fecha_prestamo = dt.date.today().strftime('%Y%m%d')
        PrestamoDB().insertPrestamo(Prestamo(None, id_lector,id_libro, fecha_prestamo, None))
        LibroDB().setNoDisponible(id_libro)
    
    @staticmethod
    def devolverLibro(id_prestamo):        
        prestamo = PrestamoDB.getById(id_prestamo)
        fecha_devolucion = dt.date.today().strftime('%Y%m%d')
        PrestamoDB.setDevuelto(fecha_devolucion, prestamo.id_prestamo)
        LibroDB().setDisponible(prestamo.id_libro)