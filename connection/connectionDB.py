from psycopg2 import connect, Error
from connection.logger import registrar_log
#from logger import registrar_log

class ConexionPG:

    cnxdb = None
    cursor = None

    def __init__(self):
        try:
            #print('Iniciando conexion....')    
            self.cnxdb = connect(
                host='127.0.0.1', 
                port='5432', 
                dbname='biblioteca', 
                user='admin_libros', 
                password='libros_2020'
                )            
            self.cursor = self.cnxdb.cursor()
            #print('Conexion Exitosa')
        except Exception as e:
            print('Conexion Fallida')
            registrar_log(e, f'No se puede conectar a la BD biblioteca')            
    
    def ejecutar_sql(self, sql, parameters=None, hacer_commit=True):
        try:
            self.cursor.execute(sql, parameters)    
            if hacer_commit:                
                self.cnxdb.commit() 
        except Error as e:
            if hacer_commit:
                self.cnxdb.rollback()
            registrar_log(e, f'No se puede ejecutar la sentencia: {sql}')
    
    def test_sql(self):
        print('-' * 75)
        self.ejecutar_sql('SELECT CURRENT_DATE;', False)
        print('FECHA:', self.cursor.fetchone())
        self.ejecutar_sql('SELECT VERSION();', False)        
        print('VERSION_POSTGRESQL:', self.cursor.fetchone())        
        print('-' * 75)

    def commit(self):
        if self.cnxdb:
            self.cnxdb.commit()

    def rollback(self):
        if self.cnxdb:
            self.cnxdb.rollback()   

    def __enter__(self):
        return self

    def __exit__(self, a, b, c):
        if self.cnxdb:
            self.cursor.close()
            self.cnxdb.close()

#====================================================================
'''
if __name__ == "__main__":
    cnx = ConexionPG()
    cnx.test_sql()
    print(cnx.ejecutar_sql('select * from lector',hacer_commit=False))
    print(cnx.cursor.fetchall())
    print(cnx.ejecutar_sql("update lector set nombre=%s where id_lector=3 returning id_lector", ('pedro',))) 
    print('rowcount:',cnx.cursor.rowcount) # -1 : no actualiza (no existe columna), 
    #0: no hay registro que cumpla la condicion, >0 numero de registros actualizados 
    print('cursor:',cnx.cursor.fetchall())
    print(cnx.ejecutar_sql('select * from lector',hacer_commit=False))
    print(cnx.cursor.fetchall())
'''