import os
import corefile.inf as info
import globales.diccionario as dic
def information():
    os.system('cls')
    menu = '1.Ingresar informacion\n2.Salir'
    print(menu)
    try: 
        op = int(input('=>'))
        while (op != 1 and op != 2):
            print ('Opción inválida.')
            os.system('pause')
            op = int(input('=>'))
        match op:
            case 1: 
                os.system('clear')
                title ="""
                ***************************
                * GUARDADO DE INFORMACION *
                ***************************
                """
                print(title)
                print('Ingrese sus datos ')
                cedula = int(input('Ingrese sus cédula: '))
                nombres = input('Nombres: ')
                apellidos = input('Apellidos: ')

                print('Ingrese su dirección:')
                ciudad = input('Ciudad: ')
                longitud = input('Longitud: ')
                latitud = input('Latitud: ')
                ubicacion = {
                    'ciudad': ciudad,
                    'longitud': longitud,
                    'latitud': latitud,
                }
                email = input('Email: ')
                edad = int(input('Edad: '))
                ocupacion = input('OCupación: ')

                usuario = {
                    'cedula':cedula,
                    'nombres':nombres,
                    'apellidos':apellidos,
                    'ubicacion':ubicacion,
                    'email':email,
                    'edad':edad,
                    'ocupacion':ocupacion,
                }
                info.AddData('datos',cedula,usuario)
                dic.informacion.get('datos').update({cedula:usuario})
                print ('1.Para agregar un nuevo usuario\n2.Salir ')
                seleccion = int(input('=>'))
                while (seleccion != 1 and seleccion != 2):
                    print ('Opción inválida.')
                    os.system('pause')
                    seleccion = int(input('=>'))
                if seleccion ==1 : 
                    information()
                else :
                    exit()
    except ValueError: 
        print('Está ingresando valores incorrectos... Intente nuevamente')
        os.system('pause')
        information()

if __name__ == '__main__':
    os.system('clear')
    info.DATOS = ('data/datos.json')
    info.checkFile(dic.informacion)
    information()