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
            print('menu lector opcion 3.....')
        elif opcion == 'S':
            return
        
        if opcion != 'S':
            ControllerLector.menu()

    @staticmethod
    def listarLectores():
        lista = ModelLector.listarLectores()
        ViewLector.listarLectores(lista)

lista_menu_lector = [
    ('1', 'Listar lectores'),
    ('2', 'Buscar lector por nombre'),
    ('3', 'Registrar lector'),
    ('s', 'presione "s" para regresar al menu principal')
]
'''
        continuar = True
        while continuar:
            ViewLector.menu()
            opcion = input("Elija una opcion: ")
            if opcion == "1":
                cont = 1
                print(cont)
            elif opcion == "2":
                lector = ModelLector.buscarLectorPorId(2)
                print(f'id: {lector.id_lector} nombre: {lector.nombre}')
            elif opcion == "3":
                lectores = ModelLector.listarLectores()
                for lector in lectores:
                    print(lector.id_lector, ' - ', lector.nombre)                          
            elif opcion == "4":
                #id = ModelLector.registrarLector(none)
                print(4)
'''