from models.modelLibro import ModelLibro
from views.viewLibro import ViewLibro
from entities.entidades import Libro

class ControllerLibro:

    @staticmethod
    def menu():
        ViewLibro.bienvenida()
        opcion = ViewLibro.menu()
        if opcion == '1':            
            print('menu libro opcion 1.....')
        elif opcion == '2':
            print('menu libro opcion 2.....')
        elif opcion == 'S':
            return
        
        if opcion != 'S':
            ControllerLibro.menu()