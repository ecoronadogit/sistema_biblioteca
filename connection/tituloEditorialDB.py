from connection.connectionDB import ConexionPG
from entities.entidades import TituloEditorial
from typing import List

class TituloEditorialDB:

    @staticmethod
    def getAll() -> List[TituloEditorial]:
        lista_titulo_editorial = []
        with ConexionPG() as cnx:
            cnx.ejecutar_sql('SELECT * FROM TITULO_EDITORIAL;', False)
            if cnx.cursor.rowcount > 0:
                for item in cnx.cursor.fetchall():
                    titulo_editorial = TituloEditorial(item[0], item[1], item[2])
                    lista_titulo_editorial.append(titulo_editorial)
        return lista_titulo_editorial
    
    @staticmethod
    def getById(isbn:int) -> TituloEditorial:
        titulo_editorial = None
        with ConexionPG() as cnx:
            cnx.ejecutar_sql('SELECT * FROM TITULO_EDITORIAL WHERE ISBN=%s;', (isbn, ), False)
            if cnx.cursor.rowcount > 0:
                item = cnx.cursor.fetchone()
                titulo_editorial = (item[0], item[1], item[2])
        return titulo_editorial
    
    @staticmethod
    def getByTituloEditorial(titulo:str, editorial:str) -> TituloEditorial:
        titulo_editorial = None
        with ConexionPG() as cnx:
            cnx.ejecutar_sql('SELECT * FROM TITULO_EDITORIAL WHERE TITULO=%s AND EDITORIAL=%s;', 
            (titulo, editorial), False)
            if cnx.cursor.rowcount > 0:
                item = cnx.cursor.fetchone()
                titulo_editorial = TituloEditorial(item[0], item[1], item[2])
        return titulo_editorial
    
    @staticmethod
    def insert(titulo_editorial:TituloEditorial) -> int:
        isbn = None
        with ConexionPG() as cnx:
            cnx.ejecutar_sql(
                'INSERT INTO TITULO_EDITORIAL (TITULO,EDITORIAL) VALUES (%s,%s) RETURNING ISBN;',
                (titulo_editorial.titulo, titulo_editorial.editorial), True
            )
            if cnx.cursor.rowcount > 0:
                isbn = cnx.cursor.fetchone()[0]
        return isbn
    
    @staticmethod
    def count() -> int:
        cnt = None
        with ConexionPG() as cnx:
            cnx.ejecutar_sql('SELECT COUNT(*) FROM TITULO_EDITORIAL;', False)
            cnt = cnx.cursor.fetchone()
        return cnt[0]