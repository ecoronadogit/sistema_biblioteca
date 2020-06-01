from connection.lectorDB import LectorDB
from connection.tituloEditorialDB import TituloEditorialDB
from entities.entidades import Lector, Libro, Prestamo, TituloEditorial
from models.modelLector import ModelLector

print(LectorDB.count())

lector = LectorDB.getById(2)
print(f'ID: {lector.id_lector} - NOMBRE: {lector.nombre}')
print('-'*20)
for lector in LectorDB.getAll():
    print(f'ID: {lector.id_lector} - NOMBRE: {lector.nombre}')
'''
lector = Lector(None, 'Pedro')
id = LectorDB.insert(lector)
print(id)'''

import datetime as dt
fecha = dt.date.today().strftime('%Y%m%d')

result = TituloEditorialDB.getByTituloEditorial('python', 'freeeditor')
print('result:', result)

lectores = ModelLector().listarLectores()
for lector in lectores:
    print(lector.id_lector, ' - ', lector.nombre)