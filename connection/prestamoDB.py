from connection.connectionDB import ConexionPG
from entities.entidades import Prestamo
from typing import List

class PrestamoDB:

    @staticmethod
    def getAll() -> List[Prestamo]:
        lista_prestamo = []
        with ConexionPG() as cnx:
            cnx.ejecutar_sql('SELECT * FROM PRESTAMO;', False)
            if cnx.cursor.rowcount > 0:
                for item in cnx.cursor.fetchall():
                    lista_prestamo.append(Prestamo(item[0], item[1], item[2], item[3], item[4]))
        return lista_prestamo
    
    @staticmethod
    def getNoDevueltos() -> List[Prestamo]:
        lista_prestamo = []
        with ConexionPG() as cnx:
            cnx.ejecutar_sql('SELECT * FROM PRESTAMO WHERE FECHA_DEVOLUCION IS NULL;', False)
            if cnx.cursor.rowcount > 0:
                for item in cnx.cursor.fetchall():
                    lista_prestamo.append(Prestamo(item[0], item[1], item[2], item[3], item[4]))
        return lista_prestamo
    
    @staticmethod
    def getById(id:int) -> Prestamo:
        prestamo = None
        with ConexionPG() as cnx:
            cnx.ejecutar_sql('SELECT * FROM PRESTAMO WHERE ID_PRESTAMO=%s;', (id, ), False)
            if cnx.cursor.rowcount > 0:
                item = cnx.cursor.fetchone()
                prestamo = Prestamo(item[0], item[1], item[2], item[3], item[4])
        return prestamo
    
    @staticmethod
    def setDevuelto(fecha_devolucion:str, id:int) -> bool:
        update = False
        with ConexionPG() as cnx:
            cnx.ejecutar_sql(
                'UPDATE PRESTAMO SET FECHA_DEVOLUCION=%s WHERE ID_PRESTAMO=%s;', 
                (fecha_devolucion, id), True
            )
            if cnx.cursor.rowcount > 0:
                update=True
        return update
    
    @staticmethod
    def insertPrestamo(prestamo:Prestamo) -> int:
        id = None
        with ConexionPG() as cnx:
            cnx.ejecutar_sql(
                'INSERT INTO PRESTAMO (ID_LECTOR, ID_LIBRO, FECHA_PRESTAMO) VALUES (%s, %s, %s) RETURNING ID_PRESTAMO;',
                (prestamo.id_lector, prestamo.id_libro, prestamo.fecha_prestamo), True
            )
            if cnx.cursor.rowcount > 0:
                id = cnx.cursor.fetchone()[0]
        return id
    
    @staticmethod
    def count() -> int:
        cnt = None
        with ConexionPG() as cnx:
            cnx.ejecutar_sql('SELECT COUNT(*) FROM PRESTAMO;', False)
            cnt = cnx.cursor.fetchone()
        return cnt[0]