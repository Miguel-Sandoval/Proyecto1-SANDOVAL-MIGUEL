import operations as op
from getpass import getpass

# Variables
usuario = 'Mick'
password = 'acceso12'


def login():
#funcion de login
    usuario_valido = input('Ingrese su usuario: ')
    password_valido = getpass('Ingrese su password: ')

    if (usuario_valido == usuario) & (password_valido == password):
        print('Hola: '+ usuario_valido)
        return True
    else:
        return False


def analysis(option):
#funcion switch en python
    switcher = {
        1: op.option_1,
        2: op.option_2,
        3: op.option_3
    }
    func = switcher.get(option, "Opcion no valida")
    return func()


logged = login()
finish = 'n'

while finish != ('y' or 'Y'):

    if not logged:
        print('Ingreso incorrecto')
        logged = login()
    else:
        print('''
        Opciones disponibles:
            1.- Top productos mas vendidos y los mas buscados
            2.- Productos por reseña en el servicio.
            3.- Total de ingresos y ventas promedio mensuales,total anual y meses con más ventas al año
        ''')

        analysis(int(input('Ingresa la opcion a realizar dentro de 1-4: ')))
        finish = input('Exit? (y/n): ')
