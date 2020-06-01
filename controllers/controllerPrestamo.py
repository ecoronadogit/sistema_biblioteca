from models.modelPrestamo import ModelPrestamo
from views.viewPrestamo import ViewPrestamo
from entities.entidades import Prestamo

class ControllerPrestamo:

    @staticmethod
    def menu():
        ViewPrestamo.bienvenida()
        opcion = ViewPrestamo.menu()
        if opcion == '1':            
            print('menu prestamo opcion 1.....')
        elif opcion == '2':
            print('menu devolucion opcion 2.....')
        elif opcion == 'S':
            return
        
        if opcion != 'S':
            ControllerPrestamo.menu()