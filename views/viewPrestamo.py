class ViewPrestamo:

    @staticmethod
    def bienvenida():
        print('\n=============== PRESTAMO Y DEVOLUCION DE LIBROS ===============')


    @staticmethod
    def menu():
        lista_menu_prestamo = [
            ('1', 'Registrar prestamo de libro'),
            ('2', 'Registrar devolucion de libro'),
            ('s', 'presione "s" para regresar al menu principal')
        ]
        opciones = [m[0].upper() for m in lista_menu_prestamo]
        for i in lista_menu_prestamo:
            print(f'[{i[0]}] - {i[1]}')
        while True:
            opcion = input('Seleccione una opcion:').upper()
            if opcion not in opciones:        
                continue
            else:
                return opcion