import os.path
import datetime as dt

def registrar_log(excepcion, mensaje):
    filename = ''.join((dt.date.today().strftime('%Y_%m_%d'),'.log'))
    filename_fn = os.path.join(os.path.dirname(__file__),filename)
    fecha = dt.datetime.today().strftime('%Y_%m_%d_%H:%M:%S')

    with open(filename_fn, 'a+') as archivo_log:
        archivo_log.write(fecha + '-' * 31 + '\n')
        archivo_log.write('Excepcion: ' + str(excepcion) + '\n')
        archivo_log.write('Mensaje: ' + str(mensaje) + '\n')
        archivo_log.write('-' * 50 + '\n')