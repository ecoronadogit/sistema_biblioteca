from entities.entidades import Lector
from typing import List

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
        while True:
            opcion = input('Seleccione una opcion:').upper()
            if opcion not in opciones:        
                continue
            else:
                return opcion
    
    @staticmethod
    def listarLectores(lista:List[Lector]):
        t = '''
        +-----------+-------------------------------+
        | ID_LECTOR |            NOMBRE             |
        |-----------+-------------------------------|
        {0}
        +-------------------------------------------+
        '''        
        t = (t.format('\n'.join("| {0:^9} | {1:<29} |".format(i.id_lector, i.nombre) for i in lista)))
        print(t)

