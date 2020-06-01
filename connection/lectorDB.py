from connection.connectionDB import ConexionPG
from entities.entidades import Lector
from typing import List

class LectorDB:

    @staticmethod
    def getAll() -> List[Lector]:
        lista_lector = []
        with ConexionPG() as cnx:
            cnx.ejecutar_sql('SELECT * FROM LECTOR;', False)
            if cnx.cursor.rowcount > 0:
                for item in cnx.cursor.fetchall():
                    lista_lector.append(Lector(item[0], item[1]))
        return lista_lector
    
    @staticmethod
    def getById(id:int) -> Lector:
        lector = None
        with ConexionPG() as cnx:
            cnx.ejecutar_sql('SELECT * FROM LECTOR WHERE ID_LECTOR=%s;', (id, ), False)
            if cnx.cursor.rowcount > 0:
                item = cnx.cursor.fetchone()
                lector = Lector(item[0], item[1])
        return lector
    
    @staticmethod
    def getByName(name:str) -> Lector:
        lector = None
        with ConexionPG() as cnx:
            cnx.ejecutar_sql('SELECT * FROM LECTOR WHERE NOMBRE=%s;', (name, ), False)
            if cnx.cursor.rowcount > 0:
                item = cnx.cursor.fetchone()
                lector = Lector(item[0], item[1])
        return lector
    
    @staticmethod
    def insert(lector:Lector) -> int:
        id = None
        with ConexionPG() as cnx:
            cnx.ejecutar_sql('INSERT INTO LECTOR (NOMBRE) VALUES (%s) RETURNING ID_LECTOR;',
            (lector.nombre, ), True)
            if cnx.cursor.rowcount > 0:
                id = cnx.cursor.fetchone()[0]
        return id
    
    @staticmethod
    def count() -> int:
        cnt = None
        with ConexionPG() as cnx:
            cnx.ejecutar_sql('SELECT COUNT(*) FROM LECTOR;', False)
            cnt = cnx.cursor.fetchone()
        return cnt[0]