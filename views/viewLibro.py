class ViewLibro:

    @staticmethod
    def bienvenida():
        print('\n=============== GESTION DE LIBROS ===============')


    @staticmethod
    def menu():
        lista_menu_libros = [
            ('1', 'Listar libros'),
            ('2', 'Registrar libro'),
            ('s', 'presione "s" para regresar al menu principal')
        ]
        opciones = [m[0].upper() for m in lista_menu_libros]
        for i in lista_menu_libros:
            print(f'[{i[0]}] - {i[1]}')
        while True:
            opcion = input('Seleccione una opcion:').upper()
            if opcion not in opciones:        
                continue
            else:
                return opcion