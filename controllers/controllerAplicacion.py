from controllers.controllerLector import ControllerLector
from controllers.controllerLibro import ControllerLibro
from controllers.controllerPrestamo import ControllerPrestamo
from views.viewAplicacion import ViewAplicacion
from views.viewLibro import ViewLibro
from views.viewLector import ViewLector

class ControllerAplicacion:
    
    @staticmethod
    def inicio():
        ViewAplicacion.bienvenida()
        opcion = ViewAplicacion.menu()
        if opcion == '1':            
            ControllerLector.menu()
        elif opcion == '2':
            ControllerLibro.menu()
        elif opcion == '3':
            ControllerPrestamo.menu()
        elif opcion == 'S':
            ControllerAplicacion.fin()
        
        if opcion != 'S':
            ControllerAplicacion.inicio()

    @staticmethod
    def fin():
        ViewAplicacion.salida() 
        
