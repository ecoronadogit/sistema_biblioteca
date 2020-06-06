from models.modelLector import ModelLector
from views.viewLector import ViewLector
from entities.entidades import Lector

class ControllerLector:

    @staticmethod
    def menu():
        ViewLector.bienvenida()
        opcion = ViewLector.menu()

        if opcion == '1':            
            #print('menu lector opcion 1.....')
            ControllerLector.listarLectores()
        elif opcion == '2':
            print('menu lector opcion 2.....')
        elif opcion == '3':
            ControllerLector.registrarLector()
        elif opcion == 'S':
            return
        
        if opcion != 'S':
            ControllerLector.menu()

    @staticmethod
    def listarLectores():
        lista = ModelLector.listarLectores()
        ViewLector.listarLectores(lista)

    @staticmethod
    def registrarLector():
        nombre_lector = ViewLector.registrarLector()
        ModelLector.registrarLector(nombre_lector)