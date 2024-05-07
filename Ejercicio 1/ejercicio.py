import os
YEN = 26.30
DOLAR= 3944
EURO = 4279 

def conversion(op:int ):
    os.system('clear')
    menu = '1.Convertir  pesos a dolares\n2.Convetir pesos a euros\n3.Convertir euros a pesos\n4.Convertir pesos a yenes\n5.Salir'
    print(menu)
    try:
        op = int(input('=>'))
        match(op):
            case 1:
                cantidad = float(input('Ingrese la cantidad  a convertir: '))
                dolares = cantidad/DOLAR
                print(f'La cantidad de dolares por {cantidad} pesos es : {round(dolares,1)}')
                os.system('pause')
                conversion(0)
            case 2:
                cantidad = float(input('Ingrese la cantidad  a convertir: '))
                euros = cantidad / EURO
                print(f'La cantidad de euros por {cantidad } pesos es : {round(euros,1)}')
                os.system('pause')
                conversion(0)
            case 3:
                cantidad = float(input('Ingrese la cantidad  a convertir: '))
                pesos = cantidad * EURO
                print(f'La cantidad de pesos por {cantidad} euros es {round(pesos,1)}')
                os.system('pause')
                conversion(0)
            case 4:
                cantidad = float(input('Ingrese la cantidad  a convertir: '))
                yanes = cantidad / YEN
                print (f'La cantidad de yanes por {cantidad} pesos es : {round(yanes,1)}')
                os.system('pause')
                conversion(0)
            case 5:
                print ('Salio del programa')
                os.system('pause')
                exit()
            case _: 
                print('Opción inválida')
                os.system('pause')
                conversion(0)
    except ValueError:
        print('Ingresó una opción inválida')

conversion(0)
