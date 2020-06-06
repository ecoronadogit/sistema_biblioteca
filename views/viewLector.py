from entities.entidades import Lector
from typing import List
from prettytable import PrettyTable

class ViewLector:

    @staticmethod
    def bienvenida():
        print('\n=============== GESTION DE LECTORES ===============')

    @staticmethod
    def menu():
        lista_menu_lector = [
            ('1', 'Listar lectores'),
            ('2', 'Buscar lector por nombre'),
            ('3', 'Registrar lector'),
            ('s', 'presione "s" para regresar al menu principal')
        ]
        opciones = [m[0].upper() for m in lista_menu_lector]
        for i in lista_menu_lector:
            print(f'[{i[0]}] - {i[1]}')
        print('-' * 60)
        while True:
            opcion = input('Seleccione una opcion:').upper()
            if opcion not in opciones:        
                continue
            else:
                return opcion
    
    @staticmethod
    def listarLectores(lista):
        t = PrettyTable()
        t.field_names = ['ID_LECTOR', 'NOMBRE']
        for lector in lista:
            t.add_row([lector.id_lector, lector.nombre])
        print(t)

    @staticmethod
    def registrarLector():
        nombre = input('Ingrese nombre de lector para registrar: ')
        return nombre