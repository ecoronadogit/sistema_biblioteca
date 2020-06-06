from connection.connectionDB import ConexionPG
from entities.entidades import Libro
from typing import List

class LibroDB:

    @staticmethod
    def getAll() -> List[Libro]:
        lista_libro = []
        with ConexionPG() as cnx:
            cnx.ejecutar_sql('SELECT * FROM LIBRO;', False)
            if cnx.cursor.rowcount > 0:
                for item in cnx.cursor.fetchall():
                    libro = Libro(item[0], item[1], item[2])
                    lista_libro.append(libro)
        return lista_libro
    
    @staticmethod
    def getById(id:int) -> Libro:
        libro = None
        with ConexionPG() as cnx:
            cnx.ejecutar_sql('SELECT * FROM LIBRO WHERE ID_LIBRO=%s;', (id, ), False)
            if cnx.cursor.rowcount > 0:
                item = cnx.cursor.fetchone()
                libro = Libro(item[0], item[1], item[2])
        return libro
    
    @staticmethod
    def getByIsbn(isbn:int) -> Libro:
        libro = None
        with ConexionPG() as cnx:
            cnx.ejecutar_sql('SELECT * FROM LIBRO WHERE ISBN=%s;', (isbn, ), False)
            if cnx.cursor.rowcount > 0:
                item = cnx.cursor.fetchone()
                libro = Libro(item[0], item[1], item[2])
        return libro

    @staticmethod
    def getDisponibles() -> List[Libro]:
        lista_libro = []
        with ConexionPG() as cnx:
            cnx.ejecutar_sql('SELECT * FROM LIBRO WHERE DISPONIBLE=1;', False)
            if cnx.cursor.rowcount > 0:
                for item in cnx.cursor.fetchall():
                    libro = Libro(item[0], item[1], item[2])
                    lista_libro.append(libro)
        return lista_libro
    
    @staticmethod
    def setDisponible(id:int) -> bool:
        update = False
        with ConexionPG() as cnx:
            cnx.ejecutar_sql('UPDATE LIBRO SET DISPONIBLE=1 WHERE ID_LIBRO=%s;', (id, ), True)
            if cnx.cursor.rowcount > 0:
                update=True
        return update
    
    @staticmethod
    def setNoDisponible(id:int) -> bool:
        update = False
        with ConexionPG() as cnx:
            cnx.ejecutar_sql('UPDATE LIBRO SET DISPONIBLE=0 WHERE ID_LIBRO=%s;', (id, ), True)
            if cnx.cursor.rowcount > 0:
                update=True
        return update
    
    @staticmethod
    def insert(libro:Libro) -> int:
        id = None
        with ConexionPG() as cnx:
            cnx.ejecutar_sql('INSERT INTO LIBRO (ISBN, DISPONIBLE) VALUES (%s, %s) RETURNING ID_LIBRO;',
                (libro.isbn, libro.disponible), True)
            if cnx.cursor.rowcount > 0:
                id = cnx.cursor.fetchone()[0]
        return id
    
    @staticmethod
    def count() -> int:
        cnt = None
        with ConexionPG() as cnx:
            cnx.ejecutar_sql('SELECT COUNT(*) FROM LIBRO;', False)
            cnt = cnx.cursor.fetchone()
        return cnt[0]