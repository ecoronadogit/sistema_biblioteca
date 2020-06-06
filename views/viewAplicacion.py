class ViewAplicacion:

    @staticmethod
    def bienvenida():
        print('\n-----------------------------------------------------------')
        print('================== GESTION DE BIBLIOTECA ===================')
        print('------------------------------------------------------------')

    @staticmethod
    def menu():
        lista_menu_principal = [
            ('1', 'Gestion de Lectores'),
            ('2', 'Gestion de Libros'),
            ('3', 'Prestamo y Devolucion de Libros'),
            ('s', 'presione "s" para salir')
        ]
        opciones = [m[0].upper() for m in lista_menu_principal]
        for i in lista_menu_principal:
            print(f'[{i[0]}] - {i[1]}')
        print('-' * 60)
        while True:
            opcion = input('Seleccione una opcion:').upper()
            if opcion not in opciones:        
                continue
            else:
                return opcion           

    @staticmethod
    def salida():
        print('\n****************** Gracias por su visita *******************')     