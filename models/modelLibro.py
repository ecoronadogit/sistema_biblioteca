from connection.tituloEditorialDB import TituloEditorialDB
from connection.libroDB import LibroDB
from entities.entidades import Libro, TituloEditorial

class ModelLibro:

    @staticmethod
    def listarLibros():
        lista_titulo_editorial = TituloEditorialDB.getAll()
        lista_libros = LibroDB.getAll()
        lista = [
            (y.id_libro, x.isbn, x.titulo, x.editorial, y.disponible)
            for x in lista_titulo_editorial for y in lista_libros
            if x.isbn == y.isbn
        ]
        return lista

    @staticmethod
    def listarLibrosDisponibles():
        lista_titulo_editorial = TituloEditorialDB.getAll()
        lista_libros = LibroDB.getDisponibles()
        lista = [
            (y.id_libro, x.isbn, x.titulo, x.editorial, y.disponible)
            for x in lista_titulo_editorial for y in lista_libros
            if x.isbn == y.isbn
        ]
        return lista
    
    @staticmethod
    def registrarLibro(titulo, editorial):
        titulo_editorial = TituloEditorialDB.getByTituloEditorial(titulo, editorial)
        if titulo_editorial: 
            LibroDB.insert(Libro(None, titulo_editorial.isbn, 1))
        else:
            isbn = TituloEditorialDB.insert(TituloEditorial(None, titulo, editorial))
            LibroDB.insert(Libro(None, isbn, 1))